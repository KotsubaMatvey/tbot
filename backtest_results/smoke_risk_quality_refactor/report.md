# Entry Models Backtest Report

Config:
- symbols: BTCUSDT
- timeframes: 5m, 15m
- models: model1, model2, model3
- warmup_bars: 100
- forward_bars: 20
- cooldown_bars: 5
- start: full history
- end: full history
- htf_mode: strict
- require_displacement: True
- model3_fill_threshold: 0.5
- stop_mode: structural
- model3_stop_mode: source_zone_extreme
- stop_buffer_bps: 2.0
- invalidation_confirmation: close
- model3_reaction_bars: 10
- model3_min_rr_to_objective: 1.5
- model3_source_zone: any
- execution_pairs: {'1m': '15m', '3m': '30m', '5m': '1h', '15m': '4h', '30m': '4h', '1h': '1d'}
- model_3_htf_map: {'1m': '15m', '3m': '30m', '5m': '1h', '15m': '4h', '30m': '4h', '1h': '1d', '4h': '1d'}
- model_3_ltf_map: {'5m': '1m', '15m': '3m', '30m': '5m', '1h': '15m', '4h': '1h'}
- generated_at: 2026-04-27T18:41:28.880893+00:00

This is an event-study backtest. It does not model fees, slippage, partial exits, breakeven, or full execution management.

## 1. Overall summary
- events: 49
- warnings: 0
- skipped_outcome_events: 0

## 2. Summary by model
| model | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | 9 | 9 | 0 | 0 | 1 | 8 | 1.029969 | 0.793124 | 1.880748 | 0.896221 | 0.666667 | 0.333333 | 0.111111 | 0.444444 | 0.333333 | 0.111111 | 5.0 | BTCUSDT | 5m |
| Entry Model 2 | 40 | 40 | 0 | 0 | 35 | 5 | 7.529311 | 5.058323 | 8.320651 | 6.596325 | 0.925 | 0.875 | 0.775 | 0.775 | 0.675 | 0.575 | 5.0 | BTCUSDT | 15m |

## 3. Summary by direction
| model | direction | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | long | 1 | 1 | 0 | 0 | 1 | 0 | 0.31303 | 0.31303 | 0.25859 | 0.25859 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 15m |
| Entry Model 1 | short | 8 | 8 | 0 | 0 | 0 | 8 | 1.119586 | 0.799319 | 2.083518 | 1.716722 | 0.75 | 0.375 | 0.125 | 0.5 | 0.375 | 0.125 | 5.0 | BTCUSDT | 5m |
| Entry Model 2 | long | 35 | 35 | 0 | 0 | 35 | 0 | 8.136504 | 5.111446 | 8.342647 | 5.948339 | 0.971429 | 0.914286 | 0.8 | 0.771429 | 0.714286 | 0.6 | 5.0 | BTCUSDT | 15m |
| Entry Model 2 | short | 5 | 5 | 0 | 0 | 0 | 5 | 3.278965 | 2.230356 | 8.166683 | 9.963306 | 0.6 | 0.6 | 0.6 | 0.8 | 0.4 | 0.4 | 5.0 | BTCUSDT | 5m |

## 4. Summary by timeframe
| model | timeframe | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | 15m | 1 | 1 | 0 | 0 | 1 | 0 | 0.31303 | 0.31303 | 0.25859 | 0.25859 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 15m |
| Entry Model 1 | 5m | 8 | 8 | 0 | 0 | 0 | 8 | 1.119586 | 0.799319 | 2.083518 | 1.716722 | 0.75 | 0.375 | 0.125 | 0.5 | 0.375 | 0.125 | 5.0 | BTCUSDT | 5m |
| Entry Model 2 | 15m | 30 | 30 | 0 | 0 | 30 | 0 | 8.447903 | 5.493009 | 9.3137 | 7.142429 | 0.966667 | 0.9 | 0.833333 | 0.833333 | 0.7 | 0.6 | 5.0 | BTCUSDT | 15m |
| Entry Model 2 | 5m | 10 | 10 | 0 | 0 | 5 | 5 | 4.773536 | 2.461649 | 5.341504 | 5.921204 | 0.8 | 0.8 | 0.6 | 0.6 | 0.6 | 0.5 | 5.0 | BTCUSDT | 5m |

