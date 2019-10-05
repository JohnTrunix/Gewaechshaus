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
			var layer = options.length - index;
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
			$(this).css("top", 2 * index + "px");
			$(this).css("width", 230 - 2 * index);
			$(this).css("margin-left", -115 + index);
		});
	}

	$(".option").bind("click", select);

	function select() {
		if ($("#select-dropdown").hasClass("open")) {
			var selection = $(this).text();
			$("#select-default").text(selection);
			var data = $(this).data("id");

			window.dropdown = data;
			selected_slot();

			collapse();
		} else {
			expand();
		}
	}

	collapse();
});

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

function selected_slot() {
	value = window.dropdown;
	document.getElementById("parameter_slot").value = value;
	parameter_name = document.getElementById("select-default").innerHTML;
	document.getElementById("parameter_name").value = parameter_name;
	document.getElementById("temperatur").innerHTML =
		"Temperatur: " + array_parameter[value - 1].temperatur;
	document.getElementById("lichtstunden").innerHTML =
		"Licht pro Tag: " + array_parameter[value - 1].lichtstunden;
	document.getElementById("wassermenge").innerHTML =
		"Wasser pro Tag: " + array_parameter[value - 1].wassermenge;
	document.getElementById("luftfeuchtigkeit").innerHTML =
		"Luftfeuchtigkeit: " + array_parameter[value - 1].luftfeuchtigkeit;
}

get_parameter();
