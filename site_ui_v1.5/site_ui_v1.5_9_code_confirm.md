# site_ui v1.5 コード確認

確認日: 2026-09-16
対象ブランチ: `develop`
判定: **合格（デザイン選定待ち）**

## 1. 実装対象
- `menu.html`
- `css/lib.css`
- `css/responsive.css`
- `css/math.css`
- `revision_history.html`
- `design_samples/v1.5/index.html`
- `design_samples/v1.5/technical-clean.html`
- `design_samples/v1.5/academic-minimal.html`
- `design_samples/v1.5/modern-dashboard.html`
- `design_samples/v1.5/design-samples.css`

## 2. トレーサビリティ
- [x] [F002][L301][L402] `refreshMobileNavigation()` から表示幅別scrolling同期を呼ぶ。
- [x] [T001][I004][I005][O006][L401] `refreshMenuScrollingMode()` を追加し、767px以下=`auto`、768px以上=`no` とする。
- [x] [L403] PC左メニュー `#sub` を180pxへ整合。
- [x] [L303] モバイル `.sub-text` / `dt` の幅と中央位置を統一。
- [x] [L501][L502] 修正履歴を `No. / 修正種類 / 対象 / 修正内容` へ変更。
- [x] [L503] 管理IDを `data-revision-id` へ移し利用者向け列から除外。
- [x] [L504] v1.5表示/操作改善を履歴へ追加。
- [x] [L601] サンプル一覧を追加。
- [x] [L602] Technical Cleanを追加。
- [x] [L603] Academic Minimalを追加。
- [x] [L604] Modern Dashboardを追加。
- [x] [L605] 独立したサンプルCSSを追加。

## 3. KEEP領域
- [x] `Init()` は変更していない。
- [x] `updateMobileMenuState()` は変更していない。
- [x] `disp()` は変更していない。
- [x] `set_height()` は変更していない。
- [x] v1.4 MathJax 4自動改行を維持。
- [x] トップ更新告知と修正履歴リンク位置を維持。
- [x] 既存メニューhrefを変更していない。
- [x] 本番FTPを変更していない。
- [x] デザインサンプルを本体CSS/HTMLへ適用していない。

## 4. ブラウザ検証
GitHub Actions run `35072574269`: **SUCCESS**

### PC左メニュー
- index: `#sub=180px`, iframe=180px, `scrolling=no`。
- FEMページ: `#sub=180px`, iframe=180px, `scrolling=no`。
- iframe文書のclientWidth/scrollWidthはいずれも180px。
- 可視リンクの左右クリップ: 0件。

### スマホメニュー
- iframe `scrolling=auto`。
- 「メインコンテンツ」見出し: left=12, right=293, width=281, center=152.5。
- 「広告」見出し: left=12, right=293, width=281, center=152.5。
- マウスホイール相当操作: scrollY 0 → 295。縦スクロール成功。

### 修正履歴
- ヘッダー: `No. / 修正種類 / 対象 / 修正内容`。
- `data-revision-id` 行: 19件。
- `R-UI-*`, `R-FEM*` 等の管理IDは表の表示テキストに含まれない。

### デザインサンプル
PC 1365px / スマホ390pxでA/B/Cの3案を確認。

|案|PC横はみ出し|スマホ横はみ出し|判定|
|---|---|---|---|
|Technical Clean|0|0|OK|
|Academic Minimal|0|0|OK|
|Modern Dashboard|0|0|OK|

サンプル一覧の3リンクも存在確認済み。

## 5. スクリーンショット目視確認
- [x] Technical Clean PC/スマホ
- [x] Academic Minimal PC/スマホ
- [x] Modern Dashboard PC/スマホ
- [x] サンプル一覧 PC/スマホ
- [x] 現行トップ PC
- [x] 現行FEM PC
- [x] 現行モバイルメニュースクロール後
- [x] 修正履歴 PC

artifact: `site-ui-v1-5-design-review` / ID `10437061500`

## 6. コーディング・追加ルール確認
参照:
- `.rules/dev/app/rules_app_8_code.md`
- `.rules/dev/app/rules_app_9_code_confirm.md`
- `.rules/dev/rules_dev_other.md`

確認:
- [x] 変更関数をF002とT001に限定。
- [x] DOM ID `menu`, `sub`, `sub-menu` の参照を実ページで検証。
- [x] リンク参照とサンプル一覧3リンクを検証。
- [x] CP932既存HTMLは変換スクリプトでCP932を維持。
- [x] 新規サンプルはUTF-8。
- [x] PC/スマホのレイアウトを自動測定＋目視確認。
- [x] 未確認の設計変更なし。

## 7. 判定
**コード確認: 合格。**

v1.5の実装範囲は確認済み。デザイン3案が揃ったため、仕様で定めたユーザレビューの停止点に到達した。本体への新デザイン適用はユーザ選定まで実施しない。