## 5. Score bucket analysis
| model | score_bucket | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | high | 9 | 9 | 0 | 0 | 1 | 8 | 1.029969 | 0.793124 | 1.880748 | 0.896221 | 0.666667 | 0.333333 | 0.111111 | 0.444444 | 0.333333 | 0.111111 | 5.0 | BTCUSDT | 5m |
| Entry Model 2 | high | 40 | 40 | 0 | 0 | 35 | 5 | 7.529311 | 5.058323 | 8.320651 | 6.596325 | 0.925 | 0.875 | 0.775 | 0.775 | 0.675 | 0.575 | 5.0 | BTCUSDT | 15m |

## 6. HTF Context Analysis
### Events by HTF bias
| model | htf_bias | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | bearish | 8 | 8 | 0 | 0 | 0 | 8 | 1.119586 | 0.799319 | 2.083518 | 1.716722 | 0.75 | 0.375 | 0.125 | 0.5 | 0.375 | 0.125 | 5.0 | BTCUSDT | 5m |
| Entry Model 1 | bullish | 1 | 1 | 0 | 0 | 1 | 0 | 0.31303 | 0.31303 | 0.25859 | 0.25859 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 15m |
| Entry Model 2 | bearish | 5 | 5 | 0 | 0 | 0 | 5 | 3.278965 | 2.230356 | 8.166683 | 9.963306 | 0.6 | 0.6 | 0.6 | 0.8 | 0.4 | 0.4 | 5.0 | BTCUSDT | 5m |
| Entry Model 2 | bullish | 35 | 35 | 0 | 0 | 35 | 0 | 8.136504 | 5.111446 | 8.342647 | 5.948339 | 0.971429 | 0.914286 | 0.8 | 0.771429 | 0.714286 | 0.6 | 5.0 | BTCUSDT | 15m |

### Performance by HTF location
| model | htf_location | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | discount | 7 | 7 | 0 | 0 | 0 | 7 | 0.715869 | 0.793124 | 2.381164 | 2.537223 | 0.714286 | 0.285714 | 0.0 | 0.571429 | 0.285714 | 0.0 | 5.0 | BTCUSDT | 5m |
| Entry Model 1 | equilibrium | 1 | 1 | 0 | 0 | 1 | 0 | 0.31303 | 0.31303 | 0.25859 | 0.25859 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 15m |
| Entry Model 1 | premium | 1 | 1 | 0 | 0 | 0 | 1 | 3.945606 | 3.945606 | 0.0 | 0.0 | 1.0 | 1.0 | 1.0 | 0.0 | 1.0 | 1.0 | 5.0 | BTCUSDT | 5m |
| Entry Model 2 | discount | 12 | 12 | 0 | 0 | 9 | 3 | 5.218665 | 2.664346 | 4.940528 | 5.921204 | 0.833333 | 0.833333 | 0.666667 | 0.583333 | 0.583333 | 0.5 | 5.0 | BTCUSDT | 15m |
| Entry Model 2 | equilibrium | 5 | 5 | 0 | 0 | 5 | 0 | 10.767988 | 6.731275 | 7.261151 | 3.503189 | 1.0 | 1.0 | 0.8 | 0.8 | 0.8 | 0.6 | 5.0 | BTCUSDT | 15m |
| Entry Model 2 | premium | 23 | 23 | 0 | 0 | 21 | 2 | 8.030805 | 5.874571 | 10.31452 | 8.243255 | 0.956522 | 0.869565 | 0.826087 | 0.869565 | 0.695652 | 0.608696 | 5.0 | BTCUSDT | 5m |

