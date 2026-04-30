# ICT Filter Grid Report

- events: `backtest_results\batch_score_may_oct_2025_30m_btc_strict_spec\events.csv`
- min_count: 10

## Top Filters
| rank | filter_name | count | filtered_out | expectancy | target_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_decision_score | avg_rr | min_decision_score | min_target_distance_r | require_smt | require_session_window | allowed_displacement_grades | allowed_htf_locations | exclude_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 25 | 30 | 0.282732 | 0.28 | 0.48 | 0.64 | 99.0 | 6.276111 | 0 | 0 | false | false |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
| 2 | allowed_htf_locations=discount,premium;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 25 | 30 | 0.282732 | 0.28 | 0.48 | 0.64 | 99.0 | 6.276111 | 0 | 0 | false | false |  | discount,premium | equilibrium,poor_pd_location,target_rr_below_2 |
| 3 | min_target_distance_r=2 | 25 | 30 | 0.282732 | 0.28 | 0.48 | 0.64 | 99.0 | 6.276111 | 0 | 2 | false | false |  |  |  |
| 4 | min_target_distance_r=2;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 25 | 30 | 0.282732 | 0.28 | 0.48 | 0.64 | 99.0 | 6.276111 | 0 | 2 | false | false |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
| 5 | min_target_distance_r=2;allowed_htf_locations=discount,premium | 25 | 30 | 0.282732 | 0.28 | 0.48 | 0.64 | 99.0 | 6.276111 | 0 | 2 | false | false |  | discount,premium |  |
| 6 | min_target_distance_r=2;allowed_htf_locations=discount,premium;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 25 | 30 | 0.282732 | 0.28 | 0.48 | 0.64 | 99.0 | 6.276111 | 0 | 2 | false | false |  | discount,premium | equilibrium,poor_pd_location,target_rr_below_2 |
| 7 | min_decision_score=50;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 25 | 30 | 0.282732 | 0.28 | 0.48 | 0.64 | 99.0 | 6.276111 | 50 | 0 | false | false |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
| 8 | min_decision_score=50;allowed_htf_locations=discount,premium;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 25 | 30 | 0.282732 | 0.28 | 0.48 | 0.64 | 99.0 | 6.276111 | 50 | 0 | false | false |  | discount,premium | equilibrium,poor_pd_location,target_rr_below_2 |
| 9 | min_decision_score=50;min_target_distance_r=2 | 25 | 30 | 0.282732 | 0.28 | 0.48 | 0.64 | 99.0 | 6.276111 | 50 | 2 | false | false |  |  |  |
| 10 | min_decision_score=50;min_target_distance_r=2;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 25 | 30 | 0.282732 | 0.28 | 0.48 | 0.64 | 99.0 | 6.276111 | 50 | 2 | false | false |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
| 11 | min_decision_score=50;min_target_distance_r=2;allowed_htf_locations=discount,premium | 25 | 30 | 0.282732 | 0.28 | 0.48 | 0.64 | 99.0 | 6.276111 | 50 | 2 | false | false |  | discount,premium |  |
| 12 | min_decision_score=50;min_target_distance_r=2;allowed_htf_locations=discount,premium;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 25 | 30 | 0.282732 | 0.28 | 0.48 | 0.64 | 99.0 | 6.276111 | 50 | 2 | false | false |  | discount,premium | equilibrium,poor_pd_location,target_rr_below_2 |
| 13 | min_decision_score=70;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 25 | 30 | 0.282732 | 0.28 | 0.48 | 0.64 | 99.0 | 6.276111 | 70 | 0 | false | false |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
| 14 | min_decision_score=70;allowed_htf_locations=discount,premium;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 25 | 30 | 0.282732 | 0.28 | 0.48 | 0.64 | 99.0 | 6.276111 | 70 | 0 | false | false |  | discount,premium | equilibrium,poor_pd_location,target_rr_below_2 |
| 15 | min_decision_score=70;min_target_distance_r=2 | 25 | 30 | 0.282732 | 0.28 | 0.48 | 0.64 | 99.0 | 6.276111 | 70 | 2 | false | false |  |  |  |
| 16 | min_decision_score=70;min_target_distance_r=2;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 25 | 30 | 0.282732 | 0.28 | 0.48 | 0.64 | 99.0 | 6.276111 | 70 | 2 | false | false |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
| 17 | min_decision_score=70;min_target_distance_r=2;allowed_htf_locations=discount,premium | 25 | 30 | 0.282732 | 0.28 | 0.48 | 0.64 | 99.0 | 6.276111 | 70 | 2 | false | false |  | discount,premium |  |
| 18 | min_decision_score=70;min_target_distance_r=2;allowed_htf_locations=discount,premium;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 25 | 30 | 0.282732 | 0.28 | 0.48 | 0.64 | 99.0 | 6.276111 | 70 | 2 | false | false |  | discount,premium | equilibrium,poor_pd_location,target_rr_below_2 |
| 19 | none | 55 |  | 0.133262 | 0.381818 | 0.327273 | 0.563636 | 94.327273 | 3.402272 | 0 | 0 | false | false |  |  |  |
| 20 | allowed_htf_locations=discount,premium | 55 |  | 0.133262 | 0.381818 | 0.327273 | 0.563636 | 94.327273 | 3.402272 | 0 | 0 | false | false |  | discount,premium |  |
| 21 | min_decision_score=50 | 55 |  | 0.133262 | 0.381818 | 0.327273 | 0.563636 | 94.327273 | 3.402272 | 50 | 0 | false | false |  |  |  |
| 22 | min_decision_score=50;allowed_htf_locations=discount,premium | 55 |  | 0.133262 | 0.381818 | 0.327273 | 0.563636 | 94.327273 | 3.402272 | 50 | 0 | false | false |  | discount,premium |  |
| 23 | min_decision_score=70 | 55 |  | 0.133262 | 0.381818 | 0.327273 | 0.563636 | 94.327273 | 3.402272 | 70 | 0 | false | false |  |  |  |
| 24 | min_decision_score=70;allowed_htf_locations=discount,premium | 55 |  | 0.133262 | 0.381818 | 0.327273 | 0.563636 | 94.327273 | 3.402272 | 70 | 0 | false | false |  | discount,premium |  |
| 25 | allowed_displacement_grades=valid,strong | 17 | 38 | 0.034228 | 0.294118 | 0.352941 | 0.705882 | 100.0 | 3.197427 | 0 | 0 | false | false | valid,strong |  |  |
| 26 | allowed_displacement_grades=valid,strong;allowed_htf_locations=discount,premium | 17 | 38 | 0.034228 | 0.294118 | 0.352941 | 0.705882 | 100.0 | 3.197427 | 0 | 0 | false | false | valid,strong | discount,premium |  |
| 27 | min_decision_score=50;allowed_displacement_grades=valid,strong | 17 | 38 | 0.034228 | 0.294118 | 0.352941 | 0.705882 | 100.0 | 3.197427 | 50 | 0 | false | false | valid,strong |  |  |
| 28 | min_decision_score=50;allowed_displacement_grades=valid,strong;allowed_htf_locations=discount,premium | 17 | 38 | 0.034228 | 0.294118 | 0.352941 | 0.705882 | 100.0 | 3.197427 | 50 | 0 | false | false | valid,strong | discount,premium |  |
| 29 | min_decision_score=70;allowed_displacement_grades=valid,strong | 17 | 38 | 0.034228 | 0.294118 | 0.352941 | 0.705882 | 100.0 | 3.197427 | 70 | 0 | false | false | valid,strong |  |  |
| 30 | min_decision_score=70;allowed_displacement_grades=valid,strong;allowed_htf_locations=discount,premium | 17 | 38 | 0.034228 | 0.294118 | 0.352941 | 0.705882 | 100.0 | 3.197427 | 70 | 0 | false | false | valid,strong | discount,premium |  |
