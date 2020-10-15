import serial
import csv
import time
arduino_serial = serial.Serial('COM6', 9600)


def arduino_imprimir():
    global arduino_lectura
    time.sleep(1)
    arduino_lectura = arduino_serial.readline().decode()

def arduino_imprimiir():
    global arduino_lecturaa
    time.sleep(2)
    arduino_lecturaa = arduino_serial.readline().decode()

while True:
    time.sleep(1)
    arduino_imprimir()
    archivo = open("temperatura.csv", "a")
    archivo.write(arduino_lectura)
    archivo.close()
    print(f"Lectura uno:{arduino_lectura}")

    time.sleep(2)
    arduino_imprimiir()
    archivo = open("humedad.csv", "a")
    archivo.write(arduino_lecturaa)
    archivo.close()
    print(f"Lectura dos:{arduino_lecturaa}")
