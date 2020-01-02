# Import von benoetigten Modulen
# ======================================================================
try:
	from datenaustausch import neue_betriebsmeldung
	import adafruit_tsl2591
	import adafruit_sht31d
	import adafruit_ads1x15.ads1115 as ADS
	from adafruit_ads1x15.analog_in import AnalogIn
	import board
	import busio
	from datenaustausch import sensorwerte_einfuegen
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
	temperatur_gerundet = (round(sensor_temperatur_luftfeuchtigkeit.temperature, 1))
# ======================================================================

# Luftfeuchtigkeitssensor wird abgefragt und die Datenbank Funktion wird aufgerufen
# ======================================================================
def luftfeuchtigkeit_abfrage():
	global luftfeuchtigkeit_gerundet
	luftfeuchtigkeit_gerundet = (round(sensor_temperatur_luftfeuchtigkeit.relative_humidity, 1))
# ======================================================================

# Bodenfeuchtigkeitsensoren werden abgefragt und die Datenbank Funktion wird aufgerufen
# ======================================================================
def bodenfeuchtigkeit_abfrage():
	global bodenfeuchtigkeit_endwert
	sensor_durchschnitt = ((sensor1.voltage + sensor2.voltage + sensor3.voltage + sensor4.voltage) / 4)
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

# Starte alle Abfrage Funktionen
# ======================================================================
def start_sensorabfrage():
	try:
		lichtsensor_abfrage()
		temperatur_abfrage()
		luftfeuchtigkeit_abfrage()
		bodenfeuchtigkeit_abfrage()
		sensorwerte_einfuegen(temperatur_gerundet, lux_gerundet, bodenfeuchtigkeit_endwert, luftfeuchtigkeit_gerundet)
	except Exception as e:
		neue_betriebsmeldung(str(e))
# ======================================================================
