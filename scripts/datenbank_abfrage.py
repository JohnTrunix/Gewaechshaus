# Import der Betriebsmeldungsfunktion
# ======================================================================
from betriebsmeldungen import neue_betriebsmeldung
# ======================================================================

# Import von benoetigten Modulen
# ======================================================================
try:
    import mysql.connector
except:
    neue_betriebsmeldung(
        "[datenbank_abfrage] Fehler bei der importierung von Modulen.")
# ======================================================================

# Datenbankverbindung herstellen
# ======================================================================
def db_connect():
	try:
		global connection
		connection = mysql.connector.connect(
            host="localhost",
            user="datenbank",
            passwd="rasp",
            database="datenbank"
        )
	except:
		neue_betriebsmeldung(
            "[datenbank_abfrage] Fehler bei der Datenbankverbindung.")
# ======================================================================

# Programmstatus abfragen
# ======================================================================
def get_status():
	try:
		global parameter_slot
		global programm_status
		sql_select_Query = "select * from betriebsmodus"
		cursor = connection.cursor()
		cursor.execute(sql_select_Query)
		records = cursor.fetchall()
		for row in records:
			parameter_slot = (row[1])
			programm_status = (row[2])
	except:
		neue_betriebsmeldung("[datenbank_abfrage] Fehler bei der Programmstatus Abfrage.")
# ======================================================================

# Abfragefunktion der aktiven Parameter
# ======================================================================
def get_parameter():
    try:
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
    except:
        neue_betriebsmeldung(
            "[datenbank_abfrage] Parameterdaten konnten nicht aus der Datenbank gelesen werden.")
# ======================================================================

# Start Datenbank Abfrage
# ======================================================================
def start_datenbank_abfrage():
	db_connect()
	get_status()
	if programm_status == 1:
		get_parameter()
	else:
		pass
# ======================================================================