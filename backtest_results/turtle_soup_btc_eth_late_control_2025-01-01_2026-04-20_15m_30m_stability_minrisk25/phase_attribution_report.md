# ICT Phase Attribution Report

- events: `backtest_results\turtle_soup_btc_eth_late_control_2025-01-01_2026-04-20_15m_30m_stability_minrisk25\events.csv`
- realized R uses `net_managed_outcome_r` when available, otherwise `managed_outcome_r`.

| phase | scope | group | filter_name | threshold | dedupe_session | dedupe_selection | trade_count | min_trades | sample_valid | win_rate_pct | expectancy_r | profit_factor | max_drawdown_r | total_pnl_r | avg_decision_score | avg_target_distance_r | avg_risk_bps | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | ALL | ALL | model_rules | 0 | True | first | 129 | 30 | True | 78.294574 | 0.307165 | 2.142191 | 4.302191 | 39.624265 | 61.705426 | 3.454979 | 50.01654 | 0.249373 | -6.3e-05 | 0.24931 |
| train | ALL | ALL | model_rules | 0 | True | first | 43 | 30 | True | 79.069767 | 0.331246 | 2.293852 | 2.923616 | 14.243563 | 61.162791 | 3.95144 | 55.632372 | 0.23598 | 0.0 | 0.23598 |
| train | by_timeframe | 15m | model_rules | 0 | True | first | 27 | 30 | False | 74.074074 | 0.238045 | 1.748761 | 1.853031 | 6.427208 | 61.851852 | 4.221432 | 49.095216 | 0.243437 | 0.0 | 0.243437 |
| train | by_timeframe | 30m | model_rules | 0 | True | first | 16 | 30 | False | 87.5 | 0.488522 | 4.223425 | 1.611966 | 7.816355 | 60.0 | 3.495829 | 66.663822 | 0.223395 | 0.0 | 0.223395 |
| train | by_symbol | BTCUSDT | model_rules | 0 | True | first | 11 | 30 | False | 100.0 | 0.716897 | inf | 0.0 | 7.885872 | 56.363636 | 3.315591 | 62.84241 | 0.22771 | 0.0 | 0.22771 |
| train | by_symbol | ETHUSDT | model_rules | 0 | True | first | 32 | 30 | True | 71.875 | 0.198678 | 1.577518 | 3.956486 | 6.357691 | 62.8125 | 4.170014 | 53.153921 | 0.238822 | 0.0 | 0.238822 |
| train | by_direction | long | model_rules | 0 | True | first | 15 | 30 | False | 73.333333 | 0.210128 | 1.641209 | 2.490737 | 3.151927 | 61.333333 | 3.334687 | 42.155812 | 0.256538 | 0.0 | 0.256538 |
| train | by_direction | short | model_rules | 0 | True | first | 28 | 30 | False | 82.142857 | 0.39613 | 2.820373 | 1.662556 | 11.091636 | 61.071429 | 4.281844 | 62.851958 | 0.224966 | 0.0 | 0.224966 |
| train | by_session_label | custom | model_rules | 0 | True | first | 4 | 30 | False | 100.0 | 0.689895 | inf | 0.0 | 2.75958 | 62.5 | 7.134443 | 32.424742 | 0.310105 | 0.0 | 0.310105 |
| train | by_session_label | london_open | model_rules | 0 | True | first | 15 | 30 | False | 73.333333 | 0.193563 | 1.577172 | 3.747686 | 2.903439 | 64.666667 | 4.856845 | 50.826278 | 0.273104 | 0.0 | 0.273104 |
| train | by_session_label | ny_open | model_rules | 0 | True | first | 24 | 30 | False | 79.166667 | 0.357523 | 2.435306 | 2.018593 | 8.580544 | 58.75 | 2.855062 | 62.504119 | 0.200422 | 0.0 | 0.200422 |
| train | by_score_bucket | high | model_rules | 0 | True | first | 21 | 30 | False | 76.190476 | 0.249543 | 1.85635 | 3.747686 | 5.240393 | 70.0 | 6.269354 | 45.671387 | 0.274267 | 0.0 | 0.274267 |
| train | by_score_bucket | medium | model_rules | 0 | True | first | 22 | 30 | False | 81.818182 | 0.409235 | 2.841441 | 1.551004 | 9.00317 | 52.727273 | 1.738886 | 65.140585 | 0.199432 | 0.0 | 0.199432 |
| train | by_no_trade_reasons | none | model_rules | 0 | True | first | 21 | 30 | False | 76.190476 | 0.249543 | 1.85635 | 3.747686 | 5.240393 | 70.0 | 6.269354 | 45.671387 | 0.274267 | 0.0 | 0.274267 |
| train | by_no_trade_reasons | target_rr_below_2 | model_rules | 0 | True | first | 16 | 30 | False | 87.5 | 0.530481 | 4.532709 | 1.251279 | 8.487694 | 50.0 | 1.464955 | 73.528329 | 0.181437 | 0.0 | 0.181437 |
| train | by_no_trade_reasons | target_rr_below_3 | model_rules | 0 | True | first | 6 | 30 | False | 66.666667 | 0.085913 | 1.207302 | 1.662527 | 0.515476 | 60.0 | 2.469369 | 42.773268 | 0.247421 | 0.0 | 0.247421 |
| validation | ALL | ALL | model_rules | 0 | True | first | 43 | 30 | True | 76.744186 | 0.270251 | 1.920704 | 2.546344 | 11.62081 | 60.930233 | 3.053684 | 48.942799 | 0.25472 | 0.000193 | 0.254913 |
| validation | by_timeframe | 15m | model_rules | 0 | True | first | 25 | 30 | False | 76.0 | 0.257393 | 1.856142 | 2.546344 | 6.434814 | 60.0 | 2.636338 | 51.994659 | 0.245889 | 0.0 | 0.245889 |
| validation | by_timeframe | 30m | model_rules | 0 | True | first | 18 | 30 | False | 77.777778 | 0.288111 | 2.015747 | 1.699113 | 5.185996 | 62.222222 | 3.633332 | 44.704105 | 0.266984 | 0.00046 | 0.267445 |
| validation | by_symbol | BTCUSDT | model_rules | 0 | True | first | 14 | 30 | False | 57.142857 | -0.154529 | 0.716545 | 2.513452 | -2.163413 | 58.571429 | 2.30508 | 45.546272 | 0.266941 | 0.000592 | 0.267533 |
| validation | by_symbol | ETHUSDT | model_rules | 0 | True | first | 29 | 30 | False | 86.206897 | 0.475318 | 3.76272 | 1.354275 | 13.784223 | 62.068966 | 3.41508 | 50.582502 | 0.24882 | 0.0 | 0.24882 |
| validation | by_direction | long | model_rules | 0 | True | first | 28 | 30 | False | 71.428571 | 0.179551 | 1.498681 | 1.566312 | 5.027429 | 61.428571 | 3.105048 | 54.576965 | 0.234094 | 0.0 | 0.234094 |
| validation | by_direction | short | model_rules | 0 | True | first | 15 | 30 | False | 86.666667 | 0.439559 | 3.595609 | 1.302334 | 6.593381 | 60.0 | 2.957806 | 38.42569 | 0.293222 | 0.000552 | 0.293775 |
| validation | by_session_label | custom | model_rules | 0 | True | first | 3 | 30 | False | 0.0 | -1.221816 | 0.0 | 3.665448 | -3.665448 | 60.0 | 2.353302 | 46.469618 | 0.221816 | 0.0 | 0.221816 |
| validation | by_session_label | london_open | model_rules | 0 | True | first | 11 | 30 | False | 90.909091 | 0.538889 | 5.463332 | 1.328106 | 5.927778 | 61.818182 | 3.278494 | 42.928752 | 0.279293 | 0.0 | 0.279293 |
| validation | by_session_label | ny_open | model_rules | 0 | True | first | 29 | 30 | False | 79.310345 | 0.322706 | 2.226842 | 1.699113 | 9.35848 | 60.689655 | 3.040865 | 51.479836 | 0.248803 | 0.000286 | 0.249089 |
| validation | by_score_bucket | high | model_rules | 0 | True | first | 17 | 30 | False | 82.352941 | 0.353349 | 2.50245 | 1.393282 | 6.006928 | 70.0 | 4.867676 | 40.381333 | 0.29371 | 0.0 | 0.29371 |
| validation | by_score_bucket | medium | model_rules | 0 | True | first | 26 | 30 | False | 73.076923 | 0.215919 | 1.650993 | 2.546344 | 5.613882 | 55.0 | 1.867613 | 54.540681 | 0.229226 | 0.000319 | 0.229545 |
| validation | by_no_trade_reasons | none | model_rules | 0 | True | first | 17 | 30 | False | 82.352941 | 0.353349 | 2.50245 | 1.393282 | 6.006928 | 70.0 | 4.867676 | 40.381333 | 0.29371 | 0.0 | 0.29371 |
| validation | by_no_trade_reasons | target_rr_below_2 | model_rules | 0 | True | first | 13 | 30 | False | 61.538462 | 0.003833 | 1.008198 | 3.628953 | 0.049823 | 50.0 | 1.247668 | 67.552301 | 0.19415 | 0.000637 | 0.194787 |
| validation | by_no_trade_reasons | target_rr_below_3 | model_rules | 0 | True | first | 13 | 30 | False | 84.615385 | 0.428005 | 3.185117 | 2.546344 | 5.564059 | 60.0 | 2.487559 | 41.52906 | 0.264303 | 0.0 | 0.264303 |
| test | ALL | ALL | model_rules | 0 | True | first | 43 | 30 | True | 79.069767 | 0.319997 | 2.243984 | 3.789843 | 13.759892 | 63.023256 | 3.359811 | 45.474448 | 0.257419 | -0.000382 | 0.257037 |
| test | by_timeframe | 15m | model_rules | 0 | True | first | 22 | 30 | False | 81.818182 | 0.36211 | 2.634524 | 2.393861 | 7.966417 | 61.818182 | 3.076407 | 40.508577 | 0.274254 | 0.0 | 0.274254 |
| test | by_timeframe | 30m | model_rules | 0 | True | first | 21 | 30 | False | 76.190476 | 0.27588 | 1.936348 | 2.471467 | 5.793475 | 64.285714 | 3.656711 | 50.676789 | 0.239783 | -0.000783 | 0.239 |
| test | by_symbol | BTCUSDT | model_rules | 0 | True | first | 15 | 30 | False | 86.666667 | 0.462781 | 3.931088 | 1.209453 | 6.941719 | 61.333333 | 2.838473 | 43.6061 | 0.271123 | -0.000571 | 0.270552 |
| test | by_symbol | ETHUSDT | model_rules | 0 | True | first | 28 | 30 | False | 75.0 | 0.243506 | 1.784343 | 3.789843 | 6.818173 | 63.928571 | 3.6391 | 46.475348 | 0.250078 | -0.000281 | 0.249796 |
| test | by_direction | long | model_rules | 0 | True | first | 23 | 30 | False | 73.913043 | 0.209909 | 1.654679 | 2.506442 | 4.827909 | 63.478261 | 3.477787 | 41.358549 | 0.268352 | 0.0 | 0.268352 |
| test | by_direction | short | model_rules | 0 | True | first | 20 | 30 | False | 85.0 | 0.446599 | 3.422769 | 1.778298 | 8.931983 | 62.5 | 3.224139 | 50.207731 | 0.244847 | -0.000822 | 0.244024 |
| test | by_session_label | custom | model_rules | 0 | True | first | 4 | 30 | False | 100.0 | 0.720604 | inf | 0.0 | 2.882415 | 65.0 | 4.575138 | 37.110893 | 0.279396 | 0.0 | 0.279396 |
| test | by_session_label | london_open | model_rules | 0 | True | first | 12 | 30 | False | 66.666667 | 0.011283 | 1.026154 | 2.619947 | 0.135395 | 68.333333 | 4.243616 | 31.9439 | 0.32205 | 0.0 | 0.32205 |
| test | by_session_label | ny_open | model_rules | 0 | True | first | 27 | 30 | False | 81.481481 | 0.397855 | 2.825575 | 2.393861 | 10.742082 | 60.37037 | 2.786961 | 52.72707 | 0.225438 | -0.000609 | 0.224829 |
| test | by_score_bucket | high | model_rules | 0 | True | first | 22 | 30 | False | 81.818182 | 0.340085 | 2.488989 | 3.789843 | 7.481862 | 70.0 | 4.687974 | 37.979277 | 0.296637 | -0.000358 | 0.296279 |
| test | by_score_bucket | medium | model_rules | 0 | True | first | 21 | 30 | False | 76.190476 | 0.298954 | 2.040036 | 3.715895 | 6.27803 | 55.714286 | 1.968402 | 53.326531 | 0.216334 | -0.000408 | 0.215926 |
| test | by_no_trade_reasons | none | model_rules | 0 | True | first | 22 | 30 | False | 81.818182 | 0.340085 | 2.488989 | 3.789843 | 7.481862 | 70.0 | 4.687974 | 37.979277 | 0.296637 | -0.000358 | 0.296279 |
| test | by_no_trade_reasons | target_rr_below_2 | model_rules | 0 | True | first | 9 | 30 | False | 88.888889 | 0.542818 | 4.69534 | 1.322034 | 4.885365 | 50.0 | 1.305246 | 58.808502 | 0.215075 | -0.000952 | 0.214123 |
| test | by_no_trade_reasons | target_rr_below_3 | model_rules | 0 | True | first | 12 | 30 | False | 66.666667 | 0.116055 | 1.295411 | 3.555469 | 1.392665 | 60.0 | 2.46577 | 49.215052 | 0.217278 | 0.0 | 0.217278 |
