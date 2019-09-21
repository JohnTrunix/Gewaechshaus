<?php
require 'php/datenbank_download.php';
?>
<!DOCTYPE html>
<html>
    <head>
        <title>Gewaechshaus Raspberry Pi 3B+</title>
        <link rel="stylesheet" href="style.css">
        <script src="js/jquery.min.js"></script>
    </head>
    <body style="background-color:white;">
        <div class="menu_rahmen">
            <div class="icon top" onclick="window.location='/';">
                <img src="img/house.svg" class="menubild">
            </div>
            <div class="icon middle" onclick="window.location='/statistik.php';">
                <img src="img/pie-chart.svg" class="menubild">
            </div>
            <div class="icon bottom aktiv" onclick="window.location='/einstellungen.php';">
                <img src="img/settings.svg" class="menubild">
            </div>
            <div class="icon shutdown" onclick="window.location='php/herunterfahren.php';">
                <img src="img/logout.svg" class="menubild">
            </div>
        </div>
        <div class="mitte">
            <form action="php/datenbank_update.php">
                <input required type="text" name="name" placeholder="Name" id="pflanze">
                <br>
                <a>Slot: </a>
                <select name="slot" onchange="getComboA(this)">
                    <option value="" disabled selected>Nr.</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                    <option value="6">6</option>
                    <option value="7">7</option>
                    <option value="8">8</option>
                    <option value="9">9</option>
                    <option value="10">10</option>
                </select>
                <p>Temperatur: <span id="wert_temperatur"></span>  °C</p>
                0
                <input type="range" id="temperatur" name="temperatur" min="0" max="30" value="15">
                30
                <script>
                    var slider_1 = document.getElementById("temperatur");
                    var output_1 = document.getElementById("wert_temperatur");
                    output_1.innerHTML = slider_1.value;

                    slider_1.oninput = function() {
                        output_1.innerHTML = this.value;
                    }
                </script>
                <br>
                <p>Licht: <span id="wert_lichtstunden"></span>  h/Tag</p>
                0
                <input type="range" id="lichtstunden" name="lichtstunden" min="0.0" max="24.0" value="12.0" step="0.1">
                24
                <script>
                    var slider_2 = document.getElementById("lichtstunden");
                    var output_2 = document.getElementById("wert_lichtstunden");
                    output_2.innerHTML = slider_2.value;

                    slider_2.oninput = function() {
                        output_2.innerHTML = this.value;
                    }
                </script>
                <br>
                <p>Wassermenge: <span id="wert_wassermenge"></span>  l/Tag</p>
                0
                <input type="range" id="wassermenge" name="wassermenge" min="0.0" max="10.0" value="5.0" step="0.1">
                10
                <script>
                    var slider_3 = document.getElementById("wassermenge");
                    var output_3 = document.getElementById("wert_wassermenge");
                    output_3.innerHTML = slider_3.value;

                    slider_3.oninput = function() {
                        output_3.innerHTML = this.value;
                    }
                </script>
                <br>
                <p>Luftfeuchtigkeit: <span id="wert_luftfeuchtigkeit"></span>  %</p>
                0
                <input type="range" id="luftfeuchtigkeit" name="luftfeuchtigkeit" min="0" max="100" value="50">
                100
                <script>
                    var slider_4 = document.getElementById("luftfeuchtigkeit");
                    var output_4 = document.getElementById("wert_luftfeuchtigkeit");
                    output_4.innerHTML = slider_4.value;

                    slider_4.oninput = function() {
                        output_4.innerHTML = this.value;
                    }
                </script>
                <br>
                <input type="submit" value="Speichern">
            </form>
            <div id="error_div">Fehler!</div>
            <div id="success_div">Erfolgreich!</div>
        </div>
        <script>
            function getComboA(selectObject) {
                var value = selectObject.value;
                if (value == 1) {
                    document.getElementById("pflanze").value = <?php echo $pflanze1 ?>;
                    document.getElementById("temperatur").value = <?php echo $temperatur1 ?>;
                    document.getElementById("lichtstunden").value = <?php echo $lichtstunden1 ?>;
                    document.getElementById("wassermenge").value = <?php echo $wassermenge1 ?>;
                    document.getElementById("luftfeuchtigkeit").value = <?php echo $luftfeuchtigkeit1 ?>;
                    document.getElementById("wert_temperatur").innerHTML = <?php echo $temperatur1 ?>;
                    document.getElementById("wert_lichtstunden").innerHTML = <?php echo $lichtstunden1 ?>;
                    document.getElementById("wert_wassermenge").innerHTML = <?php echo $wassermenge1 ?>;
                    document.getElementById("wert_luftfeuchtigkeit").innerHTML = <?php echo $luftfeuchtigkeit1 ?>;
                } else if (value == 2) {
                    document.getElementById("pflanze").value = <?php echo $pflanze2 ?>;
                    document.getElementById("temperatur").value = <?php echo $temperatur2 ?>;
                    document.getElementById("lichtstunden").value = <?php echo $lichtstunden2 ?>;
                    document.getElementById("wassermenge").value = <?php echo $wassermenge2 ?>;
                    document.getElementById("luftfeuchtigkeit").value = <?php echo $luftfeuchtigkeit2 ?>;
                    document.getElementById("wert_temperatur").innerHTML = <?php echo $temperatur2 ?>;
                    document.getElementById("wert_lichtstunden").innerHTML = <?php echo $lichtstunden2 ?>;
                    document.getElementById("wert_wassermenge").innerHTML = <?php echo $wassermenge2 ?>;
                    document.getElementById("wert_luftfeuchtigkeit").innerHTML = <?php echo $luftfeuchtigkeit2 ?>;
                } else if (value == 3) {
                    document.getElementById("pflanze").value = <?php echo $pflanze3 ?>;
                    document.getElementById("temperatur").value = <?php echo $temperatur3 ?>;
                    document.getElementById("lichtstunden").value = <?php echo $lichtstunden3 ?>;
                    document.getElementById("wassermenge").value = <?php echo $wassermenge3 ?>;
                    document.getElementById("luftfeuchtigkeit").value = <?php echo $luftfeuchtigkeit3 ?>;
                    document.getElementById("wert_temperatur").innerHTML = <?php echo $temperatur3 ?>;
                    document.getElementById("wert_lichtstunden").innerHTML = <?php echo $lichtstunden3 ?>;
                    document.getElementById("wert_wassermenge").innerHTML = <?php echo $wassermenge3 ?>;
                    document.getElementById("wert_luftfeuchtigkeit").innerHTML = <?php echo $luftfeuchtigkeit3 ?>;
                } else if (value == 4) {
                    document.getElementById("pflanze").value = <?php echo $pflanze4 ?>;
                    document.getElementById("temperatur").value = <?php echo $temperatur4 ?>;
                    document.getElementById("lichtstunden").value = <?php echo $lichtstunden4 ?>;
                    document.getElementById("wassermenge").value = <?php echo $wassermenge4 ?>;
                    document.getElementById("luftfeuchtigkeit").value = <?php echo $luftfeuchtigkeit4 ?>;
                    document.getElementById("wert_temperatur").innerHTML = <?php echo $temperatur4 ?>;
                    document.getElementById("wert_lichtstunden").innerHTML = <?php echo $lichtstunden4 ?>;
                    document.getElementById("wert_wassermenge").innerHTML = <?php echo $wassermenge4 ?>;
                    document.getElementById("wert_luftfeuchtigkeit").innerHTML = <?php echo $luftfeuchtigkeit4 ?>;
                } else if (value == 5) {
                    document.getElementById("pflanze").value = <?php echo $pflanze5 ?>;
                    document.getElementById("temperatur").value = <?php echo $temperatur5 ?>;
                    document.getElementById("lichtstunden").value = <?php echo $lichtstunden5 ?>;
                    document.getElementById("wassermenge").value = <?php echo $wassermenge5 ?>;
                    document.getElementById("luftfeuchtigkeit").value = <?php echo $luftfeuchtigkeit5 ?>;
                    document.getElementById("wert_temperatur").innerHTML = <?php echo $temperatur5 ?>;
                    document.getElementById("wert_lichtstunden").innerHTML = <?php echo $lichtstunden5 ?>;
                    document.getElementById("wert_wassermenge").innerHTML = <?php echo $wassermenge5 ?>;
                    document.getElementById("wert_luftfeuchtigkeit").innerHTML = <?php echo $luftfeuchtigkeit5 ?>;
                } else if (value == 6) {
                    document.getElementById("pflanze").value = <?php echo $pflanze6 ?>;
                    document.getElementById("temperatur").value = <?php echo $temperatur6 ?>;
                    document.getElementById("lichtstunden").value = <?php echo $lichtstunden6 ?>;
                    document.getElementById("wassermenge").value = <?php echo $wassermenge6 ?>;
                    document.getElementById("luftfeuchtigkeit").value = <?php echo $luftfeuchtigkeit6 ?>;
                    document.getElementById("wert_temperatur").innerHTML = <?php echo $temperatur6 ?>;
                    document.getElementById("wert_lichtstunden").innerHTML = <?php echo $lichtstunden6 ?>;
                    document.getElementById("wert_wassermenge").innerHTML = <?php echo $wassermenge6 ?>;
                    document.getElementById("wert_luftfeuchtigkeit").innerHTML = <?php echo $luftfeuchtigkeit6 ?>;
                } else if (value == 7) {
                    document.getElementById("pflanze").value = <?php echo $pflanze7 ?>;
                    document.getElementById("temperatur").value = <?php echo $temperatur7 ?>;
                    document.getElementById("lichtstunden").value = <?php echo $lichtstunden7 ?>;
                    document.getElementById("wassermenge").value = <?php echo $wassermenge7 ?>;
                    document.getElementById("luftfeuchtigkeit").value = <?php echo $luftfeuchtigkeit7 ?>;
                    document.getElementById("wert_temperatur").innerHTML = <?php echo $temperatur7 ?>;
                    document.getElementById("wert_lichtstunden").innerHTML = <?php echo $lichtstunden7 ?>;
                    document.getElementById("wert_wassermenge").innerHTML = <?php echo $wassermenge7 ?>;
                    document.getElementById("wert_luftfeuchtigkeit").innerHTML = <?php echo $luftfeuchtigkeit7 ?>;
                } else if (value == 8) {
                    document.getElementById("pflanze").value = <?php echo $pflanze8 ?>;
                    document.getElementById("temperatur").value = <?php echo $temperatur8 ?>;
                    document.getElementById("lichtstunden").value = <?php echo $lichtstunden8 ?>;
                    document.getElementById("wassermenge").value = <?php echo $wassermenge8 ?>;
                    document.getElementById("luftfeuchtigkeit").value = <?php echo $luftfeuchtigkeit8 ?>;
                    document.getElementById("wert_temperatur").innerHTML = <?php echo $temperatur8 ?>;
                    document.getElementById("wert_lichtstunden").innerHTML = <?php echo $lichtstunden8 ?>;
                    document.getElementById("wert_wassermenge").innerHTML = <?php echo $wassermenge8 ?>;
                    document.getElementById("wert_luftfeuchtigkeit").innerHTML = <?php echo $luftfeuchtigkeit8 ?>;
                } else if (value == 9) {
                    document.getElementById("pflanze").value = <?php echo $pflanze9 ?>;
                    document.getElementById("temperatur").value = <?php echo $temperatur9 ?>;
                    document.getElementById("lichtstunden").value = <?php echo $lichtstunden9 ?>;
                    document.getElementById("wassermenge").value = <?php echo $wassermenge9 ?>;
                    document.getElementById("luftfeuchtigkeit").value = <?php echo $luftfeuchtigkeit9 ?>;
                    document.getElementById("wert_temperatur").innerHTML = <?php echo $temperatur9 ?>;
                    document.getElementById("wert_lichtstunden").innerHTML = <?php echo $lichtstunden9 ?>;
                    document.getElementById("wert_wassermenge").innerHTML = <?php echo $wassermenge9 ?>;
                    document.getElementById("wert_luftfeuchtigkeit").innerHTML = <?php echo $luftfeuchtigkeit9 ?>;
                } else if (value == 10) {
                    document.getElementById("pflanze").value = <?php echo $pflanze10 ?>;
                    document.getElementById("temperatur").value = <?php echo $temperatur10 ?>;
                    document.getElementById("lichtstunden").value = <?php echo $lichtstunden10 ?>;
                    document.getElementById("wassermenge").value = <?php echo $wassermenge10 ?>;
                    document.getElementById("luftfeuchtigkeit").value = <?php echo $luftfeuchtigkeit10 ?>;
                    document.getElementById("wert_temperatur").innerHTML = <?php echo $temperatur10 ?>;
                    document.getElementById("wert_lichtstunden").innerHTML = <?php echo $lichtstunden10 ?>;
                    document.getElementById("wert_wassermenge").innerHTML = <?php echo $wassermenge10 ?>;
                    document.getElementById("wert_luftfeuchtigkeit").innerHTML = <?php echo $luftfeuchtigkeit10 ?>;
                }
            }
            var url = window.location.href;
            var error_msg = document.getElementById('error_div');
            var success_msg = document.getElementById('success_div');
            if ( url.search( 'fehler' ) > 0 ) {
                error_msg.style.display = "flex";
                success_msg.style.display = "none";
            }
            else if ( url.search( 'erfolgreich' ) > 0 ) {
                success_msg.style.display = "flex";
                error_msg.style.display = "none";
            }
        </script>
    </body>
</html>