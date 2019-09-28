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
logger = logging.getLogger('Gewaechshaus | run.py')
logger.setLevel(logging.DEBUG)
ch = logging.FileHandler(
    'B:/SW Repos/Gewaechshaus/gewaechshaus/log/gewaechshaus.log')
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
############################################################


# Lösche die vorhandene Log Datei (wenn vorhanden)
############################################################
try:
    if os.path.exists('B:/SW Repos/Gewaechshaus/gewaechshaus/log/gewaechshaus.log'):
        logger.debug('Lösche vorhandene Log Datei')
        os.remove('B:/SW Repos/Gewaechshaus/gewaechshaus/log/gewaechshaus.log')
    else:
        logger.debug('Log Datei nicht vorhanden')
except:
    logger.warning('Vorhandene Log Datei konnte nicht gelöscht werden')
############################################################


# Alle Aufträge mit Startintervall definiert
############################################################
schedule.every(1).minutes.do(start_sensorabfrage)
schedule.every().day.at("10:00").do(start_datenbegrenzung)
schedule.every().day.at("10:00").do(start_zeit_update)
############################################################


# Alle 30 Sekunden auf ausstehende Aufträge überprüfen
############################################################
while True:
    try:
        logger.debug('Starte ausstehende Aufträge')
        schedule.run_pending()
        time.sleep(30)
    except:
        logger.warning('Fehler bei schedule.run_pending()')
############################################################
