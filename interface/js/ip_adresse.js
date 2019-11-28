// Mit der Funktion ip_adresse wird die Grafana Adresse für die Statistik
// und die IP Adresse für das Admin Panel definiert.

//  IP Adresse definieren
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

			var url = window.location.href;
			if (url.search("statistik") > 0) {
				// IP Adresse für die Statistikseite
				document.getElementById("iframe").src =
					"http://" +
					ip_adresse +
					":3000/d/FLXpjTtWk/sensorwerte?orgId=1&kiosk=tv";
			} else if (url.search("admin") > 0) {
				// IP Adresse für das Adminpanel
				document.getElementById("ip_adress").innerHTML = ip_adresse;
			}
		}
	};

	xhr.send();
}
//======================================================================
