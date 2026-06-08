# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_2025-01-01_2025-12-31
- models: turtle_soup
- symbols: BTCUSDT
- timeframes: 30m
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 24
- commission_bps: 4.0
- slippage_bps: 1.0
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | 98 | 98 | 98 |  | 3.338681 | 2.096841 | 0.255102 | 2.0 | 62.653061 | -0.093578 | -0.012271 | -0.29428 | -0.29428 | 0.282009 | 0.255102 | 0.479592 | 0.255102 | 0.673469 | 1.0 | 3.106061 | 3.531915 | 6.16 | 11 | 98 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 98 | 98 | 98 |  | 3.338681 | 2.096841 | 0.255102 | 2.0 | 62.653061 | -0.093578 | -0.012271 | -0.29428 | -0.29428 | 0.282009 | 0.255102 | 0.479592 | 0.255102 | 0.673469 | 1.0 | 3.106061 | 3.531915 | 6.16 | 11 | 98 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 98 | 98 | 98 |  | 3.338681 | 2.096841 | 0.255102 | 2.0 | 62.653061 | -0.093578 | -0.012271 | -0.29428 | -0.29428 | 0.282009 | 0.255102 | 0.479592 | 0.255102 | 0.673469 | 1.0 | 3.106061 | 3.531915 | 6.16 | 11 | 98 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 98 | 98 | 98 |  | 3.338681 | 2.096841 | 0.255102 | 2.0 | 62.653061 | -0.093578 | -0.012271 | -0.29428 | -0.29428 | 0.282009 | 0.255102 | 0.479592 | 0.255102 | 0.673469 | 1.0 | 3.106061 | 3.531915 | 6.16 | 11 | 98 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 98 | 98 | 98 |  | 3.338681 | 2.096841 | 0.255102 | 2.0 | 62.653061 | -0.093578 | -0.012271 | -0.29428 | -0.29428 | 0.282009 | 0.255102 | 0.479592 | 0.255102 | 0.673469 | 1.0 | 3.106061 | 3.531915 | 6.16 | 11 | 98 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 98 | 98 | 98 |  | 3.338681 | 2.096841 | 0.255102 | 2.0 | 62.653061 | -0.093578 | -0.012271 | -0.29428 | -0.29428 | 0.282009 | 0.255102 | 0.479592 | 0.255102 | 0.673469 | 1.0 | 3.106061 | 3.531915 | 6.16 | 11 | 98 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 98 | 98 | 98 |  | 3.338681 | 2.096841 | 0.255102 | 2.0 | 62.653061 | -0.093578 | -0.012271 | -0.29428 | -0.29428 | 0.282009 | 0.255102 | 0.479592 | 0.255102 | 0.673469 | 1.0 | 3.106061 | 3.531915 | 6.16 | 11 | 98 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 13 | 13 | 13 |  | 2.306213 | 2.286835 | 0.307692 | 2.0 | 80.0 | 0.043583 | -0.171984 | -0.453282 | -0.453282 | 0.281298 | 0.307692 | 0.384615 | 0.307692 | 0.615385 | 1.0 | 2.375 | 1.6 | 3.5 |  | 13 |
| turtle_soup | medium | 85 | 85 | 85 |  | 3.496588 | 2.067388 | 0.247059 | 2.0 | 60.0 | -0.114556 | 0.012156 | -0.269962 | -0.269962 | 0.282118 | 0.247059 | 0.494118 | 0.247059 | 0.682353 | 1.0 | 3.206897 | 3.761905 | 6.666667 | 11 | 85 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | target_rr_below_3 | 98 | 98 | 98 |  | 3.338681 | 2.096841 | 0.255102 | 2.0 | 62.653061 | -0.093578 | -0.012271 | -0.29428 | -0.29428 | 0.282009 | 0.255102 | 0.479592 | 0.255102 | 0.673469 | 1.0 | 3.106061 | 3.531915 | 6.16 | 11 | 98 |
