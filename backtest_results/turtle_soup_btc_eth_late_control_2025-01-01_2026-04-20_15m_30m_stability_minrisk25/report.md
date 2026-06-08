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
| turtle_soup | 956 | 956 | 956 |  | 10.316673 | 6.779519 | 0.290795 | 7.585108 | 68.828452 | 0.953811 | 0.467072 | -0.248911 | -0.248911 | 0.716003 | -2.1e-05 | 0.715982 | 0.290795 | 0.725941 | 0.58159 | 0.683054 | 1.0 | 3.3951 | 1.162824 | 1.323741 | 479 | 217 |

## Symbol Analysis
| model | symbol | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | BTCUSDT | 448 | 448 | 448 |  | 11.154075 | 7.507828 | 0.3125 | 7.338385 | 68.861607 | 0.936076 | 0.431962 | -0.479885 | -0.479885 | 0.911832 | 1.4e-05 | 0.911847 | 0.3125 | 0.705357 | 0.569196 | 0.674107 | 1.0 | 3.086093 | 1.053797 | 1.188235 | 216 | 97 |
| turtle_soup | ETHUSDT | 508 | 508 | 508 |  | 9.578177 | 6.021227 | 0.271654 | 7.802691 | 68.799213 | 0.969451 | 0.498034 | -0.045217 | -0.045217 | 0.543303 | -5.2e-05 | 0.543251 | 0.271654 | 0.744094 | 0.59252 | 0.690945 | 1.0 | 3.660969 | 1.253968 | 1.438538 | 263 | 120 |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | retest | 956 | 956 | 956 |  | 10.316673 | 6.779519 | 0.290795 | 7.585108 | 68.828452 | 0.953811 | 0.467072 | -0.248911 | -0.248911 | 0.716003 | -2.1e-05 | 0.715982 | 0.290795 | 0.725941 | 0.58159 | 0.683054 | 1.0 | 3.3951 | 1.162824 | 1.323741 | 479 | 217 |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | asian_sweep_extreme | 956 | 956 | 956 |  | 10.316673 | 6.779519 | 0.290795 | 7.585108 | 68.828452 | 0.953811 | 0.467072 | -0.248911 | -0.248911 | 0.716003 | -2.1e-05 | 0.715982 | 0.290795 | 0.725941 | 0.58159 | 0.683054 | 1.0 | 3.3951 | 1.162824 | 1.323741 | 479 | 217 |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | conservative | 956 | 956 | 956 |  | 10.316673 | 6.779519 | 0.290795 | 7.585108 | 68.828452 | 0.953811 | 0.467072 | -0.248911 | -0.248911 | 0.716003 | -2.1e-05 | 0.715982 | 0.290795 | 0.725941 | 0.58159 | 0.683054 | 1.0 | 3.3951 | 1.162824 | 1.323741 | 479 | 217 |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 956 | 956 | 956 |  | 10.316673 | 6.779519 | 0.290795 | 7.585108 | 68.828452 | 0.953811 | 0.467072 | -0.248911 | -0.248911 | 0.716003 | -2.1e-05 | 0.715982 | 0.290795 | 0.725941 | 0.58159 | 0.683054 | 1.0 | 3.3951 | 1.162824 | 1.323741 | 479 | 217 |

## Turtle Quality
| model | turtle_quality | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | strong | 393 | 393 | 393 |  | 7.126424 | 4.599074 | 0.312977 | 4.901838 | 66.819338 | 0.449556 | 0.523115 | 0.054732 | 0.054732 | 0.46841 | -2.6e-05 | 0.468383 | 0.312977 | 0.753181 | 0.506361 | 0.659033 | 1.0 | 3.467181 | 1.233108 | 1.577889 | 158 | 140 |
| turtle_soup | valid | 563 | 563 | 563 |  | 12.543614 | 8.676547 | 0.275311 | 9.458155 | 70.230906 | 1.305804 | 0.42795 | -0.460867 | -0.460867 | 0.888835 | -1.7e-05 | 0.888818 | 0.275311 | 0.706927 | 0.634103 | 0.699822 | 1.0 | 3.347716 | 1.110553 | 1.182073 | 321 | 77 |