### Performance by HTF zone type
| model | htf_zone_type | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | Breaker | 2 | 2 | 0 | 0 | 0 | 2 | 2.369365 | 2.369365 | 0.279317 | 0.279317 | 1.0 | 0.5 | 0.5 | 0.0 | 0.5 | 0.5 | 5.0 | BTCUSDT | 5m |
| Entry Model 1 | PD | 7 | 7 | 0 | 0 | 1 | 6 | 0.647284 | 0.646668 | 2.3383 | 2.537223 | 0.571429 | 0.285714 | 0.0 | 0.571429 | 0.285714 | 0.0 | 5.0 | BTCUSDT | 5m |
| Entry Model 2 | Breaker | 10 | 10 | 0 | 0 | 8 | 2 | 8.385993 | 5.55987 | 7.036273 | 4.712196 | 0.9 | 0.9 | 0.7 | 0.6 | 0.7 | 0.6 | 5.0 | BTCUSDT | 15m |
| Entry Model 2 | FVG | 11 | 11 | 0 | 0 | 11 | 0 | 10.374821 | 6.70211 | 10.887302 | 9.026364 | 0.909091 | 0.727273 | 0.636364 | 0.909091 | 0.545455 | 0.363636 | 5.0 | BTCUSDT | 15m |
| Entry Model 2 | IFVG | 3 | 3 | 0 | 0 | 3 | 0 | 10.563294 | 10.021221 | 2.576914 | 0.139751 | 1.0 | 1.0 | 1.0 | 0.333333 | 0.666667 | 0.666667 | 5.0 | BTCUSDT | 5m |
| Entry Model 2 | OB | 1 | 1 | 0 | 0 | 1 | 0 | 4.523165 | 4.523165 | 18.969667 | 18.969667 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 5.0 | BTCUSDT | 15m |
| Entry Model 2 | PD | 15 | 15 | 0 | 0 | 12 | 3 | 4.465096 | 4.03328 | 7.733506 | 5.044765 | 0.933333 | 0.933333 | 0.866667 | 0.866667 | 0.733333 | 0.666667 | 5.0 | BTCUSDT | 15m |

### Performance by HTF alignment
| model | htf_alignment | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | aligned | 9 | 9 | 0 | 0 | 1 | 8 | 1.029969 | 0.793124 | 1.880748 | 0.896221 | 0.666667 | 0.333333 | 0.111111 | 0.444444 | 0.333333 | 0.111111 | 5.0 | BTCUSDT | 5m |
| Entry Model 2 | aligned | 40 | 40 | 0 | 0 | 35 | 5 | 7.529311 | 5.058323 | 8.320651 | 6.596325 | 0.925 | 0.875 | 0.775 | 0.775 | 0.675 | 0.575 | 5.0 | BTCUSDT | 15m |

### Performance by displacement
| model | displacement | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | has_displacement | 9 | 9 | 0 | 0 | 1 | 8 | 1.029969 | 0.793124 | 1.880748 | 0.896221 | 0.666667 | 0.333333 | 0.111111 | 0.444444 | 0.333333 | 0.111111 | 5.0 | BTCUSDT | 5m |
| Entry Model 2 | has_displacement | 40 | 40 | 0 | 0 | 35 | 5 | 7.529311 | 5.058323 | 8.320651 | 6.596325 | 0.925 | 0.875 | 0.775 | 0.775 | 0.675 | 0.575 | 5.0 | BTCUSDT | 15m |

### Performance by FVG status
| model | fvg_status | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | open | 5 | 5 | 0 | 0 | 1 | 4 | 1.203199 | 0.793124 | 0.850134 | 0.558635 | 0.6 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | 5.0 | BTCUSDT | 5m |
| Entry Model 1 | partially_filled | 4 | 4 | 0 | 0 | 0 | 4 | 0.813432 | 0.883319 | 3.169017 | 3.313415 | 0.75 | 0.5 | 0.0 | 0.75 | 0.5 | 0.0 | 5.0 | BTCUSDT | 5m |
| Entry Model 2 | unknown | 40 | 40 | 0 | 0 | 35 | 5 | 7.529311 | 5.058323 | 8.320651 | 6.596325 | 0.925 | 0.875 | 0.775 | 0.775 | 0.675 | 0.575 | 5.0 | BTCUSDT | 15m |

### Risk / stop modes
| model | stop_mode | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | structural | 9 | 9 | 0 | 0 | 1 | 8 | 1.029969 | 0.793124 | 1.880748 | 0.896221 | 0.666667 | 0.333333 | 0.111111 | 0.444444 | 0.333333 | 0.111111 | 5.0 | BTCUSDT | 5m |
| Entry Model 2 | structural | 40 | 40 | 0 | 0 | 35 | 5 | 7.529311 | 5.058323 | 8.320651 | 6.596325 | 0.925 | 0.875 | 0.775 | 0.775 | 0.675 | 0.575 | 5.0 | BTCUSDT | 15m |

