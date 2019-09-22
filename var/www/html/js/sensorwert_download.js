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
			display.innerHTML = "0";
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
			display.innerHTML = "0";
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
			display.innerHTML = "0";
		}
	};
}

function bodenfeuchtigkeit_download() {
	var display = document.getElementById("bodenfeuchtigkeit_wert");
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open("GET", "/api/sensorwerte/bodenfeuchtigkeit_download.php");
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

function sensorwert_download() {
	lichtstaerke_download();
	luftfeuchtigkeit_download();
	temperatur_download();
	bodenfeuchtigkeit_download();
	setTimeout(sensorwert_download, 5000);
}
sensorwert_download();
