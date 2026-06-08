# ICT Phase Attribution Report

- events: `backtest_results\turtle_soup_btc_eth_is_2022-01-01_2023-06-30_30m_strong_no_smt_first\events.csv`
- realized R uses `net_managed_outcome_r` when available, otherwise `managed_outcome_r`.

| phase | scope | group | filter_name | threshold | dedupe_session | dedupe_selection | trade_count | min_trades | sample_valid | win_rate_pct | expectancy_r | profit_factor | max_drawdown_r | total_pnl_r | avg_decision_score | avg_target_distance_r | avg_risk_bps | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | ALL | ALL | model_rules | 0 | True | first | 234 | 30 | True | 70.940171 | 0.133679 | 1.378827 | 8.455519 | 31.280788 | 61.709402 | 4.092791 | 42.677385 | 0.352608 | 0.000285 | 0.352893 |
| train | ALL | ALL | model_rules | 0 | True | first | 78 | 30 | True | 71.794872 | 0.204855 | 1.593735 | 3.716367 | 15.978724 | 63.205128 | 4.49326 | 53.993573 | 0.251662 | 0.000351 | 0.252013 |
| train | by_symbol | BTCUSDT | model_rules | 0 | True | first | 42 | 30 | True | 71.428571 | 0.186693 | 1.532606 | 2.420516 | 7.841104 | 62.619048 | 4.052539 | 46.923192 | 0.280447 | 0.000377 | 0.280824 |
| train | by_symbol | ETHUSDT | model_rules | 0 | True | first | 36 | 30 | True | 72.222222 | 0.226045 | 1.667562 | 2.521969 | 8.13762 | 63.888889 | 5.007436 | 62.242351 | 0.21808 | 0.00032 | 0.218399 |
| train | by_direction | long | model_rules | 0 | True | first | 37 | 30 | True | 70.27027 | 0.164543 | 1.448306 | 2.804899 | 6.088073 | 62.162162 | 4.159052 | 57.089398 | 0.230427 | 0.000591 | 0.231018 |
| train | by_direction | short | model_rules | 0 | True | first | 41 | 30 | True | 73.170732 | 0.241235 | 1.741872 | 2.25196 | 9.890651 | 64.146341 | 4.794863 | 51.199781 | 0.270825 | 0.000135 | 0.27096 |
| train | by_session_label | custom | model_rules | 0 | True | first | 14 | 30 | False | 78.571429 | 0.289985 | 2.005074 | 1.421599 | 4.059784 | 63.571429 | 4.196655 | 54.664916 | 0.255425 | 0.0 | 0.255425 |
| train | by_session_label | london_open | model_rules | 0 | True | first | 28 | 30 | False | 71.428571 | 0.24773 | 1.766368 | 3.796575 | 6.936441 | 66.785714 | 5.875327 | 53.759677 | 0.252073 | 0.000197 | 0.25227 |
| train | by_session_label | ny_open | model_rules | 0 | True | first | 36 | 30 | True | 69.444444 | 0.138403 | 1.36048 | 5.445182 | 4.982499 | 60.277778 | 3.533666 | 53.914415 | 0.249879 | 0.000607 | 0.250486 |
| train | by_score_bucket | high | model_rules | 0 | True | first | 46 | 30 | True | 65.217391 | 0.050781 | 1.117974 | 5.218174 | 2.335931 | 70.0 | 6.379498 | 45.191721 | 0.297045 | 0.0 | 0.297045 |
| train | by_score_bucket | medium | model_rules | 0 | True | first | 32 | 30 | True | 81.25 | 0.426337 | 2.918331 | 2.510806 | 13.642793 | 53.4375 | 1.781793 | 66.646236 | 0.186424 | 0.000855 | 0.187279 |
| train | by_no_trade_reasons | none | model_rules | 0 | True | first | 46 | 30 | True | 65.217391 | 0.050781 | 1.117974 | 5.218174 | 2.335931 | 70.0 | 6.379498 | 45.191721 | 0.297045 | 0.0 | 0.297045 |
| train | by_no_trade_reasons | target_rr_below_2 | model_rules | 0 | True | first | 21 | 30 | False | 90.47619 | 0.623568 | 6.845082 | 1.174349 | 13.094936 | 50.0 | 1.378569 | 75.458615 | 0.167306 | 0.001303 | 0.168609 |
| train | by_no_trade_reasons | target_rr_below_3 | model_rules | 0 | True | first | 11 | 30 | False | 63.636364 | 0.049805 | 1.112462 | 2.510806 | 0.547857 | 60.0 | 2.551585 | 49.822605 | 0.222922 | 0.0 | 0.222922 |
| validation | ALL | ALL | model_rules | 0 | True | first | 78 | 30 | True | 64.102564 | 0.007298 | 1.017146 | 6.222507 | 0.569265 | 61.282051 | 4.051388 | 36.87913 | 0.411133 | 0.000667 | 0.4118 |
| validation | by_symbol | BTCUSDT | model_rules | 0 | True | first | 41 | 30 | True | 63.414634 | -0.027643 | 0.933907 | 6.835125 | -1.133347 | 62.439024 | 4.454422 | 31.412638 | 0.511334 | 0.0 | 0.511334 |
| validation | by_symbol | ETHUSDT | model_rules | 0 | True | first | 37 | 30 | True | 64.864865 | 0.046017 | 1.106058 | 4.068052 | 1.702612 | 60.0 | 3.604783 | 42.936593 | 0.300099 | 0.001407 | 0.301506 |
| validation | by_direction | long | model_rules | 0 | True | first | 38 | 30 | True | 71.052632 | 0.102754 | 1.290403 | 4.284675 | 3.904645 | 61.315789 | 3.597138 | 36.800415 | 0.390784 | 0.002024 | 0.392808 |
| validation | by_direction | short | model_rules | 0 | True | first | 40 | 30 | True | 57.5 | -0.083385 | 0.831169 | 7.436026 | -3.33538 | 61.25 | 4.482925 | 36.953909 | 0.430464 | -0.000621 | 0.429843 |
| validation | by_session_label | custom | model_rules | 0 | True | first | 11 | 30 | False | 63.636364 | 0.167807 | 1.608662 | 1.321691 | 1.845877 | 59.090909 | 4.224442 | 37.749817 | 0.455679 | 0.0 | 0.455679 |
| validation | by_session_label | london_open | model_rules | 0 | True | first | 26 | 30 | False | 53.846154 | -0.220429 | 0.60386 | 7.146994 | -5.731154 | 64.615385 | 5.387851 | 31.387478 | 0.498016 | 0.002767 | 0.500783 |
| validation | by_session_label | ny_open | model_rules | 0 | True | first | 41 | 30 | True | 70.731707 | 0.108647 | 1.283708 | 6.326457 | 4.454542 | 59.756098 | 3.157445 | 40.128041 | 0.344085 | -0.000485 | 0.3436 |
| validation | by_score_bucket | high | model_rules | 0 | True | first | 37 | 30 | True | 54.054054 | -0.210821 | 0.607513 | 10.510104 | -7.800379 | 70.0 | 6.793707 | 26.95464 | 0.5609 | 0.001273 | 0.562172 |
| validation | by_score_bucket | medium | model_rules | 0 | True | first | 41 | 30 | True | 73.170732 | 0.204138 | 1.628019 | 4.089201 | 8.369644 | 53.414634 | 1.576611 | 45.835376 | 0.275977 | 0.000121 | 0.276099 |
| validation | by_no_trade_reasons | none | model_rules | 0 | True | first | 37 | 30 | True | 54.054054 | -0.210821 | 0.607513 | 10.510104 | -7.800379 | 70.0 | 6.793707 | 26.95464 | 0.5609 | 0.001273 | 0.562172 |
| validation | by_no_trade_reasons | target_rr_below_2 | model_rules | 0 | True | first | 27 | 30 | False | 70.37037 | 0.152011 | 1.427059 | 4.089201 | 4.104287 | 50.0 | 1.110081 | 46.250558 | 0.280757 | 0.000184 | 0.280941 |
| validation | by_no_trade_reasons | target_rr_below_3 | model_rules | 0 | True | first | 14 | 30 | False | 78.571429 | 0.304668 | 2.147686 | 1.321691 | 4.265357 | 60.0 | 2.476349 | 45.034668 | 0.26676 | 0.0 | 0.26676 |
| test | ALL | ALL | model_rules | 0 | True | first | 78 | 30 | True | 76.923077 | 0.188882 | 1.655977 | 3.660231 | 14.732799 | 60.641026 | 3.733724 | 37.159452 | 0.395028 | -0.000162 | 0.394866 |
| test | by_symbol | BTCUSDT | model_rules | 0 | True | first | 30 | 30 | True | 76.666667 | 0.14523 | 1.468933 | 3.731553 | 4.356888 | 62.0 | 4.091392 | 31.880084 | 0.45477 | 0.0 | 0.45477 |
| test | by_symbol | ETHUSDT | model_rules | 0 | True | first | 48 | 30 | True | 77.083333 | 0.216165 | 1.787949 | 3.240922 | 10.375911 | 59.791667 | 3.510181 | 40.459056 | 0.357689 | -0.000264 | 0.357425 |
| test | by_direction | long | model_rules | 0 | True | first | 33 | 30 | True | 66.666667 | -0.07241 | 0.842422 | 5.842478 | -2.389545 | 62.727273 | 3.383549 | 35.246663 | 0.452177 | 0.0 | 0.452177 |
| test | by_direction | short | model_rules | 0 | True | first | 45 | 30 | True | 84.444444 | 0.380497 | 3.347083 | 2.512946 | 17.122344 | 59.111111 | 3.990518 | 38.562163 | 0.353118 | -0.000281 | 0.352837 |
| test | by_session_label | custom | model_rules | 0 | True | first | 15 | 30 | False | 80.0 | 0.233442 | 1.752646 | 3.520979 | 3.501636 | 60.666667 | 2.939202 | 37.769957 | 0.366558 | 0.0 | 0.366558 |
| test | by_session_label | london_open | model_rules | 0 | True | first | 19 | 30 | False | 78.947368 | 0.262541 | 2.519636 | 1.776363 | 4.988286 | 65.789474 | 6.733929 | 24.95755 | 0.526932 | 0.0 | 0.526932 |
| test | by_session_label | ny_open | model_rules | 0 | True | first | 44 | 30 | True | 75.0 | 0.141884 | 1.429822 | 5.193394 | 6.242877 | 58.409091 | 2.70904 | 42.220328 | 0.347775 | -0.000288 | 0.347487 |
| test | by_score_bucket | high | model_rules | 0 | True | first | 31 | 30 | True | 77.419355 | 0.128547 | 1.472885 | 2.218839 | 3.984964 | 70.0 | 6.621952 | 23.609462 | 0.548872 | 0.0 | 0.548872 |
| test | by_score_bucket | medium | model_rules | 0 | True | first | 47 | 30 | True | 76.595745 | 0.228677 | 1.76593 | 3.166468 | 10.747835 | 54.468085 | 1.828722 | 46.096679 | 0.293556 | -0.000269 | 0.293287 |
| test | by_no_trade_reasons | none | model_rules | 0 | True | first | 31 | 30 | True | 77.419355 | 0.128547 | 1.472885 | 2.218839 | 3.984964 | 70.0 | 6.621952 | 23.609462 | 0.548872 | 0.0 | 0.548872 |
| test | by_no_trade_reasons | target_rr_below_2 | model_rules | 0 | True | first | 26 | 30 | False | 76.923077 | 0.288413 | 2.071668 | 2.598202 | 7.49873 | 50.0 | 1.274504 | 56.471957 | 0.232548 | -0.000487 | 0.232061 |
| test | by_no_trade_reasons | target_rr_below_3 | model_rules | 0 | True | first | 21 | 30 | False | 76.190476 | 0.154719 | 1.461838 | 2.634681 | 3.249105 | 60.0 | 2.514896 | 33.251096 | 0.36909 | 0.0 | 0.36909 |