| model | invalidation_source | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | sweep_extreme | 9 | 9 | 0 | 0 | 1 | 8 | 1.029969 | 0.793124 | 1.880748 | 0.896221 | 0.666667 | 0.333333 | 0.111111 | 0.444444 | 0.333333 | 0.111111 | 5.0 | BTCUSDT | 5m |
| Entry Model 2 | ifvg_boundary | 40 | 40 | 0 | 0 | 35 | 5 | 7.529311 | 5.058323 | 8.320651 | 6.596325 | 0.925 | 0.875 | 0.775 | 0.775 | 0.675 | 0.575 | 5.0 | BTCUSDT | 15m |

### Displacement grade
| model | displacement_grade | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | strong | 5 | 5 | 0 | 0 | 0 | 5 | 0.619598 | 0.646668 | 2.013816 | 2.537223 | 0.6 | 0.2 | 0.0 | 0.6 | 0.2 | 0.0 | 5.0 | BTCUSDT | 5m |
| Entry Model 1 | valid | 4 | 4 | 0 | 0 | 1 | 3 | 1.542932 | 0.956546 | 1.714413 | 0.408612 | 0.75 | 0.5 | 0.25 | 0.25 | 0.5 | 0.25 | 5.0 | BTCUSDT | 5m |
| Entry Model 2 | unknown | 40 | 40 | 0 | 0 | 35 | 5 | 7.529311 | 5.058323 | 8.320651 | 6.596325 | 0.925 | 0.875 | 0.775 | 0.775 | 0.675 | 0.575 | 5.0 | BTCUSDT | 15m |

### IFVG quality
| model | ifvg_grade | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | none | 9 | 9 | 0 | 0 | 1 | 8 | 1.029969 | 0.793124 | 1.880748 | 0.896221 | 0.666667 | 0.333333 | 0.111111 | 0.444444 | 0.333333 | 0.111111 | 5.0 | BTCUSDT | 5m |
| Entry Model 2 | strong | 4 | 4 | 0 | 0 | 4 | 0 | 4.811092 | 4.134182 | 11.047222 | 14.303086 | 1.0 | 0.5 | 0.5 | 0.75 | 0.5 | 0.5 | 5.0 | BTCUSDT | 15m |
| Entry Model 2 | valid | 36 | 36 | 0 | 0 | 31 | 5 | 7.831336 | 5.058323 | 8.017699 | 6.223562 | 0.916667 | 0.916667 | 0.805556 | 0.777778 | 0.694444 | 0.583333 | 5.0 | BTCUSDT | 15m |

### HTF objective and draw
| model | htf_alignment | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | aligned | 8 | 8 | 0 | 0 | 1 | 7 | 0.665514 | 0.719896 | 2.115842 | 1.716722 | 0.625 | 0.25 | 0.0 | 0.5 | 0.25 | 0.0 | 5.0 | BTCUSDT | 5m |
| Entry Model 1 | mixed | 1 | 1 | 0 | 0 | 0 | 1 | 3.945606 | 3.945606 | 0.0 | 0.0 | 1.0 | 1.0 | 1.0 | 0.0 | 1.0 | 1.0 | 5.0 | BTCUSDT | 5m |
| Entry Model 2 | aligned | 36 | 36 | 0 | 0 | 32 | 4 | 7.594108 | 4.818961 | 8.865947 | 7.46856 | 0.916667 | 0.861111 | 0.75 | 0.805556 | 0.666667 | 0.555556 | 5.0 | BTCUSDT | 15m |
| Entry Model 2 | mixed | 4 | 4 | 0 | 0 | 3 | 1 | 6.946145 | 7.563805 | 3.412987 | 3.030477 | 1.0 | 1.0 | 1.0 | 0.5 | 0.75 | 0.75 | 5.0 | BTCUSDT | 5m |

| model | objective_unreached | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | True | 9 | 9 | 0 | 0 | 1 | 8 | 1.029969 | 0.793124 | 1.880748 | 0.896221 | 0.666667 | 0.333333 | 0.111111 | 0.444444 | 0.333333 | 0.111111 | 5.0 | BTCUSDT | 5m |
| Entry Model 2 | True | 40 | 40 | 0 | 0 | 35 | 5 | 7.529311 | 5.058323 | 8.320651 | 6.596325 | 0.925 | 0.875 | 0.775 | 0.775 | 0.675 | 0.575 | 5.0 | BTCUSDT | 15m |

