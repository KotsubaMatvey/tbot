# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_crypto_2022-01-01_2026-04-20
- models: ifvg_retest
- symbols: BTCUSDT, ETHUSDT
- timeframes: 15m
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 96
- commission_bps: 4.0
- slippage_bps: 1.0
- commission_points: 0.0
- slippage_points: 0.0
- funding_data_dir: data/history_crypto_2022-01-01_2026-04-20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | 513 | 513 | 193 |  | 23.030941 | 8.191278 | 0.161793 | 4.755245 | 66.079922 | 0.563802 | 0.480875 | -0.514703 | -0.514703 | 0.374526 | 2.9e-05 | 0.374555 | 0.161793 | 0.216374 | 0.14425 | 0.214425 | 6.467836 | 2.545455 | 2.117117 | 1.094595 | 60 | 291 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | BTCUSDT | 242 | 242 | 91 |  | 20.868662 | 7.399489 | 0.157025 | 5.453966 | 66.533058 | 0.378157 | 0.452026 | -0.657995 | -0.657995 | 0.417294 | 0.000111 | 0.417405 | 0.157025 | 0.227273 | 0.14876 | 0.219008 | 6.735537 | 2.358491 | 2.8 | 1.194444 | 33 | 133 |
| ifvg_retest | ETHUSDT | 271 | 271 | 102 |  | 24.960034 | 9.078347 | 0.166052 | 4.131295 | 65.675277 | 0.729427 | 0.506613 | -0.386865 | -0.386865 | 0.336334 | -4.4e-05 | 0.336291 | 0.166052 | 0.206642 | 0.140221 | 0.210332 | 6.228782 | 2.719298 | 1.446429 | 1.0 | 27 | 158 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | edge | 513 | 513 | 193 |  | 23.030941 | 8.191278 | 0.161793 | 4.755245 | 66.079922 | 0.563802 | 0.480875 | -0.514703 | -0.514703 | 0.374526 | 2.9e-05 | 0.374555 | 0.161793 | 0.216374 | 0.14425 | 0.214425 | 6.467836 | 2.545455 | 2.117117 | 1.094595 | 60 | 291 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | opposite_boundary | 513 | 513 | 193 |  | 23.030941 | 8.191278 | 0.161793 | 4.755245 | 66.079922 | 0.563802 | 0.480875 | -0.514703 | -0.514703 | 0.374526 | 2.9e-05 | 0.374555 | 0.161793 | 0.216374 | 0.14425 | 0.214425 | 6.467836 | 2.545455 | 2.117117 | 1.094595 | 60 | 291 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | conservative | 513 | 513 | 193 |  | 23.030941 | 8.191278 | 0.161793 | 4.755245 | 66.079922 | 0.563802 | 0.480875 | -0.514703 | -0.514703 | 0.374526 | 2.9e-05 | 0.374555 | 0.161793 | 0.216374 | 0.14425 | 0.214425 | 6.467836 | 2.545455 | 2.117117 | 1.094595 | 60 | 291 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 513 | 513 | 193 |  | 23.030941 | 8.191278 | 0.161793 | 4.755245 | 66.079922 | 0.563802 | 0.480875 | -0.514703 | -0.514703 | 0.374526 | 2.9e-05 | 0.374555 | 0.161793 | 0.216374 | 0.14425 | 0.214425 | 6.467836 | 2.545455 | 2.117117 | 1.094595 | 60 | 291 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | none | 513 | 513 | 193 |  | 23.030941 | 8.191278 | 0.161793 | 4.755245 | 66.079922 | 0.563802 | 0.480875 | -0.514703 | -0.514703 | 0.374526 | 2.9e-05 | 0.374555 | 0.161793 | 0.216374 | 0.14425 | 0.214425 | 6.467836 | 2.545455 | 2.117117 | 1.094595 | 60 | 291 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | none | 513 | 513 | 193 |  | 23.030941 | 8.191278 | 0.161793 | 4.755245 | 66.079922 | 0.563802 | 0.480875 | -0.514703 | -0.514703 | 0.374526 | 2.9e-05 | 0.374555 | 0.161793 | 0.216374 | 0.14425 | 0.214425 | 6.467836 | 2.545455 | 2.117117 | 1.094595 | 60 | 291 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | unknown | 513 | 513 | 193 |  | 23.030941 | 8.191278 | 0.161793 | 4.755245 | 66.079922 | 0.563802 | 0.480875 | -0.514703 | -0.514703 | 0.374526 | 2.9e-05 | 0.374555 | 0.161793 | 0.216374 | 0.14425 | 0.214425 | 6.467836 | 2.545455 | 2.117117 | 1.094595 | 60 | 291 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | strong | 312 | 312 | 106 |  | 25.57812 | 7.407186 | 0.153846 | 4.51222 | 67.711538 | 0.653807 | 0.550858 | -0.342948 | -0.342948 | 0.303616 | 4.8e-05 | 0.303665 | 0.153846 | 0.205128 | 0.147436 | 0.185897 | 7.0 | 2.603448 | 2.28125 | 1.152174 | 30 | 183 |
| ifvg_retest | valid | 201 | 201 | 87 |  | 19.927482 | 9.499795 | 0.174129 | 5.132478 | 63.547264 | 0.454142 | 0.395609 | -0.723969 | -0.723969 | 0.484593 |  | 0.484593 | 0.174129 | 0.233831 | 0.139303 | 0.258706 | 5.641791 | 2.480769 | 1.893617 | 1.0 | 30 | 108 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | high | 222 | 222 | 78 |  | 41.480116 | 24.664672 | 0.09009 | 9.018492 | 75.905405 | 1.054066 | 0.725751 | -0.814035 | -0.814035 | 0.540901 | 0.000105 | 0.541006 | 0.09009 | 0.193694 | 0.162162 | 0.261261 | 6.941441 | 1.758621 | 1.023256 | 1.055556 | 45 |  |
| ifvg_retest | medium | 291 | 291 | 115 |  | 10.517588 | 5.090744 | 0.216495 | 1.502871 | 58.584192 | 0.231275 | 0.314785 | -0.311679 | -0.311679 | 0.2476 | -2.8e-05 | 0.247572 | 0.216495 | 0.233677 | 0.130584 | 0.178694 | 6.106529 | 3.423077 | 2.808824 | 1.131579 | 15 | 291 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ifvg_retest | none | 222 | 222 | 78 |  | 41.480116 | 24.664672 | 0.09009 | 9.018492 | 75.905405 | 1.054066 | 0.725751 | -0.814035 | -0.814035 | 0.540901 | 0.000105 | 0.541006 | 0.09009 | 0.193694 | 0.162162 | 0.261261 | 6.941441 | 1.758621 | 1.023256 | 1.055556 | 45 |  |
| ifvg_retest | target_rr_below_2 | 220 | 220 | 88 |  | 9.672521 | 4.750082 | 0.240909 | 1.194711 | 56.136364 | 0.211923 | 0.252575 | -0.275113 | -0.275113 | 0.211112 | -3.7e-05 | 0.211075 | 0.240909 | 0.222727 | 0.118182 | 0.159091 | 5.586364 | 3.2 | 3.183673 | 1.192308 | 7 | 220 |
| ifvg_retest | target_rr_below_3 | 71 | 71 | 27 |  | 13.271878 | 9.960764 | 0.140845 | 2.457734 | 66.169014 | 0.29435 | 0.517545 | -0.430856 | -0.430856 | 0.36066 |  | 0.36066 | 0.140845 | 0.267606 | 0.169014 | 0.239437 | 7.71831 | 3.882353 | 1.842105 | 1.0 | 8 | 71 |
