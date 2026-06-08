# ICT Phase Attribution Report

- events: `backtest_results\turtle_soup_btc_eth_full_2022-01-01_2026-04-20_15m_30m_strong_no_smt_minrisk35_first\events.csv`
- realized R uses `net_managed_outcome_r` when available, otherwise `managed_outcome_r`.

| phase | scope | group | filter_name | threshold | dedupe_session | dedupe_selection | trade_count | min_trades | sample_valid | win_rate_pct | expectancy_r | profit_factor | max_drawdown_r | total_pnl_r | avg_decision_score | avg_target_distance_r | avg_risk_bps | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| overall | ALL | ALL | model_rules | 0 | True | first | 345 | 30 | True | 76.521739 | 0.329612 | 2.175307 | 3.175337 | 113.716279 | 58.637681 | 3.069776 | 62.534603 | 0.185998 | 0.000292 | 0.18629 |
| train | ALL | ALL | model_rules | 0 | True | first | 116 | 30 | True | 75.0 | 0.297261 | 2.000893 | 3.011907 | 34.482333 | 61.293103 | 3.910764 | 62.480319 | 0.184331 | 0.000277 | 0.184608 |
| train | by_timeframe | 15m | model_rules | 0 | True | first | 60 | 30 | True | 80.0 | 0.393217 | 2.646445 | 3.373316 | 23.592995 | 61.5 | 4.336726 | 60.840151 | 0.189894 | -0.000245 | 0.18965 |
| train | by_timeframe | 30m | model_rules | 0 | True | first | 56 | 30 | True | 69.642857 | 0.194452 | 1.541168 | 5.042027 | 10.889338 | 61.071429 | 3.454377 | 64.237642 | 0.17837 | 0.000836 | 0.179207 |
| train | by_symbol | BTCUSDT | model_rules | 0 | True | first | 56 | 30 | True | 82.142857 | 0.400504 | 2.850319 | 1.642176 | 22.428205 | 59.821429 | 3.085634 | 55.520016 | 0.204167 | 0.000631 | 0.204798 |
| train | by_symbol | ETHUSDT | model_rules | 0 | True | first | 60 | 30 | True | 68.333333 | 0.200902 | 1.53981 | 2.829772 | 12.054128 | 62.666667 | 4.680886 | 68.976602 | 0.165817 | -5.3e-05 | 0.165765 |
| train | by_direction | long | model_rules | 0 | True | first | 61 | 30 | True | 72.131148 | 0.230784 | 1.696559 | 3.598239 | 14.077841 | 60.327869 | 3.577673 | 65.099625 | 0.183047 | 0.000677 | 0.183724 |
| train | by_direction | short | model_rules | 0 | True | first | 55 | 30 | True | 78.181818 | 0.370991 | 2.432798 | 3.626801 | 20.404492 | 62.363636 | 4.280192 | 59.57527 | 0.185755 | -0.000167 | 0.185589 |
| train | by_session_label | custom | model_rules | 0 | True | first | 19 | 30 | False | 89.473684 | 0.561857 | 5.479972 | 1.204808 | 10.675289 | 62.105263 | 4.050442 | 61.445679 | 0.188016 | 0.0 | 0.188016 |
| train | by_session_label | london_open | model_rules | 0 | True | first | 43 | 30 | True | 72.093023 | 0.251743 | 1.75811 | 6.046956 | 10.824934 | 64.651163 | 5.492309 | 67.03791 | 0.173801 | -0.000213 | 0.173587 |
| train | by_session_label | ny_open | model_rules | 0 | True | first | 54 | 30 | True | 72.222222 | 0.240409 | 1.729749 | 5.664221 | 12.98211 | 58.333333 | 2.60224 | 59.215166 | 0.19142 | 0.000765 | 0.192185 |
| train | by_score_bucket | high | model_rules | 0 | True | first | 55 | 30 | True | 69.090909 | 0.186904 | 1.503814 | 3.35504 | 10.279695 | 70.0 | 6.42774 | 58.035139 | 0.194915 | 0.0 | 0.194915 |
| train | by_score_bucket | medium | model_rules | 0 | True | first | 61 | 30 | True | 80.327869 | 0.396765 | 2.722876 | 1.850266 | 24.202638 | 53.442623 | 1.64136 | 66.488268 | 0.174788 | 0.000527 | 0.175316 |
| train | by_no_trade_reasons | none | model_rules | 0 | True | first | 55 | 30 | True | 69.090909 | 0.186904 | 1.503814 | 3.35504 | 10.279695 | 70.0 | 6.42774 | 58.035139 | 0.194915 | 0.0 | 0.194915 |
| train | by_no_trade_reasons | target_rr_below_2 | model_rules | 0 | True | first | 40 | 30 | True | 87.5 | 0.53138 | 4.657963 | 1.263157 | 21.255185 | 50.0 | 1.168946 | 71.486736 | 0.164872 | 0.001171 | 0.166043 |
| train | by_no_trade_reasons | target_rr_below_3 | model_rules | 0 | True | first | 21 | 30 | False | 66.666667 | 0.140355 | 1.357824 | 2.729354 | 2.947453 | 60.0 | 2.541195 | 56.967376 | 0.193678 | -0.000699 | 0.192978 |
| validation | ALL | ALL | model_rules | 0 | True | first | 116 | 30 | True | 79.310345 | 0.39038 | 2.575931 | 3.175337 | 45.284127 | 56.034483 | 2.364184 | 61.762547 | 0.18753 | 0.000679 | 0.188209 |
| validation | by_timeframe | 15m | model_rules | 0 | True | first | 46 | 30 | True | 84.782609 | 0.516995 | 3.875708 | 1.61114 | 23.781757 | 54.782609 | 2.089297 | 64.571273 | 0.178231 | 0.000427 | 0.178657 |
| validation | by_timeframe | 30m | model_rules | 0 | True | first | 70 | 30 | True | 75.714286 | 0.307177 | 2.050692 | 4.998661 | 21.50237 | 56.857143 | 2.544824 | 59.916812 | 0.193641 | 0.000845 | 0.194486 |
| validation | by_symbol | BTCUSDT | model_rules | 0 | True | first | 52 | 30 | True | 78.846154 | 0.367572 | 2.452286 | 3.175337 | 19.11373 | 55.192308 | 2.305141 | 61.393899 | 0.191324 | 0.001035 | 0.192359 |
| validation | by_symbol | ETHUSDT | model_rules | 0 | True | first | 64 | 30 | True | 79.6875 | 0.408912 | 2.680422 | 1.714188 | 26.170397 | 56.71875 | 2.412157 | 62.062073 | 0.184448 | 0.00039 | 0.184838 |
| validation | by_direction | long | model_rules | 0 | True | first | 59 | 30 | True | 77.966102 | 0.372948 | 2.414418 | 3.504268 | 22.003935 | 56.101695 | 2.328589 | 67.111914 | 0.176643 | 0.001971 | 0.178614 |
| validation | by_direction | short | model_rules | 0 | True | first | 57 | 30 | True | 80.701754 | 0.408424 | 2.766601 | 3.066812 | 23.280192 | 55.964912 | 2.401028 | 56.225483 | 0.1988 | -0.000658 | 0.198142 |
| validation | by_session_label | custom | model_rules | 0 | True | first | 25 | 30 | False | 80.0 | 0.409896 | 2.747259 | 2.424588 | 10.247396 | 58.8 | 2.400867 | 63.794188 | 0.190104 | 0.0 | 0.190104 |
| validation | by_session_label | london_open | model_rules | 0 | True | first | 19 | 30 | False | 84.210526 | 0.486152 | 3.473843 | 1.25795 | 9.236884 | 63.684211 | 4.882133 | 61.240031 | 0.198059 | 0.0 | 0.198059 |
| validation | by_session_label | ny_open | model_rules | 0 | True | first | 72 | 30 | True | 77.777778 | 0.358331 | 2.348224 | 3.761399 | 25.799847 | 53.055556 | 1.686988 | 61.195002 | 0.183858 | 0.001094 | 0.184952 |
| validation | by_score_bucket | high | model_rules | 0 | True | first | 25 | 30 | False | 76.0 | 0.313874 | 2.051644 | 1.699431 | 7.846854 | 70.0 | 5.60926 | 57.139181 | 0.20712 | -0.000994 | 0.206126 |
| validation | by_score_bucket | medium | model_rules | 0 | True | first | 91 | 30 | True | 80.21978 | 0.411399 | 2.759822 | 3.618197 | 37.437273 | 52.197802 | 1.47268 | 63.032702 | 0.182148 | 0.001139 | 0.183287 |
| validation | by_no_trade_reasons | none | model_rules | 0 | True | first | 25 | 30 | False | 76.0 | 0.313874 | 2.051644 | 1.699431 | 7.846854 | 70.0 | 5.60926 | 57.139181 | 0.20712 | -0.000994 | 0.206126 |
| validation | by_no_trade_reasons | target_rr_below_2 | model_rules | 0 | True | first | 71 | 30 | True | 78.873239 | 0.388855 | 2.559201 | 3.618197 | 27.608732 | 50.0 | 1.208928 | 65.851043 | 0.175515 | 0.00065 | 0.176165 |
| validation | by_no_trade_reasons | target_rr_below_3 | model_rules | 0 | True | first | 20 | 30 | False | 85.0 | 0.491427 | 3.755909 | 1.231976 | 9.828541 | 60.0 | 2.408997 | 53.027591 | 0.205698 | 0.002875 | 0.208573 |
| test | ALL | ALL | model_rules | 0 | True | first | 115 | 30 | True | 75.652174 | 0.309364 | 2.059838 | 2.977198 | 35.576812 | 58.521739 | 2.908569 | 63.297931 | 0.186143 | -9e-05 | 0.186053 |
| test | by_timeframe | 15m | model_rules | 0 | True | first | 59 | 30 | True | 71.186441 | 0.216968 | 1.619019 | 3.706981 | 12.801097 | 58.305085 | 2.580654 | 57.189084 | 0.199677 | 0.0 | 0.199677 |
| test | by_timeframe | 30m | model_rules | 0 | True | first | 56 | 30 | True | 80.357143 | 0.406709 | 2.767134 | 2.668698 | 22.775715 | 58.75 | 3.254052 | 69.734038 | 0.171883 | -0.000185 | 0.171698 |
| test | by_symbol | BTCUSDT | model_rules | 0 | True | first | 37 | 30 | True | 81.081081 | 0.37895 | 2.671234 | 2.488404 | 14.021167 | 55.945946 | 2.030043 | 62.376957 | 0.19296 | -8e-06 | 0.192952 |
| test | by_symbol | ETHUSDT | model_rules | 0 | True | first | 78 | 30 | True | 73.076923 | 0.276354 | 1.856115 | 7.074302 | 21.555645 | 59.74359 | 3.325307 | 63.734803 | 0.182909 | -0.000129 | 0.18278 |
| test | by_direction | long | model_rules | 0 | True | first | 55 | 30 | True | 70.909091 | 0.204723 | 1.585502 | 3.625311 | 11.259741 | 60.181818 | 3.173805 | 59.176188 | 0.19109 | 0.0 | 0.19109 |
| test | by_direction | short | model_rules | 0 | True | first | 60 | 30 | True | 80.0 | 0.405285 | 2.696076 | 2.308011 | 24.317071 | 57.0 | 2.665437 | 67.076196 | 0.181607 | -0.000172 | 0.181435 |
| test | by_session_label | custom | model_rules | 0 | True | first | 13 | 30 | False | 69.230769 | 0.13856 | 1.371355 | 3.665448 | 1.801279 | 58.461538 | 3.661799 | 63.248819 | 0.183568 | 0.0 | 0.183568 |
| test | by_session_label | london_open | model_rules | 0 | True | first | 26 | 30 | False | 73.076923 | 0.244287 | 1.735034 | 4.401158 | 6.351472 | 63.461538 | 3.980614 | 55.886223 | 0.217251 | 0.0 | 0.217251 |
| test | by_session_label | ny_open | model_rules | 0 | True | first | 76 | 30 | True | 77.631579 | 0.360843 | 2.365975 | 2.729833 | 27.424061 | 56.842105 | 2.412975 | 65.841916 | 0.175941 | -0.000136 | 0.175804 |
| test | by_score_bucket | high | model_rules | 0 | True | first | 36 | 30 | True | 72.222222 | 0.239665 | 1.710212 | 5.374355 | 8.627925 | 70.0 | 5.583299 | 56.325479 | 0.204999 | -0.000219 | 0.20478 |
| test | by_score_bucket | medium | model_rules | 0 | True | first | 79 | 30 | True | 77.21519 | 0.341125 | 2.258131 | 2.726103 | 26.948887 | 53.291139 | 1.689705 | 66.475251 | 0.17755 | -3.1e-05 | 0.177519 |
| test | by_no_trade_reasons | none | model_rules | 0 | True | first | 36 | 30 | True | 72.222222 | 0.239665 | 1.710212 | 5.374355 | 8.627925 | 70.0 | 5.583299 | 56.325479 | 0.204999 | -0.000219 | 0.20478 |
| test | by_no_trade_reasons | target_rr_below_2 | model_rules | 0 | True | first | 53 | 30 | True | 81.132075 | 0.424463 | 2.919267 | 3.628953 | 22.496556 | 50.0 | 1.299255 | 74.724579 | 0.159977 | -4.7e-05 | 0.15993 |
| test | by_no_trade_reasons | target_rr_below_3 | model_rules | 0 | True | first | 26 | 30 | False | 69.230769 | 0.171243 | 1.459081 | 3.992493 | 4.452331 | 60.0 | 2.485623 | 49.659312 | 0.213372 | 0.0 | 0.213372 |
