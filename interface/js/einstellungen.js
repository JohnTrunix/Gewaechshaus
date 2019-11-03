// Die Datei parameter.js kommuniziert über die API mit der Datenbank und liest
// alle relevanten Parameterdaten für die Datei einstellungen.html aus.

// Sobald ein Slot gewählt wurde die Daten anfordern.
//======================================================================
function selected_slot(selectObject) {
	var slot = selectObject.value;
	parameter_download(slot);

	function parameter_download(slot) {
		value = slot;
		var xhr = new XMLHttpRequest();
		xhr.open("POST", "/api/api.php?parameter_read", true);
		xhr.setRequestHeader(
			"Content-type",
			"application/x-www-form-urlencoded"
		);

		xhr.onreadystatechange = function() {
			if (this.readyState == 4 && this.status == 200) {
				array_parameter = JSON.parse(xhr.responseText);
				document.getElementById("pflanze").value =
					array_parameter[value - 1].pflanze;
				document.getElementById("temperatur").value =
					array_parameter[value - 1].temperatur;
				document.getElementById("lichtstunden").value =
					array_parameter[value - 1].lichtstunden;
				document.getElementById("wassermenge").value =
					array_parameter[value - 1].wassermenge;
				document.getElementById("luftfeuchtigkeit").value =
					array_parameter[value - 1].luftfeuchtigkeit;
				document.getElementById("wert_temperatur").innerHTML =
					array_parameter[value - 1].temperatur;
				document.getElementById("wert_lichtstunden").innerHTML =
					array_parameter[value - 1].lichtstunden;
				document.getElementById("wert_wassermenge").innerHTML =
					array_parameter[value - 1].wassermenge;
				document.getElementById("wert_luftfeuchtigkeit").innerHTML =
					array_parameter[value - 1].luftfeuchtigkeit;
			}
		};

		xhr.send();
	}
}
//======================================================================
