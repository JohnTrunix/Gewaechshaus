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

		cnx = mysql.connector.connect(**config)
		cursor = cnx.cursor()

		query1 = ("SELECT * from betriebsmodus")
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

# Betriebsmeldung handling
# ======================================================================
def neue_betriebsmeldung(meldung):
	try:
		lokale_zeit = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

		cnx = mysql.connector.connect(**config)
		cursor = cnx.cursor()

		query1 = ("SELECT COUNT(*) FROM betriebsmeldungen")
		cursor.execute(query1)
		for row in cursor:
			anzahl_betriebsmeldungen = (row[0])

		if anzahl_betriebsmeldungen >= 50:
			query2 = ("DELETE FROM betriebsmeldungen ORDER BY meldung DESC LIMIT 20")
			cursor.execute(query2)
		else:
			pass

		query3 = ("INSERT INTO betriebsmeldungen (datetime, meldung) VALUES (%s, %s)")
		data3 = (lokale_zeit, meldung)
		cursor.execute(query3, data3)

		cnx.commit()

		cursor.close()
		cnx.close()
	except:
		pass
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

		cnx.commit()

		cursor.close()
		cnx.close()
	except mysql.connector.Error as err:
  		neue_betriebsmeldung(str(err))
	except Exception as e:
		neue_betriebsmeldung(str(e))
# ======================================================================

# Sensorwerte einfuegen
# ======================================================================
def sensorwerte_einfuegen(temperatur, licht, bodenfuechtigkeit, luftfeuchtigkeit):
	try:
		lokale_zeit = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

		cnx = mysql.connector.connect(**config)
		cursor = cnx.cursor()

		query1 = ("INSERT INTO sensor_licht_1 (datetime, sensorwert) VALUES (%s, %s)")
		data1 = (lokale_zeit, licht)
		cursor.execute(query1, data1)

		query2 = ("INSERT INTO 	sensor_luftfeuchtigkeit_1 (datetime, sensorwert) VALUES (%s, %s)")
		data2 = (lokale_zeit, luftfeuchtigkeit)
		cursor.execute(query2, data2)

		query3 = ("INSERT INTO sensor_temperatur_1 (datetime, sensorwert) VALUES (%s, %s)")
		data3 = (lokale_zeit, temperatur)
		cursor.execute(query3, data3)

		query4 = ("INSERT INTO sensor_bodenfeuchtigkeit_1 (datetime, sensorwert) VALUES (%s, %s)")
		data4 = (lokale_zeit, bodenfuechtigkeit)
		cursor.execute(query4, data4)

		cnx.commit()

		cursor.close()
		cnx.close()
	except mysql.connector.Error as err:
  		neue_betriebsmeldung(str(err))
	except Exception as e:
		neue_betriebsmeldung(str(e))	
# ======================================================================

# Lichtzaehler reset
# ======================================================================
def reset_licht_zaehler():
	try:
		cnx = mysql.connector.connect(**config)
		cursor = cnx.cursor()

		query1 = ("UPDATE zwischenspeicher SET licht_zaehler = '0'")
		cursor.execute(query1)

		cnx.commit()

		cursor.close()
		cnx.close()
	except mysql.connector.Error as err:
  		neue_betriebsmeldung(str(err))
	except Exception as e:
		neue_betriebsmeldung(str(e))	
# ======================================================================

# Lichtzaehler update
# ======================================================================
def lichtzaehler_update():
	try:
		global neue_zaehler_zeit

		cnx = mysql.connector.connect(**config)
		cursor = cnx.cursor()

		query1 = ("SELECT licht_zaehler FROM zwischenspeicher")
		cursor.execute(query1)
		for row in cursor:
			licht_zaehler = (row[0])

		neue_zaehler_zeit = (licht_zaehler + 30)

		query2 = ("UPDATE zwischenspeicher SET licht_zaehler = licht_zaehler + 30")
		cursor.execute(query2)

		cnx.commit()

		cursor.close()
		cnx.close()
	except mysql.connector.Error as err:
  		neue_betriebsmeldung(str(err))
	except Exception as e:
		neue_betriebsmeldung(str(e))
# ======================================================================
