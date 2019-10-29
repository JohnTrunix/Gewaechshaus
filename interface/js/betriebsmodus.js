// Die Datei Betriebsmodus kommuniziert mit der API
// und liest alle aktuellen Daten zum Betriebsmodus aus.

// Die Funktion aktueller_betriebsmodus regelt CSS Regeln je nach Status. [Start, Stop]
//======================================================================
function aktueller_betriebsmodus(programm_status) {
	if (programm_status == "start") {
		document.getElementById("start").style.display = "none";
		document.getElementById("stop").style.display = "inline";
	} else if (programm_status == "stop") {
		document.getElementById("start").style.display = "inline";
		document.getElementById("stop").style.display = "none";
	} else {
		document.getElementById("start").style.display = "inline";
		document.getElementById("stop").style.display = "none";
	}
}
//======================================================================

// get_betriebsmodus liest alle relevanten Betriebsmodus Daten durch die API aus der Datenbank.
//======================================================================
function get_betriebsmodus() {
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "/api/api.php?betriebsmodus_read", true);
	xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

	xhr.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			array_betriebsmodus = JSON.parse(xhr.responseText);
			parameter_slot = array_betriebsmodus[0].parameter_slot;
			parameter_name = array_betriebsmodus[0].parameter_name;
			programm_status = array_betriebsmodus[0].programm_status;
			datetime = array_betriebsmodus[0].datetime;
			programm_datum_ende = array_betriebsmodus[0].programm_datum_ende;
			programm_zeit_ende = array_betriebsmodus[0].programm_zeit_ende;
			programm_ende = programm_datum_ende + " " + programm_zeit_ende;
			document.getElementById("betriebswahl_slot").innerHTML =
				"Gewählter Slot: " + parameter_slot;
			document.getElementById("betriebswahl_name").innerHTML =
				"Aktuelles Programm: " + parameter_name;
			document.getElementById(
				"betriebswahl_datetime"
			).innerHTML = datetime;
			document.getElementById(
				"betriebswahl_programm_ende"
			).innerHTML = programm_ende;
			start_countdown(programm_ende);
			balken_berechnung(datetime, programm_ende);
			aktueller_betriebsmodus(programm_status);
		}
	};

	xhr.send();
}
//======================================================================
