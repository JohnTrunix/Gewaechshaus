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
    help='Gewaechshaus Stop und Grundstellung'
)
parser.add_argument(
    '--start',
    default=0,
    help='Gewaechshaus Start'
)
parser.add_argument(
    '--herunterfahren',
    default=0,
    help='System Herunterfahren'
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
# ======================================================================