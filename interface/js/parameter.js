// Die Datei parameter.js kommuniziert über die API mit der Datenbank und liest
// alle relevanten Parameterdaten für die Datei index.html aus.

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
	document.getElementById("parameter_name").value = parameter_name;

	document.getElementById("temperatur").innerHTML =
		"Temperatur: " + parameter_temperatur;
	document.getElementById("lichtstunden").innerHTML =
		"Licht pro Tag: " + parameter_lichtstunden;
	document.getElementById("wassermenge").innerHTML =
		"Wasser pro Tag: " + parameter_wassermenge;
	document.getElementById("luftfeuchtigkeit").innerHTML =
		"Luftfeuchtigkeit: " + parameter_luftfeuchtigkeit;
}
//======================================================================

// Wenn Betriebsmodus Start werden hier die aktiven Parameter gesetzt.
//======================================================================
function get_active_parameter(slot) {
	active_temperatur = array_parameter[slot - 1].temperatur;
	active_lichtstunden = array_parameter[slot - 1].lichtstunden;
	active_wassermenge = array_parameter[slot - 1].wassermenge;
	active_luftfeuchtigkeit = array_parameter[slot - 1].luftfeuchtigkeit;

	document.getElementById("act_param_temperatur").innerHTML =
		"Temperatur: " + active_temperatur;
	document.getElementById("act_param_lichtstunden").innerHTML =
		"Licht pro Tag: " + active_lichtstunden;
	document.getElementById("act_param_wassermenge").innerHTML =
		"Wasser pro Tag: " + active_wassermenge;
	document.getElementById("act_param_luftfeuchtigkeit").innerHTML =
		"Luftfeuchtigkeit: " + active_luftfeuchtigkeit;
}
//======================================================================
