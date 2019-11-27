# Die Datei run.py ist der Hauptbestandteil der Python Programme.
# Run.py führt periodisch mittels scheduling die vordefinierten
# Abläufe aus.


# Import von benötigten Modulen
# ======================================================================
from sensor_abfrage import start_sensorabfrage
from datenbegrenzung import start_datenbegrenzung
from zeit_update import start_zeit_update
from datenbank_abfrage import start_datenbank_abfrage
from ansteuerung_temp_luft import start_ansteuerung_temp_luft
from ansteuerung_licht import reset_licht_zaehler
from ansteuerung_wasser import start_ansteuerung_wasser, start_auffuellen_befeuchter
from ansteuerung_pwm_shield import grundstellung
from ansteuerung_licht import start_lichtsteuerung
import schedule
import time
import os
# ======================================================================


# Zeit Aktualisierung bei Start
# ======================================================================
try:
    print('Zeit wird aktualisiert')
    start_zeit_update()
except:
    print('Fehler bei start_zeit_update()')
# ======================================================================


# Datenbegrenzung bei Start
# ======================================================================
try:
    print('Datenbegrenzung wird ausgeführt')
    start_datenbegrenzung()
except:
    print('Fehler bei start_datenbegrenzung()')
# ======================================================================


# Datenbankabfrage bei Start
# ======================================================================
try:
    print('Betriebs- und Parameterdaten werden geladen')
    start_datenbank_abfrage()
except:
    print('Fehler bei start_datenbank_abfrage()')
# ======================================================================


# Grundstellung bei Start
# ======================================================================
try:
    grundstellung()
except:
    print('Fehler bei grundstellung()')
# ======================================================================


# Alle Aufträge mit Startintervall definiert
# ======================================================================
schedule.every(10).seconds.do(start_datenbank_abfrage)
schedule.every(10).seconds.do(start_sensorabfrage)
schedule.every(10).seconds.do(start_ansteuerung_temp_luft)
schedule.every(2).hours.do(start_auffuellen_befeuchter)
schedule.every().hour.at("00:05").do(start_lichtsteuerung)
schedule.every().hour.at("00:35").do(start_lichtsteuerung)
schedule.every().hour.at("00:10").do(start_ansteuerung_wasser)
schedule.every().day.at("23:55").do(start_datenbegrenzung)
schedule.every().day.at("23:55").do(start_zeit_update)
schedule.every().day.at("08:00").do(reset_licht_zaehler)
# ======================================================================


# Alle 5 Sekunden auf ausstehende Aufträge überprüfen
# ======================================================================
while True:
    try:
        schedule.run_pending()
        time.sleep(2)
    except:
        print('Fehler bei schedule.run_pending()')
# ======================================================================