| model | draw_direction | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | down | 8 | 8 | 0 | 0 | 0 | 8 | 1.119586 | 0.799319 | 2.083518 | 1.716722 | 0.75 | 0.375 | 0.125 | 0.5 | 0.375 | 0.125 | 5.0 | BTCUSDT | 5m |
| Entry Model 1 | up | 1 | 1 | 0 | 0 | 1 | 0 | 0.31303 | 0.31303 | 0.25859 | 0.25859 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 15m |
| Entry Model 2 | down | 5 | 5 | 0 | 0 | 0 | 5 | 3.278965 | 2.230356 | 8.166683 | 9.963306 | 0.6 | 0.6 | 0.6 | 0.8 | 0.4 | 0.4 | 5.0 | BTCUSDT | 5m |
| Entry Model 2 | up | 35 | 35 | 0 | 0 | 35 | 0 | 8.136504 | 5.111446 | 8.342647 | 5.948339 | 0.971429 | 0.914286 | 0.8 | 0.771429 | 0.714286 | 0.6 | 5.0 | BTCUSDT | 15m |

### Score components
| model | objective_quality | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | high | 9 | 9 | 0 | 0 | 1 | 8 | 1.029969 | 0.793124 | 1.880748 | 0.896221 | 0.666667 | 0.333333 | 0.111111 | 0.444444 | 0.333333 | 0.111111 | 5.0 | BTCUSDT | 5m |
| Entry Model 2 | high | 40 | 40 | 0 | 0 | 35 | 5 | 7.529311 | 5.058323 | 8.320651 | 6.596325 | 0.925 | 0.875 | 0.775 | 0.775 | 0.675 | 0.575 | 5.0 | BTCUSDT | 15m |

| model | poi_quality | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | high | 2 | 2 | 0 | 0 | 0 | 2 | 2.369365 | 2.369365 | 0.279317 | 0.279317 | 1.0 | 0.5 | 0.5 | 0.0 | 0.5 | 0.5 | 5.0 | BTCUSDT | 5m |
| Entry Model 1 | medium | 7 | 7 | 0 | 0 | 1 | 6 | 0.647284 | 0.646668 | 2.3383 | 2.537223 | 0.571429 | 0.285714 | 0.0 | 0.571429 | 0.285714 | 0.0 | 5.0 | BTCUSDT | 5m |
| Entry Model 2 | high | 14 | 14 | 0 | 0 | 12 | 2 | 8.576641 | 5.55987 | 6.933081 | 4.712196 | 0.928571 | 0.928571 | 0.785714 | 0.571429 | 0.714286 | 0.642857 | 5.0 | BTCUSDT | 15m |
| Entry Model 2 | medium | 26 | 26 | 0 | 0 | 23 | 3 | 6.965364 | 4.818961 | 9.067805 | 8.467515 | 0.923077 | 0.846154 | 0.769231 | 0.884615 | 0.653846 | 0.538462 | 5.0 | BTCUSDT | 15m |

| model | risk_quality | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | high | 3 | 3 | 0 | 0 | 0 | 3 | 0.690604 | 0.793124 | 3.045429 | 2.537223 | 0.666667 | 0.333333 | 0.0 | 0.666667 | 0.333333 | 0.0 | 5.0 | BTCUSDT | 5m |
| Entry Model 1 | low | 1 | 1 | 0 | 0 | 1 | 0 | 0.31303 | 0.31303 | 0.25859 | 0.25859 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 5.0 | BTCUSDT | 15m |
| Entry Model 1 | medium | 5 | 5 | 0 | 0 | 0 | 5 | 1.376975 | 0.805514 | 1.506372 | 0.896221 | 0.8 | 0.4 | 0.2 | 0.4 | 0.4 | 0.2 | 5.0 | BTCUSDT | 5m |
| Entry Model 2 | high | 36 | 36 | 0 | 0 | 31 | 5 | 7.823491 | 5.058323 | 9.21687 | 7.917123 | 0.916667 | 0.861111 | 0.777778 | 0.861111 | 0.638889 | 0.555556 | 5.0 | BTCUSDT | 15m |
| Entry Model 2 | medium | 4 | 4 | 0 | 0 | 4 | 0 | 4.88169 | 3.902195 | 0.254679 | 0.139751 | 1.0 | 1.0 | 0.75 | 0.0 | 1.0 | 0.75 | 5.0 | BTCUSDT | 15m |

