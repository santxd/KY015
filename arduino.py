import serial
import csv
import time
arduino_serial = serial.Serial('COM6', 9600)


def arduino_print1():
    global arduino_temperature
    time.sleep(1)
    arduino_temperature = arduino_serial.readline().decode()

def arduino_print2():
    global arduino_humidity
    time.sleep(2)
    arduino_humidity = arduino_serial.readline().decode()

while True:
    time.sleep(1)
    arduino_print1()
    archivo = open("temperature.csv", "a")
    archivo.write(arduino_temperature)
    archivo.close()
    print(f"Temperature:{arduino_temperature}")

    time.sleep(2)
    arduino_print2()
    archivo = open("humidity.csv", "a")
    archivo.write(arduino_humidity)
    archivo.close()
    print(f"Humidity:{arduino_humidity}")
