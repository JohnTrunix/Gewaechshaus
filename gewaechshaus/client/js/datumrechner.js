var now = new Date(),
	minDate = now.toISOString().substring(0, 10);
$("#programm_datum_ende").prop("min", minDate);

function datum_nach_sekunden(input_datumzeit1, input_datumzeit2, teiler) {
	var input_datumzeit1, input_datumzeit2, teiler;

	var input_zeit1 = input_datumzeit1.substr(-8);
	var input_jahr1 = input_datumzeit1.substr(0, 4);
	var input_monat1 = input_datumzeit1.substr(5, 2);
	var input_tag1 = input_datumzeit1.substr(8, 2);

	var datum1_formatiert =
		input_monat1 +
		" " +
		input_tag1 +
		"," +
		" " +
		input_jahr1 +
		" " +
		input_zeit1;

	var input_zeit2 = input_datumzeit2.substr(-8);
	var input_jahr2 = input_datumzeit2.substr(0, 4);
	var input_monat2 = input_datumzeit2.substr(5, 2);
	var input_tag2 = input_datumzeit2.substr(8, 2);

	var datum2_formatiert =
		input_monat2 +
		" " +
		input_tag2 +
		"," +
		" " +
		input_jahr2 +
		" " +
		input_zeit2;

	var date1, date2;
	date1 = new Date(datum1_formatiert);
	date2 = new Date(datum2_formatiert);
	var seconds = Math.abs(date1 - date2) / 1000;

	var ergebnis = seconds / teiler;
	return ergebnis;
}
