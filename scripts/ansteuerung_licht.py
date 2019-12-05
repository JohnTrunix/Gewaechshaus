# Import der Betriebsmeldungsfunktion
# ======================================================================
from betriebsmeldungen import neue_betriebsmeldung
# ======================================================================

# Import von benoetigten Modulen
# ======================================================================
try:
    import datenbank_abfrage
    import sensor_abfrage
    from ansteuerung_pwm_shield import licht_ein, licht_aus, grundstellung
    import time
    import datetime
    import mysql.connector
except:
    neue_betriebsmeldung(
        "[ansteuerung_licht] Fehler bei der importierung von Modulen.")
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
        "[ansteuerung_licht] Fehler bei der Datenbankverbindung.")
# ======================================================================

# Lichtzaehler reset
# ======================================================================
def reset_licht_zaehler():
    try:
        mycursor = mydb.cursor()
        sql = "update zwischenspeicher set licht_zaehler = '0'"
        mycursor.execute(sql)
        mydb.commit()
    except:
        neue_betriebsmeldung(
            "[ansteuerung_licht] Lichtzaehler in Datenbank konnte nicht zurueckgesetzt werden.")
# ======================================================================

# Lichtzaehler fortschritt berechnen
# ======================================================================
def aktueller_fortschritt():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="datenbank",
            passwd="rasp",
            database="datenbank"
        )
        global licht_zaehler
        sql_select_Query = "select licht_zaehler from zwischenspeicher"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
            licht_zaehler = (row[0])
        update_licht_zaehler()
    except:
        neue_betriebsmeldung(
            "[ansteuerung_licht] Aktueller Fortschritt bei der Lichtsteuerung konnte nicht ermittelt werden.")
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
# ======================================================================

# Lichtzaehler updaten
# ======================================================================
def update_licht_zaehler():
    try:
        global neue_zaehler_zeit
        neue_zaehler_zeit = (licht_zaehler + 30)
        mycursor = mydb.cursor()
        sql = "update zwischenspeicher set licht_zaehler = %s" % neue_zaehler_zeit
        mycursor.execute(sql)
        mydb.commit()
    except:
        neue_betriebsmeldung(
            "[ansteuerung_licht] Der Fortschritt der Lichtsteuerung konnte nicht an die Datenbank uebermittelt werden.")
# ======================================================================

# Regelkreis Licht
# ======================================================================
def start_lichtsteuerung():
    try:
        if datenbank_abfrage.programm_status == 1:
            aktueller_fortschritt()

            if int(datenbank_abfrage.lichtstunden) > 0:
                sollwert = (float(datenbank_abfrage.lichtstunden) * 60)
                if neue_zaehler_zeit < sollwert:
                    licht_ein()
                elif neue_zaehler_zeit >= sollwert:
                    licht_aus()
                else:
                    pass
            else:
                pass
        else:
            grundstellung()
    except:
        neue_betriebsmeldung(
            "[ansteuerung_licht] Die Lichtsteuerung konnte die Ausgaenge nicht ansteuern.")
# ======================================================================
