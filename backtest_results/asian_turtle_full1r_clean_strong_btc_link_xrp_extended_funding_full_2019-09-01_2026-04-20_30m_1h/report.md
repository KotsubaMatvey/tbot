# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_crypto_2019-09-01_2026-04-20
- models: turtle_soup
- symbols: BTCUSDT, LINKUSDT, XRPUSDT
- timeframes: 30m, 1h
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 24
- commission_bps: 4.0
- slippage_bps: 1.0
- commission_points: 0.0
- slippage_points: 0.0
- funding_data_dir: data/history_crypto_2019-09-01_2026-04-20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | 215 | 215 | 215 |  | 3.868786 | 2.442512 | 0.483721 | 2.194183 | 75.906977 | 0.204631 | 0.381334 | 0.223097 | 0.223097 | 0.15733 | 0.000907 | 0.158236 | 0.483721 | 0.567442 | 0.223256 | 0.460465 | 1.0 | 4.252525 | 3.081967 | 2.979167 | 27 | 165 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 100 | 100 | 100 |  | 3.428419 | 2.076025 | 0.58 | 1.709439 | 74.0 | 0.216428 | 0.407026 | 0.221943 | 0.221943 | 0.184241 | 0.000842 | 0.185083 | 0.58 | 0.54 | 0.17 | 0.38 | 1.0 | 4.631579 | 3.833333 | 1.823529 | 10 | 84 |
| turtle_soup | LINKUSDT | 68 | 68 | 68 |  | 3.631132 | 2.719719 | 0.470588 | 2.205805 | 75.294118 | 0.155981 | 0.407029 | 0.283515 | 0.283515 | 0.124316 | -0.000802 | 0.123514 | 0.470588 | 0.617647 | 0.235294 | 0.5 | 1.0 | 3.617647 | 2.119048 | 2.625 | 8 | 55 |
| turtle_soup | XRPUSDT | 47 | 47 | 47 |  | 5.149576 | 2.484636 | 0.297872 | 3.208738 | 80.851064 | 0.249919 | 0.289492 | 0.13814 | 0.13814 | 0.147838 | 0.003515 | 0.151353 | 0.297872 | 0.553191 | 0.319149 | 0.574468 | 1.0 | 4.518519 | 3.076923 | 4.666667 | 9 | 26 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 215 | 215 | 215 |  | 3.868786 | 2.442512 | 0.483721 | 2.194183 | 75.906977 | 0.204631 | 0.381334 | 0.223097 | 0.223097 | 0.15733 | 0.000907 | 0.158236 | 0.483721 | 0.567442 | 0.223256 | 0.460465 | 1.0 | 4.252525 | 3.081967 | 2.979167 | 27 | 165 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 215 | 215 | 215 |  | 3.868786 | 2.442512 | 0.483721 | 2.194183 | 75.906977 | 0.204631 | 0.381334 | 0.223097 | 0.223097 | 0.15733 | 0.000907 | 0.158236 | 0.483721 | 0.567442 | 0.223256 | 0.460465 | 1.0 | 4.252525 | 3.081967 | 2.979167 | 27 | 165 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 215 | 215 | 215 |  | 3.868786 | 2.442512 | 0.483721 | 2.194183 | 75.906977 | 0.204631 | 0.381334 | 0.223097 | 0.223097 | 0.15733 | 0.000907 | 0.158236 | 0.483721 | 0.567442 | 0.223256 | 0.460465 | 1.0 | 4.252525 | 3.081967 | 2.979167 | 27 | 165 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 215 | 215 | 215 |  | 3.868786 | 2.442512 | 0.483721 | 2.194183 | 75.906977 | 0.204631 | 0.381334 | 0.223097 | 0.223097 | 0.15733 | 0.000907 | 0.158236 | 0.483721 | 0.567442 | 0.223256 | 0.460465 | 1.0 | 4.252525 | 3.081967 | 2.979167 | 27 | 165 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 111 | 111 | 111 |  | 3.932308 | 2.42225 | 0.531532 | 1.798643 | 75.225225 | 0.256424 | 0.452086 | 0.308274 | 0.308274 | 0.142945 | 0.000868 | 0.143812 | 0.531532 | 0.576577 | 0.18018 | 0.396396 | 1.0 | 4.227273 | 3.796875 | 4.2 | 11 | 90 |
| turtle_soup | valid | 104 | 104 | 104 |  | 3.800988 | 2.489194 | 0.432692 | 2.616346 | 76.634615 | 0.149352 | 0.305819 | 0.132188 | 0.132188 | 0.172683 | 0.000948 | 0.173632 | 0.432692 | 0.557692 | 0.269231 | 0.528846 | 1.0 | 4.272727 | 2.293103 | 2.107143 | 16 | 75 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 215 | 215 | 215 |  | 3.868786 | 2.442512 | 0.483721 | 2.194183 | 75.906977 | 0.204631 | 0.381334 | 0.223097 | 0.223097 | 0.15733 | 0.000907 | 0.158236 | 0.483721 | 0.567442 | 0.223256 | 0.460465 | 1.0 | 4.252525 | 3.081967 | 2.979167 | 27 | 165 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 215 | 215 | 215 |  | 3.868786 | 2.442512 | 0.483721 | 2.194183 | 75.906977 | 0.204631 | 0.381334 | 0.223097 | 0.223097 | 0.15733 | 0.000907 | 0.158236 | 0.483721 | 0.567442 | 0.223256 | 0.460465 | 1.0 | 4.252525 | 3.081967 | 2.979167 | 27 | 165 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 215 | 215 | 215 |  | 3.868786 | 2.442512 | 0.483721 | 2.194183 | 75.906977 | 0.204631 | 0.381334 | 0.223097 | 0.223097 | 0.15733 | 0.000907 | 0.158236 | 0.483721 | 0.567442 | 0.223256 | 0.460465 | 1.0 | 4.252525 | 3.081967 | 2.979167 | 27 | 165 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 215 | 215 | 215 |  | 3.868786 | 2.442512 | 0.483721 | 2.194183 | 75.906977 | 0.204631 | 0.381334 | 0.223097 | 0.223097 | 0.15733 | 0.000907 | 0.158236 | 0.483721 | 0.567442 | 0.223256 | 0.460465 | 1.0 | 4.252525 | 3.081967 | 2.979167 | 27 | 165 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 50 | 50 | 50 |  | 5.139302 | 3.520436 | 0.16 | 5.426462 | 90.0 | 0.262131 | 0.72 | 0.532721 | 0.532721 | 0.18708 | 0.000199 | 0.187279 | 0.16 | 0.86 | 0.54 | 0.74 | 1.0 | 4.594595 | 1.674419 | 2.814815 | 21 |  |
| turtle_soup | target_rr_below_2 | 138 | 138 | 138 |  | 3.062208 | 2.100702 | 0.65942 | 0.973683 | 70.0 | 0.246246 | 0.318872 | 0.174685 | 0.174685 | 0.143226 | 0.000961 | 0.144187 | 0.65942 | 0.471014 | 0.101449 | 0.311594 | 1.0 | 3.883721 | 3.984615 | 3.785714 | 2 | 138 |
| turtle_soup | target_rr_below_3 | 27 | 27 | 27 |  | 5.638485 | 2.129633 | 0.185185 | 2.446589 | 80.0 | -0.11455 | 0.073421 | -0.10284 | -0.10284 | 0.174322 | 0.00194 | 0.176262 | 0.185185 | 0.518519 | 0.259259 | 0.703704 | 1.0 | 4.421053 | 3.214286 | 2.0 | 4 | 27 |
