<?php
$servername = "localhost";
$username = "datenbank";
$password = "rasp";
$dbname = "datenbank";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT slot, pflanze, temperatur, lichtstunden, wassermenge, luftfeuchtigkeit FROM parameter WHERE slot=1";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        $slot = $row["slot"];
        $pflanze = $row["pflanze"];
        $temperatur = $row["temperatur"];
        $lichtstunden = $row["lichtstunden"];
        $wassermenge = $row["wassermenge"];
        $luftfeuchtigkeit = $row["luftfeuchtigkeit"];
    }
} else {
    echo "FEHLER!!!";
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
        slot1 = "<?php echo $slot ?>"; 
        pflanze1 = "<?php echo $pflanze ?>";
        temperatur1 = "<?php echo $temperatur ?>";
        lichtstunden1 = "<?php echo $lichtstunden ?>";
        wassermenge1 = "<?php echo $wassermenge ?>";
        luftfeuchtigkeit1 = "<?php echo $wassermenge ?>";
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
                <input required type="text" name="name" placeholder="Name">
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
                    document.getElementById("temperatur").value = temperatur1;
                    document.getElementById("lichtstunden").value = "75";
                    document.getElementById("wassermenge").value = "75";
                    document.getElementById("luftfeuchtigkeit").value = "75";
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