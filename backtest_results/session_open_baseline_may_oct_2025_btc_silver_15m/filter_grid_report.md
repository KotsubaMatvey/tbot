# ICT Filter Grid Report

- events: `backtest_results\session_open_baseline_may_oct_2025_btc_silver_15m\events.csv`
- min_count: 20

## Top Filters
| rank | filter_name | count | filtered_out | expectancy | managed_expectancy | target_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_decision_score | avg_rr | min_decision_score | min_target_distance_r | require_smt | require_session_window | allowed_displacement_grades | allowed_htf_locations | exclude_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | none | 369 |  | -0.102621 | 0.054086 | 0.257453 | 0.257453 | 0.653117 | 78.0 | 2.0 | 0 | 0 | false | false |  |  |  |
| 2 | exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 369 |  | -0.102621 | 0.054086 | 0.257453 | 0.257453 | 0.653117 | 78.0 | 2.0 | 0 | 0 | false | false |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
| 3 | require_session_window=true | 369 |  | -0.102621 | 0.054086 | 0.257453 | 0.257453 | 0.653117 | 78.0 | 2.0 | 0 | 0 | false | true |  |  |  |
| 4 | require_session_window=true;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 369 |  | -0.102621 | 0.054086 | 0.257453 | 0.257453 | 0.653117 | 78.0 | 2.0 | 0 | 0 | false | true |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
| 5 | min_target_distance_r=2 | 369 |  | -0.102621 | 0.054086 | 0.257453 | 0.257453 | 0.653117 | 78.0 | 2.0 | 0 | 2 | false | false |  |  |  |
| 6 | min_target_distance_r=2;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 369 |  | -0.102621 | 0.054086 | 0.257453 | 0.257453 | 0.653117 | 78.0 | 2.0 | 0 | 2 | false | false |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
| 7 | min_target_distance_r=2;require_session_window=true | 369 |  | -0.102621 | 0.054086 | 0.257453 | 0.257453 | 0.653117 | 78.0 | 2.0 | 0 | 2 | false | true |  |  |  |
| 8 | min_target_distance_r=2;require_session_window=true;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 369 |  | -0.102621 | 0.054086 | 0.257453 | 0.257453 | 0.653117 | 78.0 | 2.0 | 0 | 2 | false | true |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
| 9 | min_decision_score=50 | 369 |  | -0.102621 | 0.054086 | 0.257453 | 0.257453 | 0.653117 | 78.0 | 2.0 | 50 | 0 | false | false |  |  |  |
| 10 | min_decision_score=50;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 369 |  | -0.102621 | 0.054086 | 0.257453 | 0.257453 | 0.653117 | 78.0 | 2.0 | 50 | 0 | false | false |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
| 11 | min_decision_score=50;require_session_window=true | 369 |  | -0.102621 | 0.054086 | 0.257453 | 0.257453 | 0.653117 | 78.0 | 2.0 | 50 | 0 | false | true |  |  |  |
| 12 | min_decision_score=50;require_session_window=true;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 369 |  | -0.102621 | 0.054086 | 0.257453 | 0.257453 | 0.653117 | 78.0 | 2.0 | 50 | 0 | false | true |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
| 13 | min_decision_score=50;min_target_distance_r=2 | 369 |  | -0.102621 | 0.054086 | 0.257453 | 0.257453 | 0.653117 | 78.0 | 2.0 | 50 | 2 | false | false |  |  |  |
| 14 | min_decision_score=50;min_target_distance_r=2;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 369 |  | -0.102621 | 0.054086 | 0.257453 | 0.257453 | 0.653117 | 78.0 | 2.0 | 50 | 2 | false | false |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
| 15 | min_decision_score=50;min_target_distance_r=2;require_session_window=true | 369 |  | -0.102621 | 0.054086 | 0.257453 | 0.257453 | 0.653117 | 78.0 | 2.0 | 50 | 2 | false | true |  |  |  |
| 16 | min_decision_score=50;min_target_distance_r=2;require_session_window=true;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 369 |  | -0.102621 | 0.054086 | 0.257453 | 0.257453 | 0.653117 | 78.0 | 2.0 | 50 | 2 | false | true |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
| 17 | min_decision_score=70 | 369 |  | -0.102621 | 0.054086 | 0.257453 | 0.257453 | 0.653117 | 78.0 | 2.0 | 70 | 0 | false | false |  |  |  |
| 18 | min_decision_score=70;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 369 |  | -0.102621 | 0.054086 | 0.257453 | 0.257453 | 0.653117 | 78.0 | 2.0 | 70 | 0 | false | false |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
| 19 | min_decision_score=70;require_session_window=true | 369 |  | -0.102621 | 0.054086 | 0.257453 | 0.257453 | 0.653117 | 78.0 | 2.0 | 70 | 0 | false | true |  |  |  |
| 20 | min_decision_score=70;require_session_window=true;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 369 |  | -0.102621 | 0.054086 | 0.257453 | 0.257453 | 0.653117 | 78.0 | 2.0 | 70 | 0 | false | true |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
| 21 | min_decision_score=70;min_target_distance_r=2 | 369 |  | -0.102621 | 0.054086 | 0.257453 | 0.257453 | 0.653117 | 78.0 | 2.0 | 70 | 2 | false | false |  |  |  |
| 22 | min_decision_score=70;min_target_distance_r=2;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 369 |  | -0.102621 | 0.054086 | 0.257453 | 0.257453 | 0.653117 | 78.0 | 2.0 | 70 | 2 | false | false |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
| 23 | min_decision_score=70;min_target_distance_r=2;require_session_window=true | 369 |  | -0.102621 | 0.054086 | 0.257453 | 0.257453 | 0.653117 | 78.0 | 2.0 | 70 | 2 | false | true |  |  |  |
| 24 | min_decision_score=70;min_target_distance_r=2;require_session_window=true;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 369 |  | -0.102621 | 0.054086 | 0.257453 | 0.257453 | 0.653117 | 78.0 | 2.0 | 70 | 2 | false | true |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
