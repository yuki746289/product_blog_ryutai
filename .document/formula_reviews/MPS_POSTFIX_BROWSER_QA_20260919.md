# MPS Postfix Browser QA — 2026-09-19

- Overall: **FAIL**
- Scope: MPS 7 pages / desktop + mobile
- Formula replacements expected: **48**
- Known HOLD: **mps/mps_6_2.html image022.gif only**
- Source correction under test: **image020 P_i → P_j**

## Runner output

~~~text
mps/mps_1.html desktop {'formula': 1, 'matherr': 0, 'unrendered': 1, 'overflow': False, 'uncontained': 0, 'missing': []} issues= ['unrendered=1']
mps/mps_2.html desktop {'formula': 1, 'matherr': 0, 'unrendered': 0, 'overflow': False, 'uncontained': 0, 'missing': []} issues= []
mps/mps_3.html desktop {'formula': 12, 'matherr': 0, 'unrendered': 0, 'overflow': False, 'uncontained': 0, 'missing': []} issues= []
mps/mps_4.html desktop {'formula': 9, 'matherr': 0, 'unrendered': 0, 'overflow': False, 'uncontained': 0, 'missing': []} issues= []
mps/mps_5.html desktop {'formula': 2, 'matherr': 0, 'unrendered': 0, 'overflow': False, 'uncontained': 0, 'missing': []} issues= []
mps/mps_6_1.html desktop {'formula': 2, 'matherr': 0, 'unrendered': 0, 'overflow': False, 'uncontained': 0, 'missing': []} issues= []
mps/mps_6_2.html desktop {'formula': 21, 'matherr': 0, 'unrendered': 0, 'overflow': False, 'uncontained': 0, 'missing': ['./../img/mps_fluid_count.files/image022.gif']} issues= []
mps/mps_1.html mobile {'formula': 1, 'matherr': 0, 'unrendered': 1, 'overflow': False, 'uncontained': 0, 'missing': []} issues= ['unrendered=1']
mps/mps_2.html mobile {'formula': 1, 'matherr': 0, 'unrendered': 0, 'overflow': False, 'uncontained': 0, 'missing': []} issues= []
mps/mps_3.html mobile {'formula': 12, 'matherr': 0, 'unrendered': 0, 'overflow': False, 'uncontained': 0, 'missing': []} issues= []
mps/mps_4.html mobile {'formula': 9, 'matherr': 0, 'unrendered': 0, 'overflow': False, 'uncontained': 0, 'missing': []} issues= []
mps/mps_5.html mobile {'formula': 2, 'matherr': 0, 'unrendered': 0, 'overflow': False, 'uncontained': 0, 'missing': []} issues= []
mps/mps_6_1.html mobile {'formula': 2, 'matherr': 0, 'unrendered': 0, 'overflow': False, 'uncontained': 0, 'missing': []} issues= []
mps/mps_6_2.html mobile {'formula': 21, 'matherr': 0, 'unrendered': 0, 'overflow': False, 'uncontained': 0, 'missing': ['./../img/mps_fluid_count.files/image022.gif']} issues= []
checks=14 failures=2
 - [19/Sep/2026 02:57:08] "GET /css/site_v1_6.css?v=20260917e HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:08] "GET /css/site_font_size_v1_6.css?v=20260917e HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:08] "GET /css/site_utility_v1_6.css?v=20260917e HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:08] "GET /css/site_readability_v1_6.css?v=20260917a HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:08] "GET /css/site_v1_6.css HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:08] "GET /css/site_font_size_v1_6.css?v=20260917f HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:08] "GET /css/site_utility_v1_6.css?v=20260917b HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:08] "GET /mps/mps_2.html HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:08] "GET /img/shiki2.gif HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:08] "GET /img/shiki1.gif HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:08] "GET /ad.html HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:08] "GET /questionnaire.html HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:08] "GET /menu.html HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:08] "GET /img/title.jpg HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:08] "GET /img/fts012_wrap_bg.gif HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:09] "GET /mps/mps_3.html HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:12] "GET /mps/mps_4.html HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:12] "GET /css/lib.css HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:12] "GET /img/shiki2.gif HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:12] "GET /img/shiki1.gif HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:12] "GET /css/responsive.css HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:12] "GET /css/math.css HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:12] "GET /css/site_v1_6.css?v=20260917e HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:12] "GET /css/site_font_size_v1_6.css?v=20260917e HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:12] "GET /css/site_utility_v1_6.css?v=20260917e HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:12] "GET /css/site_readability_v1_6.css?v=20260917a HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:12] "GET /ad.html HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:12] "GET /questionnaire.html HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:12] "GET /menu.html HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:12] "GET /img/title.jpg HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:12] "GET /img/fts012_wrap_bg.gif HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:12] "GET /footer.html HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:13] "GET /js/site_navigation_v1_6.js?v=20260917c HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:13] "GET /js/site_font_size_v1_6.js?v=20260917f HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:13] "GET /js/site_home_cleanup_v1_6.js?v=20260917b HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:13] "GET /js/site_utility_v1_6.js?v=20260917d HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:13] "GET /js/site_formula_guard_v1_6.js?v=20260917b HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:13] "GET /css/site_v1_6.css HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:13] "GET /css/site_font_size_v1_6.css?v=20260917f HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:13] "GET /css/site_utility_v1_6.css?v=20260917b HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:14] "GET /mps/mps_5.html HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:15] "GET /css/lib.css HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:15] "GET /css/math.css HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:15] "GET /css/responsive.css HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:15] "GET /css/site_v1_6.css?v=20260917e HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:15] "GET /css/site_font_size_v1_6.css?v=20260917e HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:15] "GET /css/site_utility_v1_6.css?v=20260917e HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:15] "GET /css/site_readability_v1_6.css?v=20260917a HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:16] "GET /mps/mps_6_1.html HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:16] "GET /img/shiki1.gif HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:16] "GET /img/shiki2.gif HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:16] "GET /ad.html HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:16] "GET /questionnaire.html HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:16] "GET /img/fts012_wrap_bg.gif HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:16] "GET /img/title.jpg HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:16] "GET /menu.html HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:16] "GET /footer.html HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:16] "GET /js/site_home_cleanup_v1_6.js?v=20260917b HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:16] "GET /js/site_font_size_v1_6.js?v=20260917f HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:16] "GET /js/site_utility_v1_6.js?v=20260917d HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:16] "GET /js/site_formula_guard_v1_6.js?v=20260917b HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:16] "GET /js/site_navigation_v1_6.js?v=20260917c HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:16] "GET /css/site_v1_6.css HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:16] "GET /css/site_font_size_v1_6.css?v=20260917f HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:16] "GET /css/site_utility_v1_6.css?v=20260917b HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:17] "GET /mps/mps_6_2.html HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:17] code 404, message File not found
