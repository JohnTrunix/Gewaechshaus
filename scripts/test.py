from datenbank_abfrage import get_betriebsmodus
from datenbank_abfrage import get_parameter
import datenbank_abfrage


get_betriebsmodus()

if datenbank_abfrage.programm_status == 1:
    get_parameter()
    print(datenbank_abfrage.pflanze)
