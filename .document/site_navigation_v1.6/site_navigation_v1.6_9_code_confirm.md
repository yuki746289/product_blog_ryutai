# site_navigation v1.6 コード確認

確認日: 2026-09-16
対象: `js/site_navigation_v1_6.js`, `css/site_v1_6.css`, `footer.html`
実装前基準: `e62f0e2e8cbb0e4d5ea96c64d816191b00740c68`
実装コード確定コミット: `8abcde2c968ac5677caeba23fa2ee94817dc1dc3`

## 1. 現在の判定

**総合判定: 保留（静的確認合格 / 実ブラウザ確認待ち）**

コード差分・設計ID・文字コード・不変領域の静的確認は合格した。PC 1365px / tablet 768px / mobile 390pxでの実ブラウザ操作・スクリーンショット確認は、この実行環境から利用者PCの`localhost`へ接続できないため未実施。ルール上、実動確認完了までは最終合格としない。

## 2. 実装差分範囲

`e62f0e2...` → `8abcde2...` の比較結果:

|ファイル|状態|確認|
|---|---|---|
|`js/site_navigation_v1_6.js`|ADD|新共通ナビのみ|
|`css/site_v1_6.css`|ADD|新UI時のD Monochrome/mega/mobile CSSのみ|
|`footer.html`|MOD|ASCIIコメント＋script読込のみ。既存CP932本文を維持|

上記3ファイル以外のコード差分は0件。

### 不変領域

- `menu.html`: 実装前後blob SHA `d5d7ef93ea919e45556e62b668ec1b649da93657` で一致。
- 代表数式ページ `fem/fem_7_2_2.html`: 実装前後blob SHA `7aff6ea90c580baaad2aa90d37f558ba92a43232` で一致。
- 記事HTML、数式画像src、TeX、本文を本UI実装では変更していない。
- `release_1.0.0`、本番FTPは変更していない。

## 3. footer文字コード確認

初回の通常`update_file`では、GitHub差分からCP932→UTF-8変換が発生したことを検出したため不合格とし、直ちに修正した。

修正確認:

- 元footer blob: `2bb96ccd119d3018f5b16d29d7d82cbdce57040c`
- 元Unicode表示をCP932再エンコードしてGit blob SHAを算出 → 元SHAと完全一致。
- script追加後の期待blob SHA: `5c1e51648a79fbab62025590f940297723514f7a`
- GitHubへbase64 blobとして登録したSHA: `5c1e51648a79fbab62025590f940297723514f7a`
- develop上の`footer.html` SHA: `5c1e51648a79fbab62025590f940297723514f7a`
- 実装前後比較ではfooterは **9行追加 / 削除0行**。

判定: **OK。既存CP932バイト列を維持してscriptタグのみ追加。**

## 4. F/T割当確認レポート

|検証項目|件数|判定|備考|
|---|---:|:---:|---|
|named function 総数|13|OK|新規JSのF/T対象|
|`[Fxxx]`割当|6|OK|F001-F006|
|`[Txxx]`割当|7|OK|T001-T007|
|F/T両方併記|0|OK|排他的|
|F/T未割当|0|OK|named functionは全て割当済み|
|ID重複|0|OK|F/T/L/I/O/Vを確認|

既存`footer.html`の`Init()`はKEEP関数であり、新規JSのF/T棚卸し対象外。コード自体は変更していない。

## 5. トレーサビリティ確認

- [x] F001-F006をコード内関数定義コメントへ配置。
- [x] T001-T007をコード内関数定義コメントへ配置。
- [x] V001を共通設定定義へ配置。
- [x] I001-I025 / O001-O013を該当関数コメントへ配置。
- [x] L001-L007, L101-L105, L201-L205, L301-L304, L401-L406, L501-L507, L601-L602, L611-L614, L621-L624, L631-L632, L641, L651-L652, L661-L662を該当処理へ配置。
- [x] `anchor.href`の解決済みURLを使用。
- [x] `rv-nav-ready`はCSS読込・モデル・PC/mobile DOM・イベント登録成功後だけ付与。
- [x] `inert` / `aria-hidden` / `aria-expanded`をmobile状態と同期。
- [x] 8カテゴリは物理 / 流体力学 / 有限要素法 / メッシュ / SIMPLE法 / 伝熱工学 / Fortran / その他。
- [x] 旧`menu.html`は読み取り専用データ源。

## 6. 静的品質確認

### JavaScript

- [x] 実装元ローカルJSで`node --check`成功。
- [x] 最終追加した階層深度正規化ブロック（`minimumDepth`）をGitHub上で再確認。
- [x] `parentDocument.defaultView.getComputedStyle(...)`を使用し、footer iframe側windowを誤参照しない。
- [x] SIMPLE法・メッシュ等の先頭インデントをカテゴリ単位の最小深度で正規化する。
- [x] 初期化失敗時に`rv-nav-ready`を付けない。
- [x] 外側クリック、Escape、resize、mobile閉じる操作を実装。

### CSS

