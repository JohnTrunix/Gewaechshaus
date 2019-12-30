# Import der Betriebsmeldungsfunktion
# ======================================================================
from betriebsmeldungen import neue_betriebsmeldung
# ======================================================================

# Import von benoetigten Modulen
# ======================================================================
import argparse
import os
import time
from ansteuerung_pwm_shield import grundstellung, tuer_oeffnen, tuer_schliessen, luefter_gross_ein, luefter_gross_aus, luefter_klein_ein, luefter_klein_aus, wasserpumpe_ein, wasserpumpe_aus, ventil_wasserpumpe_oeffnen, ventil_wasserpumpe_schliessen, ventil_befeuchter_oeffnen, ventil_befeuchter_schliessen, licht_ein, licht_aus, heizung_ein, heizung_aus, befeuchter_ein, befeuchter_aus
# ======================================================================

# Startargumente
# ======================================================================
parser = argparse.ArgumentParser(description='Gewaechshaus Admin Programm')
parser.add_argument(
	'--stop',
	default=0,
	help='stop'
)
parser.add_argument(
	'--start',
	default=0,
	help='start'
)
parser.add_argument(
	'--herunterfahren',
	default=0,
	help='herunterfahren'
)
parser.add_argument(
	'--tuer',
	default=0,
	help='tuer'
)
parser.add_argument(
	'--luefter_gross',
	default=0,
	help='luefter_gross'
)
parser.add_argument(
	'--luefter_klein',
	default=0,
	help='luefter_klein'
)
parser.add_argument(
	'--wasserpumpe',
	default=0,
	help='wasserpumpe'
)
parser.add_argument(
	'--ventil_wasserpumpe',
	default=0,
	help='ventil_wasserpumpe'
)
parser.add_argument(
	'--ventil_befeuchter',
	default=0,
	help='ventil_befeuchter'
)
parser.add_argument(
	'--licht',
	default=0,
	help='licht'
)
parser.add_argument(
	'--heizung',
	default=0,
	help='heizung'	
)
parser.add_argument(
	'--befeuchter',
	default=0,
	help='befeuchter'
)
parameter = parser.parse_args()
# ======================================================================

# Steuerung
# ======================================================================
if int(parameter.stop) == 1:
	neue_betriebsmeldung("[admin] System wird gestoppt und in Grundstellung gebracht.")
	os.system("sudo service gewaechshaus stop")
	time.sleep(2)
	grundstellung()
elif int(parameter.start) == 1:
	neue_betriebsmeldung("[admin] Systemstart wird angefordert.")
	os.system("sudo service gewaechshaus start")
elif int(parameter.herunterfahren) == 1:
	neue_betriebsmeldung("[admin] System wird gestoppt, in Grundstellung gebracht und heruntergefahren.")
	os.system("sudo service gewaechshaus stop")
	time.sleep(2)
	grundstellung()
	time.sleep(10)
	os.system("sudo shutdown -h now")
elif int(parameter.tuer) == 2:
	neue_betriebsmeldung("[admin] Tueren werden geoeffnet.")
	tuer_oeffnen()
elif int(parameter.tuer) == 1:
	neue_betriebsmeldung("[admin] Tueren werden geschlossen.")
	tuer_schliessen()
elif int(parameter.luefter_gross) == 2:
	neue_betriebsmeldung("[admin] Luefter gross werden eingeschaltet.")
	luefter_gross_ein()
elif int(parameter.luefter_gross) == 1:
	neue_betriebsmeldung("[admin] Luefter gross werden ausgeschaltet.")
	luefter_gross_aus()
elif int(parameter.luefter_klein) == 2:
	neue_betriebsmeldung("[admin] Luefter klein werden eingeschaltet.")
	luefter_klein_ein()
elif int(parameter.luefter_klein) == 1:
	neue_betriebsmeldung("[admin] Luefter klein werden ausgeschaltet.")
	luefter_klein_aus()
elif int(parameter.wasserpumpe) == 2:
	neue_betriebsmeldung("[admin] Wasserpumpe wird eingeschaltet.")
	wasserpumpe_ein()
elif int(parameter.wasserpumpe) == 1:
	neue_betriebsmeldung("[admin] Wasserpumpe wird ausgeschaltet.")
	wasserpumpe_aus()
elif int(parameter.ventil_wasserpumpe) == 2:
	neue_betriebsmeldung("[admin] Ventil Wasserpumpe wird geoeffnet.")
	ventil_wasserpumpe_oeffnen()
elif int(parameter.ventil_wasserpumpe) == 1:
	neue_betriebsmeldung("[admin] Ventil Wasserpumpe wird geschlossen.")
	ventil_wasserpumpe_schliessen()
elif int(parameter.ventil_befeuchter) == 2:
	neue_betriebsmeldung("[admin] Ventil Befeuchter wird geoeffnet.")
	ventil_befeuchter_oeffnen()
elif int(parameter.ventil_befeuchter) == 1:
	neue_betriebsmeldung("[admin] Ventil Befeuchter wird geschlossen.")
	ventil_befeuchter_schliessen()
elif int(parameter.licht) == 2:
	neue_betriebsmeldung("[admin] Licht wird eingeschaltet.")
	licht_ein()
elif int(parameter.licht) == 1:
	neue_betriebsmeldung("[admin] Licht wird ausgeschaltet.")
	licht_aus()
elif int(parameter.heizung) == 2:
	neue_betriebsmeldung("[admin] Heizung wird eingeschaltet.")
	heizung_ein()
elif int(parameter.heizung) == 1:
	neue_betriebsmeldung("[admin] Heizung wird ausgeschaltet.")
	heizung_aus()
elif int(parameter.befeuchter) == 2:
	neue_betriebsmeldung("[admin] Befeuchter wird eingeschaltet.")
	befeuchter_ein()
elif int(parameter.befeuchter) == 1:
	neue_betriebsmeldung("[admin] Befeuchter wird ausgeschaltet.")
	befeuchter_aus()
else:
	pass
# ======================================================================
