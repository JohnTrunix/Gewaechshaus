# Import der Betriebsmeldungsfunktion
# ======================================================================
from betriebsmeldungen import neue_betriebsmeldung
# ======================================================================

# Import von benoetigten Modulen
# ======================================================================
try:
    import time
    from datetime import datetime
    import mysql.connector
    import subprocess
except:
    neue_betriebsmeldung(
        "[datenbegrenzung] Fehler bei der importierung von Modulen.")
# ======================================================================

# MYSQL Konfiguration
# ======================================================================
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="datenbank",
        passwd="rasp",
        database="datenbank"
    )
except:
    neue_betriebsmeldung(
        "[datenbegrenzung] Fehler bei der Datenbankverbindung.")
# ======================================================================

# Lichtsensor Begrenzung
# ======================================================================
def begrenzung_sensor_licht_1():
    mycursor = mydb.cursor()
    sql = "DELETE FROM sensor_licht_1 WHERE datetime < NOW() - INTERVAL 30 DAY;"
    mycursor.execute(sql)
    mydb.commit()
# ======================================================================

# Temperatursensor Begrenzung
# ======================================================================
def begrenzung_sensor_temperatur_1():
    mycursor = mydb.cursor()
    sql = "DELETE FROM sensor_temperatur_1 WHERE datetime < NOW() - INTERVAL 30 DAY;"
    mycursor.execute(sql)
    mydb.commit()
# ======================================================================

# Luftfeuchtigkeitsensor Begrenzung
# ======================================================================
def begrenzung_sensor_luftfeuchtigkeit_1():
    mycursor = mydb.cursor()
    sql = "DELETE FROM sensor_luftfeuchtigkeit_1 WHERE datetime < NOW() - INTERVAL 30 DAY;"
    mycursor.execute(sql)
    mydb.commit()
# ======================================================================

# Bodenfeuchtigkeitsensor Begrenzung
# ======================================================================
def begrenzung_sensor_bodenfeuchtigkeit_1():
    mycursor = mydb.cursor()
    sql = "DELETE FROM sensor_bodenfeuchtigkeit_1 WHERE datetime < NOW() - INTERVAL 30 DAY;"
    mycursor.execute(sql)
    mydb.commit()
# ======================================================================

# Start Datenbegrenzung
# ======================================================================
def start_datenbegrenzung():
    try:
        begrenzung_sensor_licht_1()
    except:
        neue_betriebsmeldung(
            "[datenbegrenzung] Fehler bei der Begrenzung von Lichtsensordaten.")
    try:
        begrenzung_sensor_temperatur_1()
    except:
        neue_betriebsmeldung(
            "[datenbegrenzung] Fehler bei der Begrenzung von Temperatursensordaten.")
    try:
        begrenzung_sensor_luftfeuchtigkeit_1()
    except:
        neue_betriebsmeldung(
            "[datenbegrenzung] Fehler bei der Begrenzung von Luftfeuchtigkeitssensordaten.")
    try:
        begrenzung_sensor_bodenfeuchtigkeit_1()
    except:
        neue_betriebsmeldung(
            "[datenbegrenzung] Fehler bei der Begrenzung von Bodenfeuchtigkeitssensordaten.")
# ======================================================================
