// Lese die neuesten Fehlermeldungen
//======================================================================
function download() {
	var display = document.getElementById("meldungen");
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open("GET", "/api/api.php?fehlermeldungen_read");
	xmlhttp.setRequestHeader(
		"Content-Type",
		"application/x-www-form-urlencoded"
	);
	xmlhttp.send();
	xmlhttp.onreadystatechange = function() {
		if (this.readyState === 4 && this.status === 200) {
			display.innerHTML = this.responseText;
		} else {
			display.innerHTML = "0";
		}
	};
}
//======================================================================

// Fehlermeldungen im 5s Takt downloaden.
//======================================================================
function fehlermeldungen_download() {
	download();
	setTimeout(fehlermeldungen_download, 5000);
}
fehlermeldungen_download();
//======================================================================
