import datenbank_abfrage
import sensor_abfrage
from ansteuerung_pwm_shield import licht_ein, licht_aus, grundstellung
import time
import datetime
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="datenbank",
    passwd="rasp",
    database="datenbank"
)

def reset_licht_zaehler():
    try:
        mycursor = mydb.cursor()
        sql = "update zwischenspeicher set licht_zaehler = '0'"
        mycursor.execute(sql)
        mydb.commit()
    except:
        print("Fehler bei reset_licht_zaehler()")

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
        print("Fehler bei aktueller_fortschritt()")
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()

def update_licht_zaehler():
    try:
        global neue_zaehler_zeit
        neue_zaehler_zeit = (licht_zaehler + 30)      
        mycursor = mydb.cursor()
        sql = "update zwischenspeicher set licht_zaehler = %s" % neue_zaehler_zeit
        mycursor.execute(sql)
        mydb.commit()
    except:
        print("Fehler bei update_licht_zaehler()")

def start_lichtsteuerung():
    try:
        if datenbank_abfrage.programm_status == 1:
            aktueller_fortschritt()

            if int(datenbank_abfrage.lichtstunden) > 0:
                sollwert = (int(datenbank_abfrage.lichtstunden) * 60)

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
        print("Fehler bei start_lichtsteuerung()")