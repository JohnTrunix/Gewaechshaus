// Datum und Uhrzeit als Text ausgeben
//======================================================================
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
window.onload = datumzeit("date_time");
//======================================================================

// Betriebsmeldungen von Datenbank als Text ausgeben
//======================================================================
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
	setTimeout(get_betriebsmeldungen, 5000);
}
get_betriebsmeldungen();
//======================================================================

// Gewaechshaus Status als Text ausgeben
//======================================================================
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
	setTimeout(get_gewaechshaus_status, 5000);
}
get_gewaechshaus_status();
//======================================================================

// Bussystem Status als Text ausgeben
//======================================================================
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
	setTimeout(get_bussystem_status, 5000);
}
get_bussystem_status();
//======================================================================

// HTML Div umschaltfunktionen
//======================================================================
var systemuebersicht_html = document.getElementById("systemuebersicht");
var betriebsmeldungen_html = document.getElementById("betriebsmeldungen");
var manuelle_aktorsteuerung_html = document.getElementById("aktorsteuerung");

function systemuebersicht() {
	systemuebersicht_html.style.display = "initial";
	betriebsmeldungen_html.style.display = "none";
	manuelle_aktorsteuerung_html.style.display = "none";
}

function betriebsmeldungen() {
	systemuebersicht_html.style.display = "none";
	betriebsmeldungen_html.style.display = "initial";
	manuelle_aktorsteuerung_html.style.display = "none";
}

function manuelle_aktorsteuerung() {
	systemuebersicht_html.style.display = "none";
	betriebsmeldungen_html.style.display = "none";
	manuelle_aktorsteuerung_html.style.display = "initial";
}
//======================================================================

// Aktor ansteuern API anforderung
//======================================================================
function aktor_steuern(aktor) {
	jQuery.ajax({
		type: "POST",
		url: "/api/api.php?aktor_steuern",
		data: {
			aktor_wahl: aktor
		}
	});
}
//======================================================================

// IP Adresse von API anfordern
//======================================================================
function get_ip_address() {
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "/api/api.php?ip_adresse_read", true);
	xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhr.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			document.getElementById("ip_adress").innerHTML = xhr.responseText;
		}
	};

	xhr.send();
}
get_ip_address();
//======================================================================

// Display Benachrichtigungen anzeigen
//======================================================================
var url = window.location.href;
if (url.search("fehler") > 0) {
	display_message("fehler");
} else if (url.search("erfolgreich") > 0) {
	display_message("erfolgreich");
}

function display_message(status) {
	var status, x;
	if (status == "fehler") {
		x = document.getElementById("error_message");
	} else if (status == "erfolgreich") {
		x = document.getElementById("success_message");
	}
	x.className = "show";
	setTimeout(function() {
		x.className = x.className.replace("show", "");
	}, 2800);
}
//======================================================================
