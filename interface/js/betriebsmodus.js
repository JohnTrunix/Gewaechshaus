// Die Datei Betriebsmodus kommuniziert mit der API
// und liest alle aktuellen Daten zum Betriebsmodus aus.

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
	if (programm_status == "start") {
		document.getElementById("start").style.display = "none";
		document.getElementById("stop").style.display = "inline";
		get_active_parameter(parameter_slot);
	} else if (programm_status == "stop") {
		document.getElementById("start").style.display = "inline";
		document.getElementById("stop").style.display = "none";
		set_dropdown_names();
	} else {
		document.getElementById("start").style.display = "inline";
		document.getElementById("stop").style.display = "none";
	}
}
//======================================================================
