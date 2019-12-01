// Lese die neuesten Betriebsmeldungen
//======================================================================
function download() {
	var display = document.getElementById("meldungen");
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open("GET", "/api/api.php?betriebsmeldungen_read");
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

// Betriebsmeldungen im 5s Takt downloaden.
//======================================================================
function betriebsmeldungen_download() {
	download();
	setTimeout(betriebsmeldungen_download, 5000);
}
betriebsmeldungen_download();
//======================================================================
