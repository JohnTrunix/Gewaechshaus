var url = window.location.href;
var error_msg = document.getElementById("error_div");
if (url.search("fehler") > 0) {
	error_msg.style.display = "flex";
}
