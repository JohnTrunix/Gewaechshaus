from betriebsmeldungen import neue_betriebsmeldung

# Import von benötigten Modulen
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


if arguments.stop == 1:
    neue_betriebsmeldung(
        "[manuelle_steuerung] System wird gestoppt.")
    os.system("sudo service gewaechshaus stop")
    os.system("sudo killall python3")
    time.sleep(2)
    grundstellung()
    os.system("sudo killall python3")
elif arguments.start == 1:
    neue_betriebsmeldung(
        "[manuelle_steuerung] System wird gestartet.")
    os.system("sudo service gewaechshaus stop")
    os.system("sudo killall python3")
    time.sleep(2)
    os.system("sudo service gewaechshaus start")
elif arguments.herunterfahren == 1:
    neue_betriebsmeldung(
        "[manuelle_steuerung] System wird heruntergefahren.")
    os.system("sudo service gewaechshaus stop")
    time.sleep(2)
    grundstellung()
    time.sleep(10)
    os.system("sudo shutdown -h now")
else:
    pass
