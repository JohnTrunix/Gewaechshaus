from abfrage import start_sensorabfrage
from datenbegrenzung import start_datenbegrenzung
from zeit_update import start_zeit_update
import schedule
import time
import logging


logger = logging.getLogger('Gewaechshaus | run.py')
logger.setLevel(logging.DEBUG)
ch = logging.FileHandler(
    'B:/SW Repos/Gewaechshaus/gewaechshaus/log/gewaechshaus.log')
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


schedule.every(1).minutes.do(start_sensorabfrage)
schedule.every().day.at("10:00").do(start_datenbegrenzung)
schedule.every().day.at("10:00").do(start_zeit_update)


while True:
    try:
        logger.debug('Starte ausstehende Aufträge')
        schedule.run_pending()
        time.sleep(30)
    except:
        logger.warning('Fehler bei schedule.run_pending()')
