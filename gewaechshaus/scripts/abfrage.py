# Die Datei abfrage.py ist für die Sensorabfrage zuständig.
# Wird start_sensorabfrage() ausgeführt, werden alle Sensorwerte
# abgefragt und in die MYSQL Datenbank geschrieben.


# Import von benötigten Modulen
############################################################
from python_tsl2591 import tsl2591
import adafruit_si7021
import board
import busio
import time
import datetime
import mysql.connector
import subprocess
import logging
############################################################


# Konfiguration des Logging Modul
############################################################
logger = logging.getLogger('abfrage')
logger.setLevel(logging.DEBUG)
ch = logging.FileHandler(
    'B:/SW Repos/Gewaechshaus/gewaechshaus/log/gewaechshaus.log')
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
############################################################


# MYSQL Konfiguration
############################################################
mydb = mysql.connector.connect(
    host="localhost",
    user="datenbank",
    passwd="rasp",
    database="datenbank"
)
############################################################


# I2C Bus Konfiguration
############################################################
i2c = busio.I2C(board.SCL, board.SDA)
sensor_temperatur_luftfeuchtigkeit = adafruit_si7021.SI7021(i2c)
############################################################


# Die Systemzeit wird als Variable gespeichert
############################################################
def systemzeit_abfrage():
    global lokale_zeit
    lokale_zeit = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
############################################################


# Lichtsensor wird abgefragt und die Datenbank Funktion wird aufgerufen
############################################################
def lichtsensor_abfrage():
    global lux_gerundet
    tsl = tsl2591()
    full, ir = tsl.get_full_luminosity()
    lux = tsl.calculate_lux(full, ir)
    lux_gerundet = (round(lux, 1))
    datenbank_lichtsensor_einfuegen()
############################################################


# Temperatursensor wird abgefragt und die Datenbank Funktion wird aufgerufen
############################################################
def temperatur_abfrage():
    global temperatur_gerundet
    aktuelle_temperatur = (
        sensor_temperatur_luftfeuchtigkeit.temperature)
    temperatur_gerundet = (round(aktuelle_temperatur, 1))
    datenbank_temperatursensor_einfuegen()
############################################################


# Luftfeuchtigkeitsensor wird abgefragt und die Datenbank Funktion wird aufgerufen
############################################################
def luftfeuchtigkeit_abfrage():
    global luftfeuchtigkeit_gerundet
    aktuelle_luftfeuchtigkeit = (
        sensor_temperatur_luftfeuchtigkeit.relative_humidity)
    luftfeuchtigkeit_gerundet = (round(aktuelle_luftfeuchtigkeit, 1))
    datenbank_luftfeuchtesensor_einfuegen()
############################################################


# Der Lichtsensor Wert wird in Datenbank geschrieben
############################################################
def datenbank_lichtsensor_einfuegen():
    mycursor = mydb.cursor()
    sql = "INSERT INTO sensor_licht_1 (datetime, sensorwert) VALUES ('%s', '%s')"
    val = (lokale_zeit, lux_gerundet)
    mycursor.execute(sql, val)
    mydb.commit()
############################################################


# Der Luftfeuchtigkeit Wert wird in Datenbank geschrieben
############################################################
def datenbank_luftfeuchtesensor_einfuegen():
    mycursor = mydb.cursor()
    sql = "INSERT INTO 	sensor_luftfeuchtigkeit_1 (datetime, sensorwert) VALUES ('%s', '%s')"
    val = (lokale_zeit, luftfeuchtigkeit_gerundet)
    mycursor.execute(sql, val)
    mydb.commit()
############################################################


# Der Temperatur Wert wird in Datenbank geschrieben
############################################################
def datenbank_temperatursensor_einfuegen():
    mycursor = mydb.cursor()
    sql = "INSERT INTO sensor_temperatur_1 (datetime, sensorwert) VALUES ('%s', '%s')"
    val = (lokale_zeit, temperatur_gerundet)
    mycursor.execute(sql, val)
    mydb.commit()
############################################################


# Starte alle Abfrage Funktionen
############################################################
def start_sensorabfrage():
    logger.debug('Start der Sensorabfrage')
    try:
        logger.debug('Aktuelle Zeit wird abgefragt')
        systemzeit_abfrage()
    except:
        logger.warning('Fehler bei systemzeit_abfrage()')
    try:
        logger.debug(
            'Aktuelle Lichtstärke wird abgefragt und an Datenbank gesendet')
        lichtsensor_abfrage()
    except:
        logger.warning('Fehler bei lichtsensor_abfrage()')
    try:
        logger.debug(
            'Aktuelle Temperatur wird abgefragt und an Datenbank gesendet')
        temperatur_abfrage()
    except:
        logger.warning('Fehler bei temperatur_abfrage()')
    try:
        logger.debug(
            'Aktuelle Luftfeuchtigkeit wird abgefragt und an Datenbank gesendet')
        luftfeuchtigkeit_abfrage()
    except:
        logger.warning('Fehler bei luftfeuchtigkeit_abfrage()')
    logger.debug('Sensorabfrage beendet')
############################################################
