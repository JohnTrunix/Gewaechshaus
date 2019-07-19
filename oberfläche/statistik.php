<!DOCTYPE html>
<html>
<head>
<title>Gewaechshaus Raspberry Pi 3B+</title>
<link rel="stylesheet" href="style.css">
<meta http-equiv="refresh" content="5">
</head>
<body>

<div class="menu_rahmen">

  <div class="icon top" onclick="window.location='/';">
    <img src="img/house.svg" class="menubild">
  </div>

  <div class="icon middle aktiv" onclick="window.location='/statistik.php';">
    <img src="img/pie-chart.svg" class="menubild">
  </div>

  <div class="icon bottom" onclick="window.location='/einstellungen.php';">
    <img src="img/settings.svg" class="menubild">
  </div>

  <div class="icon shutdown" onclick="window.location='/herunterfahren.php';">
    <img src="img/logout.svg" class="menubild">
  </div>
</div>

<div class="menu_bar">
  <p class="menu_titel">Statistik</p>
</div>
  <div class="mitte">
  <iframe class="statistik_iframe" src="localhost:3000/d/AfG9VvzRk/dashboard?orgId=1&refresh=5s&theme=light&kiosk"></iframe>
	</div>
</body>
</html>
