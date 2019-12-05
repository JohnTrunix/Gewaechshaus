// Betriebsmodus von API anfordern
//======================================================================
function get_betriebsmodus() {
	jQuery.ajax({
		type: "GET",
		url: "/api/api.php?betriebsmodus_read",
		success: function(response) {
			daten_betriebsmodus = JSON.parse(response);
			get_parameter();
		},
		error: function() {
			display_message("fehler");
		}
	});
}
get_betriebsmodus();
//======================================================================

// Parameter von API anfordern
//======================================================================
function get_parameter() {
	jQuery.ajax({
		type: "GET",
		url: "/api/api.php?parameter_read",
		success: function(response) {
			daten_parameter = JSON.parse(response);
			check_status();
		},
		error: function() {
			display_message("fehler");
		}
	});
}
//======================================================================

function check_status() {
	if (daten_betriebsmodus[0].programm_status == 1) {
		display_status(1);
		active_program(daten_betriebsmodus[0].parameter_slot);
		start_countdown(
			daten_betriebsmodus[0].programm_datum_ende +
				" " +
				daten_betriebsmodus[0].programm_zeit_ende
		);
	} else {
		display_status(0);
		get_minimum_date();
		set_dropdown_names();
	}
}

// Display Steuerung
//======================================================================
function display_status(status) {
	if (status == "1") {
		document.getElementById("start").style.display = "none";
		document.getElementById("stop").style.display = "inline";
	} else {
		document.getElementById("start").style.display = "inline";
		document.getElementById("stop").style.display = "none";
	}
}
//======================================================================

// Minimales Datum für die Datumsauswahl in HTML.
//======================================================================
function get_minimum_date() {
	now = new Date();
	minimum_date = now.toISOString().substring(0, 10);
	document.getElementById("programm_datum_ende").min = minimum_date;
}
//======================================================================

// Parameter Namen in HTML Dropdown einfuegen
//======================================================================
function set_dropdown_names() {
	document.getElementById("slot1").innerHTML = daten_parameter[0].pflanze;
	document.getElementById("slot2").innerHTML = daten_parameter[1].pflanze;
	document.getElementById("slot3").innerHTML = daten_parameter[2].pflanze;
	document.getElementById("slot4").innerHTML = daten_parameter[3].pflanze;
	document.getElementById("slot5").innerHTML = daten_parameter[4].pflanze;
	document.getElementById("slot6").innerHTML = daten_parameter[5].pflanze;
	document.getElementById("slot7").innerHTML = daten_parameter[6].pflanze;
	document.getElementById("slot8").innerHTML = daten_parameter[7].pflanze;
	document.getElementById("slot9").innerHTML = daten_parameter[8].pflanze;
	document.getElementById("slot10").innerHTML = daten_parameter[9].pflanze;
}
//======================================================================

// HTML Dropdown steuerung
//======================================================================
$(document).ready(function() {
	$("#select-default").bind("click", toggle);
	function toggle() {
		if ($("#select-dropdown").hasClass("open")) {
			collapse();
		} else {
			expand();
		}
	}
	function expand() {
		$("#select-dropdown")
			.removeClass("closed")
			.addClass("open");
		options = $(".select");
		options.each(function(index) {
			$(this).css("top", 40 * index + "px");
			$(this).css("width", 230);
			$(this).css("margin-left", -115);
		});
	}
	function collapse() {
		$("#select-dropdown")
			.removeClass("open")
			.addClass("closed");
		options = $(".select");
		options.each(function(index) {
			var layer = options.length - index;
			$(this).css("z-index", layer);
			$(this).css("top", 0 * index + "px");
		});
	}
	$(".option").bind("click", select);
	function select() {
		if ($("#select-dropdown").hasClass("open")) {
			var selection = $(this).text();
			$("#select-default").text(selection);
			var data = $(this).data("id");
			window.dropdown = data;
			selected_slot(window.dropdown);
			collapse();
		} else {
			expand();
		}
	}
	collapse();
});
//======================================================================

// Parameterdaten laden wenn in HTML Dropdown ausgewaehlt
//======================================================================
function selected_slot(slot) {
	document.getElementById("parameter_slot").value = slot;
	document.getElementById("temperatur").innerHTML =
		daten_parameter[slot - 1].temperatur + "°C";
	document.getElementById("lichtstunden").innerHTML =
		daten_parameter[slot - 1].lichtstunden + "h";
	document.getElementById("wassermenge").innerHTML =
		daten_parameter[slot - 1].wassermenge + "l";
	document.getElementById("luftfeuchtigkeit").innerHTML =
		daten_parameter[slot - 1].luftfeuchtigkeit + "%";
}
//======================================================================

