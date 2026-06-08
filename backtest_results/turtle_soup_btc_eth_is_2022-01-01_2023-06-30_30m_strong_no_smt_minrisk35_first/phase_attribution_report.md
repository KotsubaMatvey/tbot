# ICT Phase Attribution Report

- events: `backtest_results\turtle_soup_btc_eth_is_2022-01-01_2023-06-30_30m_strong_no_smt_minrisk35_first\events.csv`
- realized R uses `net_managed_outcome_r` when available, otherwise `managed_outcome_r`.

| phase | scope | group | filter_name | threshold | dedupe_session | dedupe_selection | trade_count | min_trades | sample_valid | win_rate_pct | expectancy_r | profit_factor | max_drawdown_r | total_pnl_r | avg_decision_score | avg_target_distance_r | avg_risk_bps | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | ALL | ALL | model_rules | 0 | True | first | 133 | 30 | True | 78.195489 | 0.360814 | 2.390905 | 3.749911 | 47.988199 | 58.87218 | 3.185367 | 59.549722 | 0.187947 | 0.000107 | 0.188054 |
| train | ALL | ALL | model_rules | 0 | True | first | 45 | 30 | True | 73.333333 | 0.283223 | 1.899279 | 3.12056 | 12.745057 | 61.333333 | 3.78427 | 62.281691 | 0.182402 | 0.001041 | 0.183443 |
| train | by_symbol | BTCUSDT | model_rules | 0 | True | first | 21 | 30 | False | 71.428571 | 0.21725 | 1.631311 | 2.051735 | 4.562259 | 61.428571 | 3.549472 | 51.349712 | 0.209639 | 0.001682 | 0.211321 |
| train | by_symbol | ETHUSDT | model_rules | 0 | True | first | 24 | 30 | False | 75.0 | 0.34095 | 2.178076 | 2.521969 | 8.182798 | 61.25 | 3.989718 | 71.847172 | 0.15857 | 0.00048 | 0.15905 |
| train | by_direction | long | model_rules | 0 | True | first | 24 | 30 | False | 70.833333 | 0.234199 | 1.68221 | 2.267102 | 5.620778 | 59.583333 | 3.240514 | 63.625364 | 0.180746 | 0.001722 | 0.182468 |
| train | by_direction | short | model_rules | 0 | True | first | 21 | 30 | False | 76.190476 | 0.339251 | 2.200696 | 1.614176 | 7.124279 | 63.333333 | 4.405705 | 60.746064 | 0.184296 | 0.000263 | 0.184558 |
| train | by_session_label | custom | model_rules | 0 | True | first | 8 | 30 | False | 87.5 | 0.552469 | 4.668425 | 1.204808 | 4.419748 | 63.75 | 4.075385 | 58.778868 | 0.197532 | 0.0 | 0.197532 |
| train | by_session_label | london_open | model_rules | 0 | True | first | 16 | 30 | False | 93.75 | 0.704402 | 10.72316 | 1.159132 | 11.270426 | 64.375 | 5.04949 | 66.564947 | 0.170254 | 0.000345 | 0.170598 |
| train | by_session_label | ny_open | model_rules | 0 | True | first | 21 | 30 | False | 52.380952 | -0.140244 | 0.750595 | 5.18254 | -2.945117 | 58.095238 | 2.709391 | 60.352666 | 0.185895 | 0.001968 | 0.187863 |
| train | by_score_bucket | high | model_rules | 0 | True | first | 22 | 30 | False | 72.727273 | 0.253023 | 1.774396 | 3.6619 | 5.566513 | 70.0 | 5.915909 | 52.60051 | 0.201522 | 0.0 | 0.201522 |
| train | by_score_bucket | medium | model_rules | 0 | True | first | 23 | 30 | False | 73.913043 | 0.312111 | 2.027806 | 2.724589 | 7.178544 | 53.043478 | 1.74531 | 71.541951 | 0.164114 | 0.002036 | 0.16615 |
| train | by_no_trade_reasons | none | model_rules | 0 | True | first | 22 | 30 | False | 72.727273 | 0.253023 | 1.774396 | 3.6619 | 5.566513 | 70.0 | 5.915909 | 52.60051 | 0.201522 | 0.0 | 0.201522 |
| train | by_no_trade_reasons | target_rr_below_2 | model_rules | 0 | True | first | 16 | 30 | False | 81.25 | 0.464954 | 3.153477 | 1.2142 | 7.439259 | 50.0 | 1.42146 | 77.10101 | 0.157119 | 0.002927 | 0.160046 |
| train | by_no_trade_reasons | target_rr_below_3 | model_rules | 0 | True | first | 7 | 30 | False | 57.142857 | -0.037245 | 0.926139 | 2.360664 | -0.260715 | 60.0 | 2.48554 | 58.835528 | 0.180102 | 0.0 | 0.180102 |
| validation | ALL | ALL | model_rules | 0 | True | first | 46 | 30 | True | 84.782609 | 0.48136 | 3.614214 | 3.749911 | 22.142564 | 59.565217 | 3.614289 | 58.911155 | 0.190921 | 0.0 | 0.190921 |
| validation | by_symbol | BTCUSDT | model_rules | 0 | True | first | 25 | 30 | False | 92.0 | 0.598215 | 7.065917 | 1.277242 | 14.955366 | 57.6 | 3.376361 | 56.667319 | 0.198782 | 0.0 | 0.198782 |
| validation | by_symbol | ETHUSDT | model_rules | 0 | True | first | 21 | 30 | False | 76.190476 | 0.342248 | 2.196951 | 2.472669 | 7.187198 | 61.904762 | 3.897537 | 61.582389 | 0.181562 | 0.0 | 0.181562 |
| validation | by_direction | long | model_rules | 0 | True | first | 20 | 30 | False | 85.0 | 0.461933 | 3.595169 | 1.226668 | 9.238667 | 58.5 | 3.75848 | 63.019396 | 0.184313 | 0.0 | 0.184313 |
| validation | by_direction | short | model_rules | 0 | True | first | 26 | 30 | False | 84.615385 | 0.496304 | 3.628023 | 2.523243 | 12.903897 | 60.384615 | 3.503373 | 55.75097 | 0.196004 | 0.0 | 0.196004 |
| validation | by_session_label | custom | model_rules | 0 | True | first | 9 | 30 | False | 88.888889 | 0.5519 | 4.888924 | 1.277242 | 4.967097 | 56.666667 | 4.623118 | 63.09319 | 0.185404 | 0.0 | 0.185404 |
| validation | by_session_label | london_open | model_rules | 0 | True | first | 11 | 30 | False | 63.636364 | 0.01977 | 1.045249 | 2.472669 | 0.217466 | 66.363636 | 4.971922 | 57.924443 | 0.188339 | 0.0 | 0.188339 |
| validation | by_session_label | ny_open | model_rules | 0 | True | first | 26 | 30 | False | 92.307692 | 0.652231 | 8.104693 | 2.386873 | 16.958001 | 57.692308 | 2.690696 | 57.880983 | 0.193923 | 0.0 | 0.193923 |
| validation | by_score_bucket | high | model_rules | 0 | True | first | 18 | 30 | False | 77.777778 | 0.361353 | 2.355631 | 1.606592 | 6.504359 | 70.0 | 6.984135 | 56.642115 | 0.194202 | 0.0 | 0.194202 |
| validation | by_score_bucket | medium | model_rules | 0 | True | first | 28 | 30 | False | 89.285714 | 0.558507 | 5.258731 | 2.50391 | 15.638205 | 52.857143 | 1.44796 | 60.369824 | 0.188811 | 0.0 | 0.188811 |
| validation | by_no_trade_reasons | none | model_rules | 0 | True | first | 18 | 30 | False | 77.777778 | 0.361353 | 2.355631 | 1.606592 | 6.504359 | 70.0 | 6.984135 | 56.642115 | 0.194202 | 0.0 | 0.194202 |
| validation | by_no_trade_reasons | target_rr_below_2 | model_rules | 0 | True | first | 20 | 30 | False | 95.0 | 0.661031 | 11.35091 | 1.277242 | 13.220617 | 50.0 | 1.04491 | 62.623254 | 0.185215 | 0.0 | 0.185215 |
| validation | by_no_trade_reasons | target_rr_below_3 | model_rules | 0 | True | first | 8 | 30 | False | 75.0 | 0.302198 | 2.009519 | 1.226668 | 2.417588 | 60.0 | 2.455584 | 54.736248 | 0.197802 | 0.0 | 0.197802 |
| test | ALL | ALL | model_rules | 0 | True | first | 46 | 30 | True | 78.26087 | 0.353539 | 2.371366 | 2.966217 | 16.262794 | 55.434783 | 2.156702 | 56.577108 | 0.192266 | -0.000707 | 0.191558 |
| test | by_symbol | BTCUSDT | model_rules | 0 | True | first | 15 | 30 | False | 86.666667 | 0.499122 | 4.227657 | 2.319587 | 7.486831 | 54.666667 | 2.004215 | 52.113572 | 0.203688 | 0.0 | 0.203688 |
| test | by_symbol | ETHUSDT | model_rules | 0 | True | first | 31 | 30 | True | 74.193548 | 0.283096 | 1.919986 | 2.338794 | 8.775963 | 55.806452 | 2.230487 | 58.736884 | 0.186738 | -0.00105 | 0.185689 |
| test | by_direction | long | model_rules | 0 | True | first | 19 | 30 | False | 84.210526 | 0.439892 | 3.324784 | 1.262031 | 8.357939 | 55.789474 | 1.917088 | 57.244802 | 0.195345 | 0.000262 | 0.195607 |
| test | by_direction | short | model_rules | 0 | True | first | 27 | 30 | False | 74.074074 | 0.292772 | 1.956578 | 3.066812 | 7.904855 | 55.185185 | 2.32532 | 56.10725 | 0.190099 | -0.001389 | 0.188709 |
| test | by_session_label | custom | model_rules | 0 | True | first | 7 | 30 | False | 85.714286 | 0.530318 | 4.280931 | 1.131455 | 3.712226 | 58.571429 | 2.230285 | 56.593709 | 0.183968 | 0.0 | 0.183968 |
| test | by_session_label | london_open | model_rules | 0 | True | first | 6 | 30 | False | 83.333333 | 0.440825 | 3.102585 | 1.25795 | 2.644947 | 63.333333 | 5.024364 | 45.193511 | 0.225842 | 0.0 | 0.225842 |
| test | by_session_label | ny_open | model_rules | 0 | True | first | 33 | 30 | True | 75.757576 | 0.30017 | 2.046064 | 3.801339 | 9.905621 | 53.333333 | 1.619701 | 58.643332 | 0.187921 | -0.000986 | 0.186935 |
| test | by_score_bucket | high | model_rules | 0 | True | first | 8 | 30 | False | 87.5 | 0.54257 | 4.547123 | 1.223684 | 4.340558 | 70.0 | 5.084866 | 48.263304 | 0.210537 | -0.003107 | 0.20743 |
| test | by_score_bucket | medium | model_rules | 0 | True | first | 38 | 30 | True | 76.315789 | 0.313743 | 2.121023 | 3.802509 | 11.922236 | 52.368421 | 1.540247 | 58.327383 | 0.188419 | -0.000202 | 0.188217 |
| test | by_no_trade_reasons | none | model_rules | 0 | True | first | 8 | 30 | False | 87.5 | 0.54257 | 4.547123 | 1.223684 | 4.340558 | 70.0 | 5.084866 | 48.263304 | 0.210537 | -0.003107 | 0.20743 |
| test | by_no_trade_reasons | target_rr_below_2 | model_rules | 0 | True | first | 29 | 30 | False | 72.413793 | 0.233183 | 1.711545 | 4.564319 | 6.7623 | 50.0 | 1.261582 | 60.400171 | 0.183443 | -0.000265 | 0.183178 |
| test | by_no_trade_reasons | target_rr_below_3 | model_rules | 0 | True | first | 9 | 30 | False | 88.888889 | 0.573326 | 5.560443 | 1.131455 | 5.159936 | 60.0 | 2.438166 | 51.648399 | 0.204452 | 0.0 | 0.204452 |
