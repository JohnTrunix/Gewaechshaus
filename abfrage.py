from python_tsl2591 import tsl2591
import adafruit_si7021
import board
import busio
import time
from datetime import datetime
import mysql.connector
import subprocess


mydb = mysql.connector.connect(
    host="localhost",
    user="datenbank",
    passwd="rasp",
    database="datenbank"
)


i2c = busio.I2C(board.SCL, board.SDA)
sensor_temperatur_luftfeuchtigkeit = adafruit_si7021.SI7021(i2c)


###########################################################################################################################################


def lichtsensor_abfrage():
    global lux_gerundet
    tsl = tsl2591()
    full, ir = tsl.get_full_luminosity()
    lux = tsl.calculate_lux(full, ir)
    lux_gerundet = (round(lux, 1))
    print("Lichtstärke:", lux_gerundet)


def temperatur_abfrage():
    global temperatur_gerundet
    print("Temperatur: %0.1f C" %
    sensor_temperatur_luftfeuchtigkeit.temperature)
    aktuelle_temperatur = (sensor_temperatur_luftfeuchtigkeit.temperature)
    temperatur_gerundet = (round(aktuelle_temperatur, 1))


def luftfeuchtigkeit_abfrage():
    global luftfeuchtigkeit_gerundet
    print("Luftfeuchtigkeit: %0.1f %%" %
    sensor_temperatur_luftfeuchtigkeit.relative_humidity)
    aktuelle_luftfeuchtigkeit = (
    sensor_temperatur_luftfeuchtigkeit.relative_humidity)
    luftfeuchtigkeit_gerundet = (round(aktuelle_luftfeuchtigkeit, 1))


def systemzeit_abfrage():
    global lokale_zeit
    lokale_zeit = (int(time.time()))


###########################################################################################################################################


def datenbank_lichtsensor_einfuegen():
    mycursor = mydb.cursor()
    sql = "INSERT INTO sensor_licht_1 (zeit, sensorwert) VALUES (%s, %s)"
    val = (lokale_zeit, lux_gerundet)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Lichtstärkedaten eingefügt")


def datenbank_luftfeuchtesensor_einfuegen():
    mycursor = mydb.cursor()
    sql = "INSERT INTO 	sensor_luftfeuchtigkeit_1 (zeit, sensorwert) VALUES (%s, %s)"
    val = (lokale_zeit, luftfeuchtigkeit_gerundet)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Luftfeuchtigkeitsdaten eingefügt")


def datenbank_temperatursensor_einfuegen():
    mycursor = mydb.cursor()
    sql = "INSERT INTO sensor_temperatur_1 (zeit, sensorwert) VALUES (%s, %s)"
    val = (lokale_zeit, temperatur_gerundet)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Temperaturdaten eingefügt")


###########################################################################################################################################


while True:
    print("")
    print("----------------------------")
    systemzeit_abfrage()
    lichtsensor_abfrage()
    temperatur_abfrage()
    luftfeuchtigkeit_abfrage()
    datenbank_lichtsensor_einfuegen()
    datenbank_luftfeuchtesensor_einfuegen()
    datenbank_temperatursensor_einfuegen()
    print("----------------------------")
    print("")
    time.sleep(20)