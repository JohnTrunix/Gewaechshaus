# Import der Betriebsmeldungsfunktion
# ======================================================================
from betriebsmeldungen import neue_betriebsmeldung
# ======================================================================

# Import von benoetigten Modulen
# ======================================================================
try:
	import adafruit_tsl2591
	import adafruit_sht31d
	import adafruit_ads1x15.ads1115 as ADS
	from adafruit_ads1x15.analog_in import AnalogIn
	import board
	import busio
	import time
	import datetime
	import mysql.connector
except Exception as e:
		neue_betriebsmeldung(str(e))
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
except Exception as e:
		neue_betriebsmeldung(str(e))
# ======================================================================

# I2C Bus Konfiguration
# ======================================================================
try:
	i2c = busio.I2C(board.SCL, board.SDA)
	sensor_temperatur_luftfeuchtigkeit = adafruit_sht31d.SHT31D(i2c)
	sensor_licht = adafruit_tsl2591.TSL2591(i2c)
	ads = ADS.ADS1115(i2c)
	ads.gain = 1
	sensor1 = AnalogIn(ads, ADS.P0)
	sensor2 = AnalogIn(ads, ADS.P1)
	sensor3 = AnalogIn(ads, ADS.P2)
	sensor4 = AnalogIn(ads, ADS.P3)
except Exception as e:
		neue_betriebsmeldung(str(e))
# ======================================================================

# Die Systemzeit wird als Variable gespeichert
# ======================================================================
def systemzeit_abfrage():
	global lokale_zeit
	lokale_zeit = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# ======================================================================

# Lichtsensor wird abgefragt und die Datenbank Funktion wird aufgerufen
# ======================================================================
def lichtsensor_abfrage():
	global lux_gerundet
	lux_gerundet = (round(sensor_licht.lux, 1))
# ======================================================================

# Temperatursensor wird abgefragt und die Datenbank Funktion wird aufgerufen
# ======================================================================
def temperatur_abfrage():
	global temperatur_gerundet
	temperatur_gerundet = (
		round(sensor_temperatur_luftfeuchtigkeit.temperature, 1))
# ======================================================================

# Luftfeuchtigkeitssensor wird abgefragt und die Datenbank Funktion wird aufgerufen
# ======================================================================
def luftfeuchtigkeit_abfrage():
	global luftfeuchtigkeit_gerundet
	luftfeuchtigkeit_gerundet = (
		round(sensor_temperatur_luftfeuchtigkeit.relative_humidity, 1))
# ======================================================================

# Bodenfeuchtigkeitsensoren werden abgefragt und die Datenbank Funktion wird aufgerufen
# ======================================================================
def bodenfeuchtigkeit_abfrage():
	global bodenfeuchtigkeit_endwert
	sensor_durchschnitt = (
		(sensor1.voltage + sensor2.voltage + sensor3.voltage + sensor4.voltage) / 4)
	sensor_prozentual = (((sensor_durchschnitt - 1.45) / 1.55) * 100)
	sensor_korrigiert = (100 - sensor_prozentual)
	sensor_gerundet = round(sensor_korrigiert, 1)
	if sensor_gerundet >= 100:
		bodenfeuchtigkeit_endwert = 100
	elif sensor_gerundet <= 0:
		bodenfeuchtigkeit_endwert = 0
	else:
		bodenfeuchtigkeit_endwert = sensor_gerundet
# ======================================================================

# Sensorwerte an Datenbank senden
# ======================================================================
def datenbank_kommunikation():
	try:
		db = mysql.connector.connect(
				host="localhost",
				user="datenbank",
				passwd="rasp",
				database="datenbank"
			)

		cursor = db.cursor()

		sql1 = """INSERT INTO sensor_licht_1 (datetime, sensorwert) VALUES = %(datetime)s, %(sensorwert)s"""
		data1 = {
				'datetime': lokale_zeit,
				'sensorwert': lux_gerundet
		}
		cursor.execute(sql1, data1)

		sql2 = """INSERT INTO sensor_luftfeuchtigkeit_1 (datetime, sensorwert) VALUES = %(datetime)s, %(sensorwert)s"""
		data2 = {
				'datetime': lokale_zeit,
				'sensorwert': luftfeuchtigkeit_gerundet
		}
		cursor.execute(sql2, data2)

		sql3 = """INSERT INTO sensor_temperatur_1 (datetime, sensorwert) VALUES = %(datetime)s, %(sensorwert)s"""
		data3 = {
				'datetime': lokale_zeit,
				'sensorwert': temperatur_gerundet
		}
		cursor.execute(sql3, data3)

		sql4 = """INSERT INTO sensor_bodenfeuchtigkeit_1 (datetime, sensorwert) VALUES = %(datetime)s, %(sensorwert)s"""
		data4 = {
				'datetime': lokale_zeit,
				'sensorwert': bodenfeuchtigkeit_endwert
		}
		cursor.execute(sql4, data4)

		cursor.close()
		db.close()

	except mysql.connector.Error as err:
		neue_betriebsmeldung("DB Fehler: {}".format(err))
	except Exception as e:
		neue_betriebsmeldung(str(e))


# ======================================================================

# Starte alle Abfrage Funktionen
# ======================================================================
def start_sensorabfrage():
	try:
		systemzeit_abfrage()
	except Exception as e:
		neue_betriebsmeldung(str(e))
	try:
		lichtsensor_abfrage()
	except Exception as e:
		neue_betriebsmeldung(str(e))
	try:
		temperatur_abfrage()
	except Exception as e:
		neue_betriebsmeldung(str(e))
	try:
		luftfeuchtigkeit_abfrage()
	except Exception as e:
		neue_betriebsmeldung(str(e))
	try:
		bodenfeuchtigkeit_abfrage()
	except Exception as e:
		neue_betriebsmeldung(str(e))
	try:
		datenbank_kommunikation()
	except Exception as e:
		neue_betriebsmeldung(str(e))
# ======================================================================