// Aktuelle Programmdaten laden
//======================================================================
function active_program(slot) {
	document.getElementById("betriebswahl_name").innerHTML = slot;
	document.getElementById("betriebswahl_slot").innerHTML =
		daten_parameter[slot - 1].pflanze;

	document.getElementById("act_param_temperatur").innerHTML =
		daten_parameter[slot - 1].temperatur + "°C";
	document.getElementById("act_param_lichtstunden").innerHTML =
		daten_parameter[slot - 1].lichtstunden + "h";
	document.getElementById("act_param_wassermenge").innerHTML =
		daten_parameter[slot - 1].wassermenge + "l";
	document.getElementById("act_param_luftfeuchtigkeit").innerHTML =
		daten_parameter[slot - 1].luftfeuchtigkeit + "%";

	document.getElementById("betriebswahl_datetime").innerHTML =
		daten_betriebsmodus[0].datetime;
	document.getElementById("betriebswahl_programm_ende").innerHTML =
		daten_betriebsmodus[0].programm_datum_ende +
		" " +
		daten_betriebsmodus[0].programm_zeit_ende;
}
//======================================================================

// Starte den Countdown mit der definierten input_datumzeit.
//======================================================================
function start_countdown(input_datumzeit) {
	formatiertes_datum = formatiere_datum(input_datumzeit);
	var countDownDate = new Date(formatiertes_datum);
	setInterval(function() {
		var now = new Date().getTime();
		var distance = countDownDate - now;
		var days = Math.floor(distance / (1000 * 60 * 60 * 24));
		var hours = Math.floor(
			(distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
		);
		var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
		var seconds = Math.floor((distance % (1000 * 60)) / 1000);
		if (days > 0) {
			document.getElementById("countdown").innerHTML =
				days + "t " + hours + "h " + minutes + "m " + seconds + "s ";
		} else if (days == 0 && hours > 0) {
			document.getElementById("countdown").innerHTML =
				hours + "h " + minutes + "m " + seconds + "s ";
		} else if (hours == 0 && minutes > 0) {
			document.getElementById("countdown").innerHTML =
				minutes + "m " + seconds + "s ";
		} else if (minutes == 0) {
			document.getElementById("countdown").innerHTML = seconds + "s ";
		} else {
			document.getElementById("countdown").innerHTML = "";
		}
	}, 1000);
}
//======================================================================

// Gibt die aktuelle Datumzeit aus. z.b ["2019-10-29 21:02:21"]
//======================================================================
function datumzeit_jetzt() {
	var date = new Date();
	var aaaa = date.getFullYear();
	var gg = date.getDate();
	var mm = date.getMonth() + 1;

	if (gg < 10) gg = "0" + gg;

	if (mm < 10) mm = "0" + mm;

	var cur_day = aaaa + "-" + mm + "-" + gg;

	var hours = date.getHours();
	var minutes = date.getMinutes();
	var seconds = date.getSeconds();

	if (hours < 10) hours = "0" + hours;

	if (minutes < 10) minutes = "0" + minutes;

	if (seconds < 10) seconds = "0" + seconds;

	return cur_day + " " + hours + ":" + minutes + ":" + seconds;
}
//======================================================================

// Formatiert das Datum in ein anderes Format. z.B von ["2019-10-29 20:32:34"] nach ["10 29, 2019 20:32:34"]
//======================================================================
function formatiere_datum(datum) {
	var datum;

	var input_zeit = datum.substr(-8);
	var input_jahr = datum.substr(0, 4);
	var input_monat = datum.substr(5, 2);
	var input_tag = datum.substr(8, 2);

	var datum_formatiert =
		input_monat +
		" " +
		input_tag +
		"," +
		" " +
		input_jahr +
		" " +
		input_zeit;

	return datum_formatiert;
}
//======================================================================

// Gibt den Zeitunterschied zwischen 2 Datumzeit Angaben und einem Teiler an. z.B ["2019-10-29 21:10:00"], ["2019-10-29 21:11:00"] und Teiler 1 --> 60 Sekunden
//======================================================================
function zeitrechner(input_datumzeit1, input_datumzeit2, teiler) {
	formatiertes_datum1 = formatiere_datum(input_datumzeit1);
	formatiertes_datum2 = formatiere_datum(input_datumzeit2);
	var teiler;

	var date1, date2;
	date1 = new Date(formatiertes_datum1);
	date2 = new Date(formatiertes_datum2);
	var seconds = Math.abs(date1 - date2) / 1000;

	var ergebnis = seconds / teiler;
	return ergebnis;
}
//======================================================================

// Berechnet die Verbleibende Zeit in Sekunden, bis eine Ziel Datumzeit erreicht wird. z.B ["2019-10-29 21:10:00"]
//======================================================================
function berechne_zeit_verbleibend(input_endzeit) {
	var input_endzeit;
	var zeit_jetzt = datumzeit_jetzt();

	if (input_endzeit < zeit_jetzt) {
		return 0;
	} else if (input_endzeit > zeit_jetzt) {
		var zeit_verbleibend = zeitrechner(input_endzeit, zeit_jetzt, 1) - 1;
		return zeit_verbleibend;
	} else {
		return 0;
	}
}
//======================================================================

// Berechnet den aktuellen % Forschritt zwischen 2 Datumzeit Angaben. z.B ["2019-10-29 21:10:00"], ["2019-10-29 21:11:00"]
//======================================================================
function berechne_prozent_verbleibend(input_startzeit, input_endzeit) {
	var input_startzeit, input_endzeit;

	var zeit_verbleibend = berechne_zeit_verbleibend(input_endzeit);

	var zeit_gesamt = zeitrechner(input_startzeit, input_endzeit, 1);

	var ein_prozent = zeit_gesamt / 100;
	var prozent_gesamt = zeit_verbleibend / ein_prozent;
	var prozent_resultat = 100 - prozent_gesamt;
	var prozent_gerundet = Math.round(prozent_resultat);

	if (prozent_gerundet <= 2) {
		return 2 + "%";
	} else {
		return prozent_gerundet + "%";
	}
}
//======================================================================

// Bei 100% das Programm stoppen.
//======================================================================
function programm_fertig() {
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open("GET", "/api/api.php?betriebsmodus_stop_write");
	xmlhttp.setRequestHeader(
		"Content-Type",
		"application/x-www-form-urlencoded"
	);
	xmlhttp.send();
}
//======================================================================

// Berechnet den aktuellen Forschritt des Balkens auf der Startseite.
//======================================================================
function balken_berechnung(datetime, programm_ende) {
	var datetime, programm_ende;
	setInterval(function() {
		var prozent_verbleibend = berechne_prozent_verbleibend(
			datetime,
			programm_ende
		);
		var str = prozent_verbleibend;
		var prozent = str.substring(0, str.length - 1);

		document.getElementById(
			"prozent_fortschritt"
		).style.width = prozent_verbleibend;
		document.getElementById(
			"prozent_jetzt"
		).innerHTML = prozent_verbleibend;

		if (prozent < 5) {
			document.getElementById("prozent_jetzt").style.display = "none";
		} else if (prozent > 5 && prozent != 100) {
			document.getElementById("prozent_jetzt").style.display = "flex";
		} else if (prozent == 100) {
			document.getElementById("prozent_meter").style.backgroundColor =
				"#364366";
			document.getElementById("prozent_fortschritt").style.background =
				"transparent";
			document.getElementById("text_fertig").style.display = "block";
			document.getElementById("prozent_jetzt").style.display = "none";
			document.getElementById("button_abbrechen").style.color = "#364366";
			document.getElementById("button_abbrechen").style.borderColor =
				"#364366";
			document.getElementById("button_abbrechen").value = "Startseite";
			programm_fertig();
		}
	}, 1000);
}
//======================================================================

// Lichtstaerke von API anfordern
//======================================================================
function lichtstaerke_download() {
	var display = document.getElementById("lichtstaerke_wert");
	jQuery.ajax({
		type: "GET",
		url: "/api/api.php?lichtstaerke_read",
		success: function(response) {
			display.innerHTML = response + " Lux";
		},
		error: function() {
			display.innerHTML = "ERR";
		}
	});
}
//======================================================================

// Luftfeuchtigkeit von API anfordern
//======================================================================
function luftfeuchtigkeit_download() {
	var display = document.getElementById("luftfeuchtigkeit_wert");
	jQuery.ajax({
		type: "GET",
		url: "/api/api.php?luftfeuchtigkeit_read",
		success: function(response) {
			display.innerHTML = response + " %";
		},
		error: function() {
			display.innerHTML = "ERR";
		}
	});
}
//======================================================================

// Temperatur von API anfordern
//======================================================================
function temperatur_download() {
	var display = document.getElementById("temperatur_wert");
	jQuery.ajax({
		type: "GET",
		url: "/api/api.php?temperatur_read",
		success: function(response) {
			display.innerHTML = response + " °C";
		},
		error: function() {
			display.innerHTML = "ERR";
		}
	});
}
//======================================================================

// Bodenfeuchtigkeit von API anfordern
//======================================================================
function bodenfeuchtigkeit_download() {
	var display = document.getElementById("bodenfeuchtigkeit_wert");
	jQuery.ajax({
		type: "GET",
		url: "/api/api.php?bodenfeuchtigkeit_read",
		success: function(response) {
			display.innerHTML = response + " %";
		},
		error: function() {
			display.innerHTML = "ERR";
		}
	});
}
//======================================================================

// Sensorwerte im 5s Takt anfordern
//======================================================================
function sensorwert_download() {
	lichtstaerke_download();
	luftfeuchtigkeit_download();
	temperatur_download();
	bodenfeuchtigkeit_download();
	setTimeout(sensorwert_download, 5000);
}
sensorwert_download();
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
