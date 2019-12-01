from betriebsmeldungen import neue_betriebsmeldung

# Import von benoetigten Modulen
# ======================================================================
try:
    import argparse
    import os
    import time
    from ansteuerung_pwm_shield import grundstellung, tuer_oeffnen, tuer_schliessen, luefter_gross_ein, luefter_gross_aus, luefter_klein_ein, luefter_klein_aus, wasserpumpe_ein, wasserpumpe_aus, ventil_wasserpumpe_oeffnen, ventil_wasserpumpe_schliessen, ventil_befeuchter_oeffnen, ventil_befeuchter_schliessen, licht_ein, licht_aus, heizung_ein, heizung_aus, befeuchter_ein, befeuchter_aus
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
        default=0
    )
    parser.add_argument(
        '--start',
        default=0
    )
    parser.add_argument(
        '--herunterfahren',
        default=0
    )
    parser.add_argument(
        '--tuer',
        default=0
    )
    parser.add_argument(
        '--luefter_gross',
        default=0
    )
    parser.add_argument(
        '--luefter_klein',
        default=0
    )
    parser.add_argument(
        '--wasserpumpe',
        default=0
    )
    parser.add_argument(
        '--ventil_wasserpumpe',
        default=0
    )
    parser.add_argument(
        '--ventil_befeuchter',
        default=0
    )
    parser.add_argument(
        '--licht',
        default=0
    )
    parser.add_argument(
        '--heizung',
        default=0
    )
    parser.add_argument(
        '--befeuchter',
        default=0
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
        "[manuelle_steuerung] System wird für die manuelle Aktorsteuerung gestoppt.")
    os.system("sudo service gewaechshaus stop")
    time.sleep(2)
# ======================================================================


# Tuersteuerung
# ======================================================================
def manuell_tuer_oeffnen():
    manuelle_aktorsteuerung()
    neue_betriebsmeldung(
        "[manuelle_steuerung] Tueren werden geoeffnet.")
    tuer_oeffnen()


def manuell_tuer_schliessen():
    manuelle_aktorsteuerung()
    neue_betriebsmeldung(
        "[manuelle_steuerung] Tueren werden geschlossen.")
    tuer_schliessen()
# ======================================================================


# Lueftersteuerung
# ======================================================================
def manuell_luefter_gross_ein():
    manuelle_aktorsteuerung()
    neue_betriebsmeldung(
        "[manuelle_steuerung] Luefter gross werden eingeschaltet.")
    luefter_gross_ein()


def manuell_luefter_gross_aus():
    manuelle_aktorsteuerung()
    neue_betriebsmeldung(
        "[manuelle_steuerung] Luefter gross werden ausgeschaltet.")
    luefter_gross_aus()


def manuell_luefter_klein_ein():
    manuelle_aktorsteuerung()
    neue_betriebsmeldung(
        "[manuelle_steuerung] Luefter klein werden eingeschaltet.")
    luefter_klein_ein()


def manuell_luefter_klein_aus():
    manuelle_aktorsteuerung()
    neue_betriebsmeldung(
        "[manuelle_steuerung] Luefter klein werden ausgeschaltet.")
    luefter_klein_aus()
# ======================================================================


# Wassersteuerung
# ======================================================================
def manuell_wasserpumpe_ein():
    manuelle_aktorsteuerung()
    neue_betriebsmeldung(
        "[manuelle_steuerung] Wasserpumpe wird eingeschaltet.")
    wasserpumpe_ein()


def manuell_wasserpumpe_aus():
    manuelle_aktorsteuerung()
    neue_betriebsmeldung(
        "[manuelle_steuerung] Wasserpumpe wird ausgeschaltet.")
    wasserpumpe_aus()


def manuell_ventil_wasserpumpe_oeffnen():
    manuelle_aktorsteuerung()
    neue_betriebsmeldung(
        "[manuelle_steuerung] Ventil der Wasserpumpe wird geoeffnet.")
    ventil_wasserpumpe_oeffnen()


