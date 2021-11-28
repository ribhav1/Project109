import statistics
import csv
import pandas as pd

with open('StudentsPerformance.csv') as f:
    file_data = pd.read_csv(f)

test_score_list = file_data['math score'].to_list()

test_score_mean, test_score_median, test_score_mode, test_score_stdev = statistics.mean(test_score_list), statistics.median(test_score_list), statistics.mode(test_score_list), statistics.stdev(test_score_list)

print('Mean of this data is: ' + test_score_mean)
print('Median of this data is: ' + test_score_median)
print('Mode of this data is: ' + test_score_mode)
print('Standard Deviation of this data is: ' + test_score_stdev)

test_score_1stdev_start, test_score_1stdev_end = test_score_mean - test_score_stdev, test_score_mean + test_score_stdev
test_score_2stdev_start, test_score_2stdev_end = test_score_mean - (2 * test_score_stdev), test_score_mean + (2 * test_score_stdev)
test_score_3stdev_start, test_score_3stdev_end = test_score_mean - (3 * test_score_stdev), test_score_mean + (3 * test_score_stdev)

stddev_test_score_1_data = [result for result in test_score_list if result > test_score_1stdev_start and result < test_score_1stdev_end]
stddev_test_score_2_data = [result for result in test_score_list if result > test_score_2stdev_start and result < test_score_2stdev_end]
stddev_test_score_3_data = [result for result in test_score_list if result > test_score_3stdev_start and result < test_score_3stdev_end]

print('{}% of data lies within first standard deviation'.format(len(stddev_test_score_1_data) * 100.0 / len(test_score_list)))
print('{}% of data lies within second standard deviation'.format(len(stddev_test_score_2_data) * 100.0 / len(test_score_list)))
print('{}% of data lies within third standard deviation'.format(len(stddev_test_score_3_data) * 100.0 / len(test_score_list)))