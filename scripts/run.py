# Import der Betriebsmeldungsfunktion
# ======================================================================
from datenaustausch import neue_betriebsmeldung
# ======================================================================

# Betriebsmeldung bei Systemstart
# ======================================================================
neue_betriebsmeldung(
	"[run] System wird gestartet.")
# ======================================================================

# Import von benoetigten Modulen
# ======================================================================
try:
	from sensor_abfrage import start_sensorabfrage
	from datenaustausch import start_datenbegrenzung
	from zeit_update import start_zeit_update
	from datenaustausch import start_datenbank_abfrage
	from ansteuerung_temp_luft import start_ansteuerung_temp_luft, start_lueften
	from datenaustausch import reset_licht_zaehler
	from ansteuerung_wasser import start_ansteuerung_wasser, start_auffuellen_befeuchter
	from ansteuerung_pwm_shield import grundstellung
	from ansteuerung_licht import start_lichtsteuerung
	import schedule
	import time
	import os
except Exception as e:
	neue_betriebsmeldung(str(e))
# ======================================================================

# Zeit Aktualisierung bei Start
# ======================================================================
try:
	start_zeit_update()
except Exception as e:
	neue_betriebsmeldung(str(e))
# ======================================================================

# Datenbegrenzung bei Start
# ======================================================================
try:
	start_datenbegrenzung()
except Exception as e:
	neue_betriebsmeldung(str(e))
# ======================================================================

# Datenbankabfrage bei Start
# ======================================================================
try:
	start_datenbank_abfrage()
except Exception as e:
	neue_betriebsmeldung(str(e))
# ======================================================================

# Grundstellung bei Start
# ======================================================================
try:
	grundstellung()
except Exception as e:
	neue_betriebsmeldung(str(e))
# ======================================================================

# Alle Auftraege mit Startintervall definiert
# ======================================================================
schedule.every(10).seconds.do(start_datenbank_abfrage)
schedule.every(10).seconds.do(start_sensorabfrage)
schedule.every(10).seconds.do(start_ansteuerung_temp_luft)
schedule.every().hour.at("00:05").do(start_lichtsteuerung)
schedule.every().hour.at("00:10").do(start_ansteuerung_wasser)
schedule.every().hour.at("00:20").do(start_auffuellen_befeuchter)
schedule.every().hour.at("00:35").do(start_lichtsteuerung)
schedule.every().hour.at("00:45").do(start_lueften)
schedule.every().day.at("23:55").do(start_datenbegrenzung)
schedule.every().day.at("23:55").do(start_zeit_update)
schedule.every().day.at("08:00").do(reset_licht_zaehler)
# ======================================================================

# Alle 5 Sekunden auf ausstehende Auftraege ueberpruefen
# ======================================================================
while True:
	try:
		schedule.run_pending()
		time.sleep(5)
	except Exception as e:
		neue_betriebsmeldung(str(e))
# ======================================================================
