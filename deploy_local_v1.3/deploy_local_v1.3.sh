#!/usr/bin/env bash
#
# 更新日時: 2026/09/16
# 処理概要: [S001]-[S004] Git BashからローカルApacheのhtdocs/ryutaiへサイトを配備し、HTTP確認後にブラウザ表示する。
# 前回バージョンとの違い:
# - [ADD]: ローカル環境検証、公開ファイルコピー、Apache確認・起動、HTTP/ブラウザ確認を新規追加。
# - [MOD]: なし。
# - [DEL]: なし。

set -Eeuo pipefail

scriptDir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# [V001] リポジトリルート
repoRoot="$(cd "${scriptDir}/.." && pwd)"
# [V002] Apacheルート。通常は /c/server/Apache24。テスト時のみ環境変数で上書き可能。
apacheRoot="${APACHE_ROOT:-/c/server/Apache24}"
# [V003] Apache公開先
# TARGET_DIR は自動テスト時の隔離先指定にのみ使用する。
targetDir="${TARGET_DIR:-${apacheRoot}/htdocs/ryutai}"
# [V004] ローカル確認URL
localUrl="${LOCAL_URL:-http://localhost/ryutai/}"
# [V005] Apache実行ファイル
httpdExe="${HTTPD_EXE:-${apacheRoot}/bin/httpd.exe}"
# [V006] Apache設定ファイル
httpdConf="${HTTPD_CONF:-${apacheRoot}/conf/httpd.conf}"
# [V007] ログ出力制御
isOutputLog="${IS_OUTPUT_LOG:-1}"
# [V008] ブラウザ起動制御
openBrowser="${OPEN_BROWSER:-1}"

# [T001] ログ出力補助関数
writeLog() {
    # [I001] 出力するログメッセージ
    local message="$1"

    # [L001] ログ出力フラグ確認と標準出力 (COMMON)
    if [[ "${isOutputLog}" == "1" ]]; then
        printf '%s\n' "${message}"
    fi
}

# [F001] [S001] 実行環境検証
checkEnvironment() {
    local requiredCommand
    local currentBranch
    local dirtyFiles

    # [L101] Git管理下と必須コマンドを確認する (S001)
    for requiredCommand in git tar curl; do
        if ! command -v "${requiredCommand}" >/dev/null 2>&1; then
            printf 'ERROR: required command not found: %s\n' "${requiredCommand}" >&2
            return 1
        fi
    done
    if ! git -C "${repoRoot}" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
        printf 'ERROR: repository not found: %s\n' "${repoRoot}" >&2
        return 1
    fi

    # [L102] developブランチであることを確認する (S001)
    currentBranch="$(git -C "${repoRoot}" rev-parse --abbrev-ref HEAD)"
    if [[ "${currentBranch}" != "develop" ]]; then
        printf 'ERROR: current branch is %s. Run: git checkout develop\n' "${currentBranch}" >&2
        return 1
    fi

    # [L103] 未コミット差分はローカル確認用途のため警告のみとする (S001)
    dirtyFiles="$(git -C "${repoRoot}" status --porcelain)"
    if [[ -n "${dirtyFiles}" ]]; then
        printf 'WARNING: working tree has uncommitted changes. Local deploy will include them.\n' >&2
    fi

    # [L104] サイト入口を確認する (S001)
    if [[ ! -f "${repoRoot}/index.html" ]]; then
        printf 'ERROR: index.html not found: %s\n' "${repoRoot}/index.html" >&2
        return 1
    fi

    # [L105] Apache実体と設定ファイルを確認する (S001)
    if [[ ! -d "${apacheRoot}" ]]; then
        printf 'ERROR: Apache root not found: %s\n' "${apacheRoot}" >&2
        return 1
    fi
    if [[ ! -f "${httpdExe}" ]]; then
        printf 'ERROR: httpd.exe not found: %s\n' "${httpdExe}" >&2
        return 1
    fi
    if [[ ! -f "${httpdConf}" ]]; then
        printf 'ERROR: httpd.conf not found: %s\n' "${httpdConf}" >&2
        return 1
    fi

    writeLog "Environment check: OK"
    # [O001] S001成功ステータス
    return 0
}

