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
            <div class="icon shutdown" onclick="window.location='php/herunterfahren.php';">
                <img src="img/logout.svg" class="menubild">
            </div>
        </div>
		<iframe src="livewerte.php" style="position:fixed; left:0;top:0;height:100%;width:200px;border: 0; outline:none;"></iframe>
		<div class="mitte">
			<div id="select-dropdown" class="closed">
                <div id="select-default" class="select default">Rezept auswählen</div>
                <div class="select option" id="slot1" data-id="1"></div>
                <div class="select option" id="slot2" data-id="2"></div>
                <div class="select option" id="slot3" data-id="3"></div>
				<div class="select option" id="slot4" data-id="4"></div>
				<div class="select option" id="slot5" data-id="5"></div>
                <div class="select option" id="slot6" data-id="6"></div>
                <div class="select option" id="slot7" data-id="7"></div>
                <div class="select option" id="slot8" data-id="8"></div>
                <div class="select option" id="slot9" data-id="9"></div>
                <div class="select option" id="slot10" data-id="10"></div>
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
        document.getElementById("slot1").innerHTML = '<?php echo $pflanze1 ?>';
        document.getElementById("slot2").innerHTML = '<?php echo $pflanze2 ?>';
        document.getElementById("slot3").innerHTML = '<?php echo $pflanze3 ?>';
        document.getElementById("slot4").innerHTML = '<?php echo $pflanze4 ?>';
        document.getElementById("slot5").innerHTML = '<?php echo $pflanze5 ?>';
        document.getElementById("slot6").innerHTML = '<?php echo $pflanze6 ?>';
        document.getElementById("slot7").innerHTML = '<?php echo $pflanze7 ?>';
        document.getElementById("slot8").innerHTML = '<?php echo $pflanze8 ?>';
        document.getElementById("slot9").innerHTML = '<?php echo $pflanze9 ?>';
        document.getElementById("slot10").innerHTML = '<?php echo $pflanze10 ?>';

        function getComboA() {
            var value = window.dropdown;
                if (value == 1) {
                    document.getElementById("parameter_slot").value = 1;
                    document.getElementById("temperatur").innerHTML = 'Temperatur: ' + <?php echo $temperatur1 ?>;
                    document.getElementById("lichtstunden").innerHTML = 'Licht pro Tag: ' + <?php echo $lichtstunden1 ?>;
                    document.getElementById("wassermenge").innerHTML = 'Wasser pro Tag: ' + <?php echo $wassermenge1 ?>;
                    document.getElementById("luftfeuchtigkeit").innerHTML = 'Luftfeuchtigkeit: ' + <?php echo $luftfeuchtigkeit1 ?>;
                } else if (value == 2) {
                    document.getElementById("parameter_slot").value = 2;
                    document.getElementById("temperatur").innerHTML = 'Temperatur: ' + <?php echo $temperatur2 ?>;
                    document.getElementById("lichtstunden").innerHTML = 'Licht pro Tag: ' + <?php echo $lichtstunden2 ?>;
                    document.getElementById("wassermenge").innerHTML = 'Wasser pro Tag: ' + <?php echo $wassermenge2 ?>;
                    document.getElementById("luftfeuchtigkeit").innerHTML = 'Luftfeuchtigkeit: ' + <?php echo $luftfeuchtigkeit2 ?>;
                } else if (value == 3) {
                    document.getElementById("parameter_slot").value = 3;
                    document.getElementById("temperatur").innerHTML = 'Temperatur: ' + <?php echo $temperatur3 ?>;
                    document.getElementById("lichtstunden").innerHTML = 'Licht pro Tag: ' + <?php echo $lichtstunden3 ?>;
                    document.getElementById("wassermenge").innerHTML = 'Wasser pro Tag: ' + <?php echo $wassermenge3 ?>;
                    document.getElementById("luftfeuchtigkeit").innerHTML = 'Luftfeuchtigkeit: ' + <?php echo $luftfeuchtigkeit3 ?>;
                } else if (value == 4) {
                    document.getElementById("parameter_slot").value = 4;
                    document.getElementById("temperatur").innerHTML = 'Temperatur: ' + <?php echo $temperatur4 ?>;
                    document.getElementById("lichtstunden").innerHTML = 'Licht pro Tag: ' + <?php echo $lichtstunden4 ?>;
                    document.getElementById("wassermenge").innerHTML = 'Wasser pro Tag: ' + <?php echo $wassermenge4 ?>;
                    document.getElementById("luftfeuchtigkeit").innerHTML = 'Luftfeuchtigkeit: ' + <?php echo $luftfeuchtigkeit4 ?>;
                } else if (value == 5) {
                    document.getElementById("parameter_slot").value = 5;
                    document.getElementById("temperatur").innerHTML = 'Temperatur: ' + <?php echo $temperatur5 ?>;
                    document.getElementById("lichtstunden").innerHTML = 'Licht pro Tag: ' + <?php echo $lichtstunden5 ?>;
                    document.getElementById("wassermenge").innerHTML = 'Wasser pro Tag: ' + <?php echo $wassermenge5 ?>;
                    document.getElementById("luftfeuchtigkeit").innerHTML = 'Luftfeuchtigkeit: ' + <?php echo $luftfeuchtigkeit5 ?>;
                } else if (value == 6) {
                    document.getElementById("parameter_slot").value = 6;
                    document.getElementById("temperatur").innerHTML = 'Temperatur: ' + <?php echo $temperatur6 ?>;
                    document.getElementById("lichtstunden").innerHTML = 'Licht pro Tag: ' + <?php echo $lichtstunden6 ?>;
                    document.getElementById("wassermenge").innerHTML = 'Wasser pro Tag: ' + <?php echo $wassermenge6 ?>;
                    document.getElementById("luftfeuchtigkeit").innerHTML = 'Luftfeuchtigkeit: ' + <?php echo $luftfeuchtigkeit6 ?>;
                } else if (value == 7) {
                    document.getElementById("parameter_slot").value = 7;
                    document.getElementById("temperatur").innerHTML = 'Temperatur: ' + <?php echo $temperatur7 ?>;
                    document.getElementById("lichtstunden").innerHTML = 'Licht pro Tag: ' + <?php echo $lichtstunden7 ?>;
                    document.getElementById("wassermenge").innerHTML = 'Wasser pro Tag: ' + <?php echo $wassermenge7 ?>;
                    document.getElementById("luftfeuchtigkeit").innerHTML = 'Luftfeuchtigkeit: ' + <?php echo $luftfeuchtigkeit7 ?>;
                } else if (value == 8) {
                    document.getElementById("parameter_slot").value = 8;
                    document.getElementById("temperatur").innerHTML = 'Temperatur: ' + <?php echo $temperatur8 ?>;
                    document.getElementById("lichtstunden").innerHTML = 'Licht pro Tag: ' + <?php echo $lichtstunden8 ?>;
                    document.getElementById("wassermenge").innerHTML = 'Wasser pro Tag: ' + <?php echo $wassermenge8 ?>;
                    document.getElementById("luftfeuchtigkeit").innerHTML = 'Luftfeuchtigkeit: ' + <?php echo $luftfeuchtigkeit8 ?>;
                } else if (value == 9) {
                    document.getElementById("parameter_slot").value = 9;
                    document.getElementById("temperatur").innerHTML = 'Temperatur: ' + <?php echo $temperatur9 ?>;
                    document.getElementById("lichtstunden").innerHTML = 'Licht pro Tag: ' + <?php echo $lichtstunden9 ?>;
                    document.getElementById("wassermenge").innerHTML = 'Wasser pro Tag: ' + <?php echo $wassermenge9 ?>;
                    document.getElementById("luftfeuchtigkeit").innerHTML = 'Luftfeuchtigkeit: ' + <?php echo $luftfeuchtigkeit9 ?>;
                } else if (value == 10) {
                    document.getElementById("parameter_slot").value = 10;
                    document.getElementById("temperatur").innerHTML = 'Temperatur: ' + <?php echo $temperatur10 ?>;
                    document.getElementById("lichtstunden").innerHTML = 'Licht pro Tag: ' + <?php echo $lichtstunden10 ?>;
                    document.getElementById("wassermenge").innerHTML = 'Wasser pro Tag: ' + <?php echo $wassermenge10 ?>;
                    document.getElementById("luftfeuchtigkeit").innerHTML = 'Luftfeuchtigkeit: ' + <?php echo $luftfeuchtigkeit10 ?>;
                }
            }
        </script>
    </body>
</html>