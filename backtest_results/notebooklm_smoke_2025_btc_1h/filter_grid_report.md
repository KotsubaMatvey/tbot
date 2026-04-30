# ICT Filter Grid Report

- events: `backtest_results\notebooklm_smoke_2025_btc_1h\events.csv`
- min_count: 10

## Top Filters
| rank | filter_name | count | filtered_out | expectancy | managed_expectancy | target_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | avg_decision_score | avg_rr | min_decision_score | min_target_distance_r | require_smt | require_session_window | allowed_displacement_grades | allowed_htf_locations | exclude_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 16 | 16 | -0.571429 | 0.214286 | 0.0625 | 0.1875 | 0.375 | 95.9375 | 14.115168 | 0 | 0 | false | false |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
| 2 | allowed_htf_locations=discount,premium;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 16 | 16 | -0.571429 | 0.214286 | 0.0625 | 0.1875 | 0.375 | 95.9375 | 14.115168 | 0 | 0 | false | false |  | discount,premium | equilibrium,poor_pd_location,target_rr_below_2 |
| 3 | min_target_distance_r=2 | 16 | 16 | -0.571429 | 0.214286 | 0.0625 | 0.1875 | 0.375 | 95.9375 | 14.115168 | 0 | 2 | false | false |  |  |  |
| 4 | min_target_distance_r=2;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 16 | 16 | -0.571429 | 0.214286 | 0.0625 | 0.1875 | 0.375 | 95.9375 | 14.115168 | 0 | 2 | false | false |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
| 5 | min_target_distance_r=2;allowed_htf_locations=discount,premium | 16 | 16 | -0.571429 | 0.214286 | 0.0625 | 0.1875 | 0.375 | 95.9375 | 14.115168 | 0 | 2 | false | false |  | discount,premium |  |
| 6 | min_target_distance_r=2;allowed_htf_locations=discount,premium;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 16 | 16 | -0.571429 | 0.214286 | 0.0625 | 0.1875 | 0.375 | 95.9375 | 14.115168 | 0 | 2 | false | false |  | discount,premium | equilibrium,poor_pd_location,target_rr_below_2 |
| 7 | min_decision_score=50;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 16 | 16 | -0.571429 | 0.214286 | 0.0625 | 0.1875 | 0.375 | 95.9375 | 14.115168 | 50 | 0 | false | false |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
| 8 | min_decision_score=50;allowed_htf_locations=discount,premium;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 16 | 16 | -0.571429 | 0.214286 | 0.0625 | 0.1875 | 0.375 | 95.9375 | 14.115168 | 50 | 0 | false | false |  | discount,premium | equilibrium,poor_pd_location,target_rr_below_2 |
| 9 | min_decision_score=50;min_target_distance_r=2 | 16 | 16 | -0.571429 | 0.214286 | 0.0625 | 0.1875 | 0.375 | 95.9375 | 14.115168 | 50 | 2 | false | false |  |  |  |
| 10 | min_decision_score=50;min_target_distance_r=2;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 16 | 16 | -0.571429 | 0.214286 | 0.0625 | 0.1875 | 0.375 | 95.9375 | 14.115168 | 50 | 2 | false | false |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
| 11 | min_decision_score=50;min_target_distance_r=2;allowed_htf_locations=discount,premium | 16 | 16 | -0.571429 | 0.214286 | 0.0625 | 0.1875 | 0.375 | 95.9375 | 14.115168 | 50 | 2 | false | false |  | discount,premium |  |
| 12 | min_decision_score=50;min_target_distance_r=2;allowed_htf_locations=discount,premium;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 16 | 16 | -0.571429 | 0.214286 | 0.0625 | 0.1875 | 0.375 | 95.9375 | 14.115168 | 50 | 2 | false | false |  | discount,premium | equilibrium,poor_pd_location,target_rr_below_2 |
| 13 | min_decision_score=70;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 16 | 16 | -0.571429 | 0.214286 | 0.0625 | 0.1875 | 0.375 | 95.9375 | 14.115168 | 70 | 0 | false | false |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
| 14 | min_decision_score=70;allowed_htf_locations=discount,premium;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 16 | 16 | -0.571429 | 0.214286 | 0.0625 | 0.1875 | 0.375 | 95.9375 | 14.115168 | 70 | 0 | false | false |  | discount,premium | equilibrium,poor_pd_location,target_rr_below_2 |
| 15 | min_decision_score=70;min_target_distance_r=2 | 16 | 16 | -0.571429 | 0.214286 | 0.0625 | 0.1875 | 0.375 | 95.9375 | 14.115168 | 70 | 2 | false | false |  |  |  |
| 16 | min_decision_score=70;min_target_distance_r=2;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 16 | 16 | -0.571429 | 0.214286 | 0.0625 | 0.1875 | 0.375 | 95.9375 | 14.115168 | 70 | 2 | false | false |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
| 17 | min_decision_score=70;min_target_distance_r=2;allowed_htf_locations=discount,premium | 16 | 16 | -0.571429 | 0.214286 | 0.0625 | 0.1875 | 0.375 | 95.9375 | 14.115168 | 70 | 2 | false | false |  | discount,premium |  |
| 18 | min_decision_score=70;min_target_distance_r=2;allowed_htf_locations=discount,premium;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 16 | 16 | -0.571429 | 0.214286 | 0.0625 | 0.1875 | 0.375 | 95.9375 | 14.115168 | 70 | 2 | false | false |  | discount,premium | equilibrium,poor_pd_location,target_rr_below_2 |
| 19 | none | 32 |  | -0.10499 | 0.143253 | 0.34375 | 0.09375 | 0.375 | 86.46875 | 7.416985 | 0 | 0 | false | false |  |  |  |
| 20 | allowed_htf_locations=discount,premium | 32 |  | -0.10499 | 0.143253 | 0.34375 | 0.09375 | 0.375 | 86.46875 | 7.416985 | 0 | 0 | false | false |  | discount,premium |  |
| 21 | min_decision_score=50 | 32 |  | -0.10499 | 0.143253 | 0.34375 | 0.09375 | 0.375 | 86.46875 | 7.416985 | 50 | 0 | false | false |  |  |  |
| 22 | min_decision_score=50;allowed_htf_locations=discount,premium | 32 |  | -0.10499 | 0.143253 | 0.34375 | 0.09375 | 0.375 | 86.46875 | 7.416985 | 50 | 0 | false | false |  | discount,premium |  |
| 23 | min_decision_score=70 | 32 |  | -0.10499 | 0.143253 | 0.34375 | 0.09375 | 0.375 | 86.46875 | 7.416985 | 70 | 0 | false | false |  |  |  |
| 24 | min_decision_score=70;allowed_htf_locations=discount,premium | 32 |  | -0.10499 | 0.143253 | 0.34375 | 0.09375 | 0.375 | 86.46875 | 7.416985 | 70 | 0 | false | false |  | discount,premium |  |
| 25 | min_target_distance_r=3 | 13 | 19 | -1.0 | -0.1 |  | 0.153846 | 0.384615 | 97.0 | 16.894411 | 0 | 3 | false | false |  |  |  |
| 26 | min_target_distance_r=3;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 13 | 19 | -1.0 | -0.1 |  | 0.153846 | 0.384615 | 97.0 | 16.894411 | 0 | 3 | false | false |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
| 27 | min_target_distance_r=3;allowed_htf_locations=discount,premium | 13 | 19 | -1.0 | -0.1 |  | 0.153846 | 0.384615 | 97.0 | 16.894411 | 0 | 3 | false | false |  | discount,premium |  |
| 28 | min_target_distance_r=3;allowed_htf_locations=discount,premium;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 13 | 19 | -1.0 | -0.1 |  | 0.153846 | 0.384615 | 97.0 | 16.894411 | 0 | 3 | false | false |  | discount,premium | equilibrium,poor_pd_location,target_rr_below_2 |
| 29 | min_decision_score=50;min_target_distance_r=3 | 13 | 19 | -1.0 | -0.1 |  | 0.153846 | 0.384615 | 97.0 | 16.894411 | 50 | 3 | false | false |  |  |  |
| 30 | min_decision_score=50;min_target_distance_r=3;exclude_no_trade_reasons=equilibrium,poor_pd_location,target_rr_below_2 | 13 | 19 | -1.0 | -0.1 |  | 0.153846 | 0.384615 | 97.0 | 16.894411 | 50 | 3 | false | false |  |  | equilibrium,poor_pd_location,target_rr_below_2 |
