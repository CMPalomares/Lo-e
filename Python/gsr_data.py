import math

def mean(data):
    media = 0
    for entry in data:
         media += int(entry)
    media = media / len(data)
    return media

def standard_deviation(mean, data):
    media_sum = 0
    for entry in data:
        media_sum += pow((int(entry) - mean), 2)
    media_sum = media_sum / len(data)
    standard_deviation = math.sqrt(media_sum)
    return standard_deviation

def reading(file_name):
    # Open the file in read mode
    file = open(file_name, 'r')

    try:
        data = []
        # Iterate over the file lines
        for line in file:
            # Get a list (python equivalent to array) of entries in the line,
            # using ',' as separator (CSV format).
            # Each entry in entries can be access as entries[i]
            entries = line.split(',')
            if len(entries) == 1:
                entry = int(entries[0])
                if (entry < 5000) and (entry > 0):
                    data.append(entry)
    finally:
        # Close the file in the end
        file.close()
        return data

if __name__ == '__main__':
    data = reading("read_python_times_01-04-19.csv")
    print("Max value: ", max(data))
    print("Min value: ", min(data))
    mean = mean(data)
    standard_deviation = standard_deviation(mean, data)
    confidence_interval68 = (mean - standard_deviation, mean + standard_deviation)
    confidence_interval95 = (mean - 2*standard_deviation, mean + 2*standard_deviation)
    confidence_interval99 = (mean - 3*standard_deviation, mean + 3*standard_deviation)


    print("Mean: ", mean)
    print("Standard deviation: ", standard_deviation)
    print("Confidence interval 68: ", confidence_interval68)
    print("Confidence interval 95: ", confidence_interval95)
    print("Confidence interval 99: ", confidence_interval99)

