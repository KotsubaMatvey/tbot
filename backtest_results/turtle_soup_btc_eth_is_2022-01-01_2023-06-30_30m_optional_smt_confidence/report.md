# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_crypto_2022-01-01_2026-04-20
- models: turtle_soup
- symbols: BTCUSDT, ETHUSDT
- timeframes: 30m
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 24
- commission_bps: 4.0
- slippage_bps: 1.0
- commission_points: 0.0
- slippage_points: 0.0
- funding_data_dir: data/history_crypto_2022-01-01_2026-04-20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | 691 | 691 | 691 |  | 10.102195 | 6.056164 | 0.356006 | 5.828661 | 66.324168 | 0.777525 | 0.396684 | -0.1486 | -0.1486 | 0.545047 | 0.000238 | 0.545285 | 0.356006 | 0.683068 | 0.515195 | 0.63097 | 1.0 | 3.149083 | 1.197034 | 1.348315 | 304 | 258 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 340 | 340 | 340 |  | 9.660583 | 6.114427 | 0.361765 | 5.416158 | 66.147059 | 0.765067 | 0.406445 | -0.173606 | -0.173606 | 0.579867 | 0.000184 | 0.580051 | 0.361765 | 0.685294 | 0.517647 | 0.623529 | 1.0 | 3.108491 | 1.11588 | 1.295455 | 144 | 128 |
| turtle_soup | ETHUSDT | 351 | 351 | 351 |  | 10.529967 | 5.794445 | 0.350427 | 6.228236 | 66.495726 | 0.789593 | 0.38723 | -0.124379 | -0.124379 | 0.511317 | 0.000291 | 0.511608 | 0.350427 | 0.680912 | 0.512821 | 0.638177 | 1.0 | 3.1875 | 1.276151 | 1.4 | 160 | 130 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | retest | 691 | 691 | 691 |  | 10.102195 | 6.056164 | 0.356006 | 5.828661 | 66.324168 | 0.777525 | 0.396684 | -0.1486 | -0.1486 | 0.545047 | 0.000238 | 0.545285 | 0.356006 | 0.683068 | 0.515195 | 0.63097 | 1.0 | 3.149083 | 1.197034 | 1.348315 | 304 | 258 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 691 | 691 | 691 |  | 10.102195 | 6.056164 | 0.356006 | 5.828661 | 66.324168 | 0.777525 | 0.396684 | -0.1486 | -0.1486 | 0.545047 | 0.000238 | 0.545285 | 0.356006 | 0.683068 | 0.515195 | 0.63097 | 1.0 | 3.149083 | 1.197034 | 1.348315 | 304 | 258 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 691 | 691 | 691 |  | 10.102195 | 6.056164 | 0.356006 | 5.828661 | 66.324168 | 0.777525 | 0.396684 | -0.1486 | -0.1486 | 0.545047 | 0.000238 | 0.545285 | 0.356006 | 0.683068 | 0.515195 | 0.63097 | 1.0 | 3.149083 | 1.197034 | 1.348315 | 304 | 258 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 691 | 691 | 691 |  | 10.102195 | 6.056164 | 0.356006 | 5.828661 | 66.324168 | 0.777525 | 0.396684 | -0.1486 | -0.1486 | 0.545047 | 0.000238 | 0.545285 | 0.356006 | 0.683068 | 0.515195 | 0.63097 | 1.0 | 3.149083 | 1.197034 | 1.348315 | 304 | 258 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 299 | 299 | 299 |  | 6.138491 | 3.947851 | 0.35786 | 4.104351 | 64.180602 | 0.227107 | 0.475839 | 0.115987 | 0.115987 | 0.359343 | 0.000508 | 0.359852 | 0.35786 | 0.719064 | 0.41806 | 0.632107 | 1.0 | 3.592593 | 1.311628 | 1.68 | 107 | 153 |
| turtle_soup | valid | 392 | 392 | 392 |  | 13.12553 | 7.800566 | 0.354592 | 7.143887 | 67.959184 | 1.19736 | 0.336309 | -0.350416 | -0.350416 | 0.686693 | 3.2e-05 | 0.686725 | 0.354592 | 0.655612 | 0.589286 | 0.630102 | 1.0 | 2.809717 | 1.101167 | 1.168831 | 197 | 105 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 691 | 691 | 691 |  | 10.102195 | 6.056164 | 0.356006 | 5.828661 | 66.324168 | 0.777525 | 0.396684 | -0.1486 | -0.1486 | 0.545047 | 0.000238 | 0.545285 | 0.356006 | 0.683068 | 0.515195 | 0.63097 | 1.0 | 3.149083 | 1.197034 | 1.348315 | 304 | 258 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 691 | 691 | 691 |  | 10.102195 | 6.056164 | 0.356006 | 5.828661 | 66.324168 | 0.777525 | 0.396684 | -0.1486 | -0.1486 | 0.545047 | 0.000238 | 0.545285 | 0.356006 | 0.683068 | 0.515195 | 0.63097 | 1.0 | 3.149083 | 1.197034 | 1.348315 | 304 | 258 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 691 | 691 | 691 |  | 10.102195 | 6.056164 | 0.356006 | 5.828661 | 66.324168 | 0.777525 | 0.396684 | -0.1486 | -0.1486 | 0.545047 | 0.000238 | 0.545285 | 0.356006 | 0.683068 | 0.515195 | 0.63097 | 1.0 | 3.149083 | 1.197034 | 1.348315 | 304 | 258 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 461 | 461 | 461 |  | 11.735978 | 7.715604 | 0.26898 | 7.86335 | 72.494577 | 0.977721 | 0.381283 | -0.276802 | -0.276802 | 0.657872 | 0.000213 | 0.658084 | 0.26898 | 0.687636 | 0.59436 | 0.713666 | 1.0 | 3.209726 | 1.104101 | 1.215328 | 257 | 28 |
| turtle_soup | medium | 230 | 230 | 230 |  | 6.827524 | 3.640724 | 0.530435 | 1.750435 | 53.956522 | 0.376264 | 0.427555 | 0.10836 | 0.10836 | 0.318906 | 0.000289 | 0.319195 | 0.530435 | 0.673913 | 0.356522 | 0.465217 | 1.0 | 2.962617 | 1.387097 | 1.792683 | 47 | 230 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 433 | 433 | 433 |  | 12.028805 | 7.841852 | 0.247113 | 8.263958 | 72.355658 | 1.015357 | 0.376443 | -0.299497 | -0.299497 | 0.675714 | 0.000227 | 0.675941 | 0.247113 | 0.688222 | 0.60739 | 0.734411 | 1.0 | 3.245283 | 1.100671 | 1.209125 | 253 |  |
| turtle_soup | target_rr_below_2 | 154 | 154 | 154 |  | 6.59179 | 3.009774 | 0.62987 | 1.222412 | 51.948052 | 0.349296 | 0.435772 | 0.168004 | 0.168004 | 0.267336 | 0.000431 | 0.267767 | 0.62987 | 0.649351 | 0.279221 | 0.363636 | 1.0 | 3.089286 | 1.53 | 1.604651 | 13 | 154 |
| turtle_soup | target_rr_below_3 | 104 | 104 | 104 |  | 7.278929 | 4.926783 | 0.403846 | 2.510186 | 62.5 | 0.421431 | 0.423077 | 0.010834 | 0.010834 | 0.412243 |  | 0.412243 | 0.403846 | 0.711538 | 0.480769 | 0.596154 | 1.0 | 2.709677 | 1.135135 | 1.86 | 38 | 104 |
