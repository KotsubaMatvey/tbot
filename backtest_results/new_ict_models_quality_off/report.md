# New ICT Models Backtest Report

Event-study only. No profitability claim.

## Migration Summary
- Old Entry Model 1/2/3 are archived in `strategies/legacy/`.
- Old models are disabled by default.
- New registry default models are `turtle_soup`, `silver_bullet`, `ifvg_retest`.

## Backtest Config
- models: turtle_soup, silver_bullet, ifvg_retest, ict2022_mss_fvg, breaker_block, reclaimed_ob
- symbols: BTCUSDT, ETHUSDT, SOLUSDT
- timeframes: 1m, 5m, 15m, 30m, 1h, 4h
- same_bar_policy: conservative
- context_mode: off
- forward_bars: 20
- event-study alignment: `setup_timestamp`; R outcomes are measured from `entry_time` when it differs.

## Overall Comparison
| model | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | 933 | 933 | 741 | 167 | 13.482338 | 8.183918 | 0.56806 | 2.537067 | 0.824608 | 0.56806 | 0.562701 | 0.464094 | 0.217578 | 3.33557 | 1.492611 | 1.034286 | 1.078522 |  |
| ifvg_retest | 2172 | 2172 | 2160 |  | 17.642717 | 7.21749 | 0.283149 | 2.0 | -0.109937 | 0.283149 | 0.377993 | 0.283149 | 0.696133 | 2.291204 | 1.903439 | 1.777101 | 2.326829 |  |
| reclaimed_ob | 158 | 158 | 150 | 8 | 13.289166 | 5.766214 | 0.791139 | 1.751433 | 1.12582 | 0.791139 | 0.727848 | 0.613924 | 0.158228 | 1.550633 | 1.08 | 1.017391 | 1.030928 |  |
| silver_bullet | 91 | 91 | 91 |  | 1.09827 | 0.883023 | 0.120879 | 2.0 | -0.001759 | 0.120879 | 0.340659 | 0.120879 | 0.538462 | 1.186813 | 7.102041 | 4.935484 | 8.909091 |  |
| turtle_soup | 11267 | 11267 | 11267 |  | 4.143102 | 2.550622 | 0.155942 | 6.887761 | 0.255213 | 0.155942 | 0.467471 | 0.29511 | 0.719979 | 1.0 | 4.184048 | 2.82248 | 4.540752 |  |

## Entry Mode Analysis
| model | entry_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | edge | 933 | 933 | 741 | 167 | 13.482338 | 8.183918 | 0.56806 | 2.537067 | 0.824608 | 0.56806 | 0.562701 | 0.464094 | 0.217578 | 3.33557 | 1.492611 | 1.034286 | 1.078522 |  |
| ifvg_retest | edge | 2172 | 2172 | 2160 |  | 17.642717 | 7.21749 | 0.283149 | 2.0 | -0.109937 | 0.283149 | 0.377993 | 0.283149 | 0.696133 | 2.291204 | 1.903439 | 1.777101 | 2.326829 |  |
| reclaimed_ob | body_edge | 158 | 158 | 150 | 8 | 13.289166 | 5.766214 | 0.791139 | 1.751433 | 1.12582 | 0.791139 | 0.727848 | 0.613924 | 0.158228 | 1.550633 | 1.08 | 1.017391 | 1.030928 |  |
| silver_bullet | edge | 91 | 91 | 91 |  | 1.09827 | 0.883023 | 0.120879 | 2.0 | -0.001759 | 0.120879 | 0.340659 | 0.120879 | 0.538462 | 1.186813 | 7.102041 | 4.935484 | 8.909091 |  |
| turtle_soup | close | 11267 | 11267 | 11267 |  | 4.143102 | 2.550622 | 0.155942 | 6.887761 | 0.255213 | 0.155942 | 0.467471 | 0.29511 | 0.719979 | 1.0 | 4.184048 | 2.82248 | 4.540752 |  |

## Stop Mode Analysis
| model | stop_mode | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | mean_threshold | 933 | 933 | 741 | 167 | 13.482338 | 8.183918 | 0.56806 | 2.537067 | 0.824608 | 0.56806 | 0.562701 | 0.464094 | 0.217578 | 3.33557 | 1.492611 | 1.034286 | 1.078522 |  |
| ifvg_retest | ce | 2172 | 2172 | 2160 |  | 17.642717 | 7.21749 | 0.283149 | 2.0 | -0.109937 | 0.283149 | 0.377993 | 0.283149 | 0.696133 | 2.291204 | 1.903439 | 1.777101 | 2.326829 |  |
| reclaimed_ob | mean_threshold | 158 | 158 | 150 | 8 | 13.289166 | 5.766214 | 0.791139 | 1.751433 | 1.12582 | 0.791139 | 0.727848 | 0.613924 | 0.158228 | 1.550633 | 1.08 | 1.017391 | 1.030928 |  |
| silver_bullet | swing_or_fvg | 91 | 91 | 91 |  | 1.09827 | 0.883023 | 0.120879 | 2.0 | -0.001759 | 0.120879 | 0.340659 | 0.120879 | 0.538462 | 1.186813 | 7.102041 | 4.935484 | 8.909091 |  |
| turtle_soup | sweep_extreme | 11267 | 11267 | 11267 |  | 4.143102 | 2.550622 | 0.155942 | 6.887761 | 0.255213 | 0.155942 | 0.467471 | 0.29511 | 0.719979 | 1.0 | 4.184048 | 2.82248 | 4.540752 |  |

## Same-Bar Conservative Impact
| model | same_bar_policy | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| breaker_block | conservative | 933 | 933 | 741 | 167 | 13.482338 | 8.183918 | 0.56806 | 2.537067 | 0.824608 | 0.56806 | 0.562701 | 0.464094 | 0.217578 | 3.33557 | 1.492611 | 1.034286 | 1.078522 |  |
| ifvg_retest | conservative | 2172 | 2172 | 2160 |  | 17.642717 | 7.21749 | 0.283149 | 2.0 | -0.109937 | 0.283149 | 0.377993 | 0.283149 | 0.696133 | 2.291204 | 1.903439 | 1.777101 | 2.326829 |  |
| reclaimed_ob | conservative | 158 | 158 | 150 | 8 | 13.289166 | 5.766214 | 0.791139 | 1.751433 | 1.12582 | 0.791139 | 0.727848 | 0.613924 | 0.158228 | 1.550633 | 1.08 | 1.017391 | 1.030928 |  |
| silver_bullet | conservative | 91 | 91 | 91 |  | 1.09827 | 0.883023 | 0.120879 | 2.0 | -0.001759 | 0.120879 | 0.340659 | 0.120879 | 0.538462 | 1.186813 | 7.102041 | 4.935484 | 8.909091 |  |
| turtle_soup | conservative | 11267 | 11267 | 11267 |  | 4.143102 | 2.550622 | 0.155942 | 6.887761 | 0.255213 | 0.155942 | 0.467471 | 0.29511 | 0.719979 | 1.0 | 4.184048 | 2.82248 | 4.540752 |  |

## Model Family
| model_family | count | total_setups | activated_trades | invalidated_before_entry | avg_mfe_r | median_mfe_r | win_rate | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_time_to_entry | avg_time_to_invalidation | avg_time_to_1r | avg_time_to_2r | same_bar_ambiguous_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ict | 14621 | 14621 | 14409 | 175 | 6.723043 | 3.054157 | 0.207783 | 5.798113 | 0.237197 | 0.207783 | 0.46228 | 0.306477 | 0.677177 | 1.341867 | 3.787193 | 2.535582 | 3.83709 |  |
