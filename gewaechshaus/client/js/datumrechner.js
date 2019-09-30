var now = new Date(),
	minDate = now.toISOString().substring(0, 10);
$("#programm_datum_ende").prop("min", minDate);

var date1, date2;
date1 = new Date("09 30, 2019 18:36:23");
date2 = new Date("10 23, 2019 14:00:00");
var seconds = Math.abs(date1 - date2) / 1000;
document.write("<br>Difference between 2 dates: " + seconds);
