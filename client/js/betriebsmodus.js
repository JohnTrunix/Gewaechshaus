function aktueller_betriebsmodus(programm_status) {
	if (programm_status == "start") {
		document.getElementById("start").style.display = "none";
		document.getElementById("stop").style.display = "inline";
	} else if (programm_status == "stop") {
		document.getElementById("start").style.display = "inline";
		document.getElementById("stop").style.display = "none";
	} else {
		document.getElementById("start").style.display = "inline";
		document.getElementById("stop").style.display = "none";
	}
}
