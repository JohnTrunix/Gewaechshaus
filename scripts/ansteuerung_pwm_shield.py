# Import von benoetigten Modulen
# ======================================================================
try:
	from datenaustausch import neue_betriebsmeldung
	from adafruit_servokit import ServoKit
	import board
	import busio
	import time
	import adafruit_pca9685
except Exception as e:
	neue_betriebsmeldung(str(e))
# ======================================================================

# PWM Board definition
# ======================================================================
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
	heizung = shield.channels[10]
	befeuchter = shield.channels[11]
except Exception as e:
	neue_betriebsmeldung(str(e))
# ======================================================================

# Grundstellung ausfuehren
# ======================================================================
def grundstellung():
	try:
		tuer_schliessen()
		luefter_gross_aus()
		luefter_klein_aus()
		wasserpumpe_aus()
		ventil_wasserpumpe_schliessen()
		ventil_befeuchter_schliessen()
		licht_aus()
		heizung_aus()
		befeuchter_aus()
	except Exception as e:
		neue_betriebsmeldung(str(e))
# ======================================================================

# Tuersteuerung
# ======================================================================
def tuer_oeffnen():
	try:
		kit.servo[0].angle = 42
		kit.servo[1].angle = 10
	except Exception as e:
		neue_betriebsmeldung(str(e))

def tuer_schliessen():
	try:
		kit.servo[0].angle = 5
		kit.servo[1].angle = 54
	except Exception as e:
		neue_betriebsmeldung(str(e))
# ======================================================================

# Lueftersteuerung
# ======================================================================
def luefter_gross_ein():
	try:
		luefter_gross.duty_cycle = 0
	except Exception as e:
		neue_betriebsmeldung(str(e))

def luefter_gross_aus():
	try:
		luefter_gross.duty_cycle = 0xffff
	except Exception as e:
		neue_betriebsmeldung(str(e))

def luefter_klein_ein():
	try:
		luefter_klein.duty_cycle = 0xffff
	except Exception as e:
		neue_betriebsmeldung(str(e))

def luefter_klein_aus():
	try:
		luefter_klein.duty_cycle = 0
	except Exception as e:
		neue_betriebsmeldung(str(e))
# ======================================================================

# Wasserpumpensteuerung
# ======================================================================
def wasserpumpe_ein():
	try:
		wasserpumpe.duty_cycle = 0
	except Exception as e:
		neue_betriebsmeldung(str(e))

def wasserpumpe_aus():
	try:
		wasserpumpe.duty_cycle = 0xffff
	except Exception as e:
		neue_betriebsmeldung(str(e))
# ======================================================================

# Ventilsteuerung
# ======================================================================
def ventil_wasserpumpe_oeffnen():
	try:
		ventil_wasserpumpe.duty_cycle = 0
	except Exception as e:
		neue_betriebsmeldung(str(e))

def ventil_wasserpumpe_schliessen():
	try:
		ventil_wasserpumpe.duty_cycle = 0xffff
	except Exception as e:
		neue_betriebsmeldung(str(e))

def ventil_befeuchter_oeffnen():
	try:
		ventil_befeuchter.duty_cycle = 0
	except Exception as e:
		neue_betriebsmeldung(str(e))

def ventil_befeuchter_schliessen():
	try:
		ventil_befeuchter.duty_cycle = 0xffff
	except Exception as e:
		neue_betriebsmeldung(str(e))
# ======================================================================

# Lichtsteuerung
# ======================================================================
def licht_ein():
	try:
		licht.duty_cycle = 0
	except Exception as e:
		neue_betriebsmeldung(str(e))


def licht_aus():
	try:
		licht.duty_cycle = 0xffff
	except Exception as e:
		neue_betriebsmeldung(str(e))
# ======================================================================

# Heizungssteuerung
# ======================================================================
def heizung_ein():
	try:
		heizung.duty_cycle = 0xffff
	except Exception as e:
		neue_betriebsmeldung(str(e))

def heizung_aus():
	try:
		heizung.duty_cycle = 0
	except Exception as e:
		neue_betriebsmeldung(str(e))
# ======================================================================

# Befeuchtersteuerung
# ======================================================================
def befeuchter_ein():
	try:
		befeuchter.duty_cycle = 0xffff
	except Exception as e:
		neue_betriebsmeldung(str(e))

def befeuchter_aus():
	try:
		befeuchter.duty_cycle = 0
	except Exception as e:
		neue_betriebsmeldung(str(e))
# ======================================================================
