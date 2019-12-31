# Import von benoetigten Modulen
# ======================================================================
try:
	from datenaustausch import neue_betriebsmeldung
	from datenaustausch import lichtzaehler_update
	from ansteuerung_pwm_shield import licht_ein, licht_aus, grundstellung
	import datenaustausch
except Exception as e:
	neue_betriebsmeldung(str(e))
# ======================================================================

# Regelkreis Licht
# ======================================================================
def start_lichtsteuerung():
	try:
		if datenaustausch.programm_status == 1:
			lichtzaehler_update()
			if int(datenaustausch.lichtstunden) > 0:
				sollwert = (float(datenaustausch.lichtstunden) * 60)
				if datenaustausch.neue_zaehler_zeit < sollwert:
					licht_ein()
				elif datenaustausch.neue_zaehler_zeit >= sollwert:
					licht_aus()
				else:
					pass
			else:
				pass
		else:
			grundstellung()
	except Exception as e:
		neue_betriebsmeldung(str(e))
# ======================================================================
