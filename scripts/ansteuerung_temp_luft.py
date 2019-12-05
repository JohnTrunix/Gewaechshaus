# Import der Betriebsmeldungsfunktion
# ======================================================================
from betriebsmeldungen import neue_betriebsmeldung
# ======================================================================

# Import von benoetigten Modulen
# ======================================================================
try:
	import time
	import datenbank_abfrage
	import sensor_abfrage
	from ansteuerung_pwm_shield import heizung_ein, heizung_aus, befeuchter_ein, befeuchter_aus, luefter_klein_ein, luefter_klein_aus, tuer_oeffnen, tuer_schliessen, luefter_gross_ein, luefter_gross_aus, grundstellung
except:
    neue_betriebsmeldung(
        "[ansteuerung_temp_luft] Fehler bei der importierung von Modulen.")
# ======================================================================

# Regelkreis Temperatur und Luft
# ======================================================================
def start_ansteuerung_temp_luft():
    try:
        if datenbank_abfrage.programm_status == 1:
            if (int(sensor_abfrage.temperatur_gerundet) < int(datenbank_abfrage.temperatur)):
                heizung_ein()
                status_heizung = 1
            elif ((int(sensor_abfrage.temperatur_gerundet) + 2) > int(datenbank_abfrage.temperatur)):
                heizung_aus()
                status_heizung = 0
            else:
                pass
            if (int(sensor_abfrage.luftfeuchtigkeit_gerundet) < int(datenbank_abfrage.luftfeuchtigkeit)):
                befeuchter_ein()
                status_befeuchter = 1
            elif ((int(sensor_abfrage.luftfeuchtigkeit_gerundet) + 5) > int(datenbank_abfrage.luftfeuchtigkeit)):
                befeuchter_aus()
                status_befeuchter = 0
            else:
                pass
            if status_heizung == 1 or status_befeuchter == 1:
                luefter_klein_ein()
            elif status_heizung == 0 and status_befeuchter == 0:
                luefter_klein_aus()
            else:
                pass
        else:
            grundstellung()
    except:
        neue_betriebsmeldung(
            "[ansteuerung_temp_luft] Fehler bei der Zyklusberechnung der Heizung und des Befeuchters.")
# ======================================================================

# Lueften
# ======================================================================
def start_lueften():
	try:
		if datenbank_abfrage.programm_status == 1:
			tuer_oeffnen()
			luefter_gross_ein()
			time.sleep(60)
			luefter_gross_aus()
			tuer_schliessen()
		else:
			grundstellung()
	except:
		neue_betriebsmeldung(
            "[ansteuerung_temp_luft] Fehler beim lueften.")

# ======================================================================