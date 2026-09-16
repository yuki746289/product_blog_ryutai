# site_ui v1.4 詳細設計確認

確認対象:
- `site_ui_v1.4_6_detail.md`
- `site_ui_v1.4_6_detail.json`
- 現行 `menu.html`, `css/responsive.css`, `css/math.css`, `index.html`, `footer.html`
- v1.1 `responsive_navigation_v1.1_6_detail.md`

## 1. 形式・構造
- [x] S001〜S004を個別章で記載し、各章に7項目を完備。
- [x] 現行関数IDを再照合し、F001=Init、F002=refreshMobileNavigation、F003=updateMobileMenuState、F004=disp、F005=set_heightを維持。
- [x] 変更する実在関数はF002のみをMODとし、変更不要関数F001/F003/F004/F005はKEEP。
- [x] I001〜I003、O001〜O005、V001〜V004を重複なく定義。
- [x] ADD/MOD/KEEPの視覚装飾と変更区分を確認。

## 2. Markdown / JSON整合
- [x] S/L/F/I/O/Vの名称、区分、役割が一致。
- [x] S001/S002の静的HTML/CSS変更は概念関数を捏造せず、L-IDで対象ファイルを明示。
- [x] F002に関係するV003/V004とL301をJSONへ定義。
- [x] 既存F003/F004/F005の変更なしを明示。

## 3. 内容・論理
- [x] 数式はTeX本文を変更せず、表示方式だけをMathJax 4自動改行へ変更。
- [x] 修正履歴リンクはfooterからmenuへ移動し、トップ告知にもリンクを追加。
- [x] モバイルiframeのscrolling属性とCSSの縦スクロール指定を両方設計。
- [x] 背景ずれ対策としてスマホ時のmenu文書背景を白へ統一。
- [x] PC左メニュー、disp、set_height、updateMobileMenuStateを保護。

## 4. コンパイル・ダイジェスト
|区分|Markdown|JSON|判定|
|---|---:|---:|:---:|
|ADD|5|5|OK|
|MOD|9|9|OK|
|KEEP|20|20|OK|
|DEL|0|0|OK|

## 5. 実装前条件
- [x] MathJax 4公式ドキュメントで `output.displayOverflow='linebreak'` と `linebreaks.width='100%'` を確認。
- [x] 既存MathJaxページは5ページのみを今回対象とする。
- [x] CP932 HTMLはGitHub APIのUTF-8直接更新を避け、バイト変換を管理する実装スクリプトで更新する。
- [x] 実装後は静的確認だけでなくPC/スマホのスクリーンショットを取得し目視確認する。

**総合判定: 合格**
