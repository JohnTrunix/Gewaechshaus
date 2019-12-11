# Import der Betriebsmeldungsfunktion
# ======================================================================
from betriebsmeldungen import neue_betriebsmeldung
# ======================================================================

# Import von benoetigten Modulen
# ======================================================================
import argparse
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
elif int(parameter.start) == 1:
	neue_betriebsmeldung("[admin] System wird gestartet.")
elif int(parameter.herunterfahren) == 1:
	neue_betriebsmeldung("[admin] System wird gestoppt, in Grundstellung gebracht und heruntergefahren.")
elif int(parameter.tuer) == 2:
	neue_betriebsmeldung("[admin] Tueren werden geoeffnet.")
elif int(parameter.tuer) == 1:
	neue_betriebsmeldung("[admin] Tueren werden geschlossen.")
elif int(parameter.luefter_gross) == 2:
	neue_betriebsmeldung("[admin] Luefter gross werden eingeschaltet.")
elif int(parameter.luefter_gross) == 1:
	neue_betriebsmeldung("[admin] Luefter gross werden ausgeschaltet.")
elif int(parameter.luefter_klein) == 2:
	neue_betriebsmeldung("[admin] Luefter klein werden eingeschaltet.")
elif int(parameter.luefter_klein) == 1:
	neue_betriebsmeldung("[admin] Luefter klein werden ausgeschaltet.")
elif int(parameter.wasserpumpe) == 2:
	neue_betriebsmeldung("[admin] Wasserpumpe wird eingeschaltet.")
elif int(parameter.wasserpumpe) == 1:
	neue_betriebsmeldung("[admin] Wasserpumpe wird ausgeschaltet.")
elif int(parameter.ventil_wasserpumpe) == 2:
	neue_betriebsmeldung("[admin] Ventil Wasserpumpe wird geoeffnet.")
elif int(parameter.ventil_wasserpumpe) == 1:
	neue_betriebsmeldung("[admin] Ventil Wasserpumpe wird geschlossen.")
elif int(parameter.ventil_befeuchter) == 2:
	neue_betriebsmeldung("[admin] Ventil Befeuchter wird geoeffnet.")
elif int(parameter.ventil_befeuchter) == 1:
	neue_betriebsmeldung("[admin] Ventil Befeuchter wird geschlossen.")
elif int(parameter.licht) == 2:
	neue_betriebsmeldung("[admin] Licht wird eingeschaltet.")
elif int(parameter.licht) == 1:
	neue_betriebsmeldung("[admin] Licht wird ausgeschaltet.")
elif int(parameter.heizung) == 2:
	neue_betriebsmeldung("[admin] Heizung wird eingeschaltet.")
elif int(parameter.heizung) == 1:
	neue_betriebsmeldung("[admin] Heizung wird ausgeschaltet.")
elif int(parameter.befeuchter) == 2:
	neue_betriebsmeldung("[admin] Befeuchter wird eingeschaltet.")
elif int(parameter.befeuchter) == 1:
	neue_betriebsmeldung("[admin] Befeuchter wird ausgeschaltet.")
else:
	pass
# ======================================================================