// Betriebsmodus von API anfordern
//======================================================================
function get_betriebsmodus() {
	jQuery.ajax({
		type: "GET",
		url: "/api/api.php?betriebsmodus_read",
		success: function(response) {
			daten_betriebsmodus = JSON.parse(response);
			get_parameter();
		},
		error: function() {
			display_message("fehler");
		}
	});
}
get_betriebsmodus();
//======================================================================

// Parameter von API anfordern
//======================================================================
function get_parameter() {
	jQuery.ajax({
		type: "GET",
		url: "/api/api.php?parameter_read",
		success: function(response) {
			daten_parameter = JSON.parse(response);
			check_status();
		},
		error: function() {
			display_message("fehler");
		}
	});
}
//======================================================================

function check_status() {
	if (daten_betriebsmodus[0].programm_status == 1) {
		display_status(1);
	} else {
		display_status(0);
		get_minimum_date();
		set_dropdown_names();
	}
}

// Display Steuerung
//======================================================================
function display_status(status) {
	if (status == "1") {
		document.getElementById("start").style.display = "none";
		document.getElementById("stop").style.display = "inline";
	} else {
		document.getElementById("start").style.display = "inline";
		document.getElementById("stop").style.display = "none";
	}
}
//======================================================================

// Minimales Datum für die Datumsauswahl in HTML.
//======================================================================
function get_minimum_date() {
	now = new Date();
	minimum_date = now.toISOString().substring(0, 10);
	document.getElementById("programm_datum_ende").min = minimum_date;
}
//======================================================================

// Parameter Namen in HTML Dropdown einfuegen
//======================================================================
function set_dropdown_names() {
	document.getElementById("slot1").innerHTML = daten_parameter[0].pflanze;
	document.getElementById("slot2").innerHTML = daten_parameter[1].pflanze;
	document.getElementById("slot3").innerHTML = daten_parameter[2].pflanze;
	document.getElementById("slot4").innerHTML = daten_parameter[3].pflanze;
	document.getElementById("slot5").innerHTML = daten_parameter[4].pflanze;
	document.getElementById("slot6").innerHTML = daten_parameter[5].pflanze;
	document.getElementById("slot7").innerHTML = daten_parameter[6].pflanze;
	document.getElementById("slot8").innerHTML = daten_parameter[7].pflanze;
	document.getElementById("slot9").innerHTML = daten_parameter[8].pflanze;
	document.getElementById("slot10").innerHTML = daten_parameter[9].pflanze;
}
//======================================================================

// HTML Dropdown steuerung
//======================================================================
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
			$(this).css("top", 0 * index + "px");
		});
	}
	$(".option").bind("click", select);
	function select() {
		if ($("#select-dropdown").hasClass("open")) {
			var selection = $(this).text();
			$("#select-default").text(selection);
			var data = $(this).data("id");
			window.dropdown = data;
			selected_slot(window.dropdown);
			collapse();
		} else {
			expand();
		}
	}
	collapse();
});
//======================================================================

// Parameterdaten laden wenn in HTML Dropdown ausgewaehlt
//======================================================================
function selected_slot(slot) {
	document.getElementById("parameter_slot").value = slot;
	document.getElementById("temperatur").innerHTML =
		daten_parameter[slot - 1].temperatur + "°C";
	document.getElementById("lichtstunden").innerHTML =
		daten_parameter[slot - 1].lichtstunden + "h";
	document.getElementById("wassermenge").innerHTML =
		daten_parameter[slot - 1].wassermenge + "l";
	document.getElementById("luftfeuchtigkeit").innerHTML =
		daten_parameter[slot - 1].luftfeuchtigkeit + "%";
}
//======================================================================

// Lichtstaerke von API anfordern
//======================================================================
function lichtstaerke_download() {
	var display = document.getElementById("lichtstaerke_wert");
	jQuery.ajax({
		type: "GET",
		url: "/api/api.php?lichtstaerke_read",
		success: function(response) {
			display.innerHTML = response + " Lux";
		},
		error: function() {
			display.innerHTML = "ERR";
		}
	});
}
//======================================================================

// Luftfeuchtigkeit von API anfordern
//======================================================================
function luftfeuchtigkeit_download() {
	var display = document.getElementById("luftfeuchtigkeit_wert");
	jQuery.ajax({
		type: "GET",
		url: "/api/api.php?luftfeuchtigkeit_read",
		success: function(response) {
			display.innerHTML = response + " %";
		},
		error: function() {
			display.innerHTML = "ERR";
		}
	});
}
//======================================================================

// Temperatur von API anfordern
//======================================================================
function temperatur_download() {
	var display = document.getElementById("temperatur_wert");
	jQuery.ajax({
		type: "GET",
		url: "/api/api.php?temperatur_read",
		success: function(response) {
			display.innerHTML = response + " °C";
		},
		error: function() {
			display.innerHTML = "ERR";
		}
	});
}
//======================================================================

// Bodenfeuchtigkeit von API anfordern
//======================================================================
function bodenfeuchtigkeit_download() {
	var display = document.getElementById("bodenfeuchtigkeit_wert");
	jQuery.ajax({
		type: "GET",
		url: "/api/api.php?bodenfeuchtigkeit_read",
		success: function(response) {
			display.innerHTML = response + " %";
		},
		error: function() {
			display.innerHTML = "ERR";
		}
	});
}
//======================================================================

// Sensorwerte im 5s Takt anfordern
//======================================================================
function sensorwert_download() {
	lichtstaerke_download();
	luftfeuchtigkeit_download();
	temperatur_download();
	bodenfeuchtigkeit_download();
	setTimeout(sensorwert_download, 5000);
}
sensorwert_download();
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
