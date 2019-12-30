# Import der Betriebsmeldungsfunktion
# ======================================================================
from betriebsmeldungen import neue_betriebsmeldung
# ======================================================================

# Import von benoetigten Modulen
# ======================================================================
try:
	import mysql.connector
	import time
	import datetime
except Exception as e:
		neue_betriebsmeldung(str(e))
# ======================================================================

# Datenbank Konfiguration
# ======================================================================
config = {
  'user': 'datenbank',
  'password': 'rasp',
  'host': '127.0.0.1',
  'database': 'datenbank',
  'raise_on_warnings': True
}
# ======================================================================

# Aktueller Programmstatus und Parameter abfragen
# ======================================================================
def get_active_state():
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

		cnx = mysql.connector.connect(**config)
		cursor = cnx.cursor()

		query1 = ("select * from betriebsmodus")
		cursor.execute(query1)

		for row in cursor:
			parameter_slot = (row[1])
			programm_status = (row[2])

		query2 = ("SELECT slot, pflanze, temperatur, lichtstunden, wassermenge, luftfeuchtigkeit FROM parameter WHERE slot = %(slot)s")
		data2 = {
				'slot': parameter_slot
			}
		cursor.execute(query2, data2)

		for row in cursor:
			slot = (row[0])
			pflanze = (row[1])
			temperatur = (row[2])
			lichtstunden = (row[3])
			wassermenge = (row[4])
			luftfeuchtigkeit = (row[5])

		cursor.close()
		cnx.close()
	except mysql.connector.Error as err:
  		neue_betriebsmeldung(str(err))
	except Exception as e:
		neue_betriebsmeldung(str(e))
# ======================================================================

# Licht-Zwischenspeicher
# ======================================================================
def licht_zwischenspeicher():
	try:
		global licht_zaehler

		cnx = mysql.connector.connect(**config)
		cursor = cnx.cursor()

		query1 = ("select licht_zaehler from zwischenspeicher")
		cursor.execute(query1)

		for row in cursor:
			licht_zaehler = (row[0])

		neue_zaehler_zeit = (licht_zaehler + 30)

		query2 = ("update zwischenspeicher set licht_zaehler = %(wert)s")
		data2 = {
				'wert': neue_zaehler_zeit
			}
		cursor.execute(query2, data2)

		cursor.close()
		cnx.close()
	except mysql.connector.Error as err:
  		neue_betriebsmeldung(str(err))
	except Exception as e:
		neue_betriebsmeldung(str(e))
# ======================================================================

# Betriebsmeldung an Datenbank senden
# ======================================================================
def betriebsmeldung_einfuegen(meldung):
	try:
		lokale_zeit = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

		cnx = mysql.connector.connect(**config)
		cursor = cnx.cursor()

		query = ("INSERT INTO betriebsmeldungen (datetime, meldung) VALUES %(datetime)s, %(meldung)s")
		data = {
				'datetime': lokale_zeit,
				'meldung': meldung
			}
		cursor.execute(query, data)

		cursor.close()
		cnx.close()
	except mysql.connector.Error as err:
  		neue_betriebsmeldung(str(err))
	except Exception as e:
		neue_betriebsmeldung(str(e))
# ======================================================================

# Datenbegrenzung
# ======================================================================
def start_datenbegrenzung():
	try:
		cnx = mysql.connector.connect(**config)
		cursor = cnx.cursor()

		query1 = ("DELETE FROM sensor_licht_1 WHERE datetime < NOW() - INTERVAL 30 DAY")
		cursor.execute(query1)

		query2 = ("DELETE FROM sensor_temperatur_1 WHERE datetime < NOW() - INTERVAL 30 DAY")
		cursor.execute(query2)

		query3 = ("DELETE FROM sensor_luftfeuchtigkeit_1 WHERE datetime < NOW() - INTERVAL 30 DAY")
		cursor.execute(query3)

		query4 = ("DELETE FROM sensor_bodenfeuchtigkeit_1 WHERE datetime < NOW() - INTERVAL 30 DAY")
		cursor.execute(query4)

		cursor.close()
		cnx.close()
	except mysql.connector.Error as err:
  		neue_betriebsmeldung(str(err))
	except Exception as e:
		neue_betriebsmeldung(str(e))
# ======================================================================

# Sensorwerte einfuegen
# ======================================================================
def sensorwerte_einfuegen(datetime, temperatur, licht, bodenfuechtigkeit, luftfeuchtigkeit):
	try:
		cnx = mysql.connector.connect(**config)
		cursor = cnx.cursor()

		query1 = ("INSERT INTO 	sensor_licht_1 (datetime, sensorwert) VALUES %(datetime)s, %(sensorwert)s")
		data1 = {
				'datetime': datetime,
				'sensorwert': licht
			}
		cursor.execute(query1, data1)

		query2 = ("INSERT INTO 	sensor_luftfeuchtigkeit_1 (datetime, sensorwert) VALUES %(datetime)s, %(sensorwert)s")
		data2 = {
				'datetime': datetime,
				'sensorwert': luftfeuchtigkeit
			}
		cursor.execute(query2, data2)

		query3 = ("INSERT INTO 	sensor_temperatur_1 (datetime, sensorwert) VALUES %(datetime)s, %(sensorwert)s")
		data3 = {
				'datetime': datetime,
				'sensorwert': temperatur
			}
		cursor.execute(query3, data3)

		query4 = ("INSERT INTO 	sensor_bodenfeuchtigkeit_1 (datetime, sensorwert) VALUES %(datetime)s, %(sensorwert)s")
		data4 = {
				'datetime': datetime,
				'sensorwert': bodenfuechtigkeit
			}
		cursor.execute(query4, data4)

		cursor.close()
		cnx.close()
	except mysql.connector.Error as err:
  		neue_betriebsmeldung(str(err))
	except Exception as e:
		neue_betriebsmeldung(str(e))	
# ======================================================================