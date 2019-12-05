# Import der Betriebsmeldungsfunktion
# ======================================================================
from betriebsmeldungen import neue_betriebsmeldung
# ======================================================================

# Betriebsmeldung bei Systemstart
# ======================================================================
neue_betriebsmeldung(
    "[run] System wird gestartet.")
# ======================================================================

# Import von benoetigten Modulen
# ======================================================================
try:
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
except:
    neue_betriebsmeldung(
        "[run] Fehler bei der importierung von Modulen.")
# ======================================================================

# Zeit Aktualisierung bei Start
# ======================================================================
try:
    start_zeit_update()
except:
    neue_betriebsmeldung(
        "[run] Fehler bei der Anforderung der Zeitaktualisierung.")
# ======================================================================

# Datenbegrenzung bei Start
# ======================================================================
try:
    start_datenbegrenzung()
except:
    neue_betriebsmeldung(
        "[run] Fehler bei der Anforderung der Datenbegrenzung.")
# ======================================================================

# Datenbankabfrage bei Start
# ======================================================================
try:
    start_datenbank_abfrage()
except:
    neue_betriebsmeldung(
        "[run] Fehler bei der Anforderung der Datenbankabfrage.")
# ======================================================================

# Grundstellung bei Start
# ======================================================================
try:
    grundstellung()
except:
    neue_betriebsmeldung(
        "[run] Fehler bei der Anforderung der Grundstellung.")
# ======================================================================

# Alle Auftraege mit Startintervall definiert
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

# Alle 5 Sekunden auf ausstehende Auftraege ueberpruefen
# ======================================================================
while True:
    try:
        schedule.run_pending()
        time.sleep(2)
    except:
        neue_betriebsmeldung(
            "[run] Kritischer Fehler bei der Ausfuehrung der ausstehenden Auftraege (Evtl. Busfehler).")
# ======================================================================
