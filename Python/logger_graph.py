import matplotlib.pyplot as plt # pip3 install matplotlib
import csv

from statistics import mean


def average_period(time_list):
    time_difference = []
    for i in range(1, len(time_list) - 1):
        time_difference.append(time_list[i] - time_list[i - 1])

    return mean(time_difference)


def average_reduction(data, window_size=20):
    averaged_data = []
    start = 0
    iteration = 1
    max_iterations = int(len(data) / window_size)
    max_iterations += 1 if len(data) % window_size > 0 else max_iterations
    while iteration <= max_iterations:
        data_sum = 0
        end = window_size * iteration if iteration < max_iterations else len(data)
        for i in range(start, end):
            data_sum += data[i]
        average = data_sum / abs(end - start)
        averaged_data.append(average)
        start += window_size
        iteration += 1
    return averaged_data
    

x = []
y = []

with open('sensors_log_15.1_2019-05-15T16-12-09.440914Z.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[1]))
        y.append(int(row[0]))
time_stamps = average_reduction(x, window_size=20)
data = average_reduction(y, window_size=20)

plt.plot(x, y, label='raw_data')
plt.plot(time_stamps, data, label='averaged_data')
plt.xlabel('milliseconds')
plt.ylabel('Galvanic response [0-1023]')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
