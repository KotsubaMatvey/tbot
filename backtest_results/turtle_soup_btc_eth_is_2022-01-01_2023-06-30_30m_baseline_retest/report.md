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
| turtle_soup | 12216 | 12216 | 12216 |  | 11.8946 | 7.357586 | 0.375327 | 5.839387 | 63.02554 | 0.65732 | 0.333447 | -0.360221 | -0.360221 | 0.693721 | -5.2e-05 | 0.693669 | 0.375327 | 0.650868 | 0.472904 | 0.617796 | 1.0 | 2.487346 | 1.187775 | 1.29202 | 5037 | 5130 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 6213 | 6213 | 6213 |  | 11.550646 | 7.246612 | 0.375664 | 5.572077 | 62.918075 | 0.619203 | 0.333054 | -0.428419 | -0.428419 | 0.761599 | -0.000126 | 0.761473 | 0.375664 | 0.651054 | 0.46966 | 0.616288 | 1.0 | 2.509533 | 1.183684 | 1.289925 | 2531 | 2661 |
| turtle_soup | ETHUSDT | 6003 | 6003 | 6003 |  | 12.250586 | 7.533559 | 0.374979 | 6.116048 | 63.136765 | 0.696771 | 0.333855 | -0.289638 | -0.289638 | 0.623468 | 2.5e-05 | 0.623493 | 0.374979 | 0.650675 | 0.476262 | 0.619357 | 1.0 | 2.464497 | 1.192012 | 1.294159 | 2506 | 2469 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | retest | 12216 | 12216 | 12216 |  | 11.8946 | 7.357586 | 0.375327 | 5.839387 | 63.02554 | 0.65732 | 0.333447 | -0.360221 | -0.360221 | 0.693721 | -5.2e-05 | 0.693669 | 0.375327 | 0.650868 | 0.472904 | 0.617796 | 1.0 | 2.487346 | 1.187775 | 1.29202 | 5037 | 5130 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | sweep_extreme | 12216 | 12216 | 12216 |  | 11.8946 | 7.357586 | 0.375327 | 5.839387 | 63.02554 | 0.65732 | 0.333447 | -0.360221 | -0.360221 | 0.693721 | -5.2e-05 | 0.693669 | 0.375327 | 0.650868 | 0.472904 | 0.617796 | 1.0 | 2.487346 | 1.187775 | 1.29202 | 5037 | 5130 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 12216 | 12216 | 12216 |  | 11.8946 | 7.357586 | 0.375327 | 5.839387 | 63.02554 | 0.65732 | 0.333447 | -0.360221 | -0.360221 | 0.693721 | -5.2e-05 | 0.693669 | 0.375327 | 0.650868 | 0.472904 | 0.617796 | 1.0 | 2.487346 | 1.187775 | 1.29202 | 5037 | 5130 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 12216 | 12216 | 12216 |  | 11.8946 | 7.357586 | 0.375327 | 5.839387 | 63.02554 | 0.65732 | 0.333447 | -0.360221 | -0.360221 | 0.693721 | -5.2e-05 | 0.693669 | 0.375327 | 0.650868 | 0.472904 | 0.617796 | 1.0 | 2.487346 | 1.187775 | 1.29202 | 5037 | 5130 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 6069 | 6069 | 6069 |  | 8.348921 | 5.541052 | 0.388861 | 4.123626 | 61.316527 | 0.296759 | 0.402907 | -0.099586 | -0.099586 | 0.502535 | -4.1e-05 | 0.502493 | 0.388861 | 0.679848 | 0.408469 | 0.603889 | 1.0 | 2.643929 | 1.228308 | 1.477209 | 2098 | 3166 |
| turtle_soup | valid | 6147 | 6147 | 6147 |  | 15.395287 | 10.044732 | 0.361965 | 7.533377 | 64.712868 | 1.013306 | 0.264869 | -0.617549 | -0.617549 | 0.882481 | -6.2e-05 | 0.882418 | 0.361965 | 0.622255 | 0.536522 | 0.631528 | 1.0 | 2.339516 | 1.144052 | 1.15282 | 2939 | 1964 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 12216 | 12216 | 12216 |  | 11.8946 | 7.357586 | 0.375327 | 5.839387 | 63.02554 | 0.65732 | 0.333447 | -0.360221 | -0.360221 | 0.693721 | -5.2e-05 | 0.693669 | 0.375327 | 0.650868 | 0.472904 | 0.617796 | 1.0 | 2.487346 | 1.187775 | 1.29202 | 5037 | 5130 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 12216 | 12216 | 12216 |  | 11.8946 | 7.357586 | 0.375327 | 5.839387 | 63.02554 | 0.65732 | 0.333447 | -0.360221 | -0.360221 | 0.693721 | -5.2e-05 | 0.693669 | 0.375327 | 0.650868 | 0.472904 | 0.617796 | 1.0 | 2.487346 | 1.187775 | 1.29202 | 5037 | 5130 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 12216 | 12216 | 12216 |  | 11.8946 | 7.357586 | 0.375327 | 5.839387 | 63.02554 | 0.65732 | 0.333447 | -0.360221 | -0.360221 | 0.693721 | -5.2e-05 | 0.693669 | 0.375327 | 0.650868 | 0.472904 | 0.617796 | 1.0 | 2.487346 | 1.187775 | 1.29202 | 5037 | 5130 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 7086 | 7086 | 7086 |  | 14.435704 | 9.567845 | 0.236946 | 8.932357 | 70.0 | 0.885448 | 0.298223 | -0.549083 | -0.549083 | 0.847458 | -0.000153 | 0.847306 | 0.236946 | 0.649026 | 0.533728 | 0.752611 | 1.0 | 2.563848 | 1.085236 | 1.193284 | 4053 |  |
| turtle_soup | medium | 5130 | 5130 | 5130 |  | 8.384607 | 5.04911 | 0.566472 | 1.567109 | 53.391813 | 0.342211 | 0.382103 | -0.099349 | -0.099349 | 0.481365 | 8.7e-05 | 0.481452 | 0.566472 | 0.653411 | 0.388889 | 0.431579 | 1.0 | 2.303071 | 1.328461 | 1.479198 | 984 | 5130 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 7086 | 7086 | 7086 |  | 14.435704 | 9.567845 | 0.236946 | 8.932357 | 70.0 | 0.885448 | 0.298223 | -0.549083 | -0.549083 | 0.847458 | -0.000153 | 0.847306 | 0.236946 | 0.649026 | 0.533728 | 0.752611 | 1.0 | 2.563848 | 1.085236 | 1.193284 | 4053 |  |
| turtle_soup | target_rr_below_2 | 3390 | 3390 | 3390 |  | 7.994187 | 4.680086 | 0.648673 | 1.10144 | 50.0 | 0.309864 | 0.397696 | -0.036459 | -0.036459 | 0.43405 | 0.000105 | 0.434154 | 0.648673 | 0.641888 | 0.348083 | 0.348968 | 1.0 | 2.245985 | 1.359375 | 1.305932 | 494 | 3390 |
| turtle_soup | target_rr_below_3 | 1740 | 1740 | 1740 |  | 9.145254 | 5.859571 | 0.406322 | 2.474362 | 60.0 | 0.405231 | 0.351724 | -0.221877 | -0.221877 | 0.573548 | 5.3e-05 | 0.573601 | 0.406322 | 0.675862 | 0.468391 | 0.592529 | 1.0 | 2.368574 | 1.271259 | 1.730061 | 490 | 1740 |
