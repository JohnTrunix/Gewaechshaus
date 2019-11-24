# Die Datei ausgabe.py ist für die Aktoransteuerung zuständig.

# Import von benötigten Modulen
# ======================================================================
import mysql.connector
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
def get_betriebsmodus():
    global id
    global parameter_slot
    global programm_status
    global datetime
    global programm_datum_ende
    global programm_zeit_ende
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


# Abfrage der Aktiven Parameter
# ======================================================================
def get_parameter():
    global slot
    global pflanze
    global temperatur
    global lichtstunden
    global wassermenge
    global luftfeuchtigkeit
    sql_select_Query = (
        "SELECT `slot`, `pflanze`, `temperatur`, `lichtstunden`, `wassermenge`, `luftfeuchtigkeit` FROM `parameter` WHERE slot = %s" % parameter_slot)
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    for row in records:
        slot = (row[0])
        pflanze = (row[1])
        temperatur = (row[2])
        lichtstunden = (row[3])
        wassermenge = (row[4])
        luftfeuchtigkeit = (row[5])
