var now = new Date(),
	minDate = now.toISOString().substring(0, 10);
$("#programm_datum_ende").prop("min", minDate);

function start_countdown(input_datumzeit) {
	formatiertes_datum = formatiere_datum(input_datumzeit);

	var countDownDate = new Date(formatiertes_datum);

	var x = setInterval(function() {
		var now = new Date().getTime();

		var distance = countDownDate - now;

		var days = Math.floor(distance / (1000 * 60 * 60 * 24));
		var hours = Math.floor(
			(distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
		);
		var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
		var seconds = Math.floor((distance % (1000 * 60)) / 1000);

		if (days > 0) {
			document.getElementById("countdown").innerHTML =
				days + "t " + hours + "h " + minutes + "m " + seconds + "s ";
		} else if (days == 0 && hours > 0) {
			document.getElementById("countdown").innerHTML =
				hours + "h " + minutes + "m " + seconds + "s ";
		} else if (hours == 0 && minutes > 0) {
			document.getElementById("countdown").innerHTML =
				minutes + "m " + seconds + "s ";
		} else if (minutes == 0) {
			document.getElementById("countdown").innerHTML = seconds + "s ";
		} else {
			document.getElementById("countdown").innerHTML = "";
		}
	}, 1000);
}

function datumzeit_jetzt() {
	var date = new Date();
	var aaaa = date.getFullYear();
	var gg = date.getDate();
	var mm = date.getMonth() + 1;

	if (gg < 10) gg = "0" + gg;

	if (mm < 10) mm = "0" + mm;

	var cur_day = aaaa + "-" + mm + "-" + gg;

	var hours = date.getHours();
	var minutes = date.getMinutes();
	var seconds = date.getSeconds();

	if (hours < 10) hours = "0" + hours;

	if (minutes < 10) minutes = "0" + minutes;

	if (seconds < 10) seconds = "0" + seconds;

	return cur_day + " " + hours + ":" + minutes + ":" + seconds;
}

function formatiere_datum(datum) {
	var datum;

	var input_zeit = datum.substr(-8);
	var input_jahr = datum.substr(0, 4);
	var input_monat = datum.substr(5, 2);
	var input_tag = datum.substr(8, 2);

	var datum_formatiert =
		input_monat +
		" " +
		input_tag +
		"," +
		" " +
		input_jahr +
		" " +
		input_zeit;

	return datum_formatiert;
}

function zeitrechner(input_datumzeit1, input_datumzeit2, teiler) {
	formatiertes_datum1 = formatiere_datum(input_datumzeit1);
	formatiertes_datum2 = formatiere_datum(input_datumzeit2);
	var teiler;

	var date1, date2;
	date1 = new Date(formatiertes_datum1);
	date2 = new Date(formatiertes_datum2);
	var seconds = Math.abs(date1 - date2) / 1000;

	var ergebnis = seconds / teiler;
	return ergebnis;
}

function berechne_zeit_verbleibend(input_endzeit) {
	var input_endzeit;
	var zeit_jetzt = datumzeit_jetzt();

	if (input_endzeit < zeit_jetzt) {
		return 0;
	} else if (input_endzeit > zeit_jetzt) {
		var zeit_verbleibend = zeitrechner(input_endzeit, zeit_jetzt, 1);
		return zeit_verbleibend;
	} else {
		return 0;
	}
}

function berechne_prozent_verbleibend(input_startzeit, input_endzeit) {
	var input_startzeit, input_endzeit;

	var zeit_verbleibend = berechne_zeit_verbleibend(input_endzeit);

	var zeit_gesamt = zeitrechner(input_startzeit, input_endzeit, 1);

	var ein_prozent = zeit_gesamt / 100;
	var prozent_gesamt = zeit_verbleibend / ein_prozent;
	var prozent_resultat = 100 - prozent_gesamt;
	var prozent_gerundet = Math.round(prozent_resultat);

	if (prozent_gerundet <= 2) {
		return 2 + "%";
	} else {
		return prozent_gerundet + "%";
	}
}

function balken_berechnung(datetime, programm_ende) {
	var datetime, programm_ende;
	setInterval(function() {
		var prozent_verbleibend = berechne_prozent_verbleibend(
			datetime,
			programm_ende
		);
		var str = prozent_verbleibend;
		var prozent = str.substring(0, str.length - 1);

		document.getElementById(
			"prozent_fortschritt"
		).style.width = prozent_verbleibend;
		document.getElementById(
			"prozent_jetzt"
		).innerHTML = prozent_verbleibend;

		if (prozent < 5) {
			document.getElementById("prozent_jetzt").style.display = "none";
		} else if (prozent > 5 && prozent != 100) {
			document.getElementById("prozent_jetzt").style.display = "flex";
		} else if (prozent == 100) {
			document.getElementById("prozent_meter").style.backgroundColor =
				"#24fe41";
			document.getElementById("prozent_fortschritt").style.background =
				"transparent";
			document.getElementById("text_fertig").style.display = "block";
			document.getElementById("prozent_jetzt").style.display = "none";
			document.getElementById("button_abbrechen").style.color = "#05c11e";
		}
	}, 1000);
}
