<!DOCTYPE html>
<html>
    <head>
        <title>Gewaechshaus Raspberry Pi 3B+</title>
		<link rel="stylesheet" href="style.css">
    </head>
    <body>
        <div class="menu_rahmen">
            <div class="icon top aktiv" onclick="window.location='/';">
                <img src="img/house.svg" class="menubild">
            </div>
            <div class="icon middle" onclick="window.location='/statistik.php';">
                <img src="img/pie-chart.svg" class="menubild">
            </div>
            <div class="icon bottom" onclick="window.location='/einstellungen.php';">
                <img src="img/settings.svg" class="menubild">
            </div>
            <div class="icon shutdown" onclick="window.location='/herunterfahren.php';">
                <img src="img/logout.svg" class="menubild">
            </div>
        </div>
		<iframe src="livewerte.php" style="position:fixed; left:0;top:0;height:100%;width:200px;border: 0; outline:none;"></iframe> 
		<div class="mitte">
		<script src="js/jquery.min.js"></script>
		<script src="js/drop-down.js"></script>
			<div class=navigation_oben>
				<div id="select-dropdown" class="closed">
                    <div id="select-default" class="select default">Rezept auswählen</div>
                    <div class="select option" data-id="1">Karotten</div>
                    <div class="select option" data-id="2">Tomaten</div>
                    <div class="select option" data-id="3">Karotten</div>
					<div class="select option" data-id="4">Tomaten</div>
					<div class="select option" data-id="5">Karotten</div>
                    <div class="select option" data-id="6">Tomaten</div>
				</div>
			</div>
		</div>
    </body>
</html>

