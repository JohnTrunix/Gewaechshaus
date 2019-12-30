# Import von benoetigten Modulen
# ======================================================================
try:
	from datenaustausch import neue_betriebsmeldung
	from ansteuerung_pwm_shield import heizung_ein, heizung_aus, befeuchter_ein, befeuchter_aus, luefter_klein_ein, luefter_klein_aus, tuer_oeffnen, tuer_schliessen, luefter_gross_ein, luefter_gross_aus, grundstellung
	import time
	import datenaustausch
	import sensor_abfrage
except Exception as e:
	neue_betriebsmeldung(str(e))
# ======================================================================

# Regelkreis Temperatur und Luft
# ======================================================================
def start_ansteuerung_temp_luft():
	try:
		if datenaustausch.programm_status == 1:
			if (int(sensor_abfrage.temperatur_gerundet) < int(datenaustausch.temperatur)):
				heizung_ein()
				status_heizung = 1
			elif ((int(sensor_abfrage.temperatur_gerundet) + 2) > int(datenaustausch.temperatur)):
				heizung_aus()
				status_heizung = 0
			else:
				pass
			if (int(sensor_abfrage.luftfeuchtigkeit_gerundet) < int(datenaustausch.luftfeuchtigkeit)):
				befeuchter_ein()
				status_befeuchter = 1
			elif ((int(sensor_abfrage.luftfeuchtigkeit_gerundet) + 5) > int(datenaustausch.luftfeuchtigkeit)):
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
	except Exception as e:
		neue_betriebsmeldung(str(e))
# ======================================================================

# Zyklus 60s Lueften
# ======================================================================
def start_lueften():
	try:
		if datenaustausch.programm_status == 1:
			tuer_oeffnen()
			luefter_gross_ein()
			time.sleep(60)
			luefter_gross_aus()
			tuer_schliessen()
		else:
			grundstellung()
	except Exception as e:
		neue_betriebsmeldung(str(e))
# ======================================================================
