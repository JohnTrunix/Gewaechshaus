from betriebsmeldungen import neue_betriebsmeldung
try:
    from adafruit_servokit import ServoKit
    import board
    import busio
    import time
    import adafruit_pca9685
except:
    neue_betriebsmeldung(
        "[ansteuerung_pwm_shield] Fehler bei der importierung von Modulen.")

try:
    i2c = busio.I2C(board.SCL, board.SDA)
    shield = adafruit_pca9685.PCA9685(i2c)
    shield.frequency = 60
    kit = ServoKit(channels=16)
    kit.servo[0].actuation_range = 180
    kit.servo[1].actuation_range = 180
    luefter_gross = shield.channels[4]
    luefter_klein = shield.channels[5]
    wasserpumpe = shield.channels[6]
    ventil_wasserpumpe = shield.channels[7]
    ventil_befeuchter = shield.channels[8]
    licht = shield.channels[9]
    heizung1 = shield.channels[10]
    heizung2 = shield.channels[11]
    befeuchter = shield.channels[12]
except:
    neue_betriebsmeldung(
        "[ansteuerung_pwm_shield] Fehler bei der initialen definierung.")


def grundstellung():
    try:
        tuer_geschlossen()
        luefter_gross_aus()
        luefter_klein_aus()
        wasserpumpe_aus()
        ventil_wasserpumpe_geschlossen()
        ventil_befeuchter_geschlossen()
        licht_aus()
        heizung_aus()
        befeuchter_aus()
    except:
        neue_betriebsmeldung(
            "[ansteuerung_pwm_shield] Grundstellung konnte nicht angefordert werden.")


def tuer_offen():
    try:
        kit.servo[0].angle = 90
        kit.servo[1].angle = 90
    except:
        neue_betriebsmeldung(
            "[ansteuerung_pwm_shield] Tueren konnten nicht geoeffnet werden.")


def tuer_geschlossen():
    try:
        kit.servo[0].angle = 0
        kit.servo[1].angle = 0
    except:
        neue_betriebsmeldung(
            "[ansteuerung_pwm_shield] Tueren konnten nicht geschlossen werden.")


def luefter_gross_ein():
    try:
        luefter_gross.duty_cycle = 0
    except:
        neue_betriebsmeldung(
            "[ansteuerung_pwm_shield] Grosse Luefter konnten nicht eingeschaltet werden.")


def luefter_gross_aus():
    try:
        luefter_gross.duty_cycle = 0xffff
    except:
        neue_betriebsmeldung(
            "[ansteuerung_pwm_shield] Grosse Luefter konnten nicht ausgeschaltet werden.")


def luefter_klein_ein():
    try:
        luefter_klein.duty_cycle = 0
    except:
        neue_betriebsmeldung(
            "[ansteuerung_pwm_shield] Kleine Luefter konnten nicht eingeschaltet werden.")


def luefter_klein_aus():
    try:
        luefter_klein.duty_cycle = 0xffff
    except:
        neue_betriebsmeldung(
            "[ansteuerung_pwm_shield] Kleine Luefter konnten nicht ausgeschaltet werden.")


def wasserpumpe_ein():
    try:
        wasserpumpe.duty_cycle = 0
    except:
        neue_betriebsmeldung(
            "[ansteuerung_pwm_shield] Wasserpumpe konnte nicht eingeschaltet werden.")


def wasserpumpe_aus():
    try:
        wasserpumpe.duty_cycle = 0xffff
    except:
        neue_betriebsmeldung(
            "[ansteuerung_pwm_shield] Wasserpumpe konnte nicht ausgeschaltet werden.")


def ventil_wasserpumpe_offen():
    try:
        ventil_wasserpumpe.duty_cycle = 0
    except:
        neue_betriebsmeldung(
            "[ansteuerung_pwm_shield] Das Ventil der Wasserpumpe konnte nicht geoeffnet werden.")


def ventil_wasserpumpe_geschlossen():
    try:
        ventil_wasserpumpe.duty_cycle = 0xffff
    except:
        neue_betriebsmeldung(
            "[ansteuerung_pwm_shield] Das Ventil der Wasserpumpe konnte nicht geschlossen werden.")


def ventil_befeuchter_offen():
    try:
        ventil_befeuchter.duty_cycle = 0
    except:
        neue_betriebsmeldung(
            "[ansteuerung_pwm_shield] Das Ventil des Befeuchters konnte nicht geoeffnet werden.")


def ventil_befeuchter_geschlossen():
    try:
        ventil_befeuchter.duty_cycle = 0xffff
    except:
        neue_betriebsmeldung(
            "[ansteuerung_pwm_shield] Das Ventil des Befeuchters konnte nicht geschlossen werden.")


def licht_ein():
    try:
        licht.duty_cycle = 0
    except:
        neue_betriebsmeldung(
            "[ansteuerung_pwm_shield] Das Licht konnte nicht eingeschaltet werden.")


def licht_aus():
    try:
        licht.duty_cycle = 0xffff
    except:
        neue_betriebsmeldung(
            "[ansteuerung_pwm_shield] Das Licht konnte nicht ausgeschaltet werden.")


def heizung_ein():
    try:
        heizung1.duty_cycle = 0
        heizung2.duty_cycle = 0
    except:
        neue_betriebsmeldung(
            "[ansteuerung_pwm_shield] Die Heizung konnte nicht eingeschaltet werden.")


def heizung_aus():
    try:
        heizung1.duty_cycle = 0xffff
        heizung2.duty_cycle = 0xffff
    except:
        neue_betriebsmeldung(
            "[ansteuerung_pwm_shield] Die Heizung konnte nicht ausgeschaltet werden.")


def befeuchter_ein():
    try:
        befeuchter.duty_cycle = 0
    except:
        neue_betriebsmeldung(
            "[ansteuerung_pwm_shield] Der Befeuchter konnte nicht eingeschaltet werden.")


def befeuchter_aus():
    try:
        befeuchter.duty_cycle = 0xffff
    except:
        neue_betriebsmeldung(
            "[ansteuerung_pwm_shield] Der Befeuchter konnte nicht ausgeschaltet werden.")
