// Die Datei parameter.js kommuniziert über die API mit der Datenbank und liest
// alle relevanten Parameterdaten für die Datei einstellungen.html aus.

// Sobald ein Slot gewählt wurde die Parameterdaten anfordern.
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

// Steuerung für Slider 1 [Temperatur]
//======================================================================
var slider_1 = document.getElementById("temperatur");
var output_1 = document.getElementById("wert_temperatur");
output_1.innerHTML = slider_1.value;

slider_1.oninput = function() {
	output_1.innerHTML = this.value;
};
//======================================================================

// Steuerung für Slider 2 [Lichtstunden]
//======================================================================
var slider_2 = document.getElementById("lichtstunden");
var output_2 = document.getElementById("wert_lichtstunden");
output_2.innerHTML = slider_2.value;

slider_2.oninput = function() {
	output_2.innerHTML = this.value;
};
//======================================================================

// Steuerung für Slider 3 [Wassermenge]
//======================================================================
var slider_3 = document.getElementById("wassermenge");
var output_3 = document.getElementById("wert_wassermenge");
output_3.innerHTML = slider_3.value;

slider_3.oninput = function() {
	output_3.innerHTML = this.value;
};

// Steuerung für Slider 4 [Luftfeuchtigkeit]
//======================================================================
var slider_4 = document.getElementById("luftfeuchtigkeit");
var output_4 = document.getElementById("wert_luftfeuchtigkeit");
output_4.innerHTML = slider_4.value;

slider_4.oninput = function() {
	output_4.innerHTML = this.value;
};
//======================================================================
