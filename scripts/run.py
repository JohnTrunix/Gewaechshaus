# Die Datei run.py ist der Hauptbestandteil der Python Programme.
# Run.py führt periodisch mittels scheduling die vordefinierten
# Abläufe aus. Das logging Modul von Python protokolliert Fehlermeldungen
# und Debug informationen. Die Log Datei wird bei jedem Programstart gelöscht.


# Import von benötigten Modulen
############################################################
from abfrage import start_sensorabfrage
from datenbegrenzung import start_datenbegrenzung
from zeit_update import start_zeit_update
import schedule
import time
import logging
import os
############################################################


# Konfiguration des Logging Modul
############################################################
logger = logging.getLogger('run')
logger.setLevel(logging.DEBUG)
ch = logging.FileHandler(
    '/etc/gewaechshaus/log/gewaechshaus.log')
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
############################################################


# Bei Start die Zeit updaten und Datenbegrenzung ausführen
############################################################
try:
    logger.debug('Zeit wird aktualisiert und Datenbegrenzung wird ausgeführt')
    start_zeit_update()
    start_datenbegrenzung()
except:
    logger.warning('Zeitupdate und Datenbegrenzung fehlgeschlagen')
############################################################


# Alle Aufträge mit Startintervall definiert
############################################################
schedule.every(0.5).minutes.do(start_sensorabfrage)
schedule.every().day.at("10:00").do(start_datenbegrenzung)
schedule.every().day.at("10:00").do(start_zeit_update)
############################################################


# Alle 30 Sekunden auf ausstehende Aufträge überprüfen
############################################################
while True:
    try:
        logger.debug('Starte ausstehende Aufträge')
        schedule.run_pending()
        time.sleep(15)
    except:
        logger.warning('Fehler bei schedule.run_pending()')
############################################################
