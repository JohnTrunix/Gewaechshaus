// Grafana URL dem HTML Iframe zuweisen
//======================================================================
function get_ip_address() {
	var display = document.getElementById("iframe");
	jQuery.ajax({
		type: "GET",
		url: "/api/api.php?ip_adresse_read",
		success: function(response) {
			display.src =
				"http://" +
				response +
				":3000/d/mAnGWsRgk/sensorwerte?orgId=1&kiosk=tv&refresh=5s";
		}
	});
}
get_ip_address();
//======================================================================
