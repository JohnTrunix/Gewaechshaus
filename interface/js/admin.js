function datumzeit(id) {
	date = new Date();
	year = date.getFullYear();
	month = date.getMonth();
	months = new Array(
		"Januar",
		"Februar",
		"März",
		"April",
		"Mai",
		"Juni",
		"Juli",
		"August",
		"September",
		"Oktober",
		"November",
		"Dezember"
	);
	d = date.getDate();
	day = date.getDay();
	days = new Array(
		"Sonntag",
		"Montag",
		"Dienstag",
		"Mittwoch",
		"Donnerstag",
		"Freitag",
		"Samstag"
	);
	h = date.getHours();
	if (h < 10) {
		h = "0" + h;
	}
	m = date.getMinutes();
	if (m < 10) {
		m = "0" + m;
	}
	s = date.getSeconds();
	if (s < 10) {
		s = "0" + s;
	}
	result = d + " " + months[month] + " " + year + " " + h + ":" + m + ":" + s;
	document.getElementById(id).innerHTML = result;
	setTimeout('datumzeit("' + id + '");', "1000");
	return true;
}
