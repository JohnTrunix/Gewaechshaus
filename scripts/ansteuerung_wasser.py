from betriebsmeldungen import neue_betriebsmeldung
try:
    import datenbank_abfrage
    import sensor_abfrage
    from ansteuerung_pwm_shield import ventil_wasserpumpe_offen, ventil_wasserpumpe_geschlossen, ventil_befeuchter_offen, ventil_befeuchter_geschlossen, wasserpumpe_ein, wasserpumpe_aus, grundstellung
    import time
    import RPi.GPIO as GPIO
except:
    neue_betriebsmeldung(
        "[ansteuerung_wasser] Fehler bei der importierung von Modulen.")

try:
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
except:
    neue_betriebsmeldung(
        "[ansteuerung_wasser] Fehler bei der GPIO definierung.")


def start_ansteuerung_wasser():
    try:
        if datenbank_abfrage.programm_status == 1:
            if int(datenbank_abfrage.wassermenge) > 0:
                ausgabe_wassermenge_mililiter = (
                    (int(datenbank_abfrage.wassermenge) / 24) * 100)
                pumpe_mililiter_pro_sekunde = 5
                einschaltdauer_pumpe = ausgabe_wassermenge_mililiter / pumpe_mililiter_pro_sekunde
                ventil_wasserpumpe_offen()
                time.sleep(1)
                wasserpumpe_ein()
                time.sleep(einschaltdauer_pumpe)
                wasserpumpe_aus()
                time.sleep(1)
                ventil_wasserpumpe_geschlossen()
            else:
                pass
        else:
            grundstellung()
    except:
        neue_betriebsmeldung(
            "[ansteuerung_wasser] Fehler bei der Zyklusberechnung der Wasseransteuerung.")


def start_auffuellen_befeuchter():
    try:
        if datenbank_abfrage.programm_status == 1:
            auffuellen_fertig = 0
            pumpe_gestartet = 0
            while auffuellen_fertig == 0 and GPIO.input(21) == GPIO.LOW:

                if GPIO.input(21) == GPIO.LOW and pumpe_gestartet == 0:
                    ventil_befeuchter_offen()
                    time.sleep(1)
                    wasserpumpe_ein()
                    pumpe_gestartet = 1

                if GPIO.input(21) == GPIO.HIGH:
                    wasserpumpe_aus()
                    time.sleep(1)
                    ventil_befeuchter_geschlossen()
                    auffuellen_fertig = 1
            else:
                pass
        else:
            grundstellung()
    except:
        neue_betriebsmeldung(
            "[ansteuerung_wasser] Fehler bei der Auffuellung des Befeuchters.")
