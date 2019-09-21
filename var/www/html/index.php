<?php
require 'php/datenbank_download.php';
?>
<!DOCTYPE html>
<html>
    <head>
        <title>Gewaechshaus Raspberry Pi 3B+</title>
		<link rel="stylesheet" href="style.css">
        <script src="js/jquery.min.js"></script>
		<script src="js/drop-down.js"></script>
        <script>
        slot1 = "<?php echo $slot1 ?>";
        pflanze1 = "<?php echo $pflanze1 ?>";
        temperatur1 = "<?php echo $temperatur1 ?>";
        lichtstunden1 = "<?php echo $lichtstunden1 ?>";
        wassermenge1 = "<?php echo $wassermenge1 ?>";
        luftfeuchtigkeit1 = "<?php echo $luftfeuchtigkeit1 ?>";

        slot2 = "<?php echo $slot2 ?>";
        pflanze2 = "<?php echo $pflanze2 ?>";
        temperatur2 = "<?php echo $temperatur2 ?>";
        lichtstunden2 = "<?php echo $lichtstunden2 ?>";
        wassermenge2 = "<?php echo $wassermenge2 ?>";
        luftfeuchtigkeit2 = "<?php echo $luftfeuchtigkeit2 ?>";

        slot3 = "<?php echo $slot3 ?>";
        pflanze3 = "<?php echo $pflanze3 ?>";
        temperatur3 = "<?php echo $temperatur3 ?>";
        lichtstunden3 = "<?php echo $lichtstunden3 ?>";
        wassermenge3 = "<?php echo $wassermenge3 ?>";
        luftfeuchtigkeit3 = "<?php echo $luftfeuchtigkeit3 ?>";

        slot4 = "<?php echo $slot4 ?>";
        pflanze4 = "<?php echo $pflanze4 ?>";
        temperatur4 = "<?php echo $temperatur4 ?>";
        lichtstunden4 = "<?php echo $lichtstunden4 ?>";
        wassermenge4 = "<?php echo $wassermenge4 ?>";
        luftfeuchtigkeit4 = "<?php echo $luftfeuchtigkeit4 ?>";

        slot5 = "<?php echo $slot5 ?>";
        pflanze5 = "<?php echo $pflanze5 ?>";
        temperatur5 = "<?php echo $temperatur5 ?>";
        lichtstunden5 = "<?php echo $lichtstunden5 ?>";
        wassermenge5 = "<?php echo $wassermenge5 ?>";
        luftfeuchtigkeit5 = "<?php echo $luftfeuchtigkeit5 ?>";

        slot6 = "<?php echo $slot6 ?>";
        pflanze6 = "<?php echo $pflanze6 ?>";
        temperatur6 = "<?php echo $temperatur6 ?>";
        lichtstunden6 = "<?php echo $lichtstunden6 ?>";
        wassermenge6 = "<?php echo $wassermenge6 ?>";
        luftfeuchtigkeit6 = "<?php echo $luftfeuchtigkeit6 ?>";

        slot7 = "<?php echo $slot7 ?>";
        pflanze7 = "<?php echo $pflanze7 ?>";
        temperatur7 = "<?php echo $temperatur7 ?>";
        lichtstunden7 = "<?php echo $lichtstunden7 ?>";
        wassermenge7 = "<?php echo $wassermenge7 ?>";
        luftfeuchtigkeit7 = "<?php echo $luftfeuchtigkeit7 ?>";

        slot8 = "<?php echo $slot8 ?>";
        pflanze8 = "<?php echo $pflanze8 ?>";
        temperatur8 = "<?php echo $temperatur8 ?>";
        lichtstunden8 = "<?php echo $lichtstunden8 ?>";
        wassermenge8 = "<?php echo $wassermenge8 ?>";
        luftfeuchtigkeit8 = "<?php echo $luftfeuchtigkeit8 ?>";

        slot9 = "<?php echo $slot9 ?>";
        pflanze9 = "<?php echo $pflanze9 ?>";
        temperatur9 = "<?php echo $temperatur9 ?>";
        lichtstunden9 = "<?php echo $lichtstunden9 ?>";
        wassermenge9 = "<?php echo $wassermenge9 ?>";
        luftfeuchtigkeit9 = "<?php echo $luftfeuchtigkeit9 ?>";

        slot10 = "<?php echo $slot10 ?>";
        pflanze10 = "<?php echo $pflanze10 ?>";
        temperatur10 = "<?php echo $temperatur10 ?>";
        lichtstunden10 = "<?php echo $lichtstunden10 ?>";
        wassermenge10 = "<?php echo $wassermenge10 ?>";
        luftfeuchtigkeit10 = "<?php echo $luftfeuchtigkeit10 ?>";
        </script>
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
			<div id="select-dropdown" class="closed">
                <div id="select-default" class="select default">Rezept auswählen</div>
                <div class="select option" id="slot1" data-id="1">Leer</div>
                <div class="select option" id="slot2" data-id="2">Leer</div>
                <div class="select option" id="slot3" data-id="3">Leer</div>
				<div class="select option" id="slot4" data-id="4">Leer</div>
				<div class="select option" id="slot5" data-id="5">Leer</div>
                <div class="select option" id="slot6" data-id="6">Leer</div>
                <div class="select option" id="slot7" data-id="7">Leer</div>
                <div class="select option" id="slot8" data-id="8">Leer</div>
                <div class="select option" id="slot9" data-id="9">Leer</div>
                <div class="select option" id="slot10" data-id="10">Leer</div>
			</div>
            <div class="slot_parameter">
                <p class=title_parameter>Soll-Werte:</p>
                <div class="parameter" id="temperatur">Temperatur:</div>
                <div class="parameter" id="lichtstunden">Lichtstunden:</div>
                <div class="parameter" id="wassermenge">Wassermenge:</div>
                <div class="parameter" id="luftfeuchtigkeit">Luftfeuchtigkeit:</div>
            </div>

            <div class="betriebsmodus">
                <form action="betriebsmodus.php">
                    <input required type="hidden" name="parameter_slot" id="parameter_slot" value="0">
                    <input type="submit" value="Start">
                </form>
            </div>
		</div>

        <script>
        document.getElementById("slot1").innerHTML = pflanze1;
        document.getElementById("slot2").innerHTML = pflanze2;
        document.getElementById("slot3").innerHTML = pflanze3;
        document.getElementById("slot4").innerHTML = pflanze4;
        document.getElementById("slot5").innerHTML = pflanze5;
        document.getElementById("slot6").innerHTML = pflanze6;
        document.getElementById("slot7").innerHTML = pflanze7;
        document.getElementById("slot8").innerHTML = pflanze8;
        document.getElementById("slot9").innerHTML = pflanze9;
        document.getElementById("slot10").innerHTML = pflanze10;

        function getComboA() {
            var value = window.dropdown;
                if (value == 1) {
                    document.getElementById("parameter_slot").value = 1;
                    document.getElementById("temperatur").innerHTML = 'Temperatur: ' + temperatur1;
                    document.getElementById("lichtstunden").innerHTML = 'Licht pro Tag: ' + lichtstunden1;
                    document.getElementById("wassermenge").innerHTML = 'Wasser pro Tag: ' + wassermenge1;
                    document.getElementById("luftfeuchtigkeit").innerHTML = 'Luftfeuchtigkeit: ' + luftfeuchtigkeit1;
                } else if (value == 2) {
                    document.getElementById("parameter_slot").value = 2;
                    document.getElementById("temperatur").innerHTML = 'Temperatur: ' + temperatur2;
                    document.getElementById("lichtstunden").innerHTML = 'Licht pro Tag: ' + lichtstunden2;
                    document.getElementById("wassermenge").innerHTML = 'Wasser pro Tag: ' + wassermenge2;
                    document.getElementById("luftfeuchtigkeit").innerHTML = 'Luftfeuchtigkeit: ' + luftfeuchtigkeit2;
                } else if (value == 3) {
                    document.getElementById("parameter_slot").value = 3;
                    document.getElementById("temperatur").innerHTML = 'Temperatur: ' + temperatur3;
                    document.getElementById("lichtstunden").innerHTML = 'Licht pro Tag: ' + lichtstunden3;
                    document.getElementById("wassermenge").innerHTML = 'Wasser pro Tag: ' + wassermenge3;
                    document.getElementById("luftfeuchtigkeit").innerHTML = 'Luftfeuchtigkeit: ' + luftfeuchtigkeit3;
                } else if (value == 4) {
                    document.getElementById("parameter_slot").value = 4;
                    document.getElementById("temperatur").innerHTML = 'Temperatur: ' + temperatur4;
                    document.getElementById("lichtstunden").innerHTML = 'Licht pro Tag: ' + lichtstunden4;
                    document.getElementById("wassermenge").innerHTML = 'Wasser pro Tag: ' + wassermenge4;
                    document.getElementById("luftfeuchtigkeit").innerHTML = 'Luftfeuchtigkeit: ' + luftfeuchtigkeit4;
                } else if (value == 5) {
                    document.getElementById("parameter_slot").value = 5;
                    document.getElementById("temperatur").innerHTML = 'Temperatur: ' + temperatur5;
                    document.getElementById("lichtstunden").innerHTML = 'Licht pro Tag: ' + lichtstunden5;
                    document.getElementById("wassermenge").innerHTML = 'Wasser pro Tag: ' + wassermenge5;
                    document.getElementById("luftfeuchtigkeit").innerHTML = 'Luftfeuchtigkeit: ' + luftfeuchtigkeit5;
                } else if (value == 6) {
                    document.getElementById("parameter_slot").value = 6;
                    document.getElementById("temperatur").innerHTML = 'Temperatur: ' + temperatur6;
                    document.getElementById("lichtstunden").innerHTML = 'Licht pro Tag: ' + lichtstunden6;
                    document.getElementById("wassermenge").innerHTML = 'Wasser pro Tag: ' + wassermenge6;
                    document.getElementById("luftfeuchtigkeit").innerHTML = 'Luftfeuchtigkeit: ' + luftfeuchtigkeit6;
                } else if (value == 7) {
                    document.getElementById("parameter_slot").value = 7;
                    document.getElementById("temperatur").innerHTML = 'Temperatur: ' + temperatur7;
                    document.getElementById("lichtstunden").innerHTML = 'Licht pro Tag: ' + lichtstunden7;
                    document.getElementById("wassermenge").innerHTML = 'Wasser pro Tag: ' + wassermenge7;
                    document.getElementById("luftfeuchtigkeit").innerHTML = 'Luftfeuchtigkeit: ' + luftfeuchtigkeit7;
                } else if (value == 8) {
                    document.getElementById("parameter_slot").value = 8;
                    document.getElementById("temperatur").innerHTML = 'Temperatur: ' + temperatur8;
                    document.getElementById("lichtstunden").innerHTML = 'Licht pro Tag: ' + lichtstunden8;
                    document.getElementById("wassermenge").innerHTML = 'Wasser pro Tag: ' + wassermenge8;
                    document.getElementById("luftfeuchtigkeit").innerHTML = 'Luftfeuchtigkeit: ' + luftfeuchtigkeit8;
                } else if (value == 9) {
                    document.getElementById("parameter_slot").value = 9;
                    document.getElementById("temperatur").innerHTML = 'Temperatur: ' + temperatur9;
                    document.getElementById("lichtstunden").innerHTML = 'Licht pro Tag: ' + lichtstunden9;
                    document.getElementById("wassermenge").innerHTML = 'Wasser pro Tag: ' + wassermenge9;
                    document.getElementById("luftfeuchtigkeit").innerHTML = 'Luftfeuchtigkeit: ' + luftfeuchtigkeit9;
                } else if (value == 10) {
                    document.getElementById("parameter_slot").value = 10;
                    document.getElementById("temperatur").innerHTML = 'Temperatur: ' + temperatur10;
                    document.getElementById("lichtstunden").innerHTML = 'Licht pro Tag: ' + lichtstunden10;
                    document.getElementById("wassermenge").innerHTML = 'Wasser pro Tag: ' + wassermenge10;
                    document.getElementById("luftfeuchtigkeit").innerHTML = 'Luftfeuchtigkeit: ' + luftfeuchtigkeit10;
                }
            }
        </script>
    </body>
</html>

