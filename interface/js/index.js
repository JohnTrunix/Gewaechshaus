// Minimales Datum für die Datumsauswahl in HTML.
//======================================================================
function get_minimum_date() {
	now = new Date();
	minimum_date = now.toISOString().substring(0, 10);
	document.getElementById("programm_datum_ende").min = minimum_date;
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
