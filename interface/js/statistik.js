function get_ip_address() {
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "/api/api.php?ip_adresse_read", true);
	xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhr.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			document.getElementById("iframe").src =
				"http://" +
				xhr.responseText +
				":3000/d/FLXpjTtWk/sensorwerte?orgId=1&kiosk=tv";
		}
	};

	xhr.send();
}
get_ip_address();
