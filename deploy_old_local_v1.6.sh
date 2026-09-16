#!/usr/bin/env bash
#
# 更新日時: 2026/09/17
# 処理概要: release_1.0.0 の旧版サイトをローカルApacheの ryutai/old/ へ展開する。

set -Eeuo pipefail

scriptDir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repoRoot="${scriptDir}"
apacheRoot="${APACHE_ROOT:-/c/server/Apache24}"
targetDir="${TARGET_DIR:-${apacheRoot}/htdocs/ryutai}"
oldTargetDir="${targetDir}/old"
releaseRef="${OLD_RELEASE_REF:-origin/release_1.0.0}"

writeLog() {
    printf '%s\n' "$1"
}

if ! git -C "${repoRoot}" rev-parse --verify "${releaseRef}^{commit}" >/dev/null 2>&1; then
    writeLog "[INFO] Fetching release_1.0.0 for old-page preview..."
    git -C "${repoRoot}" fetch origin release_1.0.0:refs/remotes/origin/release_1.0.0
fi

if ! git -C "${repoRoot}" rev-parse --verify "${releaseRef}^{commit}" >/dev/null 2>&1; then
    printf 'ERROR: old-page release ref not found: %s\n' "${releaseRef}" >&2
    exit 1
fi

if [[ -z "${oldTargetDir}" || "${oldTargetDir}" == "/" || "${oldTargetDir}" == "${targetDir}" ]]; then
    printf 'ERROR: unsafe old-page target directory: %s\n' "${oldTargetDir}" >&2
    exit 1
fi

rm -rf -- "${oldTargetDir}"
mkdir -p "${oldTargetDir}"

git -C "${repoRoot}" archive "${releaseRef}" | tar -xf - -C "${oldTargetDir}"

# Development-only resources are not needed in the legacy web copy.
rm -rf -- \
    "${oldTargetDir}/.github" \
    "${oldTargetDir}/.document" \
    "${oldTargetDir}/.rules" 2>/dev/null || true

if [[ ! -f "${oldTargetDir}/index.html" ]]; then
    printf 'ERROR: old-page index.html was not deployed: %s\n' "${oldTargetDir}/index.html" >&2
    exit 1
fi

writeLog "Old-page preview deployed: ${oldTargetDir}"
writeLog "Old-page URL: ${LOCAL_URL:-http://localhost/ryutai/}old/"
