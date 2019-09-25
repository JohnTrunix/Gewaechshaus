var url = window.location.href;
var error_msg = document.getElementById("error_div");
var success_msg = document.getElementById("success_div");
if (url.search("fehler") > 0) {
	error_msg.style.display = "flex";
	success_msg.style.display = "none";
} else if (url.search("erfolgreich") > 0) {
	success_msg.style.display = "flex";
	error_msg.style.display = "none";
}
