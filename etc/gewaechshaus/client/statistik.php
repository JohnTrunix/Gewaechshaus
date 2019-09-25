<!DOCTYPE html>
<html>
    <head>
        <title>Gewaechshaus Raspberry Pi 3B+</title>
        <link rel="stylesheet" href="/css/style.css">
    </head>
    <body>
        <div class="menu_rahmen">
            <div class="icon top" onclick="window.location='/';">
                <img src="/img/house.svg" class="menubild">
            </div>
            <div class="icon middle aktiv" onclick="window.location='/statistik.php';">
                <img src="/img/pie-chart.svg" class="menubild">
            </div>
            <div class="icon bottom" onclick="window.location='/einstellungen.php';">
                <img src="/img/settings.svg" class="menubild">
            </div>
            <div class="icon shutdown" onclick="window.location='/api/herunterfahren/herunterfahren.php';">
                <img src="/img/logout.svg" class="menubild">
            </div>
        </div>
        <div class="statistik_iframe">
            <iframe src="http://<?php echo $_SERVER['HTTP_HOST']; ?>:3000/d/FLXpjTtWk/sensorwerte?orgId=1&kiosk=tv" width="100%" height="100%" frameborder="0"></iframe>
        </div>
    </body>
</html>