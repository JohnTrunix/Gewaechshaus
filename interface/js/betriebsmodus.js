// Die Datei Betriebsmodus kommuniziert mit der API
// und liest alle aktuellen Daten zum Betriebsmodus aus.

// get_betriebsmodus liest alle relevanten Betriebsmodus Daten durch die API aus der Datenbank.
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
			parameter_name = array_betriebsmodus[0].parameter_name;
			programm_status = array_betriebsmodus[0].programm_status;
			datetime = array_betriebsmodus[0].datetime;
			programm_datum_ende = array_betriebsmodus[0].programm_datum_ende;
			programm_zeit_ende = array_betriebsmodus[0].programm_zeit_ende;
			programm_ende = programm_datum_ende + " " + programm_zeit_ende;
			// Weitere Funktionen ausführen.
			set_betriebsmodus(
				parameter_slot,
				parameter_name,
				datetime,
				programm_ende
			);
			start_countdown(programm_ende);
			balken_berechnung(datetime, programm_ende);
			betriebsmodus_display(programm_status);
		}
	};

	xhr.send();
}
//======================================================================

// Die Funktion aktueller_betriebsmodus regelt ob das Start oder Stop Display angezeigt werden soll.
//======================================================================
function betriebsmodus_display(programm_status) {
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

// Die Funktion set_betriebsmodus ist für alle allgemeinen Zuweisungen von Betriebsmodus Daten zuständig.
//======================================================================
function set_betriebsmodus(
	parameter_slot,
	parameter_name,
	datetime,
	programm_ende
) {
	document.getElementById("betriebswahl_slot").innerHTML =
		"Gewählter Slot: " + parameter_slot;
	document.getElementById("betriebswahl_name").innerHTML =
		"Aktuelles Programm: " + parameter_name;
	document.getElementById("betriebswahl_datetime").innerHTML = datetime;
	document.getElementById(
		"betriebswahl_programm_ende"
	).innerHTML = programm_ende;
}
//======================================================================
