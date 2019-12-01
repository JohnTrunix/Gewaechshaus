# Die Datei betriebsmeldungen.py schreibt Betriebsmeldungen
# in die Datenbank.


# Import von benoetigten Modulen
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


# Die Betriebsmeldung wird in Datenbank geschrieben
# ======================================================================
def betriebsmeldung_einfuegen(meldung):
    mycursor = mydb.cursor()
    sql = "INSERT INTO betriebsmeldungen (datetime, meldung) VALUES (%s, %s)"
    val = (lokale_zeit, meldung)
    mycursor.execute(sql, val)
    mydb.commit()
# ======================================================================


# Abfrage anzahl vorhandener Betriebsmeldungen
# ======================================================================
def abfrage_anzahl_betriebsmeldungen():
    global anzahl_betriebsmeldungen
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT COUNT(*) FROM betriebsmeldungen")
    result = mycursor.fetchone()
    anzahl_betriebsmeldungen = int(result[0])
# ======================================================================


# Letzte 50 Betriebsmeldungen loeschen
# ======================================================================
def begrenzung_betriebsmeldung():
    mycursor = mydb.cursor()
    sql = "DELETE FROM betriebsmeldungen ORDER BY meldung DESC LIMIT 20;"
    mycursor.execute(sql)
    mydb.commit()
# ======================================================================


# Betriebsmeldung einfuegen
# ======================================================================
def neue_betriebsmeldung(meldung):
    systemzeit_abfrage()
    abfrage_anzahl_betriebsmeldungen()
    if anzahl_betriebsmeldungen >= 50:
        begrenzung_betriebsmeldung()
    else:
        pass
    betriebsmeldung_einfuegen(meldung)
# ======================================================================
