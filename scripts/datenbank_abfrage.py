# Die Datei datenbank_abfrage.py ist für die Abfrage von Parameter- und Betriebsmodus Daten zuständig.

# Import von benötigten Modulen
# ======================================================================
import mysql.connector
# ======================================================================


# Abfragefunktion der Betriebsmodus Daten
# ======================================================================
def get_betriebsmodus():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="datenbank",
            passwd="rasp",
            database="datenbank"
        )

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

        print('Aktive Betriebsmodusdaten werden von Datenbank geladen')
        print('ID:', id)
        print('Slot:', parameter_slot)
        print('Status:', programm_status)
        print('Start:', datetime)
        print('Enddatum:', programm_datum_ende)
        print('Endzeit:', programm_zeit_ende)
    except:
        print("Fehler bei get_betriebsmodus()")
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("Betriebsmodusdaten Abfrage beendet")
# ======================================================================


# Abfragefunktion der Aktiven Parameter
# ======================================================================
def get_parameter():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="datenbank",
            passwd="rasp",
            database="datenbank"
        )

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

        print('Aktive Parameterdaten werden von Datenbank geladen')
        print('Slot:', slot)
        print('Pflanze:', pflanze)
        print('Temperatur:', temperatur)
        print('Lichtstunden:', lichtstunden)
        print('Wassermenge:', wassermenge)
        print('Luftfeuchtigkeit:', luftfeuchtigkeit)
    except:
        print("Fehler bei get_parameter()")
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("Betriebsmodusdaten Abfrage beendet")
# ======================================================================


# Start Datenbank Abfrage
# ======================================================================
def start_datenbank_abfrage():
    print('Start der Datenbankabfrage')
    get_betriebsmodus()
    get_parameter()
    print('Datenbankabfrage beendet')
# ======================================================================
