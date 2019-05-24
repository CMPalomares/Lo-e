import serial
import time
import usb_finder as usb

from datetime import datetime


def get_timestamp():
    """Get timestamp in ISO 8601."""
    timestamp = datetime.utcnow()
    timestamp = timestamp.isoformat("T") + "Z"
    timestamp = timestamp.replace(":", "-")
    return timestamp

if __name__ == '__main__':

    print("")
    print("********************************************")
    print("*           GSR DATA LOGGER                *")
    print("********************************************")
    print("")
    
    # Get port where an arduino in connected.
    # Arduino Hardware ID is 2341
    port = usb.usb_finder("2341")
    # Connecto to port and read five lines from the buffer
    # to check that everything is alright. Then close
    connection = serial.Serial(port, 115200)
    for i in range(0, 5):
            connection.readline()
    connection.close()
    print("Connection established on port {}".format(port))

    # connection = serial.Serial("COM5", 115200)
    # print("Connection established")

    file_name = 'sensors_log_{}.csv'.format(get_timestamp())
    file = open(file_name, 'w')
    print("File opened")

    counter = 0

    try:
        # Wait for enter key press, then re-open serial
        # connection and read 5 lines to empty from 
        # wired data.
        input("Press enter to start reading")
        print("")
        connection = serial.Serial(port, 115200)
        for i in range(0, 5):
            connection.readline()
        
        # Read and parse a line, log it and print the data
        # to the screen in an overwritting message.
        while True:
            try:
                line = connection.readline().decode().rstrip()
                if line != "":
                    file.write("{}\n".format(line))
                    print("\r{} - value = {}                            ".format(counter, line), end="")
                    counter += 1

            except Exception as e:
                # Print exception an continue with next iteration
                print("Exception occurred {}".format(e))
                continue

    except KeyboardInterrupt:
        print("")
        print("User shutdown")

    finally:
        file.close()
        connection.close()
        print("")
        print("Connection closed")
        print("File closed")
        print("Bye bye sweettie")
