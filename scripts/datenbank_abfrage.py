# Import der Betriebsmeldungsfunktion
# ======================================================================
from betriebsmeldungen import neue_betriebsmeldung
# ======================================================================

# Import von benoetigten Modulen
# ======================================================================
try:
	import mysql.connector
	from mysql.connector.cursor import MySQLCursor
except Exception as e:
		neue_betriebsmeldung(str(e))
# ======================================================================

# Datenbank Abfrage
# ======================================================================
def start_datenbank_abfrage():
	try:
		global parameter_slot
		global programm_status
		global slot
		global pflanze
		global temperatur
		global lichtstunden
		global wassermenge
		global luftfeuchtigkeit

		parameter_slot = 1
		programm_status = 0
		slot = 1
		pflanze = 0
		temperatur = 0
		lichtstunden = 0
		wassermenge = 0
		luftfeuchtigkeit = 0

		db = mysql.connector.connect(
				host="localhost",
				user="datenbank",
				passwd="rasp",
				database="datenbank"
			)

		cursor = db.cursor()

		sql1 = """select * from betriebsmodus"""
		cursor.execute(sql1)
		for row in cursor:
			parameter_slot = (row[1])
			programm_status = (row[2])

		sql2 = """SELECT `slot`, `pflanze`, `temperatur`, `lichtstunden`, `wassermenge`, `luftfeuchtigkeit` FROM `parameter` WHERE slot = %(slot)s"""
		data2 = {
				'slot': parameter_slot
		}
		cursor.execute(sql2, data2)
		for row in cursor:
			slot = (row[0])
			pflanze = (row[1])
			temperatur = (row[2])
			lichtstunden = (row[3])
			wassermenge = (row[4])
			luftfeuchtigkeit = (row[5])

		cursor.close()
		db.close()

	except mysql.connector.Error as err:
		neue_betriebsmeldung("DB Fehler: {}".format(err))
	except Exception as e:
		neue_betriebsmeldung(str(e))
# ======================================================================