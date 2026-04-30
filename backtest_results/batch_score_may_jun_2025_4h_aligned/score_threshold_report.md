# ICT Decision Score Threshold Report

- events: `backtest_results\batch_score_may_jun_2025_4h_aligned\events.csv`
- thresholds: 0, 50, 70

## All Models
| scope | model | threshold | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | 102 | 94 | 5 | 64.872549 | 10.255853 | 2.965326 | 6.139794 | 0.230883 | 0.264706 | 0.411765 | 0.264706 | 0.607843 |  | 49 | target_rr_below_2:40;poor_pd_location:21;insufficient_displacement:11;equilibrium:7;target_rr_below_3:4 |
| all | ALL | 50 | 96 | 88 | 5 | 66.84375 | 10.85167 | 3.636237 | 6.415146 | 0.262566 | 0.270833 | 0.40625 | 0.28125 | 0.604167 |  | 43 | target_rr_below_2:36;poor_pd_location:21;insufficient_displacement:11;equilibrium:7;target_rr_below_3:2 |
| all | ALL | 70 | 41 | 36 | 2 | 87.682927 | 19.170037 | 2.965326 | 3.039949 | 0.456734 | 0.463415 | 0.414634 | 0.268293 | 0.414634 |  | 37 | target_rr_below_2:30;poor_pd_location:19;insufficient_displacement:7;equilibrium:3;target_rr_below_3:2 |

## By Model
| scope | model | threshold | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | breaker_block | 0 | 11 | 4 | 5 | 78.545455 | 15.78748 | 15.159227 | 1.928618 | 1.926678 | 0.363636 | 0.363636 | 0.363636 |  |  | 11 | insufficient_displacement:11;target_rr_below_2:8;poor_pd_location:5;equilibrium:3;target_rr_below_3:1 |
| model | ifvg_retest | 0 | 8 | 7 |  | 99.25 | 77.619041 | 9.722848 | 7.916192 | 2.217487 | 0.5 | 0.5 | 0.375 | 0.375 |  | 7 | target_rr_below_2:4;poor_pd_location:4;equilibrium:1;target_rr_below_3:1 |
| model | mitigation_block | 0 | 12 | 12 |  | 79.416667 | 3.184502 | 1.598802 | 0.533201 | -0.470817 | 0.333333 | 0.25 |  | 0.666667 |  | 12 | target_rr_below_2:12;poor_pd_location:5;equilibrium:2 |
| model | reclaimed_ob | 0 | 2 | 2 |  | 83.5 | 5.343611 | 5.343611 | 4.992324 | -0.28096 | 0.5 | 0.5 | 0.5 | 0.5 |  | 2 | target_rr_below_2:1;poor_pd_location:1 |
| model | rejection_block | 0 | 14 | 14 |  | 84.928571 | 5.547183 | 2.408596 | 2.145225 | 0.00882 | 0.571429 | 0.428571 | 0.285714 | 0.428571 |  | 11 | target_rr_below_2:11;poor_pd_location:6;equilibrium:1 |
| model | turtle_soup | 0 | 55 | 55 |  | 48.181818 | 4.200093 | 2.608813 | 9.005426 | 0.082948 | 0.109091 | 0.436364 | 0.272727 | 0.8 |  | 6 | target_rr_below_2:4;target_rr_below_3:2 |
| model | breaker_block | 50 | 11 | 4 | 5 | 78.545455 | 15.78748 | 15.159227 | 1.928618 | 1.926678 | 0.363636 | 0.363636 | 0.363636 |  |  | 11 | insufficient_displacement:11;target_rr_below_2:8;poor_pd_location:5;equilibrium:3;target_rr_below_3:1 |
| model | ifvg_retest | 50 | 8 | 7 |  | 99.25 | 77.619041 | 9.722848 | 7.916192 | 2.217487 | 0.5 | 0.5 | 0.375 | 0.375 |  | 7 | target_rr_below_2:4;poor_pd_location:4;equilibrium:1;target_rr_below_3:1 |
| model | mitigation_block | 50 | 12 | 12 |  | 79.416667 | 3.184502 | 1.598802 | 0.533201 | -0.470817 | 0.333333 | 0.25 |  | 0.666667 |  | 12 | target_rr_below_2:12;poor_pd_location:5;equilibrium:2 |
| model | reclaimed_ob | 50 | 2 | 2 |  | 83.5 | 5.343611 | 5.343611 | 4.992324 | -0.28096 | 0.5 | 0.5 | 0.5 | 0.5 |  | 2 | target_rr_below_2:1;poor_pd_location:1 |
| model | rejection_block | 50 | 14 | 14 |  | 84.928571 | 5.547183 | 2.408596 | 2.145225 | 0.00882 | 0.571429 | 0.428571 | 0.285714 | 0.428571 |  | 11 | target_rr_below_2:11;poor_pd_location:6;equilibrium:1 |
| model | turtle_soup | 50 | 49 | 49 |  | 50.0 | 4.528612 | 3.880096 | 9.895786 | 0.121733 | 0.102041 | 0.428571 | 0.306122 | 0.816327 |  |  |  |
| model | breaker_block | 70 | 7 | 3 | 2 | 88.0 | 11.41046 | 10.460501 | 2.198301 | 2.072475 | 0.428571 | 0.428571 | 0.428571 |  |  | 7 | insufficient_displacement:7;target_rr_below_2:4;poor_pd_location:4;target_rr_below_3:1 |
| model | ifvg_retest | 70 | 8 | 7 |  | 99.25 | 77.619041 | 9.722848 | 7.916192 | 2.217487 | 0.5 | 0.5 | 0.375 | 0.375 |  | 7 | target_rr_below_2:4;poor_pd_location:4;equilibrium:1;target_rr_below_3:1 |
| model | mitigation_block | 70 | 11 | 11 |  | 81.0 | 2.391287 | 1.598802 | 0.555602 | -0.422709 | 0.363636 | 0.272727 |  | 0.636364 |  | 11 | target_rr_below_2:11;poor_pd_location:5;equilibrium:1 |
| model | reclaimed_ob | 70 | 2 | 2 |  | 83.5 | 5.343611 | 5.343611 | 4.992324 | -0.28096 | 0.5 | 0.5 | 0.5 | 0.5 |  | 2 | target_rr_below_2:1;poor_pd_location:1 |
| model | rejection_block | 70 | 13 | 13 |  | 86.692308 | 5.812714 | 2.721903 | 2.294154 | -0.00659 | 0.538462 | 0.461538 | 0.307692 | 0.461538 |  | 10 | target_rr_below_2:10;poor_pd_location:5;equilibrium:1 |
