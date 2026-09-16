#!/usr/bin/env bash
#
# 更新日時: 2026/09/17
# 処理概要: ローカル配備本体を実行し、その後 release_1.0.0 の旧版を /old/ へ展開する。
# 前回バージョンとの違い:
# - [MOD]: develop配備後に旧版比較用サイトを ryutai/old/ へ追加する。

set -Eeuo pipefail

scriptDir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

bash "${scriptDir}/deploy_local_v1.3/deploy_local_v1.3.sh"
bash "${scriptDir}/deploy_old_local_v1.6.sh"
