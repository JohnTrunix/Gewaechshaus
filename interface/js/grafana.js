function grafana_adresse() {
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "/api/api.php?ip_adresse_read", true);
	xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

	xhr.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			ip_adresse = xhr.responseText;
			document.getElementById("iframe").src =
				"http://" +
				ip_adresse +
				":3000/d/FLXpjTtWk/sensorwerte?orgId=1&kiosk=tv";
			return ip_adresse;
		}
	};

	xhr.send();
}
