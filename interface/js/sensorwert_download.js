// In der Datei sensorwert_download befinden sich die Funktionen
// um mit der API die neuesten Sensorwerte zu lesen.

// Lese die neueste Lichtstärke
//======================================================================
function lichtstaerke_download() {
	var display = document.getElementById("lichtstaerke_wert");
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open("GET", "/api/api.php?lichtstaerke_read");
	xmlhttp.setRequestHeader(
		"Content-Type",
		"application/x-www-form-urlencoded"
	);
	xmlhttp.send();
	xmlhttp.onreadystatechange = function() {
		if (this.readyState === 4 && this.status === 200) {
			display.innerHTML = this.responseText + " Lux";
		} else {
			display.innerHTML = "0";
		}
	};
}
//======================================================================

// Lese die neueste Luftfeuchtigkeit
//======================================================================
function luftfeuchtigkeit_download() {
	var display = document.getElementById("luftfeuchtigkeit_wert");
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open("GET", "/api/api.php?luftfeuchtigkeit_read");
	xmlhttp.setRequestHeader(
		"Content-Type",
		"application/x-www-form-urlencoded"
	);
	xmlhttp.send();
	xmlhttp.onreadystatechange = function() {
		if (this.readyState === 4 && this.status === 200) {
			display.innerHTML = this.responseText + " %";
		} else {
			display.innerHTML = "0";
		}
	};
}
//======================================================================

// Lese die neueste Temperatur
//======================================================================
function temperatur_download() {
	var display = document.getElementById("temperatur_wert");
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open("GET", "/api/api.php?temperatur_read");
	xmlhttp.setRequestHeader(
		"Content-Type",
		"application/x-www-form-urlencoded"
	);
	xmlhttp.send();
	xmlhttp.onreadystatechange = function() {
		if (this.readyState === 4 && this.status === 200) {
			display.innerHTML = this.responseText + " °C";
		} else {
			display.innerHTML = "0";
		}
	};
}
//======================================================================

// Lese die neueste Bodenfeuchtigkeit
//======================================================================
function bodenfeuchtigkeit_download() {
	var display = document.getElementById("bodenfeuchtigkeit_wert");
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open("GET", "/api/api.php?bodenfeuchtigkeit_read");
	xmlhttp.setRequestHeader(
		"Content-Type",
		"application/x-www-form-urlencoded"
	);
	xmlhttp.send();
	xmlhttp.onreadystatechange = function() {
		if (this.readyState === 4 && this.status === 200) {
			display.innerHTML = this.responseText + " %";
		} else {
			display.innerHTML = "0";
		}
	};
}
//======================================================================

// Alle download Funktionen im 5s Takt ausführen.
function sensorwert_download() {
	lichtstaerke_download();
	luftfeuchtigkeit_download();
	temperatur_download();
	bodenfeuchtigkeit_download();
	setTimeout(sensorwert_download, 5000);
}
sensorwert_download();
//======================================================================