### Swing / liquidity quality
| model | sweep_swing_significance | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | intermediate | 6 | 6 | 0 | 0 | 0 | 6 | 1.078742 | 0.719896 | 1.769818 | 1.716722 | 0.666667 | 0.166667 | 0.166667 | 0.5 | 0.166667 | 0.166667 | 5.0 | BTCUSDT | 5m |
| Entry Model 1 | long | 2 | 2 | 0 | 0 | 1 | 1 | 0.838648 | 0.838648 | 0.133699 | 0.133699 | 0.5 | 0.5 | 0.0 | 0.0 | 0.5 | 0.0 | 5.0 | BTCUSDT | 5m |
| Entry Model 1 | short | 1 | 1 | 0 | 0 | 0 | 1 | 1.119969 | 1.119969 | 6.040428 | 6.040428 | 1.0 | 1.0 | 0.0 | 1.0 | 1.0 | 0.0 | 5.0 | BTCUSDT | 5m |
| Entry Model 2 | intermediate | 15 | 15 | 0 | 0 | 13 | 2 | 8.224241 | 6.731275 | 8.233126 | 6.693866 | 0.866667 | 0.866667 | 0.866667 | 0.866667 | 0.733333 | 0.666667 | 5.0 | BTCUSDT | 15m |
| Entry Model 2 | long | 16 | 16 | 0 | 0 | 16 | 0 | 6.245283 | 4.852107 | 8.188842 | 3.81345 | 1.0 | 1.0 | 0.75 | 0.625 | 0.75 | 0.5625 | 5.0 | BTCUSDT | 15m |
| Entry Model 2 | short | 9 | 9 | 0 | 0 | 6 | 3 | 8.653812 | 2.635748 | 8.700855 | 9.736795 | 0.888889 | 0.666667 | 0.666667 | 0.888889 | 0.444444 | 0.444444 | 5.0 | BTCUSDT | 15m |

| model | objective_is_equal_high_low | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | True | 9 | 9 | 0 | 0 | 1 | 8 | 1.029969 | 0.793124 | 1.880748 | 0.896221 | 0.666667 | 0.333333 | 0.111111 | 0.444444 | 0.333333 | 0.111111 | 5.0 | BTCUSDT | 5m |
| Entry Model 2 | True | 40 | 40 | 0 | 0 | 35 | 5 | 7.529311 | 5.058323 | 8.320651 | 6.596325 | 0.925 | 0.875 | 0.775 | 0.775 | 0.675 | 0.575 | 5.0 | BTCUSDT | 15m |

### Model 3 fill variants
| model | fill_mode | count | valid_outcome_count | skipped_outcome_count | invalid_risk_count | long_count | short_count | avg_mfe_r | median_mfe_r | avg_mae_r | median_mae_r | hit_0_5r_rate | hit_1r_rate | hit_2r_rate | invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | avg_score | best_symbol | best_timeframe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Entry Model 1 | none | 9 | 9 | 0 | 0 | 1 | 8 | 1.029969 | 0.793124 | 1.880748 | 0.896221 | 0.666667 | 0.333333 | 0.111111 | 0.444444 | 0.333333 | 0.111111 | 5.0 | BTCUSDT | 5m |
| Entry Model 2 | none | 40 | 40 | 0 | 0 | 35 | 5 | 7.529311 | 5.058323 | 8.320651 | 6.596325 | 0.925 | 0.875 | 0.775 | 0.775 | 0.675 | 0.575 | 5.0 | BTCUSDT | 15m |

## 7. Warnings / skipped events
- none

## 8. Interpretation notes
- Replay is bar-by-bar: strategies receive only candles visible at the current bar.
- Forward candles are used only after event detection for outcome measurement.
- `bars_to_*` values are 1-based future bar offsets from the signal bar.
- `*_before_invalidation` uses OHLC bar ordering only; same-bar threshold/invalidation ordering is not modeled.
- HTF-filtered event studies should usually have fewer signals than legacy/off mode.
- If strict signal count does not decrease, HTF gating is too weak.
- If score buckets remain mostly high, scoring is not calibrated enough.