def manuell_ventil_wasserpumpe_schliessen():
    manuelle_aktorsteuerung()
    neue_betriebsmeldung(
        "[manuelle_steuerung] Ventil der Wasserpumpe wird geschlossen.")
    ventil_wasserpumpe_schliessen()


def manuell_ventil_befeuchter_oeffnen():
    manuelle_aktorsteuerung()
    neue_betriebsmeldung(
        "[manuelle_steuerung] Ventil des Befeuchters wird geoeffnet.")
    ventil_befeuchter_oeffnen()


def manuell_ventil_befeuchter_schliessen():
    manuelle_aktorsteuerung()
    neue_betriebsmeldung(
        "[manuelle_steuerung] Ventil des Befeuchters wird geschlossen.")
    ventil_befeuchter_schliessen()
# ======================================================================


# Lichtsteuerung
# ======================================================================
def manuell_licht_ein():
    manuelle_aktorsteuerung()
    neue_betriebsmeldung(
        "[manuelle_steuerung] Licht wird eingeschaltet.")
    licht_ein()


def manuell_licht_aus():
    manuelle_aktorsteuerung()
    neue_betriebsmeldung(
        "[manuelle_steuerung] Licht wird ausgeschaltet.")
    licht_aus()
# ======================================================================


# Heizungssteuerung
# ======================================================================
def manuell_heizung_ein():
    manuelle_aktorsteuerung()
    neue_betriebsmeldung(
        "[manuelle_steuerung] Heizung wird eingeschaltet.")
    heizung_ein()


def manuell_heizung_aus():
    manuelle_aktorsteuerung()
    neue_betriebsmeldung(
        "[manuelle_steuerung] Heizung wird ausgeschaltet.")
    heizung_aus()
# ======================================================================


# Befeuchtersteuerung
# ======================================================================
def manuell_befeuchter_ein():
    manuelle_aktorsteuerung()
    neue_betriebsmeldung(
        "[manuelle_steuerung] Befeuchter wird eingeschaltet.")
    befeuchter_ein()


def manuell_befeuchter_aus():
    manuelle_aktorsteuerung()
    neue_betriebsmeldung(
        "[manuelle_steuerung] Befeuchter wird ausgeschaltet.")
    befeuchter_aus()
# ======================================================================


# Startoptionen
# ======================================================================
if arguments.stop == 1:
    stop()
elif arguments.start == 1:
    start()
elif arguments.herunterfahren == 1:
    shutdown()
elif arguments.tuer == 1:
    manuell_tuer_oeffnen()
elif arguments.luefter_gross == 1:
    manuell_luefter_gross_ein()
elif arguments.luefter_klein == 1:
    manuell_luefter_klein_ein()
elif arguments.wasserpumpe == 1:
    manuell_wasserpumpe_ein()
elif arguments.ventil_wasserpumpe == 1:
    manuell_ventil_wasserpumpe_oeffnen()
elif arguments.ventil_befeuchter == 1:
    manuell_ventil_befeuchter_oeffnen()
elif arguments.licht == 1:
    manuell_licht_ein()
elif arguments.heizung == 1:
    manuell_heizung_ein()
elif arguments.befeuchter == 1:
    manuell_befeuchter_ein()
elif arguments.tuer == 0:
    manuell_tuer_schliessen()
elif arguments.luefter_gross == 0:
    manuell_luefter_gross_aus()
elif arguments.luefter_klein == 0:
    manuell_luefter_klein_aus()
elif arguments.wasserpumpe == 0:
    manuell_wasserpumpe_aus()
elif arguments.ventil_wasserpumpe == 0:
    manuell_ventil_wasserpumpe_schliessen()
elif arguments.ventil_befeuchter == 0:
    manuell_ventil_befeuchter_schliessen()
elif arguments.licht == 0:
    manuell_licht_aus()
elif arguments.heizung == 0:
    manuell_heizung_aus()
elif arguments.befeuchter == 0:
    manuell_befeuchter_aus()
else:
    pass
# ======================================================================
