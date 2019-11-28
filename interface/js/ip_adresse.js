// Mit der Funktion ip_adresse wird die IFRAME Adresse für die Seite
// Statistik.html generiert. Zudem kann die Ip Adresse abgefragt werden.

//  IP Adresse abfragen und Grafana Adresse definieren
//======================================================================
function ip_adresse() {
	// Neuer XMLHttpRequest erstellen
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "/api/api.php?ip_adresse_read", true);
	xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

	// Wenn Bereit --> XMLHttpRequest ausführen
	xhr.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			// Die empfangene IP Adresse der Variable zuweisen
			ip_adresse = xhr.responseText;

			// Die IFRAME Adresse generieren
			document.getElementById("iframe").src =
				"http://" +
				ip_adresse +
				":3000/d/FLXpjTtWk/sensorwerte?orgId=1&kiosk=tv";
			return ip_adresse;
		}
	};

	xhr.send();
}
//======================================================================
