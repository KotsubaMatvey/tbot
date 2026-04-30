# ICT Filter Grid Report

- events: `backtest_results\full_2025_4h_strict_ce_mt\events.csv`
- min_count: 10

## Top Filters
| rank | filter_name | count | filtered_out | expectancy | target_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_decision_score | avg_rr | min_decision_score | min_target_distance_r | require_smt | require_session_window | allowed_displacement_grades | allowed_htf_locations | exclude_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | allowed_displacement_grades=strong | 10 | 39 | 3.738123 | 0.3 | 0.2 | 0.1 | 100.0 | 3.224273 | 0 | 0 | false | false | strong |  |  |
| 2 | allowed_displacement_grades=strong;allowed_htf_locations=discount,premium | 10 | 39 | 3.738123 | 0.3 | 0.2 | 0.1 | 100.0 | 3.224273 | 0 | 0 | false | false | strong | discount,premium |  |
| 3 | min_decision_score=50;allowed_displacement_grades=strong | 10 | 39 | 3.738123 | 0.3 | 0.2 | 0.1 | 100.0 | 3.224273 | 50 | 0 | false | false | strong |  |  |
| 4 | min_decision_score=50;allowed_displacement_grades=strong;allowed_htf_locations=discount,premium | 10 | 39 | 3.738123 | 0.3 | 0.2 | 0.1 | 100.0 | 3.224273 | 50 | 0 | false | false | strong | discount,premium |  |
| 5 | min_decision_score=70;allowed_displacement_grades=strong | 10 | 39 | 3.738123 | 0.3 | 0.2 | 0.1 | 100.0 | 3.224273 | 70 | 0 | false | false | strong |  |  |
| 6 | min_decision_score=70;allowed_displacement_grades=strong;allowed_htf_locations=discount,premium | 10 | 39 | 3.738123 | 0.3 | 0.2 | 0.1 | 100.0 | 3.224273 | 70 | 0 | false | false | strong | discount,premium |  |
| 7 | allowed_displacement_grades=valid,strong | 15 | 34 | 2.790499 | 0.2 | 0.133333 | 0.133333 | 99.466667 | 2.942714 | 0 | 0 | false | false | valid,strong |  |  |
| 8 | allowed_displacement_grades=valid,strong;allowed_htf_locations=discount,premium | 15 | 34 | 2.790499 | 0.2 | 0.133333 | 0.133333 | 99.466667 | 2.942714 | 0 | 0 | false | false | valid,strong | discount,premium |  |
| 9 | min_decision_score=50;allowed_displacement_grades=valid,strong | 15 | 34 | 2.790499 | 0.2 | 0.133333 | 0.133333 | 99.466667 | 2.942714 | 50 | 0 | false | false | valid,strong |  |  |
| 10 | min_decision_score=50;allowed_displacement_grades=valid,strong;allowed_htf_locations=discount,premium | 15 | 34 | 2.790499 | 0.2 | 0.133333 | 0.133333 | 99.466667 | 2.942714 | 50 | 0 | false | false | valid,strong | discount,premium |  |
| 11 | min_decision_score=70;allowed_displacement_grades=valid,strong | 15 | 34 | 2.790499 | 0.2 | 0.133333 | 0.133333 | 99.466667 | 2.942714 | 70 | 0 | false | false | valid,strong |  |  |
| 12 | min_decision_score=70;allowed_displacement_grades=valid,strong;allowed_htf_locations=discount,premium | 15 | 34 | 2.790499 | 0.2 | 0.133333 | 0.133333 | 99.466667 | 2.942714 | 70 | 0 | false | false | valid,strong | discount,premium |  |
| 13 | min_target_distance_r=3 | 14 | 35 | 2.43045 | 0.214286 | 0.285714 | 0.285714 | 100.0 | 5.889971 | 0 | 3 | false | false |  |  |  |
| 14 | min_target_distance_r=3;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 14 | 35 | 2.43045 | 0.214286 | 0.285714 | 0.285714 | 100.0 | 5.889971 | 0 | 3 | false | false |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
| 15 | min_target_distance_r=3;allowed_htf_locations=discount,premium | 14 | 35 | 2.43045 | 0.214286 | 0.285714 | 0.285714 | 100.0 | 5.889971 | 0 | 3 | false | false |  | discount,premium |  |
| 16 | min_target_distance_r=3;allowed_htf_locations=discount,premium;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 14 | 35 | 2.43045 | 0.214286 | 0.285714 | 0.285714 | 100.0 | 5.889971 | 0 | 3 | false | false |  | discount,premium | equilibrium,poor_pd_location,target_rr_below_2 |
| 17 | min_decision_score=50;min_target_distance_r=3 | 14 | 35 | 2.43045 | 0.214286 | 0.285714 | 0.285714 | 100.0 | 5.889971 | 50 | 3 | false | false |  |  |  |
| 18 | min_decision_score=50;min_target_distance_r=3;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 14 | 35 | 2.43045 | 0.214286 | 0.285714 | 0.285714 | 100.0 | 5.889971 | 50 | 3 | false | false |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
| 19 | min_decision_score=50;min_target_distance_r=3;allowed_htf_locations=discount,premium | 14 | 35 | 2.43045 | 0.214286 | 0.285714 | 0.285714 | 100.0 | 5.889971 | 50 | 3 | false | false |  | discount,premium |  |
| 20 | min_decision_score=50;min_target_distance_r=3;allowed_htf_locations=discount,premium;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 14 | 35 | 2.43045 | 0.214286 | 0.285714 | 0.285714 | 100.0 | 5.889971 | 50 | 3 | false | false |  | discount,premium | equilibrium,poor_pd_location,target_rr_below_2 |
| 21 | min_decision_score=70;min_target_distance_r=3 | 14 | 35 | 2.43045 | 0.214286 | 0.285714 | 0.285714 | 100.0 | 5.889971 | 70 | 3 | false | false |  |  |  |
| 22 | min_decision_score=70;min_target_distance_r=3;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 14 | 35 | 2.43045 | 0.214286 | 0.285714 | 0.285714 | 100.0 | 5.889971 | 70 | 3 | false | false |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
| 23 | min_decision_score=70;min_target_distance_r=3;allowed_htf_locations=discount,premium | 14 | 35 | 2.43045 | 0.214286 | 0.285714 | 0.285714 | 100.0 | 5.889971 | 70 | 3 | false | false |  | discount,premium |  |
| 24 | min_decision_score=70;min_target_distance_r=3;allowed_htf_locations=discount,premium;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 14 | 35 | 2.43045 | 0.214286 | 0.285714 | 0.285714 | 100.0 | 5.889971 | 70 | 3 | false | false |  | discount,premium | equilibrium,poor_pd_location,target_rr_below_2 |
| 25 | exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 16 | 33 | 1.668128 | 0.1875 | 0.25 | 0.375 | 98.875 | 5.478067 | 0 | 0 | false | false |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
| 26 | allowed_htf_locations=discount,premium;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 16 | 33 | 1.668128 | 0.1875 | 0.25 | 0.375 | 98.875 | 5.478067 | 0 | 0 | false | false |  | discount,premium | equilibrium,poor_pd_location,target_rr_below_2 |
| 27 | min_target_distance_r=2 | 16 | 33 | 1.668128 | 0.1875 | 0.25 | 0.375 | 98.875 | 5.478067 | 0 | 2 | false | false |  |  |  |
| 28 | min_target_distance_r=2;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 16 | 33 | 1.668128 | 0.1875 | 0.25 | 0.375 | 98.875 | 5.478067 | 0 | 2 | false | false |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
| 29 | min_target_distance_r=2;allowed_htf_locations=discount,premium | 16 | 33 | 1.668128 | 0.1875 | 0.25 | 0.375 | 98.875 | 5.478067 | 0 | 2 | false | false |  | discount,premium |  |
| 30 | min_target_distance_r=2;allowed_htf_locations=discount,premium;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 16 | 33 | 1.668128 | 0.1875 | 0.25 | 0.375 | 98.875 | 5.478067 | 0 | 2 | false | false |  | discount,premium | equilibrium,poor_pd_location,target_rr_below_2 |
