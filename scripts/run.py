# Die Datei run.py ist der Hauptbestandteil der Python Programme.
# Run.py führt periodisch mittels scheduling die vordefinierten
# Abläufe aus.


# Import von benötigten Modulen
# ======================================================================
from sensor_abfrage import start_sensorabfrage
from datenbegrenzung import start_datenbegrenzung
from zeit_update import start_zeit_update
from datenbank_abfrage import start_datenbank_abfrage
import schedule
import time
import os
# ======================================================================


# Bei Start die Zeit updaten, Datenbegrenzung ausführen und die Aktiven Parameter laden.
# ======================================================================
try:
    print('Zeit wird aktualisiert')
    start_zeit_update()
except:
    print('Fehler bei start_zeit_update()')
try:
    print('Datenbegrenzung wird ausgeführt')
    start_datenbegrenzung()
except:
    print('Fehler bei start_datenbegrenzung()')
try:
    print('Betriebs- und Parameterdaten werden geladen')
    start_datenbank_abfrage()
except:
    print('Fehler bei start_datenbank_abfrage()')
# ======================================================================


# Alle Aufträge mit Startintervall definiert
# ======================================================================
schedule.every(0.5).minutes.do(start_sensorabfrage)
schedule.every(120).minutes.do(start_datenbegrenzung)
schedule.every(120).minutes.do(start_zeit_update)
schedule.every(4).hours.do(start_datenbank_abfrage)
# ======================================================================


# Alle 30 Sekunden auf ausstehende Aufträge überprüfen
# ======================================================================
while True:
    try:
        print('Starte ausstehende Aufträge')
        schedule.run_pending()
        time.sleep(4)
    except:
        print('Fehler bei schedule.run_pending()')
# ======================================================================
