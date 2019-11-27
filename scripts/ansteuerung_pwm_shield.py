import board
import busio
import time
import adafruit_pca9685
i2c = busio.I2C(board.SCL, board.SDA)
shield = adafruit_pca9685.PCA9685(i2c)

shield.frequency = 60

from adafruit_servokit import ServoKit
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

def grundstellung():
    try:
        print("Grundstellung wird ausgeführt")
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
        print("Fehler bei grundstellung()")

def tuer_offen():
    try:
        print("Türen werden geöffnet")
        kit.servo[0].angle = 90
        kit.servo[1].angle = 90
    except:
        print("Fehler bei tuer_offen()")

def tuer_geschlossen():
    try:
        print("Türen werden geschlossen")
        kit.servo[0].angle = 0
        kit.servo[1].angle = 0
    except:
        print("Fehler bei tuer_geschlossen()")

def luefter_gross_ein():
    try:
        print("luefter gross ein")
        luefter_gross.duty_cycle = 0
    except:
        print("Fehler bei luefter_gross_ein()")

def luefter_gross_aus():
    try:
        print("luefter gross aus")
        luefter_gross.duty_cycle = 0xffff
    except:
        print("Fehler bei luefter_gross_aus()")

def luefter_klein_ein():
    try:
        print("luefter klein ein")
        luefter_klein.duty_cycle = 0
    except:
        print("Fehler bei luefter_klein_ein()")

def luefter_klein_aus():
    try:
        print("luefter klein aus")
        luefter_klein.duty_cycle = 0xffff
    except:
        print("Fehler bei luefter_klein_aus()")

def wasserpumpe_ein():
    try:
        print("Wasserpumpe Ein")
        wasserpumpe.duty_cycle = 0
    except:
        print("Fehler bei wasserpumpe_ein()")

def wasserpumpe_aus():
    try:
        print("Wasserpumpe aus")
        wasserpumpe.duty_cycle = 0xffff
    except:
        print("Fehler bei wasserpumpe_aus()")

def ventil_wasserpumpe_offen():
    try:
        print("Ventil wasserpumpe offen")
        ventil_wasserpumpe.duty_cycle = 0
    except:
        print("Fehler bei ventil_wasserpumpe_offen()")

def ventil_wasserpumpe_geschlossen():
    try:
        print("Ventil wasserpumpe schliessen")
        ventil_wasserpumpe.duty_cycle = 0xffff
    except:
        print("Fehler bei ventil_wasserpumpe_geschlossen()")

def ventil_befeuchter_offen():
    try:
        print("Ventil befeuchter offen")
        ventil_befeuchter.duty_cycle = 0
    except:
        print("Fehler bei ventil_befeuchter_offen()")

def ventil_befeuchter_geschlossen():
    try:
        print("Ventil befeuchter schliessen")
        ventil_befeuchter.duty_cycle = 0xffff
    except:
        print("Fehler bei ventil_befeuchter_geschlossen()")

def licht_ein():
    try:
        print("Licht ein")
        licht.duty_cycle = 0
    except:
        print("Fehler bei licht_ein()")

def licht_aus():
    try:
        print("Licht aus")
        licht.duty_cycle = 0xffff
    except:
        print("Fehler bei licht_aus()")

def heizung_ein():
    try:
        print("Heizung ein")
        heizung1.duty_cycle = 0
        heizung2.duty_cycle = 0
    except:
        print("Fehler bei heizung_ein()")

def heizung_aus():
    try:
        print("Heizung aus")
        heizung1.duty_cycle = 0xffff
        heizung2.duty_cycle = 0xffff
    except:
        print("Fehler bei heizung_aus()")

def befeuchter_ein():
    try:
        print("Befeuchter ein")
        befeuchter.duty_cycle = 0
    except:
        print("Fehler bei befeuchter_ein()")

def befeuchter_aus():
    try:
        print("Befeuchter aus")
        befeuchter.duty_cycle = 0xffff
    except:
        print("Fehler bei befeuchter_aus()")