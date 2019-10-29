function get_parameter() {
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "/api/api.php?parameter_read", true);
	xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

	xhr.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			array_parameter = JSON.parse(xhr.responseText);

			document.getElementById("slot1").innerHTML =
				array_parameter[0].pflanze;

			document.getElementById("slot2").innerHTML =
				array_parameter[1].pflanze;

			document.getElementById("slot3").innerHTML =
				array_parameter[2].pflanze;

			document.getElementById("slot4").innerHTML =
				array_parameter[3].pflanze;

			document.getElementById("slot5").innerHTML =
				array_parameter[4].pflanze;

			document.getElementById("slot6").innerHTML =
				array_parameter[5].pflanze;

			document.getElementById("slot7").innerHTML =
				array_parameter[6].pflanze;

			document.getElementById("slot8").innerHTML =
				array_parameter[7].pflanze;

			document.getElementById("slot9").innerHTML =
				array_parameter[8].pflanze;

			document.getElementById("slot10").innerHTML =
				array_parameter[9].pflanze;
		}
	};

	xhr.send();
}

function selected_slot(slot) {
	document.getElementById("parameter_slot").value = slot;
	parameter_name = document.getElementById("select-default").innerHTML;
	document.getElementById("parameter_name").value = parameter_name;
	document.getElementById("temperatur").innerHTML =
		"Temperatur: " + array_parameter[slot - 1].temperatur;
	document.getElementById("lichtstunden").innerHTML =
		"Licht pro Tag: " + array_parameter[slot - 1].lichtstunden;
	document.getElementById("wassermenge").innerHTML =
		"Wasser pro Tag: " + array_parameter[slot - 1].wassermenge;
	document.getElementById("luftfeuchtigkeit").innerHTML =
		"Luftfeuchtigkeit: " + array_parameter[slot - 1].luftfeuchtigkeit;
}

get_parameter();
