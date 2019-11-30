# Die Datei fehlermeldungen.py schreibt Fehlermeldungen
# in die Datenbank.


# Import von benötigten Modulen
# ======================================================================
import time
import datetime
import mysql.connector
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


# Die Systemzeit wird als Variable gespeichert
# ======================================================================
def systemzeit_abfrage():
    global lokale_zeit
    lokale_zeit = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# ======================================================================


# Die Fehlermeldung wird in Datenbank geschrieben
# ======================================================================
def fehlermeldung_einfuegen(meldung):
    mycursor = mydb.cursor()
    sql = "INSERT INTO fehlermeldungen (datetime, meldung) VALUES (%s, %s)"
    val = (lokale_zeit, meldung)
    mycursor.execute(sql, val)
    mydb.commit()
# ======================================================================


# Abfrage anzahl vorhandener Fehlermeldungen
# ======================================================================
def abfrage_anzahl_fehlermeldungen():
    global anzahl_fehlermeldungen
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT COUNT(*) FROM fehlermeldungen")
    result = mycursor.fetchone()
    anzahl_fehlermeldungen = int(result[0])
# ======================================================================


# Letzte 50 Fehlermeldungen löschen
# ======================================================================
def begrenzung_fehlermeldung():
    mycursor = mydb.cursor()
    sql = "DELETE FROM fehlermeldungen ORDER BY meldung DESC LIMIT 20;"
    mycursor.execute(sql)
    mydb.commit()
# ======================================================================


# Fehlermeldung einfuegen
# ======================================================================
def neue_fehlermeldung(meldung):
    systemzeit_abfrage()
    abfrage_anzahl_fehlermeldungen()
    if anzahl_fehlermeldungen >= 50:
        begrenzung_fehlermeldung()
    else:
        pass
    fehlermeldung_einfuegen(meldung)
# ======================================================================
