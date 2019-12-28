# Import der Betriebsmeldungsfunktion
# ======================================================================
from betriebsmeldungen import neue_betriebsmeldung
# ======================================================================

# Import von benoetigten Modulen
# ======================================================================
try:
    import mysql.connector
except:
    neue_betriebsmeldung(
        "[datenbank_abfrage] Fehler bei der importierung von Modulen.")
# ======================================================================