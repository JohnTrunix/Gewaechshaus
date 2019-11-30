from fehlermeldungen import neue_fehlermeldung
try:
    import datenbank_abfrage
    import sensor_abfrage
    from ansteuerung_pwm_shield import heizung_ein, heizung_aus, befeuchter_ein, befeuchter_aus, luefter_klein_ein, luefter_klein_aus, grundstellung
except:
    neue_fehlermeldung(
        "[ansteuerung_temp_luft] Fehler bei der importierung von Modulen.")


def start_ansteuerung_temp_luft():
    try:
        if datenbank_abfrage.programm_status == 1:
            if (int(sensor_abfrage.temperatur_gerundet) < int(datenbank_abfrage.temperatur)):
                heizung_ein()
                status_heizung = 1
            elif ((int(sensor_abfrage.temperatur_gerundet) + 2) > int(datenbank_abfrage.temperatur)):
                heizung_aus()
                status_heizung = 0
            else:
                pass

            if (int(sensor_abfrage.luftfeuchtigkeit_gerundet) < int(datenbank_abfrage.luftfeuchtigkeit)):
                befeuchter_ein()
                status_befeuchter = 1
            elif ((int(sensor_abfrage.luftfeuchtigkeit_gerundet) + 5) > int(datenbank_abfrage.luftfeuchtigkeit)):
                befeuchter_aus()
                status_befeuchter = 0
            else:
                pass

            if status_heizung == 1 or status_befeuchter == 1:
                luefter_klein_ein()
            elif status_heizung == 0 and status_befeuchter == 0:
                luefter_klein_aus()
            else:
                pass
        else:
            grundstellung()
    except:
        neue_fehlermeldung(
            "[ansteuerung_temp_luft] Fehler bei der Zyklusberechnung der Heizung und des Befeuchters.")
