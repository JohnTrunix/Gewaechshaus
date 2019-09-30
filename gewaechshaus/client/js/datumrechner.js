var now = new Date(),
	minDate = now.toISOString().substring(0, 10);
$("#programm_datum_ende").prop("min", minDate);
