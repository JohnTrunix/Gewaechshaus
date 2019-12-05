# Import der Betriebsmeldungsfunktion
# ======================================================================
from betriebsmeldungen import neue_betriebsmeldung
# ======================================================================

# Import von benoetigten Modulen
# ======================================================================
try:
    from python_tsl2591 import tsl2591
    import adafruit_sht31d
    import adafruit_ads1x15.ads1115 as ADS
    from adafruit_ads1x15.analog_in import AnalogIn
    import board
    import busio
    import time
    import datetime
    import mysql.connector
except:
    neue_betriebsmeldung(
        "[sensor_abfrage] Fehler bei der importierung von Modulen.")
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
        "[sensor_abfrage] Fehler bei der Datenbankverbindung.")
# ======================================================================

# I2C Bus Konfiguration
# ======================================================================
try:
    i2c = busio.I2C(board.SCL, board.SDA)
    sensor_temperatur_luftfeuchtigkeit = adafruit_sht31d.SHT31D(i2c)
    ads = ADS.ADS1115(i2c)
    ads.gain = 1
    sensor1 = AnalogIn(ads, ADS.P0)
    sensor2 = AnalogIn(ads, ADS.P1)
    sensor3 = AnalogIn(ads, ADS.P2)
    sensor4 = AnalogIn(ads, ADS.P3)
except:
    neue_betriebsmeldung(
        "[sensor_abfrage] Fehler bei der initialen I2C Bus Konfiguration.")
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
    tsl = tsl2591()
    full, ir = tsl.get_full_luminosity()
    lux = tsl.calculate_lux(full, ir)
    lux_gerundet = (round(lux, 1))
    datenbank_lichtsensor_einfuegen()
# ======================================================================

# Temperatursensor wird abgefragt und die Datenbank Funktion wird aufgerufen
# ======================================================================
def temperatur_abfrage():
    global temperatur_gerundet
    temperatur_gerundet = (
        round(sensor_temperatur_luftfeuchtigkeit.temperature, 1))
    datenbank_temperatursensor_einfuegen()
# ======================================================================

# Luftfeuchtigkeitssensor wird abgefragt und die Datenbank Funktion wird aufgerufen
# ======================================================================
def luftfeuchtigkeit_abfrage():
    global luftfeuchtigkeit_gerundet
    luftfeuchtigkeit_gerundet = (
        round(sensor_temperatur_luftfeuchtigkeit.relative_humidity, 1))
    datenbank_luftfeuchtesensor_einfuegen()
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
        datenbank_bodenfeuchtigkeitsensor_einfuegen()
    elif sensor_gerundet <= 0:
        bodenfeuchtigkeit_endwert = 0
        datenbank_bodenfeuchtigkeitsensor_einfuegen()
    else:
        bodenfeuchtigkeit_endwert = sensor_gerundet
        datenbank_bodenfeuchtigkeitsensor_einfuegen()
# ======================================================================

# Der Lichtsensor Wert wird in Datenbank geschrieben
# ======================================================================
def datenbank_lichtsensor_einfuegen():
    mycursor = mydb.cursor()
    sql = "INSERT INTO sensor_licht_1 (datetime, sensorwert) VALUES (%s, %s)"
    val = (lokale_zeit, lux_gerundet)
    mycursor.execute(sql, val)
    mydb.commit()
# ======================================================================

# Der Luftfeuchtigkeit Wert wird in Datenbank geschrieben
# ======================================================================
def datenbank_luftfeuchtesensor_einfuegen():
    mycursor = mydb.cursor()
    sql = "INSERT INTO 	sensor_luftfeuchtigkeit_1 (datetime, sensorwert) VALUES (%s, %s)"
    val = (lokale_zeit, luftfeuchtigkeit_gerundet)
    mycursor.execute(sql, val)
    mydb.commit()
# ======================================================================

# Der Temperatur Wert wird in Datenbank geschrieben
# ======================================================================
def datenbank_temperatursensor_einfuegen():
    mycursor = mydb.cursor()
    sql = "INSERT INTO sensor_temperatur_1 (datetime, sensorwert) VALUES (%s, %s)"
    val = (lokale_zeit, temperatur_gerundet)
    mycursor.execute(sql, val)
    mydb.commit()
# ======================================================================

# Der Bodenfeuchtigkeits Wert wird in Datenbank geschrieben
# ======================================================================
def datenbank_bodenfeuchtigkeitsensor_einfuegen():
    mycursor = mydb.cursor()
    sql = "INSERT INTO sensor_bodenfeuchtigkeit_1 (datetime, sensorwert) VALUES (%s, %s)"
    val = (lokale_zeit, bodenfeuchtigkeit_endwert)
    mycursor.execute(sql, val)
    mydb.commit()
# ======================================================================

# Starte alle Abfrage Funktionen
# ======================================================================
def start_sensorabfrage():
    try:
        systemzeit_abfrage()
    except:
        neue_betriebsmeldung(
            "[sensor_abfrage] Fehler bei der Systemzeitabfrage.")
    try:
        lichtsensor_abfrage()
    except:
        neue_betriebsmeldung(
            "[sensor_abfrage] Fehler bei der Abfrage des Lichtsensor.")
    try:
        temperatur_abfrage()
    except:
        neue_betriebsmeldung(
            "[sensor_abfrage] Fehler bei der Abfrage des Temperatursensor.")
    try:
        luftfeuchtigkeit_abfrage()
    except:
        neue_betriebsmeldung(
            "[sensor_abfrage] Fehler bei der Abfrage des Luftfeuchtigkeitssensor.")
    try:
        bodenfeuchtigkeit_abfrage()
    except:
        neue_betriebsmeldung(
            "[sensor_abfrage] Fehler bei der Abfrage des Bodenfeuchtigkeitssensor.")
# ======================================================================
