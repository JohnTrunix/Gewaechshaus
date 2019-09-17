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


def systemzeit_abfrage():
    global lokale_zeit
    lokale_zeit = (int(time.time()))


def lichtsensor_abfrage():
    global lux_gerundet
    tsl = tsl2591()
    full, ir = tsl.get_full_luminosity()
    lux = tsl.calculate_lux(full, ir)
    lux_gerundet = (round(lux, 1))
    datenbank_lichtsensor_einfuegen()


def temperatur_abfrage():
    global temperatur_gerundet
    aktuelle_temperatur = (sensor_temperatur_luftfeuchtigkeit.temperature)
    temperatur_gerundet = (round(aktuelle_temperatur, 1))
    datenbank_temperatursensor_einfuegen()


def luftfeuchtigkeit_abfrage():
    global luftfeuchtigkeit_gerundet
    aktuelle_luftfeuchtigkeit = (sensor_temperatur_luftfeuchtigkeit.relative_humidity)
    luftfeuchtigkeit_gerundet = (round(aktuelle_luftfeuchtigkeit, 1))
    datenbank_luftfeuchtesensor_einfuegen()


###########################################################################################################################################


def datenbank_lichtsensor_einfuegen():
    mycursor = mydb.cursor()
    sql = "INSERT INTO sensor_licht_1 (zeit, sensorwert) VALUES (%s, %s)"
    val = (lokale_zeit, lux_gerundet)
    mycursor.execute(sql, val)
    mydb.commit()


def datenbank_luftfeuchtesensor_einfuegen():
    mycursor = mydb.cursor()
    sql = "INSERT INTO 	sensor_luftfeuchtigkeit_1 (zeit, sensorwert) VALUES (%s, %s)"
    val = (lokale_zeit, luftfeuchtigkeit_gerundet)
    mycursor.execute(sql, val)
    mydb.commit()


def datenbank_temperatursensor_einfuegen():
    mycursor = mydb.cursor()
    sql = "INSERT INTO sensor_temperatur_1 (zeit, sensorwert) VALUES (%s, %s)"
    val = (lokale_zeit, temperatur_gerundet)
    mycursor.execute(sql, val)
    mydb.commit()


###########################################################################################################################################


while True:
    print("")
    print("----------------------------")
    try:
        systemzeit_abfrage()
        print("Neue Sensorabfrage wird ausgeführt. Aktuelle Zeit:", lokale_zeit)
    except:
        print("Fehler bei systemzeit_abfrage()")
    try:
        lichtsensor_abfrage()
        print("Aktuelle Lichtstärke wird abgefragt und an Datenbank gesendet.")
    except:
        print("Fehler bei lichtsensor_abfrage()") 
    try:
        temperatur_abfrage()
        print("Aktuelle Temperatur wird abgefragt und an Datenbank gesendet.")
    except:
        print("Fehler bei temperatur_abfrage()") 
    try:
        luftfeuchtigkeit_abfrage()
        print("Aktuelle Luftfeuchtigkeit wird abgefragt und an Datenbank gesendet.")
    except:
        print("Fehler bei luftfeuchtigkeit_abfrage()") 
    print("Alle Sensorwerte wurden aktualisiert. Die nächste Aktualisierung erfolgt in 20 Sekunden.")
    print("----------------------------")
    print("")
    time.sleep(20)