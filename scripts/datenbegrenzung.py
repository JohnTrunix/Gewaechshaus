# Die Datei datenbegrenzung.py löscht alle Sensorwerte,
# welche älter als 30 Tage alt sind automatisch.


# Import von benötigten Modulen
# ======================================================================
import time
from datetime import datetime
import mysql.connector
import subprocess
# ======================================================================


# MYSQL Konfiguration
# ======================================================================
mydb = mysql.connector.connect(
    host="localhost",
    user="datenbank",
    passwd="rasp",
    database="datenbank"
)
# ======================================================================


# Lichtsensor Begrenzung
# ======================================================================
def begrenzung_sensor_licht_1():
    mycursor = mydb.cursor()
    sql = "DELETE FROM sensor_licht_1 WHERE DATE(datetime) = CURDATE() - INTERVAL 30 DAY"
    mycursor.execute(sql)
    mydb.commit()
# ======================================================================


# Temperatursensor Begrenzung
# ======================================================================
def begrenzung_sensor_temperatur_1():
    mycursor = mydb.cursor()
    sql = "DELETE FROM sensor_temperatur_1 WHERE DATE(datetime) = CURDATE() - INTERVAL 30 DAY"
    mycursor.execute(sql)
    mydb.commit()
# ======================================================================


# Luftfeuchtigkeitsensor Begrenzung
# ======================================================================
def begrenzung_sensor_luftfeuchtigkeit_1():
    mycursor = mydb.cursor()
    sql = "DELETE FROM sensor_luftfeuchtigkeit_1 WHERE DATE(datetime) = CURDATE() - INTERVAL 30 DAY"
    mycursor.execute(sql)
    mydb.commit()
# ======================================================================


# Start Datenbegrenzung
# ======================================================================
def start_datenbegrenzung():
    print('Start der Sensorabfrage')
    try:
        print('Daten von sensor_licht_1 älter als 30 Tage werden gelöscht')
        begrenzung_sensor_licht_1()
    except:
        print('Fehler bei begrenzung_sensor_licht_1()')
    try:
        print('Daten von sensor_temperatur_1 älter als 30 Tage werden gelöscht')
        begrenzung_sensor_temperatur_1()
    except:
        print('Fehler bei begrenzung_sensor_temperatur_1()')
    try:
        print('Daten von sensor_luftfeuchtigkeit_1 älter als 30 Tage werden gelöscht')
        begrenzung_sensor_luftfeuchtigkeit_1()
    except:
        print('Fehler bei begrenzung_sensor_luftfeuchtigkeit_1')
    print('Datenbegrenzung beendet')
# ======================================================================