## Asian Failed Sweep Count
| model | asian_failed_sweep_count_before_reclaim | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup |  | 956 | 956 | 956 |  | 10.316673 | 6.779519 | 0.290795 | 7.585108 | 68.828452 | 0.953811 | 0.467072 | -0.248911 | -0.248911 | 0.716003 | -2.1e-05 | 0.715982 | 0.290795 | 0.725941 | 0.58159 | 0.683054 | 1.0 | 3.3951 | 1.162824 | 1.323741 | 479 | 217 |

## HTF Location
| model | htf_location | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | unknown | 956 | 956 | 956 |  | 10.316673 | 6.779519 | 0.290795 | 7.585108 | 68.828452 | 0.953811 | 0.467072 | -0.248911 | -0.248911 | 0.716003 | -2.1e-05 | 0.715982 | 0.290795 | 0.725941 | 0.58159 | 0.683054 | 1.0 | 3.3951 | 1.162824 | 1.323741 | 479 | 217 |

## Displacement
| model | displacement_grade | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 956 | 956 | 956 |  | 10.316673 | 6.779519 | 0.290795 | 7.585108 | 68.828452 | 0.953811 | 0.467072 | -0.248911 | -0.248911 | 0.716003 | -2.1e-05 | 0.715982 | 0.290795 | 0.725941 | 0.58159 | 0.683054 | 1.0 | 3.3951 | 1.162824 | 1.323741 | 479 | 217 |

## Decision Score Buckets
| model | score_bucket | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | high | 758 | 758 | 758 |  | 11.130139 | 8.226545 | 0.224274 | 9.081709 | 72.506596 | 1.085335 | 0.461741 | -0.350943 | -0.350943 | 0.812705 | -2.1e-05 | 0.812685 | 0.224274 | 0.730871 | 0.622691 | 0.742744 | 1.0 | 3.493783 | 1.052347 | 1.252119 | 444 | 19 |
| turtle_soup | medium | 198 | 198 | 198 |  | 7.202493 | 3.651604 | 0.545455 | 1.855696 | 54.747475 | 0.4503 | 0.487477 | 0.141698 | 0.141698 | 0.345799 | -2.1e-05 | 0.345779 | 0.545455 | 0.707071 | 0.424242 | 0.454545 | 1.0 | 2.777778 | 1.6 | 1.72619 | 35 | 198 |

## No-Trade Reasons
| model | no_trade_reasons | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | avg_decision_score | expectancy | gross_managed_expectancy | managed_expectancy | avg_managed_outcome_r | avg_execution_cost_r | avg_funding_cost_r | avg_total_cost_r | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count | no_trade_reason_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_soup | none | 739 | 739 | 739 |  | 11.242783 | 8.324937 | 0.213802 | 9.2703 | 72.435724 | 1.096146 | 0.461434 | -0.363801 | -0.363801 | 0.825257 | -2.1e-05 | 0.825235 | 0.213802 | 0.730717 | 0.623816 | 0.752368 | 1.0 | 3.5 | 1.053704 | 1.240781 | 442 |  |
| turtle_soup | target_rr_below_2 | 113 | 113 | 113 |  | 7.979179 | 3.328841 | 0.654867 | 1.230532 | 51.59292 | 0.396467 | 0.491331 | 0.177763 | 0.177763 | 0.313604 | -3.6e-05 | 0.313568 | 0.654867 | 0.681416 | 0.353982 | 0.345133 | 1.0 | 3.307692 | 1.896104 | 1.5 | 9 | 113 |
| turtle_soup | target_rr_below_3 | 104 | 104 | 104 |  | 6.275728 | 4.418344 | 0.442308 | 2.515013 | 61.923077 | 0.547988 | 0.480769 | 0.103876 | 0.103876 | 0.376894 |  | 0.376894 | 0.442308 | 0.740385 | 0.528846 | 0.557692 | 1.0 | 2.448276 | 1.194805 | 1.890909 | 28 | 104 |
