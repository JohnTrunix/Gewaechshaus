function get_parameter() {
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "/api/api.php?parameter_read", true);
	xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

	xhr.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			array_parameter = JSON.parse(xhr.responseText);
			set_dropdown_names();
		}
	};

	xhr.send();
}
get_parameter();

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

function selected_slot(dropdown) {
	parameter_slot = dropdown;
	parameter_name = array_parameter[dropdown - 1].pflanze;
	parameter_temperatur = array_parameter[dropdown - 1].temperatur;
	parameter_lichtstunden = array_parameter[dropdown - 1].lichtstunden;
	parameter_wassermenge = array_parameter[dropdown - 1].wassermenge;
	parameter_luftfeuchtigkeit = array_parameter[dropdown - 1].luftfeuchtigkeit;

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
