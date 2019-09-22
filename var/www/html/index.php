<?php
require 'api/parameter/parameter_download.php';
require 'api/betriebsmodus/betriebsmodus_download.php';
?>
<!DOCTYPE html>
<html>
    <head>
        <title>Gewaechshaus Raspberry Pi 3B+</title>
        <link rel="stylesheet" href="/css/style.css">
        <script src="/js/jquery.min.js"></script>
		<script src="/js/drop-down.js"></script>
    </head>
    <body>
        <div class="menu_rahmen">
            <div class="icon top aktiv" onclick="window.location='/';">
                <img src="/img/house.svg" class="menubild">
            </div>
            <div class="icon middle" onclick="window.location='/statistik.php';">
                <img src="/img/pie-chart.svg" class="menubild">
            </div>
            <div class="icon bottom" onclick="window.location='/einstellungen.php';">
                <img src="/img/settings.svg" class="menubild">
            </div>
            <div class="icon shutdown" onclick="window.location='/api/herunterfahren/herunterfahren.php';">
                <img src="/img/logout.svg" class="menubild">
            </div>
        </div>
        <div class="menu_bar">
            <p class="menu_titel">Live Werte</p>
            <div class="sensorwert sensorwert_1">
                <img src="/img/idea.svg" class="sensor_icon">
                <a class='sensor_zahl' id='lichtstaerke_wert'></a>
                <a class="sensor_beschreibung">Lichtstärke</a>
            </div>
            <div class="sensorwert sensorwert_2">
                <img src="/img/breeze.svg" class="sensor_icon">
                <a class='sensor_zahl' id='luftfeuchtigkeit_wert'></a>
                <a class="sensor_beschreibung">Luftfeuchtigkeit</a>
            </div>
            <div class="sensorwert sensorwert_3">
                <img src="/img/thermometer.svg" class="sensor_icon">
                <a class='sensor_zahl' id='temperatur_wert'></a>
                <a class="sensor_beschreibung">Temperatur</a>
            </div>
        </div>
        <div class="mitte">
            <div class="mode_selector" id="starter">
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
                    <form action="/api/betriebsmodus/betriebsmodus_update.php">
						<input required type="hidden" name="parameter_slot" id="parameter_slot" value="0">
						<input required type="hidden" name="parameter_name" id="parameter_name" value="0">
                        <input required type="hidden" name="programm_status" id="programm_status" value="start">
                        <input type="submit" value="Start">
                    </form>
                    <div id="error_div">Fehler!</div>
                    <div id="success_div">Erfolgreich!</div>
                </div>
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

            function selected_slot(selectObject) {
                ar = <?php echo json_encode($get_parameter_daten) ?>;
                var value = window.dropdown;
				document.getElementById("parameter_slot").value = value;
				parameter_name = document.getElementById('select-default').innerHTML;
				document.getElementById("parameter_name").value = parameter_name;
                document.getElementById("temperatur").innerHTML = 'Temperatur: ' + ar[value-1].temperatur;
                document.getElementById("lichtstunden").innerHTML = 'Licht pro Tag: ' + ar[value-1].lichtstunden;
                document.getElementById("wassermenge").innerHTML = 'Wasser pro Tag: ' + ar[value-1].wassermenge;
                document.getElementById("luftfeuchtigkeit").innerHTML = 'Luftfeuchtigkeit: ' + ar[value-1].luftfeuchtigkeit;
			}

			function get_betriebsmodus_daten() {
				ar = <?php echo json_encode($get_betriebsmodus_daten) ?>;
                parameter_slot = ar[0].parameter_slot;
                parameter_name = ar[0].parameter_name;
                programm_status = ar[0].programm_status;
                datetime = ar[0].datetime;
			}

			get_betriebsmodus_daten();

		</script>
		<script src="/js/sensorwert_download.js"></script>
		<script src="/js/error_message.js"></script>
		<script src="/js/betriebsmodus_display.js"></script>
    </body>
</html>