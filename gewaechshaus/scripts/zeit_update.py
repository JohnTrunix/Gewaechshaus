import busio
import adafruit_pcf8523
import time
import datetime
import board
import socket
import os

myI2C = busio.I2C(board.SCL, board.SDA)
rtc = adafruit_pcf8523.PCF8523(myI2C)
t = rtc.datetime


print("")
print("----------------------------")
print("Zeit Update wird ausgeführt.")


def start_zeit_update():
    try:
        socket.create_connection(("www.google.com", 443))
        print("Verbunden mit Internet")
        rtc_update()
    except:
        print("Keine Internetverbindung")
        systemzeit_schreiben()


def rtc_abfrage():
    try:
        print("Aktuelle RTC Zeit wird abgefragt.")
        print("RTC Datum: %d/%d/%d" % (t.tm_mday, t.tm_mon, t.tm_year))
        print("RTC Zeit: %d:%02d:%02d" % (t.tm_hour, t.tm_min, t.tm_sec))
    except:
        print("Fehler bei rtc_abfrage()")


def rtc_update():
    try:
        print("RTC wird aktualisiert.")
        now = datetime.datetime.now()
        t = time.struct_time((now.year, now.month, now.day,
                              now.hour, now.minute, now.second, 0, 0, 0))
        rtc.datetime = t
        print("Zeit auf RTC:", t)
    except:
        print("Fehler bei rtc_update()")


def systemzeit_schreiben():
    try:
        print("Systemzeit wird aktualisiert.")
        rtc_abfrage()
        os.system("sudo timedatectl set-ntp false")
        time.sleep(1)
        os.system("sudo timedatectl set-time " + str(t.tm_hour) +
                  ":" + str(t.tm_min) + ":" + str(t.tm_sec))
        time.sleep(1)
        os.system("sudo timedatectl set-ntp true")
    except:
        print("Fehler bei systemzeit_schreiben()")


print("Zeit Update beendet.")
print("----------------------------")
print("")
