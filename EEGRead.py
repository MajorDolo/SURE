#SECOND CODE FROM GPT
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

ser = serial.Serial('/dev/tty.usbmodem14401', 9600)  # Change the serial port name to match your setup

plt.ion()
fig, ax = plt.subplots()
data = np.array([])
i = 0
while True:
    a = ser.readline()
    a = a.decode()
    b = float(a)
    data = np.append(data, b)

    ax.cla()
    ax.plot(data)

    xmin, xmax = ax.get_xlim()
    if i > xmax - xmin:
        ax.set_xlim(i - xmax + xmin, i)

    ax.relim()
    ax.autoscale_view()
    i += 1

    plt.pause(0.01)

ser.close()



# FIRST CODE
# import time
#
# import serial
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# import numpy as np
#
# ser = serial.Serial('/dev/tty.usbmodem14201', 9600) # Change the serial port name to match your setup
# plt.figure()
# plt.ion()
# plt.show()
# data = np.array([])
# i=0
# while True:
#     a= ser.readline()
#     a.decode()
#     b= float(a)
#     #actual_voltage_value = b * (5.0 / (1024 - 1));
#     data = np.append(data,b)
#     plt.cla()
#
#     plt.plot(data)
#     plt.pause(0.01)
#
# ser.close()
# def read_data():
#     line = ser.readline().decode().strip()
#     return int(line)

# def update(i):
#     y = read_data()
#     print(y)
#     plt.clf()
#     plt.plot(y, "-r")



# ani = animation.FuncAnimation(plt.gcf(), update, interval=1000)
#
# plt.show()

