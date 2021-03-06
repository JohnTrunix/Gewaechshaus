// Parameter von Datenbank anfordern
//======================================================================
function get_parameter() {
	jQuery.ajax({
		type: "GET",
		url: "/api/api.php?parameter_read",
		success: function(response) {
			array_parameter = JSON.parse(response);
		},
		error: function() {
			display_message("fehler");
		}
	});
}
get_parameter();
//======================================================================

// Parameterwerte HTML Elementen zuweisen
//======================================================================
function selected_slot(selectObject) {
	var value = selectObject.value;
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
//======================================================================

// Steuerung für Slider1
//======================================================================
var slider_1 = document.getElementById("temperatur");
var output_1 = document.getElementById("wert_temperatur");
output_1.innerHTML = slider_1.value;

slider_1.oninput = function() {
	output_1.innerHTML = this.value;
};
//======================================================================

// Steuerung für Slider2
//======================================================================
var slider_2 = document.getElementById("lichtstunden");
var output_2 = document.getElementById("wert_lichtstunden");
output_2.innerHTML = slider_2.value;

slider_2.oninput = function() {
	output_2.innerHTML = this.value;
};
//======================================================================

// Steuerung für Slider3
//======================================================================
var slider_3 = document.getElementById("wassermenge");
var output_3 = document.getElementById("wert_wassermenge");
output_3.innerHTML = slider_3.value;

slider_3.oninput = function() {
	output_3.innerHTML = this.value;
};
//======================================================================

// Steuerung für Slider4
//======================================================================
var slider_4 = document.getElementById("luftfeuchtigkeit");
var output_4 = document.getElementById("wert_luftfeuchtigkeit");
output_4.innerHTML = slider_4.value;

slider_4.oninput = function() {
	output_4.innerHTML = this.value;
};
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