127.0.0.1 - - [19/Sep/2026 02:57:17] "GET /img/mps_fluid_count.files/image022.gif HTTP/1.1" 404 -
127.0.0.1 - - [19/Sep/2026 02:57:19] "GET /mps/mps_1.html HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:19] "GET /css/lib.css HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:19] "GET /img/shiki2.gif HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:19] "GET /img/shiki1.gif HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:19] "GET /css/responsive.css HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:19] "GET /css/math.css HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:19] "GET /css/site_v1_6.css?v=20260917e HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:19] "GET /css/site_utility_v1_6.css?v=20260917e HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:19] "GET /css/site_font_size_v1_6.css?v=20260917e HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:19] "GET /css/site_readability_v1_6.css?v=20260917a HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:19] "GET /ad.html HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:19] "GET /questionnaire.html HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:19] "GET /menu.html HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:19] "GET /img/title.jpg HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:21] "GET /footer.html HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:21] "GET /js/site_navigation_v1_6.js?v=20260917c HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:21] "GET /js/site_home_cleanup_v1_6.js?v=20260917b HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:21] "GET /js/site_utility_v1_6.js?v=20260917d HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:21] "GET /js/site_formula_guard_v1_6.js?v=20260917b HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:21] "GET /js/site_font_size_v1_6.js?v=20260917f HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:21] "GET /css/site_v1_6.css HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:21] "GET /css/site_font_size_v1_6.css?v=20260917f HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:21] "GET /css/site_utility_v1_6.css?v=20260917b HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:21] "GET /mps/mps_2.html HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:22] "GET /mps/mps_3.html HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:23] "GET /css/lib.css HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:23] "GET /css/responsive.css HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:23] "GET /css/math.css HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:23] "GET /css/site_v1_6.css?v=20260917e HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:23] "GET /css/site_font_size_v1_6.css?v=20260917e HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:23] "GET /css/site_utility_v1_6.css?v=20260917e HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:23] "GET /css/site_readability_v1_6.css?v=20260917a HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:24] "GET /mps/mps_4.html HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:24] "GET /img/shiki1.gif HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:24] "GET /img/shiki2.gif HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:24] "GET /ad.html HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:24] "GET /questionnaire.html HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:24] "GET /menu.html HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:24] "GET /img/title.jpg HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:25] "GET /footer.html HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:25] "GET /js/site_navigation_v1_6.js?v=20260917c HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:25] "GET /js/site_font_size_v1_6.js?v=20260917f HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:25] "GET /js/site_home_cleanup_v1_6.js?v=20260917b HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:25] "GET /js/site_formula_guard_v1_6.js?v=20260917b HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:25] "GET /js/site_utility_v1_6.js?v=20260917d HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:25] "GET /css/site_v1_6.css HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:25] "GET /css/site_font_size_v1_6.css?v=20260917f HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:25] "GET /css/site_utility_v1_6.css?v=20260917b HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:26] "GET /mps/mps_5.html HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:27] "GET /css/lib.css HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:27] "GET /css/responsive.css HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:27] "GET /css/math.css HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:27] "GET /css/site_v1_6.css?v=20260917e HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:27] "GET /css/site_font_size_v1_6.css?v=20260917e HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:27] "GET /css/site_utility_v1_6.css?v=20260917e HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:27] "GET /css/site_readability_v1_6.css?v=20260917a HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:28] "GET /mps/mps_6_1.html HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:29] "GET /mps/mps_6_2.html HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 02:57:29] "GET /img/shiki1.gif HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:29] "GET /img/shiki2.gif HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:29] code 404, message File not found
127.0.0.1 - - [19/Sep/2026 02:57:29] "GET /img/mps_fluid_count.files/image022.gif HTTP/1.1" 404 -
127.0.0.1 - - [19/Sep/2026 02:57:29] "GET /ad.html HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:29] "GET /menu.html HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:29] "GET /questionnaire.html HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:29] "GET /img/title.jpg HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:29] "GET /footer.html HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:30] "GET /js/site_navigation_v1_6.js?v=20260917c HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:30] "GET /js/site_font_size_v1_6.js?v=20260917f HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:30] "GET /js/site_home_cleanup_v1_6.js?v=20260917b HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:30] "GET /js/site_formula_guard_v1_6.js?v=20260917b HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:30] "GET /js/site_utility_v1_6.js?v=20260917d HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:30] "GET /css/site_v1_6.css HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:30] "GET /css/site_font_size_v1_6.css?v=20260917f HTTP/1.1" 304 -
127.0.0.1 - - [19/Sep/2026 02:57:30] "GET /css/site_utility_v1_6.css?v=20260917b HTTP/1.1" 304 -
~~~
