# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `silver_bullet, ifvg_retest, ict2022_mss_fvg, turtle_soup`.

## Backtest Config
- data_dir: data/history_2025-05-01_2025-06-30
- models: turtle_soup
- symbols: BTCUSDT
- timeframes: 5m
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 144
- commission_bps: 4.0
- slippage_bps: 1.0
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | 4226 | 4226 | 4226 |  | 11.00977 | 7.317814 | 0.270942 | 2.0 | 60.946522 | -0.186825 | -0.009589 | -1.146521 | -1.146521 | 1.136932 | 0.270942 | 0.479413 | 0.270942 | 0.728822 | 1.0 | 4.332468 | 3.415104 | 5.425328 | 433 | 4226 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | close | 4226 | 4226 | 4226 |  | 11.00977 | 7.317814 | 0.270942 | 2.0 | 60.946522 | -0.186825 | -0.009589 | -1.146521 | -1.146521 | 1.136932 | 0.270942 | 0.479413 | 0.270942 | 0.728822 | 1.0 | 4.332468 | 3.415104 | 5.425328 | 433 | 4226 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | sweep_extreme | 4226 | 4226 | 4226 |  | 11.00977 | 7.317814 | 0.270942 | 2.0 | 60.946522 | -0.186825 | -0.009589 | -1.146521 | -1.146521 | 1.136932 | 0.270942 | 0.479413 | 0.270942 | 0.728822 | 1.0 | 4.332468 | 3.415104 | 5.425328 | 433 | 4226 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 4226 | 4226 | 4226 |  | 11.00977 | 7.317814 | 0.270942 | 2.0 | 60.946522 | -0.186825 | -0.009589 | -1.146521 | -1.146521 | 1.136932 | 0.270942 | 0.479413 | 0.270942 | 0.728822 | 1.0 | 4.332468 | 3.415104 | 5.425328 | 433 | 4226 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 4226 | 4226 | 4226 |  | 11.00977 | 7.317814 | 0.270942 | 2.0 | 60.946522 | -0.186825 | -0.009589 | -1.146521 | -1.146521 | 1.136932 | 0.270942 | 0.479413 | 0.270942 | 0.728822 | 1.0 | 4.332468 | 3.415104 | 5.425328 | 433 | 4226 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 4226 | 4226 | 4226 |  | 11.00977 | 7.317814 | 0.270942 | 2.0 | 60.946522 | -0.186825 | -0.009589 | -1.146521 | -1.146521 | 1.136932 | 0.270942 | 0.479413 | 0.270942 | 0.728822 | 1.0 | 4.332468 | 3.415104 | 5.425328 | 433 | 4226 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 4226 | 4226 | 4226 |  | 11.00977 | 7.317814 | 0.270942 | 2.0 | 60.946522 | -0.186825 | -0.009589 | -1.146521 | -1.146521 | 1.136932 | 0.270942 | 0.479413 | 0.270942 | 0.728822 | 1.0 | 4.332468 | 3.415104 | 5.425328 | 433 | 4226 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 273 | 273 | 273 |  | 9.777507 | 6.393027 | 0.216117 | 2.0 | 80.0 | -0.351648 | -0.14652 | -1.091904 | -1.091904 | 0.945383 | 0.216117 | 0.424908 | 0.216117 | 0.783883 | 1.0 | 4.635514 | 4.051724 | 5.338983 | 28 | 273 |
| turtle_soup | low | 73 | 73 | 73 |  | 12.875917 | 8.154122 | 0.191781 | 2.0 | 40.0 | -0.424658 | -0.171233 | -1.49029 | -1.49029 | 1.319057 | 0.191781 | 0.424658 | 0.191781 | 0.808219 | 1.0 | 3.271186 | 2.612903 | 4.857143 | 9 | 73 |
| turtle_soup | medium | 3880 | 3880 | 3880 |  | 11.061362 | 7.388974 | 0.276289 | 2.0 | 60.0 | -0.170753 | 0.003087 | -1.143896 | -1.143896 | 1.146983 | 0.276289 | 0.484278 | 0.276289 | 0.723454 | 1.0 | 4.331671 | 3.389037 | 5.4375 | 396 | 3880 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | target_rr_below_3 | 4226 | 4226 | 4226 |  | 11.00977 | 7.317814 | 0.270942 | 2.0 | 60.946522 | -0.186825 | -0.009589 | -1.146521 | -1.146521 | 1.136932 | 0.270942 | 0.479413 | 0.270942 | 0.728822 | 1.0 | 4.332468 | 3.415104 | 5.425328 | 433 | 4226 |
