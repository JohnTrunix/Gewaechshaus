<?php
require 'php/parameter_download.php';
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
		<div class="menu_bar">
            <p class="menu_titel">Live Werte</p>
            <div class="sensorwert sensorwert_1">
                <img src="img/idea.svg" class="sensor_icon">
                <a class='sensor_zahl' id='lichtstaerke_wert'></a>
                <a class="sensor_beschreibung">Lichtstärke</a>
            </div>
            <div class="sensorwert sensorwert_2">
                <img src="img/breeze.svg" class="sensor_icon">
                <a class='sensor_zahl' id='luftfeuchtigkeit_wert'></a>
                <a class="sensor_beschreibung">Luftfeuchtigkeit</a>
            </div>
            <div class="sensorwert sensorwert_3">
                <img src="img/thermometer.svg" class="sensor_icon">
                <a class='sensor_zahl' id='temperatur_wert'></a>
                <a class="sensor_beschreibung">Temperatur</a>
            </div>
		</div>
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
                <div class="parameter" id="lichtstunden">Licht pro Tag:</div>
                <div class="parameter" id="wassermenge">Wasser pro Tag:</div>
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

        function getComboA(selectObject) {
            ar = <?php echo json_encode($arr) ?>;
            var value = window.dropdown;
            document.getElementById("parameter_slot").value = value;
            document.getElementById("temperatur").innerHTML = 'Temperatur: ' + ar[value-1].temperatur;
            document.getElementById("lichtstunden").innerHTML = 'Licht pro Tag: ' + ar[value-1].lichtstunden;
            document.getElementById("wassermenge").innerHTML = 'Wasser pro Tag: ' + ar[value-1].wassermenge;
            document.getElementById("luftfeuchtigkeit").innerHTML = 'Luftfeuchtigkeit: ' + ar[value-1].luftfeuchtigkeit;
        }

        function lichtstaerke_download(){
            var display = document.getElementById("lichtstaerke_wert");
            var xmlhttp = new XMLHttpRequest();
            xmlhttp.open("GET", "php/lichtstaerke_download.php");
            xmlhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
            xmlhttp.send();
            xmlhttp.onreadystatechange = function() {
            if (this.readyState === 4 && this.status === 200) {
                display.innerHTML = this.responseText + ' Lux';
            } else {
                display.innerHTML = "Lade...";
            };
            }
        }

        function luftfeuchtigkeit_download(){
            var display = document.getElementById("luftfeuchtigkeit_wert");
            var xmlhttp = new XMLHttpRequest();
            xmlhttp.open("GET", "php/luftfeuchtigkeit_download.php");
            xmlhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
            xmlhttp.send();
            xmlhttp.onreadystatechange = function() {
            if (this.readyState === 4 && this.status === 200) {
                display.innerHTML = this.responseText + ' %';
            } else {
                display.innerHTML = "Lade...";
            };
            }
        }

        function temperatur_download(){
            var display = document.getElementById("temperatur_wert");
            var xmlhttp = new XMLHttpRequest();
            xmlhttp.open("GET", "php/temperatur_download.php");
            xmlhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
            xmlhttp.send();
            xmlhttp.onreadystatechange = function() {
            if (this.readyState === 4 && this.status === 200) {
                display.innerHTML = this.responseText + ' °C';
            } else {
                display.innerHTML = "Lade...";
            };
            }
        }

        function sensorwert_download(){
            lichtstaerke_download();
            luftfeuchtigkeit_download()
            temperatur_download()
            setTimeout(sensorwert_download, 5000);
        }
        sensorwert_download();
        </script>
    </body>
</html>