# MPS Source Recovery Recheck — 2026-09-19

## 結論

MPS 49参照を再確認した。

現時点の判定:

**SOURCE BLOCKED / HOLD（ただし HP.7z のLibrary実体は確認済み）**

以前の「HP.7z自体を確認できない」状態からは進展している。
現在の主な阻害要因は、Library上の7zをProject実行環境へraw-byte materializeできないこと。

## 1. develop上のMPS参照再確認

| Page | References |
|---|---:|
| `mps/mps_1.html` | 1 |
| `mps/mps_2.html` | 1 |
| `mps/mps_3.html` | 12 |
| `mps/mps_4.html` | 9 |
| `mps/mps_5.html` | 2 |
| `mps/mps_6_1.html` | 2 |
| `mps/mps_6_2.html` | 22 |
| **Total** | **49** |

参照名:
- `img/mps_weight.files/image001.gif`
- `img/mps_num.files/image001.gif`
- `img/mps_nabra.files/image001.gif` ... `image012.gif`
- `img/mps_dot.files/image001.gif` ... `image009.gif`
- `img/mps_rap.files/image001.gif` ... `image002.gif`
- `img/mps_fluid_eq.files/image001.gif` ... `image002.gif`
- `img/mps_fluid_count.files/image001.gif` ... `image022.gif`

## 2. ページ内容

対象章:
- 重み関数
- 粒子の数密度
- 勾配モデル
- 発散モデル
- ラプラシアンモデル
- 支配方程式
- 計算の流れ

HTML本文は残っているが、式部分は画像参照のため、本文だけから元画像と厳密一致する式を復元することはできない。

## 3. Library再確認

Library上で以下の7z実体を確認した。

- `HP.7z`
- `HP(1).7z`
- `_tmp_HP_mps_materialize_root.7z`
- `_tmp_HP_mps_materialize_test.7z`
- `_tmp_HP_mps_recovery.7z`

いずれも約30.4MB。

ただし4候補をraw-file materializeしたところ、すべて:

`This Project file does not have an authorized raw-byte materialization path.`

で失敗した。

したがって、アーカイブの存在は確認できるが、現Project実行環境では展開できない。

## 4. Word / 別原稿検索

以下のページ題名・MPS名称でLibraryを再検索した。

- MPS / 粒子法
- 重み関数
- 粒子の数密度
- 勾配モデル
- 発散モデル
- ラプラシアンモデル
- 支配方程式
- 計算の流れ

該当するWord原稿は確認できなかった。

## 5. GitHub再確認

以下の元ファイル名でリポジトリ検索したが、復元用のWord/PDF/画像資産は確認できなかった。

- `mps_weight`
- `mps_num`
- `mps_nabra`
- `mps_dot`
- `mps_rap`
- `mps_fluid_eq`
- `mps_fluid_count`

## 6. 外部確認

公開画像URLの直接取得はWeb取得ツールの制約で確認不能。
ファイル名によるWeb検索では該当結果なし。

過去のFTPS固定名49件確認:
- recovered: 0
- missing: 49

と今回の状態は矛盾しない。

## 7. 次の再開条件

以下のどちらかが満たされた場合のみMPS数式変換を再開する。

1. `HP.7z` / `HP(1).7z` を実行環境へraw byteとして取得できる
2. MPSのWord原稿または元GIF画像を別途取得できる

それまでは推測による数式復元を行わない。

## 8. 現在の最終状態

- MPS HTML参照: **49/49確認**
- GitHub画像実体: **なし**
- 本番FTPS画像実体: **過去確認で0/49**
- Library HP.7z: **存在確認**
- Library HP.7z展開: **権限制約で不可**
- Word原稿: **未発見**
- 推測復元: **実施しない**
- Status: **SOURCE BLOCKED / HOLD**
