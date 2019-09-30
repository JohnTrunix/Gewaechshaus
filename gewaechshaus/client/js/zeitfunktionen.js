var now = new Date(),
	minDate = now.toISOString().substring(0, 10);
$("#programm_datum_ende").prop("min", minDate);

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

		document.getElementById("countdown").innerHTML =
			"Zeit Verbleibend: " +
			days +
			"d " +
			hours +
			"h " +
			minutes +
			"m " +
			seconds +
			"s ";

		if (distance < 0) {
			clearInterval(x);
			document.getElementById("countdown").innerHTML = "Fertig";
		}
	}, 1000);
}
