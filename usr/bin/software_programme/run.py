import abfrage
import rtc_zeit


try:
    connection_check()
except:
    print("Zeit konnte nicht aktualisiert werden.")


while True:
    try:
        abfrage_start()
    except:
        print("Abfrage konnte nicht ausgeführt werden.")
