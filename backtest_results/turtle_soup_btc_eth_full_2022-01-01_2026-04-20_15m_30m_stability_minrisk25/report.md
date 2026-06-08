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
- timeframes: 15m, 30m
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
| turtle_soup | 3546 | 3546 | 3546 |  | 9.948796 | 6.190964 | 0.318951 | 6.643547 | 67.577552 | 0.844606 | 0.441844 | -0.261566 | -0.261566 | 0.70341 | -1e-06 | 0.703409 | 0.318951 | 0.713198 | 0.547659 | 0.661309 | 1.0 | 3.378252 | 1.198893 | 1.412461 | 1687 | 1000 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 1748 | 1748 | 1748 |  | 9.938113 | 6.39551 | 0.340389 | 6.238297 | 67.494279 | 0.85652 | 0.431698 | -0.35184 | -0.35184 | 0.783384 | 0.000154 | 0.783538 | 0.340389 | 0.705378 | 0.54119 | 0.644737 | 1.0 | 3.277728 | 1.136253 | 1.346723 | 796 | 508 |
| turtle_soup | ETHUSDT | 1798 | 1798 | 1798 |  | 9.959181 | 5.987282 | 0.298109 | 7.037527 | 67.658509 | 0.833023 | 0.451707 | -0.173802 | -0.173802 | 0.62566 | -0.000151 | 0.625509 | 0.298109 | 0.720801 | 0.553949 | 0.677419 | 1.0 | 3.471264 | 1.258488 | 1.4749 | 891 | 492 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | retest | 3546 | 3546 | 3546 |  | 9.948796 | 6.190964 | 0.318951 | 6.643547 | 67.577552 | 0.844606 | 0.441844 | -0.261566 | -0.261566 | 0.70341 | -1e-06 | 0.703409 | 0.318951 | 0.713198 | 0.547659 | 0.661309 | 1.0 | 3.378252 | 1.198893 | 1.412461 | 1687 | 1000 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 3546 | 3546 | 3546 |  | 9.948796 | 6.190964 | 0.318951 | 6.643547 | 67.577552 | 0.844606 | 0.441844 | -0.261566 | -0.261566 | 0.70341 | -1e-06 | 0.703409 | 0.318951 | 0.713198 | 0.547659 | 0.661309 | 1.0 | 3.378252 | 1.198893 | 1.412461 | 1687 | 1000 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 3546 | 3546 | 3546 |  | 9.948796 | 6.190964 | 0.318951 | 6.643547 | 67.577552 | 0.844606 | 0.441844 | -0.261566 | -0.261566 | 0.70341 | -1e-06 | 0.703409 | 0.318951 | 0.713198 | 0.547659 | 0.661309 | 1.0 | 3.378252 | 1.198893 | 1.412461 | 1687 | 1000 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 3546 | 3546 | 3546 |  | 9.948796 | 6.190964 | 0.318951 | 6.643547 | 67.577552 | 0.844606 | 0.441844 | -0.261566 | -0.261566 | 0.70341 | -1e-06 | 0.703409 | 0.318951 | 0.713198 | 0.547659 | 0.661309 | 1.0 | 3.378252 | 1.198893 | 1.412461 | 1687 | 1000 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 1538 | 1538 | 1538 |  | 6.377527 | 4.161421 | 0.33485 | 4.422255 | 65.396619 | 0.373174 | 0.526716 | 0.063592 | 0.063592 | 0.463051 | 7.2e-05 | 0.463123 | 0.33485 | 0.753576 | 0.460988 | 0.645644 | 1.0 | 3.659617 | 1.314064 | 1.818054 | 575 | 642 |
| turtle_soup | valid | 2008 | 2008 | 2008 |  | 12.684159 | 8.630738 | 0.306773 | 8.344914 | 69.248008 | 1.205693 | 0.376837 | -0.510616 | -0.510616 | 0.88751 | -5.7e-05 | 0.887453 | 0.306773 | 0.682271 | 0.614044 | 0.673307 | 1.0 | 3.171598 | 1.10146 | 1.179238 | 1112 | 358 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 3546 | 3546 | 3546 |  | 9.948796 | 6.190964 | 0.318951 | 6.643547 | 67.577552 | 0.844606 | 0.441844 | -0.261566 | -0.261566 | 0.70341 | -1e-06 | 0.703409 | 0.318951 | 0.713198 | 0.547659 | 0.661309 | 1.0 | 3.378252 | 1.198893 | 1.412461 | 1687 | 1000 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 3546 | 3546 | 3546 |  | 9.948796 | 6.190964 | 0.318951 | 6.643547 | 67.577552 | 0.844606 | 0.441844 | -0.261566 | -0.261566 | 0.70341 | -1e-06 | 0.703409 | 0.318951 | 0.713198 | 0.547659 | 0.661309 | 1.0 | 3.378252 | 1.198893 | 1.412461 | 1687 | 1000 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 3546 | 3546 | 3546 |  | 9.948796 | 6.190964 | 0.318951 | 6.643547 | 67.577552 | 0.844606 | 0.441844 | -0.261566 | -0.261566 | 0.70341 | -1e-06 | 0.703409 | 0.318951 | 0.713198 | 0.547659 | 0.661309 | 1.0 | 3.378252 | 1.198893 | 1.412461 | 1687 | 1000 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 2630 | 2630 | 2630 |  | 11.265028 | 7.664519 | 0.246768 | 8.333461 | 72.239544 | 1.00634 | 0.433178 | -0.388535 | -0.388535 | 0.821824 | -0.000111 | 0.821714 | 0.246768 | 0.715209 | 0.606844 | 0.728517 | 1.0 | 3.395094 | 1.088251 | 1.295113 | 1524 | 84 |
| turtle_soup | medium | 916 | 916 | 916 |  | 6.169657 | 3.46671 | 0.526201 | 1.791501 | 54.19214 | 0.380239 | 0.466723 | 0.102986 | 0.102986 | 0.363422 | 0.000314 | 0.363737 | 0.526201 | 0.707424 | 0.377729 | 0.468341 | 1.0 | 3.30303 | 1.520062 | 1.953757 | 163 | 916 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 2546 | 2546 | 2546 |  | 11.404964 | 7.72993 | 0.233307 | 8.553278 | 72.168107 | 1.020413 | 0.428908 | -0.405728 | -0.405728 | 0.834764 | -0.000128 | 0.834636 | 0.233307 | 0.714454 | 0.612333 | 0.741163 | 1.0 | 3.410705 | 1.063222 | 1.288647 | 1514 |  |
| turtle_soup | target_rr_below_2 | 579 | 579 | 579 |  | 5.791852 | 3.149887 | 0.632124 | 1.2469 | 51.623489 | 0.36742 | 0.446157 | 0.133725 | 0.133725 | 0.312025 | 0.000407 | 0.312432 | 0.632124 | 0.677029 | 0.302245 | 0.364421 | 1.0 | 3.488152 | 1.716837 | 1.754286 | 56 | 579 |
| turtle_soup | target_rr_below_3 | 421 | 421 | 421 |  | 6.859639 | 4.165914 | 0.406176 | 2.516428 | 61.75772 | 0.437684 | 0.514139 | 0.066611 | 0.066611 | 0.44732 | 0.000208 | 0.447528 | 0.406176 | 0.755344 | 0.494062 | 0.586698 | 1.0 | 3.036437 | 1.336478 | 2.052885 | 117 | 421 |
