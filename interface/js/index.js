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

function sensorwert_download() {
	lichtstaerke_download();
	luftfeuchtigkeit_download();
	temperatur_download();
	bodenfeuchtigkeit_download();
	setTimeout(sensorwert_download, 5000);
}
sensorwert_download();

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

// Minimales Datum für die Datumsauswahl in HTML.
//======================================================================
function get_minimum_date() {
	now = new Date();
	minimum_date = now.toISOString().substring(0, 10);
	document.getElementById("programm_datum_ende").min = minimum_date;
	return minimum_date;
}
//======================================================================

// Starte den Countdown mit der definierten input_datumzeit.
//======================================================================
function start_countdown(input_datumzeit) {
	formatiertes_datum = formatiere_datum(input_datumzeit);

	var countDownDate = new Date(formatiertes_datum);

	var x = setInterval(function() {
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
		var zeit_verbleibend = zeitrechner(input_endzeit, zeit_jetzt, 1);
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

// get_parameter liest alle relevanten Daten durch die API aus der Datenbank.
//======================================================================
function get_parameter() {
	// Neuer XMLHttpRequest erstellen
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "/api/api.php?parameter_read", true);
	xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

	// Wenn Bereit --> XMLHttpRequest ausführen
	xhr.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			array_parameter = JSON.parse(xhr.responseText);
			return array_parameter;
		}
	};

	xhr.send();
}
get_parameter();
//======================================================================

// set_dropdown_names schreibt die Slotnamen in das HTML Dropdown
//======================================================================
function set_dropdown_names() {
	document.getElementById("slot1").innerHTML = array_parameter[0].pflanze;
	document.getElementById("slot2").innerHTML = array_parameter[1].pflanze;
	document.getElementById("slot3").innerHTML = array_parameter[2].pflanze;
	document.getElementById("slot4").innerHTML = array_parameter[3].pflanze;
	document.getElementById("slot5").innerHTML = array_parameter[4].pflanze;
	document.getElementById("slot6").innerHTML = array_parameter[5].pflanze;
	document.getElementById("slot7").innerHTML = array_parameter[6].pflanze;
	document.getElementById("slot8").innerHTML = array_parameter[7].pflanze;
	document.getElementById("slot9").innerHTML = array_parameter[8].pflanze;
	document.getElementById("slot10").innerHTML = array_parameter[9].pflanze;
}
//======================================================================

// Die Funktion selected_slot ist für alle allgemeinen Zuweisungen von Parameterdaten zuständig.
//======================================================================
function selected_slot(slot) {
	parameter_slot = slot;
	parameter_name = array_parameter[slot - 1].pflanze;
	parameter_temperatur = array_parameter[slot - 1].temperatur;
	parameter_lichtstunden = array_parameter[slot - 1].lichtstunden;
	parameter_wassermenge = array_parameter[slot - 1].wassermenge;
	parameter_luftfeuchtigkeit = array_parameter[slot - 1].luftfeuchtigkeit;

	document.getElementById("parameter_slot").value = parameter_slot;

	document.getElementById("temperatur").innerHTML =
		parameter_temperatur + "°C";
	document.getElementById("lichtstunden").innerHTML =
		parameter_lichtstunden + "h";
	document.getElementById("wassermenge").innerHTML =
		parameter_wassermenge + "l";
	document.getElementById("luftfeuchtigkeit").innerHTML =
		parameter_luftfeuchtigkeit + "%";
}
//======================================================================

// Wenn Betriebsmodus Start werden hier die aktiven Parameter gesetzt.
//======================================================================
function get_active_parameter(slot) {
	parameter_slot = slot;
	parameter_name = array_parameter[slot - 1].pflanze;
	active_temperatur = array_parameter[slot - 1].temperatur;
	active_lichtstunden = array_parameter[slot - 1].lichtstunden;
	active_wassermenge = array_parameter[slot - 1].wassermenge;
	active_luftfeuchtigkeit = array_parameter[slot - 1].luftfeuchtigkeit;

	document.getElementById("betriebswahl_name").innerHTML = parameter_slot;
	document.getElementById("betriebswahl_slot").innerHTML = parameter_name;

	document.getElementById("act_param_temperatur").innerHTML =
		active_temperatur + "°C";
	document.getElementById("act_param_lichtstunden").innerHTML =
		active_lichtstunden + "h";
	document.getElementById("act_param_wassermenge").innerHTML =
		active_wassermenge + "l";
	document.getElementById("act_param_luftfeuchtigkeit").innerHTML =
		active_luftfeuchtigkeit + "%";

	document.getElementById("betriebswahl_datetime").innerHTML = datetime;
	document.getElementById(
		"betriebswahl_programm_ende"
	).innerHTML = programm_ende;
}
//======================================================================

// get_betriebsmodus liest alle relevanten Daten durch die API aus der Datenbank.
//======================================================================
function get_betriebsmodus() {
	// Neuer XMLHttpRequest erstellen
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "/api/api.php?betriebsmodus_read", true);
	xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

	// Wenn Bereit --> XMLHttpRequest ausführen
	xhr.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			// JSON Response.
			array_betriebsmodus = JSON.parse(xhr.responseText);
			// JSON Daten Variablen zuweisen.
			parameter_slot = array_betriebsmodus[0].parameter_slot;
			programm_status = array_betriebsmodus[0].programm_status;
			datetime = array_betriebsmodus[0].datetime;
			programm_datum_ende = array_betriebsmodus[0].programm_datum_ende;
			programm_zeit_ende = array_betriebsmodus[0].programm_zeit_ende;
			programm_ende = programm_datum_ende + " " + programm_zeit_ende;
			// Weitere Funktionen ausführen.
			start_countdown(programm_ende);
			balken_berechnung(datetime, programm_ende);
			betriebsmodus_display(programm_status);
		}
	};

	xhr.send();
}
//======================================================================

// Die Funktion aktueller_betriebsmodus regelt ob das Start Stop Verhalten.
//======================================================================
function betriebsmodus_display(programm_status) {
	if (programm_status == "1") {
		document.getElementById("start").style.display = "none";
		document.getElementById("stop").style.display = "inline";
		get_active_parameter(parameter_slot);
	} else if (programm_status == "0") {
		document.getElementById("start").style.display = "inline";
		document.getElementById("stop").style.display = "none";
		set_dropdown_names();
	} else {
		document.getElementById("start").style.display = "inline";
		document.getElementById("stop").style.display = "none";
	}
}
//======================================================================

get_betriebsmodus();
get_minimum_date();
