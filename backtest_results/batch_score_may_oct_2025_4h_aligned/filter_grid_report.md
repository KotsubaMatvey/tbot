# ICT Filter Grid Report

- events: `backtest_results\batch_score_may_oct_2025_4h_aligned\events.csv`
- min_count: 10

## Top Filters
| rank | filter_name | count | filtered_out | expectancy | target_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_decision_score | avg_rr | min_decision_score | min_target_distance_r | require_smt | require_session_window | allowed_displacement_grades | allowed_htf_locations | exclude_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | min_target_distance_r=3;allowed_displacement_grades=valid,strong | 11 | 260 | 4.459337 | 0.181818 | 0.272727 | 0.636364 | 99.727273 | 13.722614 | 0 | 3 | false | false | valid,strong |  |  |
| 2 | min_target_distance_r=3;allowed_displacement_grades=valid,strong;allowed_htf_locations=discount,premium | 11 | 260 | 4.459337 | 0.181818 | 0.272727 | 0.636364 | 99.727273 | 13.722614 | 0 | 3 | false | false | valid,strong | discount,premium |  |
| 3 | min_decision_score=50;min_target_distance_r=3;allowed_displacement_grades=valid,strong | 11 | 260 | 4.459337 | 0.181818 | 0.272727 | 0.636364 | 99.727273 | 13.722614 | 50 | 3 | false | false | valid,strong |  |  |
| 4 | min_decision_score=50;min_target_distance_r=3;allowed_displacement_grades=valid,strong;allowed_htf_locations=discount,premium | 11 | 260 | 4.459337 | 0.181818 | 0.272727 | 0.636364 | 99.727273 | 13.722614 | 50 | 3 | false | false | valid,strong | discount,premium |  |
| 5 | min_decision_score=70;min_target_distance_r=3;allowed_displacement_grades=valid,strong | 11 | 260 | 4.459337 | 0.181818 | 0.272727 | 0.636364 | 99.727273 | 13.722614 | 70 | 3 | false | false | valid,strong |  |  |
| 6 | min_decision_score=70;min_target_distance_r=3;allowed_displacement_grades=valid,strong;allowed_htf_locations=discount,premium | 11 | 260 | 4.459337 | 0.181818 | 0.272727 | 0.636364 | 99.727273 | 13.722614 | 70 | 3 | false | false | valid,strong | discount,premium |  |
| 7 | min_target_distance_r=2;allowed_displacement_grades=valid,strong | 12 | 259 | 4.298858 | 0.25 | 0.333333 | 0.583333 | 99.75 | 12.803569 | 0 | 2 | false | false | valid,strong |  |  |
| 8 | min_target_distance_r=2;allowed_displacement_grades=valid,strong;allowed_htf_locations=discount,premium | 12 | 259 | 4.298858 | 0.25 | 0.333333 | 0.583333 | 99.75 | 12.803569 | 0 | 2 | false | false | valid,strong | discount,premium |  |
| 9 | min_decision_score=50;min_target_distance_r=2;allowed_displacement_grades=valid,strong | 12 | 259 | 4.298858 | 0.25 | 0.333333 | 0.583333 | 99.75 | 12.803569 | 50 | 2 | false | false | valid,strong |  |  |
| 10 | min_decision_score=50;min_target_distance_r=2;allowed_displacement_grades=valid,strong;allowed_htf_locations=discount,premium | 12 | 259 | 4.298858 | 0.25 | 0.333333 | 0.583333 | 99.75 | 12.803569 | 50 | 2 | false | false | valid,strong | discount,premium |  |
| 11 | min_decision_score=70;min_target_distance_r=2;allowed_displacement_grades=valid,strong | 12 | 259 | 4.298858 | 0.25 | 0.333333 | 0.583333 | 99.75 | 12.803569 | 70 | 2 | false | false | valid,strong |  |  |
| 12 | min_decision_score=70;min_target_distance_r=2;allowed_displacement_grades=valid,strong;allowed_htf_locations=discount,premium | 12 | 259 | 4.298858 | 0.25 | 0.333333 | 0.583333 | 99.75 | 12.803569 | 70 | 2 | false | false | valid,strong | discount,premium |  |
| 13 | allowed_displacement_grades=strong | 16 | 255 | 2.388797 | 0.4375 | 0.3125 | 0.4375 | 98.6875 | 7.872087 | 0 | 0 | false | false | strong |  |  |
| 14 | allowed_displacement_grades=strong;allowed_htf_locations=discount,premium | 16 | 255 | 2.388797 | 0.4375 | 0.3125 | 0.4375 | 98.6875 | 7.872087 | 0 | 0 | false | false | strong | discount,premium |  |
| 15 | min_decision_score=50;allowed_displacement_grades=strong | 16 | 255 | 2.388797 | 0.4375 | 0.3125 | 0.4375 | 98.6875 | 7.872087 | 50 | 0 | false | false | strong |  |  |
| 16 | min_decision_score=50;allowed_displacement_grades=strong;allowed_htf_locations=discount,premium | 16 | 255 | 2.388797 | 0.4375 | 0.3125 | 0.4375 | 98.6875 | 7.872087 | 50 | 0 | false | false | strong | discount,premium |  |
| 17 | min_decision_score=70;allowed_displacement_grades=strong | 16 | 255 | 2.388797 | 0.4375 | 0.3125 | 0.4375 | 98.6875 | 7.872087 | 70 | 0 | false | false | strong |  |  |
| 18 | min_decision_score=70;allowed_displacement_grades=strong;allowed_htf_locations=discount,premium | 16 | 255 | 2.388797 | 0.4375 | 0.3125 | 0.4375 | 98.6875 | 7.872087 | 70 | 0 | false | false | strong | discount,premium |  |
| 19 | allowed_displacement_grades=valid,strong | 24 | 247 | 1.934527 | 0.375 | 0.25 | 0.541667 | 98.875 | 6.69314 | 0 | 0 | false | false | valid,strong |  |  |
| 20 | allowed_displacement_grades=valid,strong;allowed_htf_locations=discount,premium | 24 | 247 | 1.934527 | 0.375 | 0.25 | 0.541667 | 98.875 | 6.69314 | 0 | 0 | false | false | valid,strong | discount,premium |  |
| 21 | min_decision_score=50;allowed_displacement_grades=valid,strong | 24 | 247 | 1.934527 | 0.375 | 0.25 | 0.541667 | 98.875 | 6.69314 | 50 | 0 | false | false | valid,strong |  |  |
| 22 | min_decision_score=50;allowed_displacement_grades=valid,strong;allowed_htf_locations=discount,premium | 24 | 247 | 1.934527 | 0.375 | 0.25 | 0.541667 | 98.875 | 6.69314 | 50 | 0 | false | false | valid,strong | discount,premium |  |
| 23 | min_decision_score=70;allowed_displacement_grades=valid,strong | 24 | 247 | 1.934527 | 0.375 | 0.25 | 0.541667 | 98.875 | 6.69314 | 70 | 0 | false | false | valid,strong |  |  |
| 24 | min_decision_score=70;allowed_displacement_grades=valid,strong;allowed_htf_locations=discount,premium | 24 | 247 | 1.934527 | 0.375 | 0.25 | 0.541667 | 98.875 | 6.69314 | 70 | 0 | false | false | valid,strong | discount,premium |  |
| 25 | min_target_distance_r=3 | 136 | 135 | 0.626553 | 0.117647 | 0.301471 | 0.757353 | 80.735294 | 9.014319 | 0 | 3 | false | false |  |  |  |
| 26 | min_target_distance_r=3;allowed_htf_locations=discount,premium | 136 | 135 | 0.626553 | 0.117647 | 0.301471 | 0.757353 | 80.735294 | 9.014319 | 0 | 3 | false | false |  | discount,premium |  |
| 27 | min_decision_score=50;min_target_distance_r=3 | 136 | 135 | 0.626553 | 0.117647 | 0.301471 | 0.757353 | 80.735294 | 9.014319 | 50 | 3 | false | false |  |  |  |
| 28 | min_decision_score=50;min_target_distance_r=3;allowed_htf_locations=discount,premium | 136 | 135 | 0.626553 | 0.117647 | 0.301471 | 0.757353 | 80.735294 | 9.014319 | 50 | 3 | false | false |  | discount,premium |  |
| 29 | min_decision_score=70;min_target_distance_r=3 | 111 | 160 | 0.61572 | 0.108108 | 0.288288 | 0.765766 | 84.279279 | 9.344967 | 70 | 3 | false | false |  |  |  |
| 30 | min_decision_score=70;min_target_distance_r=3;allowed_htf_locations=discount,premium | 111 | 160 | 0.61572 | 0.108108 | 0.288288 | 0.765766 | 84.279279 | 9.344967 | 70 | 3 | false | false |  | discount,premium |  |
