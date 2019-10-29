// dropdown_parameter.js steuert die Logik und Animationen
// des HTML Dropdown.

// Steuerung
//======================================================================

// Sobald die Seite geladen ist -->
$(document).ready(function() {
	// Event Listener auf #select-default
	$("#select-default").bind("click", toggle);

	// Toggle Funktionen
	function toggle() {
		if ($("#select-dropdown").hasClass("open")) {
			collapse();
		} else {
			expand();
		}
	}

	// Menu ausklappen
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

	// Menu einklappen
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

	// Wenn Slot ausgewählt wurde -->
	function select() {
		if ($("#select-dropdown").hasClass("open")) {
			var selection = $(this).text();
			$("#select-default").text(selection);
			var data = $(this).data("id");

			window.dropdown = data;

			// Funktion an parameter.js weiterleiten.
			selected_slot(window.dropdown);

			collapse();
		} else {
			expand();
		}
	}

	collapse();
});
//======================================================================
