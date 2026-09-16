# deploy_local v1.3 詳細設計確認

確認対象:
- `deploy_local_v1.3_6_detail.md`
- `deploy_local_v1.3_6_detail.json`

## 1. 形式・構造
- [x] S001〜S004を個別章で記載し、各章に7項目を完備。
- [x] IDは S4 / L20 / F4 / T1 / O4 / V8、重複なし。
- [x] 引数は全関数なしのためI-IDは0件。
- [x] 全関数にFまたはTの一方のみを割当。
- [x] 初版の全管理対象41件をADDとして管理。

## 2. Markdown / JSON整合
- [x] 全L-IDにsourceStepId対応あり。
- [x] 関数名 `checkEnvironment`, `updateLocalSite`, `updateApacheState`, `refreshLocalPreview`, `writeLog` が一致。
- [x] O/V定義が一致。
- [x] 共通補助関数T001はCOMMONとして定義。

## 3. 基本設計との整合
- [x] S001〜S004を全て詳細化。
- [x] Git pullは事前条件のまま維持。
- [x] 本番FTP非接触、Apache設定非変更、targetDir限定削除を維持。

## 4. ダイジェスト
- ADD 41 = S4 + L20 + F4 + T1 + O4 + V8
- MOD 0 / DEL 0 / KEEP 0
- MarkdownとJSONの件数一致。

**総合判定: 合格**
