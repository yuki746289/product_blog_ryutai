#!/usr/bin/env bash
#
# 更新日時: 2026/09/16
# 処理概要: ローカル配備v1.3実装本体をGit Bashで起動する運用入口。
# 前回バージョンとの違い:
# - [ADD]: `bash deploy_local.sh` で実装本体を実行できる入口を追加。

set -Eeuo pipefail

scriptDir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec bash "${scriptDir}/deploy_local_v1.3/deploy_local_v1.3.sh"