# [F002] [S002] 公開ファイルコピー
updateLocalSite() {
    # [L201] 削除対象がApache公開先の下位であることを確認して既存targetDirを削除する (S002)
    if [[ -z "${targetDir}" || "${targetDir}" == "/" || "${targetDir}" == "${apacheRoot}" || "${targetDir}" == "${apacheRoot}/htdocs" ]]; then
        printf 'ERROR: unsafe target directory: %s\n' "${targetDir}" >&2
        return 1
    fi
    rm -rf -- "${targetDir}"

    # [L202] targetDirを再作成する (S002)
    mkdir -p "${targetDir}"

    # [L203] 開発管理物を除外し、バイト列を変換せずtarストリームでコピーする (S002)
    if ! (
        cd "${repoRoot}"
        tar -cf - \
            --exclude='./.git' \
            --exclude='./.github' \
            --exclude='./.document' \
            --exclude='./.rules' \
            --exclude='./responsive_navigation_v1.1' \
            --exclude='./deploy_local_v1.3' \
            --exclude='./deploy_local.sh' \
            --exclude='./.gitignore' \
            .
    ) | (
        cd "${targetDir}"
        tar -xf -
    ); then
        printf 'ERROR: site copy failed.\n' >&2
        return 1
    fi

    # [L204] コピー後のサイト入口を検証する (S002)
    if [[ ! -f "${targetDir}/index.html" ]]; then
        printf 'ERROR: copied index.html not found: %s\n' "${targetDir}/index.html" >&2
        return 1
    fi

    # [L205] 配置先をログ表示する (S002)
    writeLog "Local site copied to: ${targetDir}"
    # [O002] S002成功ステータス
    return 0
}

# [F003] [S003] Apache確認・起動
updateApacheState() {
    local httpCode
    local retryCount
    local apacheLog="/tmp/ryutai_apache_start.log"
    local httpdExeWin
    local httpdConfWin

    # [L301] Apache設定テストを実行する (S003)
    if ! "${httpdExe}" -t -f "${httpdConf}"; then
        printf 'ERROR: Apache configuration test failed.\n' >&2
        return 1
    fi

    # [L302] localhostが既に応答しているか確認する (S003)
    httpCode="$(curl -sS -o /dev/null --max-time 2 -w '%{http_code}' 'http://localhost/' || true)"
    if [[ -n "${httpCode}" && "${httpCode}" != "000" ]]; then
        # [L306] 起動済みの場合は重複起動しない (S003)
        writeLog "Apache is already responding on localhost."
        # [O003] S003成功ステータス
        return 0
    fi

    # [L303] 未応答の場合はApacheをバックグラウンド起動する (S003)
    writeLog "Starting Apache..."
    if command -v cmd.exe >/dev/null 2>&1 && command -v cygpath >/dev/null 2>&1; then
        httpdExeWin="$(cygpath -w "${httpdExe}")"
        httpdConfWin="$(cygpath -w "${httpdConf}")"
        cmd.exe //C start "" "${httpdExeWin}" -f "${httpdConfWin}" >/dev/null 2>&1 || true
    else
        "${httpdExe}" -f "${httpdConf}" >"${apacheLog}" 2>&1 &
    fi

    # [L304] 最大10回、1秒間隔で応答待機する (S003)
    for retryCount in $(seq 1 10); do
        sleep 1
        httpCode="$(curl -sS -o /dev/null --max-time 2 -w '%{http_code}' 'http://localhost/' || true)"
        if [[ -n "${httpCode}" && "${httpCode}" != "000" ]]; then
            writeLog "Apache started."
            # [O003] S003成功ステータス
            return 0
        fi
    done

    # [L305] 起動失敗時はログ位置を示して異常終了する (S003)
    printf 'ERROR: Apache did not respond on http://localhost/.\n' >&2
    if [[ -f "${apacheLog}" ]]; then
        printf 'Apache start log: %s\n' "${apacheLog}" >&2
    fi
    return 1
}

# [F004] [S004] HTTP確認・ブラウザ表示
refreshLocalPreview() {
    # [L401] localUrlへのHTTP GETが成功することを確認する (S004)
    if ! curl -fsS --max-time 5 "${localUrl}" >/dev/null; then
        printf 'ERROR: local site is not reachable: %s\n' "${localUrl}" >&2
        return 1
    fi

    # [L402] 成功URLをログ表示する (S004)
    writeLog "Local preview: ${localUrl}"

    # [L403] 指定時はWindows既定ブラウザの起動を試行する (S004)
    if [[ "${openBrowser}" == "1" ]]; then
        if command -v cmd.exe >/dev/null 2>&1; then
            if ! cmd.exe //C start "" "${localUrl}" >/dev/null 2>&1; then
                # [L404] ブラウザ起動失敗は警告のみとする (S004)
                printf 'WARNING: browser could not be opened automatically. Open manually: %s\n' "${localUrl}" >&2
            fi
        else
            # [L404] ブラウザ起動失敗は警告のみとする (S004)
            printf 'WARNING: cmd.exe not available. Open manually: %s\n' "${localUrl}" >&2
        fi
    fi

    # [O004] S004成功ステータス
    return 0
}

writeLog "Rail View/ryutai local deploy start"
checkEnvironment
updateLocalSite
updateApacheState
refreshLocalPreview
writeLog "Local deploy completed successfully."
