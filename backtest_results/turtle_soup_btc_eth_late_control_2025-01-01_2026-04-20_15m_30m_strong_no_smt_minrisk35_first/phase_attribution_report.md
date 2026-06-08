# ICT Phase Attribution Report

- events: `backtest_results\turtle_soup_btc_eth_late_control_2025-01-01_2026-04-20_15m_30m_strong_no_smt_minrisk35_first\events.csv`
- realized R uses `net_managed_outcome_r` when available, otherwise `managed_outcome_r`.

| phase | scope | group | filter_name | threshold | dedupe_session | dedupe_selection | trade_count | min_trades | sample_valid | win_rate_pct | expectancy_r | profit_factor | max_drawdown_r | total_pnl_r | avg_decision_score | avg_target_distance_r | avg_risk_bps | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | ALL | ALL | model_rules | 0 | True | first | 82 | 30 | True | 73.170732 | 0.260068 | 1.806924 | 2.977198 | 21.325562 | 59.390244 | 2.876589 | 63.83521 | 0.188658 | -0.000126 | 0.188532 |
| train | ALL | ALL | model_rules | 0 | True | first | 27 | 30 | False | 62.962963 | 0.052021 | 1.116413 | 2.977198 | 1.404562 | 58.148148 | 3.122618 | 68.215631 | 0.184752 | -8.1e-05 | 0.184671 |
| train | by_timeframe | 15m | model_rules | 0 | True | first | 18 | 30 | False | 61.111111 | 0.026894 | 1.056395 | 2.490737 | 0.484085 | 58.888889 | 3.076086 | 58.364603 | 0.195329 | 0.0 | 0.195329 |
| train | by_timeframe | 30m | model_rules | 0 | True | first | 9 | 30 | False | 66.666667 | 0.102275 | 1.264384 | 2.668698 | 0.920477 | 56.666667 | 3.215682 | 87.917688 | 0.163599 | -0.000242 | 0.163356 |
| train | by_symbol | BTCUSDT | model_rules | 0 | True | first | 8 | 30 | False | 100.0 | 0.732677 | inf | 0.0 | 5.861413 | 53.75 | 1.97264 | 74.791391 | 0.191159 | 0.0 | 0.191159 |
| train | by_symbol | ETHUSDT | model_rules | 0 | True | first | 19 | 30 | False | 47.368421 | -0.234571 | 0.630608 | 7.074302 | -4.456851 | 60.0 | 3.606819 | 65.44689 | 0.182054 | -0.000115 | 0.18194 |
| train | by_direction | long | model_rules | 0 | True | first | 9 | 30 | False | 55.555556 | -0.10486 | 0.808011 | 2.58998 | -0.943743 | 62.222222 | 3.711289 | 48.250808 | 0.215971 | 0.0 | 0.215971 |
| train | by_direction | short | model_rules | 0 | True | first | 18 | 30 | False | 66.666667 | 0.130461 | 1.328444 | 2.308011 | 2.348305 | 56.111111 | 2.828282 | 78.198042 | 0.169142 | -0.000121 | 0.169021 |
| train | by_session_label | london_open | model_rules | 0 | True | first | 8 | 30 | False | 50.0 | -0.23212 | 0.630857 | 3.747686 | -1.856959 | 61.25 | 4.011772 | 50.834937 | 0.23212 | 0.0 | 0.23212 |
| train | by_session_label | ny_open | model_rules | 0 | True | first | 19 | 30 | False | 68.421053 | 0.171659 | 1.463618 | 2.729833 | 3.261521 | 56.842105 | 2.748237 | 75.533818 | 0.164808 | -0.000115 | 0.164693 |
| train | by_score_bucket | high | model_rules | 0 | True | first | 9 | 30 | False | 44.444444 | -0.334928 | 0.507415 | 4.098592 | -3.014353 | 70.0 | 6.05288 | 46.168117 | 0.223817 | 0.0 | 0.223817 |
| train | by_score_bucket | medium | model_rules | 0 | True | first | 18 | 30 | False | 72.222222 | 0.245495 | 1.743183 | 2.726103 | 4.418915 | 52.222222 | 1.657487 | 79.239388 | 0.165219 | -0.000121 | 0.165098 |
| train | by_no_trade_reasons | none | model_rules | 0 | True | first | 9 | 30 | False | 44.444444 | -0.334928 | 0.507415 | 4.098592 | -3.014353 | 70.0 | 6.05288 | 46.168117 | 0.223817 | 0.0 | 0.223817 |
| train | by_no_trade_reasons | target_rr_below_2 | model_rules | 0 | True | first | 14 | 30 | False | 78.571429 | 0.37695 | 2.525523 | 2.326422 | 5.277295 | 50.0 | 1.421293 | 88.141715 | 0.151112 | -0.000156 | 0.150956 |
| train | by_no_trade_reasons | target_rr_below_3 | model_rules | 0 | True | first | 4 | 30 | False | 50.0 | -0.214595 | 0.654797 | 1.662527 | -0.85838 | 60.0 | 2.484163 | 48.081245 | 0.214595 | 0.0 | 0.214595 |
| validation | ALL | ALL | model_rules | 0 | True | first | 27 | 30 | False | 77.777778 | 0.35873 | 2.337127 | 1.702068 | 9.685699 | 58.518519 | 2.682136 | 68.167689 | 0.18104 | 0.000307 | 0.181346 |
| validation | by_timeframe | 15m | model_rules | 0 | True | first | 17 | 30 | False | 76.470588 | 0.315014 | 2.096121 | 1.586594 | 5.355233 | 57.058824 | 2.205006 | 63.975315 | 0.189813 | 0.0 | 0.189813 |
| validation | by_timeframe | 30m | model_rules | 0 | True | first | 10 | 30 | False | 80.0 | 0.433047 | 2.836467 | 1.237872 | 4.330466 | 61.0 | 3.493258 | 75.294724 | 0.166125 | 0.000828 | 0.166953 |
| validation | by_symbol | BTCUSDT | model_rules | 0 | True | first | 7 | 30 | False | 57.142857 | -0.103124 | 0.799958 | 2.488404 | -0.721867 | 55.714286 | 1.994436 | 61.99669 | 0.185091 | 0.001183 | 0.186274 |
| validation | by_symbol | ETHUSDT | model_rules | 0 | True | first | 20 | 30 | False | 85.0 | 0.520378 | 3.863083 | 1.24401 | 10.407566 | 59.5 | 2.922831 | 70.327538 | 0.179622 | 0.0 | 0.179622 |
| validation | by_direction | long | model_rules | 0 | True | first | 18 | 30 | False | 72.222222 | 0.247786 | 1.74264 | 1.932731 | 4.460145 | 59.444444 | 2.851173 | 68.45405 | 0.173439 | 0.0 | 0.173439 |
| validation | by_direction | short | model_rules | 0 | True | first | 9 | 30 | False | 88.888889 | 0.580617 | 5.221401 | 1.237872 | 5.225554 | 56.666667 | 2.344063 | 67.594966 | 0.19624 | 0.00092 | 0.197161 |
| validation | by_session_label | custom | model_rules | 0 | True | first | 3 | 30 | False | 0.0 | -1.221816 | 0.0 | 3.665448 | -3.665448 | 60.0 | 2.353302 | 46.469618 | 0.221816 | 0.0 | 0.221816 |
| validation | by_session_label | london_open | model_rules | 0 | True | first | 6 | 30 | False | 100.0 | 0.826802 | inf | 0.0 | 4.96081 | 61.666667 | 3.302174 | 81.481937 | 0.173198 | 0.0 | 0.173198 |
| validation | by_session_label | ny_open | model_rules | 0 | True | first | 18 | 30 | False | 83.333333 | 0.46613 | 3.344837 | 1.633278 | 8.390337 | 57.222222 | 2.530262 | 67.345951 | 0.176857 | 0.00046 | 0.177317 |
| validation | by_score_bucket | high | model_rules | 0 | True | first | 8 | 30 | False | 87.5 | 0.590035 | 4.77462 | 1.250532 | 4.720283 | 70.0 | 4.93918 | 79.262561 | 0.159965 | 0.0 | 0.159965 |
| validation | by_score_bucket | medium | model_rules | 0 | True | first | 19 | 30 | False | 73.684211 | 0.261338 | 1.828518 | 1.692154 | 4.965416 | 53.684211 | 1.731802 | 63.496163 | 0.189913 | 0.000436 | 0.190349 |
| validation | by_no_trade_reasons | none | model_rules | 0 | True | first | 8 | 30 | False | 87.5 | 0.590035 | 4.77462 | 1.250532 | 4.720283 | 70.0 | 4.93918 | 79.262561 | 0.159965 | 0.0 | 0.159965 |
| validation | by_no_trade_reasons | target_rr_below_2 | model_rules | 0 | True | first | 12 | 30 | False | 66.666667 | 0.131252 | 1.331645 | 3.628953 | 1.575023 | 50.0 | 1.28867 | 72.725011 | 0.166562 | 0.00069 | 0.167252 |
| validation | by_no_trade_reasons | target_rr_below_3 | model_rules | 0 | True | first | 7 | 30 | False | 85.714286 | 0.484342 | 3.725374 | 1.24401 | 3.390393 | 60.0 | 2.491456 | 47.675282 | 0.229944 | 0.0 | 0.229944 |
| test | ALL | ALL | model_rules | 0 | True | first | 28 | 30 | False | 78.571429 | 0.365546 | 2.43771 | 2.393861 | 10.235301 | 61.428571 | 2.826854 | 55.433485 | 0.199772 | -0.000587 | 0.199185 |
| test | by_timeframe | 15m | model_rules | 0 | True | first | 13 | 30 | False | 76.923077 | 0.326924 | 2.195346 | 2.393861 | 4.250014 | 60.0 | 2.566922 | 49.497334 | 0.211537 | 0.0 | 0.211537 |
| test | by_timeframe | 30m | model_rules | 0 | True | first | 15 | 30 | False | 80.0 | 0.399019 | 2.679514 | 2.101327 | 5.985287 | 62.666667 | 3.052128 | 60.57815 | 0.189575 | -0.001096 | 0.188479 |
| test | by_symbol | BTCUSDT | model_rules | 0 | True | first | 9 | 30 | False | 77.777778 | 0.351288 | 2.33496 | 1.209453 | 3.161596 | 60.0 | 2.520266 | 54.601503 | 0.205219 | -0.000952 | 0.204267 |
| test | by_symbol | ETHUSDT | model_rules | 0 | True | first | 19 | 30 | False | 78.947368 | 0.3723 | 2.488931 | 1.234951 | 7.073705 | 62.105263 | 2.97208 | 55.827582 | 0.197192 | -0.000415 | 0.196777 |
| test | by_direction | long | model_rules | 0 | True | first | 15 | 30 | False | 73.333333 | 0.254707 | 1.804192 | 1.562243 | 3.820606 | 62.666667 | 3.171066 | 49.802509 | 0.21196 | 0.0 | 0.21196 |
| test | by_direction | short | model_rules | 0 | True | first | 13 | 30 | False | 84.615385 | 0.493438 | 3.708556 | 1.209453 | 6.414695 | 60.0 | 2.429687 | 61.930766 | 0.185709 | -0.001265 | 0.184444 |
| test | by_session_label | custom | model_rules | 0 | True | first | 2 | 30 | False | 100.0 | 0.770783 | inf | 0.0 | 1.541567 | 70.0 | 4.911367 | 43.651048 | 0.229216 | 0.0 | 0.229216 |
| test | by_session_label | london_open | model_rules | 0 | True | first | 4 | 30 | False | 75.0 | 0.240785 | 1.7799 | 1.234951 | 0.963138 | 70.0 | 3.672166 | 38.73138 | 0.259216 | 0.0 | 0.259216 |
| test | by_session_label | ny_open | model_rules | 0 | True | first | 22 | 30 | False | 77.272727 | 0.351391 | 2.313784 | 2.393861 | 7.730596 | 59.090909 | 2.48366 | 59.541363 | 0.186287 | -0.000748 | 0.18554 |
| test | by_score_bucket | high | model_rules | 0 | True | first | 10 | 30 | False | 80.0 | 0.373415 | 2.552759 | 1.681003 | 3.734147 | 70.0 | 4.197784 | 49.383841 | 0.227373 | -0.000788 | 0.226585 |
| test | by_score_bucket | medium | model_rules | 0 | True | first | 18 | 30 | False | 77.777778 | 0.361175 | 2.379021 | 2.393861 | 6.501154 | 56.666667 | 2.065226 | 58.794399 | 0.184438 | -0.000476 | 0.183962 |
| test | by_no_trade_reasons | none | model_rules | 0 | True | first | 10 | 30 | False | 80.0 | 0.373415 | 2.552759 | 1.681003 | 3.734147 | 70.0 | 4.197784 | 49.383841 | 0.227373 | -0.000788 | 0.226585 |
| test | by_no_trade_reasons | target_rr_below_2 | model_rules | 0 | True | first | 6 | 30 | False | 100.0 | 0.820537 | inf | 0.0 | 4.923222 | 50.0 | 1.188432 | 73.724025 | 0.149636 | -0.001428 | 0.148208 |
| test | by_no_trade_reasons | target_rr_below_3 | model_rules | 0 | True | first | 12 | 30 | False | 66.666667 | 0.131494 | 1.33471 | 3.555469 | 1.577932 | 60.0 | 2.503624 | 51.329586 | 0.201839 | 0.0 | 0.201839 |
