<?php
$servername = "localhost";
$username = "datenbank";
$password = "rasp";
$dbname = "datenbank";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT slot, pflanze, temperatur, lichtstunden, wassermenge, luftfeuchtigkeit FROM parameter ORDER BY slot";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        if ($row["slot"] == 1) {
            $slot1 = $row["slot"];
            $pflanze1 = $row["pflanze"];
            $temperatur1 = $row["temperatur"];
            $lichtstunden1 = $row["lichtstunden"];
            $wassermenge1 = $row["wassermenge"];
            $luftfeuchtigkeit1 = $row["luftfeuchtigkeit"];
        } else if ($row["slot"] == 2) {
            $slot2 = $row["slot"];
            $pflanze2 = $row["pflanze"];
            $temperatur2 = $row["temperatur"];
            $lichtstunden2 = $row["lichtstunden"];
            $wassermenge2 = $row["wassermenge"];
            $luftfeuchtigkeit2 = $row["luftfeuchtigkeit"];
        } else if ($row["slot"] == 3) {
            $slot3 = $row["slot"];
            $pflanze3 = $row["pflanze"];
            $temperatur3 = $row["temperatur"];
            $lichtstunden3 = $row["lichtstunden"];
            $wassermenge3 = $row["wassermenge"];
            $luftfeuchtigkeit3 = $row["luftfeuchtigkeit"];
        } else if ($row["slot"] == 4) {
            $slot4 = $row["slot"];
            $pflanze4 = $row["pflanze"];
            $temperatur4 = $row["temperatur"];
            $lichtstunden4 = $row["lichtstunden"];
            $wassermenge4 = $row["wassermenge"];
            $luftfeuchtigkeit4 = $row["luftfeuchtigkeit"];
        } else if ($row["slot"] == 5) {
            $slot5 = $row["slot"];
            $pflanze5 = $row["pflanze"];
            $temperatur5 = $row["temperatur"];
            $lichtstunden5 = $row["lichtstunden"];
            $wassermenge5 = $row["wassermenge"];
            $luftfeuchtigkeit5 = $row["luftfeuchtigkeit"];
        } else if ($row["slot"] == 6) {
            $slot6 = $row["slot"];
            $pflanze6 = $row["pflanze"];
            $temperatur6 = $row["temperatur"];
            $lichtstunden6 = $row["lichtstunden"];
            $wassermenge6 = $row["wassermenge"];
            $luftfeuchtigkeit6 = $row["luftfeuchtigkeit"];
        } else if ($row["slot"] == 7) {
            $slot7 = $row["slot"];
            $pflanze7 = $row["pflanze"];
            $temperatur7 = $row["temperatur"];
            $lichtstunden7 = $row["lichtstunden"];
            $wassermenge7 = $row["wassermenge"];
            $luftfeuchtigkeit7 = $row["luftfeuchtigkeit"];
        } else if ($row["slot"] == 8) {
            $slot8 = $row["slot"];
            $pflanze8 = $row["pflanze"];
            $temperatur8 = $row["temperatur"];
            $lichtstunden8 = $row["lichtstunden"];
            $wassermenge8 = $row["wassermenge"];
            $luftfeuchtigkeit8 = $row["luftfeuchtigkeit"];
        } else if ($row["slot"] == 9) {
            $slot9 = $row["slot"];
            $pflanze9 = $row["pflanze"];
            $temperatur9 = $row["temperatur"];
            $lichtstunden9 = $row["lichtstunden"];
            $wassermenge9 = $row["wassermenge"];
            $luftfeuchtigkeit9 = $row["luftfeuchtigkeit"];
        } else if ($row["slot"] == 10) {
            $slot10 = $row["slot"];
            $pflanze10 = $row["pflanze"];
            $temperatur10 = $row["temperatur"];
            $lichtstunden10 = $row["lichtstunden"];
            $wassermenge10 = $row["wassermenge"];
            $luftfeuchtigkeit10 = $row["luftfeuchtigkeit"];
        }
    }
}
$conn->close();
?>
<!DOCTYPE html>
<html>
    <head>
        <title>Gewaechshaus Raspberry Pi 3B+</title>
        <link rel="stylesheet" href="style.css">
        <script src="js/jquery.min.js"></script>
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
            <div class="icon shutdown" onclick="window.location='/herunterfahren.php';">
                <img src="img/logout.svg" class="menubild">
            </div>
        </div>
        <div class="mitte">
            <form action="parameter-update.php">
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
                    document.getElementById("pflanze").value = pflanze1;
                    document.getElementById("temperatur").value = temperatur1;
                    document.getElementById("lichtstunden").value = lichtstunden1;
                    document.getElementById("wassermenge").value = wassermenge1;
                    document.getElementById("luftfeuchtigkeit").value = luftfeuchtigkeit1;
                    document.getElementById("wert_temperatur").innerHTML = temperatur1;
                    document.getElementById("wert_lichtstunden").innerHTML = lichtstunden1;
                    document.getElementById("wert_wassermenge").innerHTML = wassermenge1;
                    document.getElementById("wert_luftfeuchtigkeit").innerHTML = luftfeuchtigkeit1;
                } else if (value == 2) {
                    document.getElementById("pflanze").value = pflanze2;
                    document.getElementById("temperatur").value = temperatur2;
                    document.getElementById("lichtstunden").value = lichtstunden2;
                    document.getElementById("wassermenge").value = wassermenge2;
                    document.getElementById("luftfeuchtigkeit").value = luftfeuchtigkeit2;
                    document.getElementById("wert_temperatur").innerHTML = temperatur2;
                    document.getElementById("wert_lichtstunden").innerHTML = lichtstunden2;
                    document.getElementById("wert_wassermenge").innerHTML = wassermenge2;
                    document.getElementById("wert_luftfeuchtigkeit").innerHTML = luftfeuchtigkeit2;
                } else if (value == 3) {
                    document.getElementById("pflanze").value = pflanze3;
                    document.getElementById("temperatur").value = temperatur3;
                    document.getElementById("lichtstunden").value = lichtstunden3;
                    document.getElementById("wassermenge").value = wassermenge3;
                    document.getElementById("luftfeuchtigkeit").value = luftfeuchtigkeit3;
                    document.getElementById("wert_temperatur").innerHTML = temperatur3;
                    document.getElementById("wert_lichtstunden").innerHTML = lichtstunden3;
                    document.getElementById("wert_wassermenge").innerHTML = wassermenge3;
                    document.getElementById("wert_luftfeuchtigkeit").innerHTML = luftfeuchtigkeit3;
                } else if (value == 4) {
                    document.getElementById("pflanze").value = pflanze4;
                    document.getElementById("temperatur").value = temperatur4;
                    document.getElementById("lichtstunden").value = lichtstunden4;
                    document.getElementById("wassermenge").value = wassermenge4;
                    document.getElementById("luftfeuchtigkeit").value = luftfeuchtigkeit4;
                    document.getElementById("wert_temperatur").innerHTML = temperatur4;
                    document.getElementById("wert_lichtstunden").innerHTML = lichtstunden4;
                    document.getElementById("wert_wassermenge").innerHTML = wassermenge4;
                    document.getElementById("wert_luftfeuchtigkeit").innerHTML = luftfeuchtigkeit4;
                } else if (value == 5) {
                    document.getElementById("pflanze").value = pflanze5;
                    document.getElementById("temperatur").value = temperatur5;
                    document.getElementById("lichtstunden").value = lichtstunden5;
                    document.getElementById("wassermenge").value = wassermenge5;
                    document.getElementById("luftfeuchtigkeit").value = luftfeuchtigkeit5;
                    document.getElementById("wert_temperatur").innerHTML = temperatur5;
                    document.getElementById("wert_lichtstunden").innerHTML = lichtstunden5;
                    document.getElementById("wert_wassermenge").innerHTML = wassermenge5;
                    document.getElementById("wert_luftfeuchtigkeit").innerHTML = luftfeuchtigkeit5;
                } else if (value == 6) {
                    document.getElementById("pflanze").value = pflanze6;
                    document.getElementById("temperatur").value = temperatur6;
                    document.getElementById("lichtstunden").value = lichtstunden6;
                    document.getElementById("wassermenge").value = wassermenge6;
                    document.getElementById("luftfeuchtigkeit").value = luftfeuchtigkeit6;
                    document.getElementById("wert_temperatur").innerHTML = temperatur6;
                    document.getElementById("wert_lichtstunden").innerHTML = lichtstunden6;
                    document.getElementById("wert_wassermenge").innerHTML = wassermenge6;
                    document.getElementById("wert_luftfeuchtigkeit").innerHTML = luftfeuchtigkeit6;
                } else if (value == 7) {
                    document.getElementById("pflanze").value = pflanze7;
                    document.getElementById("temperatur").value = temperatur7;
                    document.getElementById("lichtstunden").value = lichtstunden7;
                    document.getElementById("wassermenge").value = wassermenge7;
                    document.getElementById("luftfeuchtigkeit").value = luftfeuchtigkeit7;
                    document.getElementById("wert_temperatur").innerHTML = temperatur7;
                    document.getElementById("wert_lichtstunden").innerHTML = lichtstunden7;
                    document.getElementById("wert_wassermenge").innerHTML = wassermenge7;
                    document.getElementById("wert_luftfeuchtigkeit").innerHTML = luftfeuchtigkeit7;
                } else if (value == 8) {
                    document.getElementById("pflanze").value = pflanze8;
                    document.getElementById("temperatur").value = temperatur8;
                    document.getElementById("lichtstunden").value = lichtstunden8;
                    document.getElementById("wassermenge").value = wassermenge8;
                    document.getElementById("luftfeuchtigkeit").value = luftfeuchtigkeit8;
                    document.getElementById("wert_temperatur").innerHTML = temperatur8;
                    document.getElementById("wert_lichtstunden").innerHTML = lichtstunden8;
                    document.getElementById("wert_wassermenge").innerHTML = wassermenge8;
                    document.getElementById("wert_luftfeuchtigkeit").innerHTML = luftfeuchtigkeit8;
                } else if (value == 9) {
                    document.getElementById("pflanze").value = pflanze9;
                    document.getElementById("temperatur").value = temperatur9;
                    document.getElementById("lichtstunden").value = lichtstunden9;
                    document.getElementById("wassermenge").value = wassermenge9;
                    document.getElementById("luftfeuchtigkeit").value = luftfeuchtigkeit9;
                    document.getElementById("wert_temperatur").innerHTML = temperatur9;
                    document.getElementById("wert_lichtstunden").innerHTML = lichtstunden9;
                    document.getElementById("wert_wassermenge").innerHTML = wassermenge9;
                    document.getElementById("wert_luftfeuchtigkeit").innerHTML = luftfeuchtigkeit9;
                } else if (value == 10) {
                    document.getElementById("pflanze").value = pflanze10;
                    document.getElementById("temperatur").value = temperatur10;
                    document.getElementById("lichtstunden").value = lichtstunden10;
                    document.getElementById("wassermenge").value = wassermenge10;
                    document.getElementById("luftfeuchtigkeit").value = luftfeuchtigkeit10;
                    document.getElementById("wert_temperatur").innerHTML = temperatur10;
                    document.getElementById("wert_lichtstunden").innerHTML = lichtstunden10;
                    document.getElementById("wert_wassermenge").innerHTML = wassermenge10;
                    document.getElementById("wert_luftfeuchtigkeit").innerHTML = luftfeuchtigkeit10;
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