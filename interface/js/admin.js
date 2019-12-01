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
