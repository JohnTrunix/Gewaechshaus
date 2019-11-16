// In error_message.js wird die Logik und Animation des Error Popup
// gesteuert, welches bei ?fehler in der URL erscheint.

// URL check auf ?fehler
//======================================================================
var url = window.location.href;
if (url.search("fehler") > 0) {
	display_message();
}
//======================================================================

// Steuerung der Animation
//======================================================================
function display_message() {
	var x = document.getElementById("error_message");
	x.className = "show";
	setTimeout(function() {
		x.className = x.className.replace("show", "");
	}, 2800);
}
//======================================================================
