import time
from datetime import datetime
import mysql.connector
import subprocess


mydb = mysql.connector.connect(
    host="localhost",
    user="datenbank",
    passwd="rasp",
    database="datenbank"
)


def begrenzung_sensor_licht_1():
    mycursor = mydb.cursor()
    sql = "DELETE FROM sensor_licht_1 WHERE zeit < UNIX_TIMESTAMP(DATE_SUB(NOW(), INTERVAL 30 DAY))"
    mycursor.execute(sql)
    mydb.commit()


def begrenzung_sensor_temperatur_1():
    mycursor = mydb.cursor()
    sql = "DELETE FROM sensor_temperatur_1 WHERE zeit < UNIX_TIMESTAMP(DATE_SUB(NOW(), INTERVAL 30 DAY))"
    mycursor.execute(sql)
    mydb.commit()


def begrenzung_sensor_luftfeuchtigkeit_1():
    mycursor = mydb.cursor()
    sql = "DELETE FROM sensor_luftfeuchtigkeit_1 WHERE zeit < UNIX_TIMESTAMP(DATE_SUB(NOW(), INTERVAL 30 DAY))"
    mycursor.execute(sql)
    mydb.commit()


def start_datenbegrenzung():
    begrenzung_sensor_licht_1()
    begrenzung_sensor_temperatur_1()
    begrenzung_sensor_luftfeuchtigkeit_1()
