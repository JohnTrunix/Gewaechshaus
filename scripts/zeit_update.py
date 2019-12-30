# Import der Betriebsmeldungsfunktion
# ======================================================================
from betriebsmeldungen import neue_betriebsmeldung
# ======================================================================

# Import von benoetigten Modulen
# ======================================================================
try:
	import busio
	import adafruit_pcf8523
	import time
	import datetime
	import board
	import socket
	import os
except Exception as e:
		neue_betriebsmeldung(str(e))
# ======================================================================

# I2C Bus Konfiguration
# ======================================================================
try:
	myI2C = busio.I2C(board.SCL, board.SDA)
	rtc = adafruit_pcf8523.PCF8523(myI2C)
	t = rtc.datetime
except Exception as e:
		neue_betriebsmeldung(str(e))
# ======================================================================

# Ueberpruefe Internetverbindung
# ======================================================================
def start_zeit_update():
	try:
		socket.create_connection(("www.google.com", 443))
		rtc_update()
	except:
		systemzeit_schreiben()
# ======================================================================

# RTC Update
# ======================================================================
def rtc_update():
	try:
		now = datetime.datetime.now()
		t = time.struct_time(
			(now.year, now.month, now.day, now.hour, now.minute, now.second, 0, 0, 0))
		rtc.datetime = t
	except Exception as e:
		neue_betriebsmeldung(str(e))
# ======================================================================

# Systemzeit schreiben von RTC
# ======================================================================
def systemzeit_schreiben():
	try:
		os.system("sudo timedatectl set-ntp false")
		time.sleep(1)
		os.system("sudo timedatectl set-time " + str(t.tm_hour) + ":" + str(t.tm_min) + ":" + str(t.tm_sec))
		time.sleep(1)
	except Exception as e:
		neue_betriebsmeldung(str(e))
	finally:
		os.system("sudo timedatectl set-ntp true")
# ======================================================================
