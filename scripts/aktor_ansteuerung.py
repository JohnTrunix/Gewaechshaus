# Die Datei ausgabe.py ist für die Aktoransteuerung zuständig.

# Import von benötigten Modulen
# ======================================================================
from datenbank_abfrage import *
# ======================================================================

get_betriebsmodus()
if programm_status == 1:
    get_parameter()
