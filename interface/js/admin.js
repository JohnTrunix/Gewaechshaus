function datumzeit(id) {
	date = new Date();
	year = date.getFullYear();
	month = date.getMonth();
	months = new Array(
		"Januar",
		"Februar",
		"März",
		"April",
		"Mai",
		"Juni",
		"Juli",
		"August",
		"September",
		"Oktober",
		"November",
		"Dezember"
	);
	d = date.getDate();
	day = date.getDay();
	days = new Array(
		"Sonntag",
		"Montag",
		"Dienstag",
		"Mittwoch",
		"Donnerstag",
		"Freitag",
		"Samstag"
	);
	h = date.getHours();
	if (h < 10) {
		h = "0" + h;
	}
	m = date.getMinutes();
	if (m < 10) {
		m = "0" + m;
	}
	s = date.getSeconds();
	if (s < 10) {
		s = "0" + s;
	}
	result = d + " " + months[month] + " " + year + " " + h + ":" + m + ":" + s;
	document.getElementById(id).innerHTML = result;
	setTimeout('datumzeit("' + id + '");', "1000");
	return true;
}

function get_betriebsmeldungen() {
	var display = document.getElementById("meldungen");
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open("GET", "/api/api.php?betriebsmeldungen_read");
	xmlhttp.setRequestHeader(
		"Content-Type",
		"application/x-www-form-urlencoded"
	);
	xmlhttp.send();
	xmlhttp.onreadystatechange = function() {
		if (this.readyState === 4 && this.status === 200) {
			display.innerHTML = this.responseText;
		} else {
			display.innerHTML = "0";
		}
	};
}

function get_gewaechshaus_status() {
	var display = document.getElementById("gewaechshaus_status");
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open("GET", "/api/api.php?gewaechshaus_status_read");
	xmlhttp.setRequestHeader(
		"Content-Type",
		"application/x-www-form-urlencoded"
	);
	xmlhttp.send();
	xmlhttp.onreadystatechange = function() {
		if (this.readyState === 4 && this.status === 200) {
			display.innerHTML = this.responseText;
		} else {
			display.innerHTML = "0";
		}
	};
}

function get_bussystem_status() {
	var display = document.getElementById("bussystem_status");
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open("GET", "/api/api.php?bussystem_status_read");
	xmlhttp.setRequestHeader(
		"Content-Type",
		"application/x-www-form-urlencoded"
	);
	xmlhttp.send();
	xmlhttp.onreadystatechange = function() {
		if (this.readyState === 4 && this.status === 200) {
			display.innerHTML = this.responseText;
		} else {
			display.innerHTML = "0";
		}
	};
}

function admin_download() {
	get_betriebsmeldungen();
	get_gewaechshaus_status();
	get_bussystem_status();
	setTimeout(get_betriebsmeldungen, 5000);
	setTimeout(get_gewaechshaus_status, 5000);
	setTimeout(get_bussystem_status, 5000);
}
admin_download();

function systemuebersicht() {
	var systemuebersicht = document.getElementById("systemuebersicht");
	var betriebsmeldungen = document.getElementById("betriebsmeldungen");
	var manuelle_aktorsteuerung = document.getElementById("aktorsteuerung");
	systemuebersicht.style.display = "initial";
	betriebsmeldungen.style.display = "none";
	manuelle_aktorsteuerung.style.display = "none";
}

function betriebsmeldungen() {
	var systemuebersicht = document.getElementById("systemuebersicht");
	var betriebsmeldungen = document.getElementById("betriebsmeldungen");
	var manuelle_aktorsteuerung = document.getElementById("aktorsteuerung");
	systemuebersicht.style.display = "none";
	betriebsmeldungen.style.display = "initial";
	manuelle_aktorsteuerung.style.display = "none";
}

function manuelle_aktorsteuerung() {
	var systemuebersicht = document.getElementById("systemuebersicht");
	var betriebsmeldungen = document.getElementById("betriebsmeldungen");
	var manuelle_aktorsteuerung = document.getElementById("aktorsteuerung");
	systemuebersicht.style.display = "none";
	betriebsmeldungen.style.display = "none";
	manuelle_aktorsteuerung.style.display = "initial";
}

function aktor_steuern(aktor) {
	jQuery.ajax({
		type: "POST",
		url: "/api/api.php?aktor_steuern",
		data: {
			aktor_wahl: aktor
		}
	});
}
