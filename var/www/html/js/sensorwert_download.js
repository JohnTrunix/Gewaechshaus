function lichtstaerke_download() {
	var display = document.getElementById("lichtstaerke_wert");
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open("GET", "/api/sensorwerte/lichtstaerke_download.php");
	xmlhttp.setRequestHeader(
		"Content-Type",
		"application/x-www-form-urlencoded"
	);
	xmlhttp.send();
	xmlhttp.onreadystatechange = function() {
		if (this.readyState === 4 && this.status === 200) {
			display.innerHTML = this.responseText + " Lux";
		} else {
			display.innerHTML = "Lade...";
		}
	};
}

function luftfeuchtigkeit_download() {
	var display = document.getElementById("luftfeuchtigkeit_wert");
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open("GET", "/api/sensorwerte/luftfeuchtigkeit_download.php");
	xmlhttp.setRequestHeader(
		"Content-Type",
		"application/x-www-form-urlencoded"
	);
	xmlhttp.send();
	xmlhttp.onreadystatechange = function() {
		if (this.readyState === 4 && this.status === 200) {
			display.innerHTML = this.responseText + " %";
		} else {
			display.innerHTML = "Lade...";
		}
	};
}

function temperatur_download() {
	var display = document.getElementById("temperatur_wert");
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open("GET", "/api/sensorwerte/temperatur_download.php");
	xmlhttp.setRequestHeader(
		"Content-Type",
		"application/x-www-form-urlencoded"
	);
	xmlhttp.send();
	xmlhttp.onreadystatechange = function() {
		if (this.readyState === 4 && this.status === 200) {
			display.innerHTML = this.responseText + " °C";
		} else {
			display.innerHTML = "Lade...";
		}
	};
}

function sensorwert_download() {
	lichtstaerke_download();
	luftfeuchtigkeit_download();
	temperatur_download();
	setTimeout(sensorwert_download, 5000);
}
sensorwert_download();
