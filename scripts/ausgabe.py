# Die Datei ausgabe.py ist für die Aktoransteuerung zuständig.

# Import von benötigten Modulen
# ======================================================================
import busio
import time
import datetime
import mysql.connector
import subprocess
# ======================================================================


# MYSQL Konfiguration
# ======================================================================
connection = mysql.connector.connect(
    host="localhost",
    user="datenbank",
    passwd="rasp",
    database="datenbank"
)
# ======================================================================


# Abfrage der Betriebsmodus Daten
# ======================================================================
sql_select_Query = "select * from betriebsmodus"
cursor = connection.cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchall()
for row in records:
    id = (row[0])
    parameter_slot = (row[1])
    programm_status = (row[2])
    datetime = (row[3])
    programm_datum_ende = (row[4])
    programm_zeit_ende = (row[5])
# ======================================================================

print(id)
print(parameter_slot)
print(programm_status)
print(datetime)
print(programm_datum_ende)
print(programm_zeit_ende)
