var url = window.location.href;
if (url.search("fehler") > 0) {
	display_message();
}

function display_message() {
	var x = document.getElementById("error_message");
	x.className = "show";
	setTimeout(function() {
		x.className = x.className.replace("show", "");
	}, 2800);
}
