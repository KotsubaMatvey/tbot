# ICT Decision Score Threshold Report

- events: `backtest_results\batch_score_may_oct_2025_4h_strict_spec\events.csv`
- thresholds: 0, 50, 70

## All Models
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all | ALL | 0 | none |  | 40 | 40 |  | 92.3 | 9.852785 | 3.727477 | 2.810224 | 0.827924 | 0.6 | 0.475 | 0.275 | 0.4 |  | 28 | target_rr_below_2:25;target_rr_below_3:3 |
| filtered_all | ALL | 0 | model_rules | 25 | 15 | 15 |  | 97.0 | 22.101545 | 10.574804 | 6.314256 | 1.875124 | 0.4 | 0.466667 | 0.466667 | 0.6 |  | 3 | target_rr_below_3:3 |
| all | ALL | 50 | none |  | 40 | 40 |  | 92.3 | 9.852785 | 3.727477 | 2.810224 | 0.827924 | 0.6 | 0.475 | 0.275 | 0.4 |  | 28 | target_rr_below_2:25;target_rr_below_3:3 |
| filtered_all | ALL | 50 | model_rules | 25 | 15 | 15 |  | 97.0 | 22.101545 | 10.574804 | 6.314256 | 1.875124 | 0.4 | 0.466667 | 0.466667 | 0.6 |  | 3 | target_rr_below_3:3 |
| all | ALL | 70 | none |  | 40 | 40 |  | 92.3 | 9.852785 | 3.727477 | 2.810224 | 0.827924 | 0.6 | 0.475 | 0.275 | 0.4 |  | 28 | target_rr_below_2:25;target_rr_below_3:3 |
| filtered_all | ALL | 70 | model_rules | 25 | 15 | 15 |  | 97.0 | 22.101545 | 10.574804 | 6.314256 | 1.875124 | 0.4 | 0.466667 | 0.466667 | 0.6 |  | 3 | target_rr_below_3:3 |

## By Model
| scope | model | threshold | filter_name | filtered_out | count | activated_trades | invalidated_before_entry | avg_decision_score | avg_mfe_r | median_mfe_r | avg_rr | expectancy | target_before_invalidation_rate | hit_1r_before_invalidation_rate | hit_2r_before_invalidation_rate | invalidation_rate | same_bar_ambiguous_count | no_trade_reason_count | top_no_trade_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model | ifvg_retest | 0 | none |  | 11 | 11 |  | 100.0 | 21.476651 | 2.58886 | 3.739624 | 1.260362 | 0.545455 | 0.545455 | 0.272727 | 0.454545 |  | 6 | target_rr_below_2:6 |
| model | reclaimed_ob | 0 | none |  | 4 | 4 |  | 87.25 | 12.810196 | 9.397534 | 3.128678 | 2.559446 | 0.75 | 0.75 | 0.75 | 0.25 |  | 3 | target_rr_below_2:2;target_rr_below_3:1 |
| model | rejection_block | 0 | none |  | 25 | 25 |  | 89.72 | 4.265098 | 3.506069 | 2.350335 | 0.360607 | 0.6 | 0.4 | 0.2 | 0.4 |  | 19 | target_rr_below_2:17;target_rr_below_3:2 |
| filtered_model | ifvg_retest | 0 | model_rules | 6 | 5 | 5 |  | 100.0 | 45.433077 | 33.024085 | 7.594709 | 2.902601 | 0.4 | 0.4 | 0.4 | 0.6 |  |  |  |
| filtered_model | reclaimed_ob | 0 | model_rules | 2 | 2 | 2 |  | 93.5 | 20.27678 | 20.27678 | 5.399852 | 5.399852 | 1.0 | 1.0 | 1.0 |  |  | 1 | target_rr_below_3:1 |
| filtered_model | rejection_block | 0 | model_rules | 17 | 8 | 8 |  | 96.0 | 7.975529 | 8.256012 | 5.742573 | 0.351769 | 0.25 | 0.375 | 0.375 | 0.75 |  | 2 | target_rr_below_3:2 |
| model | ifvg_retest | 50 | none |  | 11 | 11 |  | 100.0 | 21.476651 | 2.58886 | 3.739624 | 1.260362 | 0.545455 | 0.545455 | 0.272727 | 0.454545 |  | 6 | target_rr_below_2:6 |
| model | reclaimed_ob | 50 | none |  | 4 | 4 |  | 87.25 | 12.810196 | 9.397534 | 3.128678 | 2.559446 | 0.75 | 0.75 | 0.75 | 0.25 |  | 3 | target_rr_below_2:2;target_rr_below_3:1 |
| model | rejection_block | 50 | none |  | 25 | 25 |  | 89.72 | 4.265098 | 3.506069 | 2.350335 | 0.360607 | 0.6 | 0.4 | 0.2 | 0.4 |  | 19 | target_rr_below_2:17;target_rr_below_3:2 |
| filtered_model | ifvg_retest | 50 | model_rules | 6 | 5 | 5 |  | 100.0 | 45.433077 | 33.024085 | 7.594709 | 2.902601 | 0.4 | 0.4 | 0.4 | 0.6 |  |  |  |
| filtered_model | reclaimed_ob | 50 | model_rules | 2 | 2 | 2 |  | 93.5 | 20.27678 | 20.27678 | 5.399852 | 5.399852 | 1.0 | 1.0 | 1.0 |  |  | 1 | target_rr_below_3:1 |
| filtered_model | rejection_block | 50 | model_rules | 17 | 8 | 8 |  | 96.0 | 7.975529 | 8.256012 | 5.742573 | 0.351769 | 0.25 | 0.375 | 0.375 | 0.75 |  | 2 | target_rr_below_3:2 |
| model | ifvg_retest | 70 | none |  | 11 | 11 |  | 100.0 | 21.476651 | 2.58886 | 3.739624 | 1.260362 | 0.545455 | 0.545455 | 0.272727 | 0.454545 |  | 6 | target_rr_below_2:6 |
| model | reclaimed_ob | 70 | none |  | 4 | 4 |  | 87.25 | 12.810196 | 9.397534 | 3.128678 | 2.559446 | 0.75 | 0.75 | 0.75 | 0.25 |  | 3 | target_rr_below_2:2;target_rr_below_3:1 |
| model | rejection_block | 70 | none |  | 25 | 25 |  | 89.72 | 4.265098 | 3.506069 | 2.350335 | 0.360607 | 0.6 | 0.4 | 0.2 | 0.4 |  | 19 | target_rr_below_2:17;target_rr_below_3:2 |
| filtered_model | ifvg_retest | 70 | model_rules | 6 | 5 | 5 |  | 100.0 | 45.433077 | 33.024085 | 7.594709 | 2.902601 | 0.4 | 0.4 | 0.4 | 0.6 |  |  |  |
| filtered_model | reclaimed_ob | 70 | model_rules | 2 | 2 | 2 |  | 93.5 | 20.27678 | 20.27678 | 5.399852 | 5.399852 | 1.0 | 1.0 | 1.0 |  |  | 1 | target_rr_below_3:1 |
| filtered_model | rejection_block | 70 | model_rules | 17 | 8 | 8 |  | 96.0 | 7.975529 | 8.256012 | 5.742573 | 0.351769 | 0.25 | 0.375 | 0.375 | 0.75 |  | 2 | target_rr_below_3:2 |
