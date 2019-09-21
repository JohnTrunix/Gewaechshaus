from abfrage import start_sensorabfrage
from datenbegrenzung import start_datenbegrenzung
from zeit_update import start_zeit_update
import schedule
import time

schedule.every(1).minutes.do(start_sensorabfrage)
schedule.every().day.at("10:30").do(start_datenbegrenzung)
schedule.every().day.at("10:30").do(start_zeit_update)

while True:
    schedule.run_pending()
    time.sleep(1)
