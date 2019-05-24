import serial
import time

connection = serial.Serial("COM5", 115200)

print("Hello")

file = open("read_1.csv", "w")
file2 = open("read_times", "w")
counter = 0
limit = 20000 

try:
    while True:
        # lines = []
        # lines = connection.readlines()
        # for line in lines:
        #   print("value = {}".format(line))
        start_time = int(time.time() * 1000000)
        line = connection.readline().decode().rstrip()
        if line != "":
            file.write("{}\n".format(line))
            print("\r{} - value = {}    ".format(counter, line), end="")
            finish_time = int(time.time() * 1000000) - start_time
            file2.write("{}\n".format(finish_time))
            counter += 1
        if counter >= limit:
            break
        time.sleep(0.01)
finally:
    file.close()
    file2.close()
