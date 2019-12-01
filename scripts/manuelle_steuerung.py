from betriebsmeldungen import neue_betriebsmeldung

# Import von benoetigten Modulen
# ======================================================================
try:
    import argparse
    import os
    import time
    from ansteuerung_pwm_shield import grundstellung
except:
    neue_betriebsmeldung(
        "[manuelle_steuerung] Fehler bei der importierung von Modulen.")
# ======================================================================


# Definierung von Startoptionen
# ======================================================================
try:
    parser = argparse.ArgumentParser(description='Manuelle Ansteuerung')
    parser.add_argument(
        '--stop',
        default=0,
        help='Wenn 1 -> System wird gestoppt und in Grundstellung positioniert.'
    )
    parser.add_argument(
        '--start',
        default=0,
        help='Wenn 1 -> System wird gestartet.'
    )
    parser.add_argument(
        '--herunterfahren',
        default=0,
        help='Wenn 1 -> System wird in gestoppt, in Grundstellung gebracht und heruntergefahren.'
    )
    arguments = parser.parse_args()
except:
    neue_betriebsmeldung(
        "[manuelle_steuerung] Fehler bei der definierung von Startsignalen.")
# ======================================================================


# Stop
# ======================================================================
def stop():
    neue_betriebsmeldung(
        "[manuelle_steuerung] System wird gestoppt.")
    os.system("sudo service gewaechshaus stop")
    time.sleep(2)
    grundstellung()
    time.sleep(2)
# ======================================================================


# Start
# ======================================================================
def start():
    stop()
    neue_betriebsmeldung(
        "[manuelle_steuerung] System wird gestartet.")
    os.system("sudo service gewaechshaus start")
# ======================================================================


# Shutdown
# ======================================================================
def shutdown():
    stop()
    neue_betriebsmeldung(
        "[manuelle_steuerung] System wird heruntergefahren.")
    time.sleep(10)
    os.system("sudo shutdown -h now")
# ======================================================================


# Manuelle Aktorsteuerung
# ======================================================================
def manuelle_aktorsteuerung():
    neue_betriebsmeldung(
        "[manuelle_steuerung] System wird für manuelle Aktorsteuerung gestoppt.")
    os.system("sudo service gewaechshaus stop")
    time.sleep(2)
# ======================================================================


# Tuersteuerung
# ======================================================================
def tuer_oeffnen():
    manuelle_aktorsteuerung()
    neue_betriebsmeldung(
        "[manuelle_steuerung] Tueren werden geoeffnet.")


# ======================================================================
if arguments.stop == 1:
    stop()
elif arguments.start == 1:
    start()
elif arguments.herunterfahren == 1:
    shutdown()
else:
    pass