- [x] GitHub上blob SHA `a39fcfcb621443a7fd44f4f283f1375c32084f6e` とローカル検証ファイルSHAが一致。
- [x] `{` / `}` は93 / 93で一致。
- [x] legacy layout上書きは原則`body.rv-nav-ready`配下に限定。
- [x] 767px以下でPCナビを隠し、mobile trigger/drawerを表示。
- [x] 768px以上でmobile UIが通常表示されない。
- [x] drawerは縦スクロール可能。

## 7. コーディング規約確認レポート

|規約ファイル|章・項目|適用有無|判定|確認根拠|
|---|---|:---:|:---:|---|
|`.rules/rules_common.md`|作業前ルール提示|適用|OK|実装前に参照ルールを提示済み|
|同上|参照ファイル提示|適用|OK|本確認書と進捗報告に記録|
|同上|矛盾時停止|適用|OK|footer文字コード矛盾を検出し、通常更新を不合格として修正|
|同上|指示外ファイル変更禁止|適用|OK|コード差分は設計対象3ファイルのみ|
|`.rules/dev/rules_dev.md`|通常開発の工程順|適用|OK|v1.6仕様→要件→基本→詳細→実装の順に実施|
|同上|変更区分の独立判定|適用|OK|新JS/CSS=ADD、footer include=MOD、menu/article=KEEP|
|同上|コーディング規約全文確認|適用|OK|実装前にcommon/custom/other/app code rulesを確認|
|同上|KEEP領域保護|適用|OK|menu/formula代表ページSHA一致|
|`.rules/dev/rules_dev_custom.md`|元画像完全一致|対象外|OK|本実装で数式内容を変更していない|
|同上|D Monochrome + 多層メニュー|適用|OK|新CSS/JSへ実装|
|同上|本番反映禁止|適用|OK|developのみ|
|`.rules/dev/rules_dev_other.md`|参照URL・タグ|適用|OK|既存リンクは`anchor.href`で解決、新CSS/JSパスを確認|
|同上|id/DOM参照|適用|OK|`header/menu/sub-menu/footer`等の既存IDを現行HTMLと照合|
|同上|レイアウト崩れ確認|適用|保留|静的CSS確認済み、実ブラウザ目視が未実施|
|`rules_app_8_code.md`|実装前プレフライト|適用|OK|統合JSON、ADD/MOD対象、KEEP対象を宣言|
|同上|IDコメント|適用|OK|F/T/L/I/O/Vを実装へ配置|
|同上|不変条件保護|適用|OK|差分3ファイル限定、menu/formula SHA一致|
|同上|引数/戻り値変数化|適用|OK|新規主関数/補助関数で意味を持つ値を変数化して返却|
|同上|ヘッダー情報|適用|OK|新JS/CSSとfooter先頭に更新情報を記載|
|同上|キャメルケース/命名|適用|OK|関数`regist/select/update/refresh`、map/list命名を適用|
|同上|PowerShellエンコード|対象外|OK|PowerShell変更なし|
|`rules_app_9_code_confirm.md`|トレーサビリティ|適用|OK|本書4-5章|
|同上|JSONカバレッジ|適用|OK|F/T/L/Vおよび制約を照合|
|同上|静的実行確認|適用|OK|JS構文、CSS括弧、blob SHAを確認|
|同上|ブラウザ実行確認|適用|保留|利用者PC localhostで要確認|

## 8. ブラウザ確認項目（未実施）

ローカルプレビュー更新後、以下を確認する。

### PC 1365px
- [ ] 左固定メニューが消え、上部8カテゴリが1行で欠落なく表示される。
- [ ] 有限要素法のメガメニューを開き、深い階層を確認できる。
- [ ] 他カテゴリへ切替できる。
- [ ] 外側クリック / Escapeで閉じる。
- [ ] メガパネルが画面外へ不自然にはみ出さない。
- [ ] 本文がD Monochromeの中央単一カラムで表示される。

### Tablet 768px
- [ ] PCカテゴリ方式が表示される。
- [ ] 8カテゴリが操作可能。
- [ ] ページ横スクロールがない。

### Mobile 390px
- [ ] ハンバーガーが表示される。
- [ ] 右ドロワーが開閉する。
- [ ] カテゴリアコーディオンと下位アコーディオンを開閉できる。
- [ ] ドロワーを最下部までスクロールできる。
- [ ] Escape / overlay / ×で閉じる。
- [ ] 閉状態でドロワー内へTabフォーカスが入らない。
- [ ] ページ横スクロールがない。

### リンク・本文
- [ ] `index.html`から主要リンクが正しく遷移する。
- [ ] nestedページ（例:`fem/fem_7_2_2.html`）からメニューリンクが正しく遷移する。
- [ ] 数式画像・本文がデザイン変更前と同内容で表示される。

## 9. 次工程

ブラウザ確認が全てOKになった後、スクリーンショットを確認し、本書の保留項目をOKへ変更して手順10最終確認を行う。本番FTPへの反映は、その後も利用者の明示承認があるまで行わない。
