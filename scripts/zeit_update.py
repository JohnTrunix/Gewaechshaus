# zeit_update.py stellt sicher, dass der Raspberry Pi
# mit der korrekten Zeit arbeitet. Ist der Raspberry Pi
# mit dem Internet verbunden, wird die Zeit mittels NTP aktualisert.
# Besteht keine Internetverbindung, wird die Zeit von der RTC gelesen
# und als Systemzeit geschrieben.


# Import von benötigten Modulen
############################################################
import busio
import adafruit_pcf8523
import time
import datetime
import board
import socket
import os
import logging
############################################################


# Konfiguration des Logging Modul
############################################################
logger = logging.getLogger('datenbegrenzung')
logger.setLevel(logging.DEBUG)
ch = logging.FileHandler(
    'B:/SW Repos/Gewaechshaus/gewaechshaus/log/gewaechshaus.log')
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
############################################################


# I2C Bus Konfiguration
############################################################
myI2C = busio.I2C(board.SCL, board.SDA)
rtc = adafruit_pcf8523.PCF8523(myI2C)
t = rtc.datetime
############################################################


logger.debug('Zeit Update wird ausgeführt')


# Überprüfe Internetverbindung
############################################################
def start_zeit_update():
    try:
        socket.create_connection(("www.google.com", 443))
        logger.debug('Verbunden mit Internet')
        rtc_update()
    except:
        logger.warning('Keine Internetverbindung')
        systemzeit_schreiben()
############################################################


# RTC Abfrage
############################################################
def rtc_abfrage():
    try:
        logger.debug('Aktuelle RTC Zeit wird abgefragt')
        logger.debug('RTC Datum: %d/%d/%d' % (t.tm_mday, t.tm_mon, t.tm_year))
        logger.debug('RTC Zeit: %d:%02d:%02d' %
                     (t.tm_hour, t.tm_min, t.tm_sec))
    except:
        logger.warning('Fehler bei rtc_abfrage()')
############################################################


# RTC Update
############################################################
def rtc_update():
    try:
        logger.debug('RTC wird aktualisiert')
        now = datetime.datetime.now()
        t = time.struct_time((now.year, now.month, now.day,
                              now.hour, now.minute, now.second, 0, 0, 0))
        rtc.datetime = t
        logger.debug('%s Zeit auf RTC', t)
    except:
        logger.warning('Fehler bei rtc_update()')
############################################################


# Systemzeit schreiben von RTC
############################################################
def systemzeit_schreiben():
    try:
        logger.debug('Systemzeit wird aktualisiert')
        rtc_abfrage()
        os.system("sudo timedatectl set-ntp false")
        time.sleep(1)
        os.system("sudo timedatectl set-time " + str(t.tm_hour) +
                  ":" + str(t.tm_min) + ":" + str(t.tm_sec))
        time.sleep(1)
        os.system("sudo timedatectl set-ntp true")
    except:
        logger.warning('Fehler bei systemzeit_schreiben()')
############################################################


logger.debug('Zeit Update beendet')
