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
            $pflanze1 = $row["pflanze"];
        } else if ($row["slot"] == 2) {
            $pflanze2 = $row["pflanze"];
        } else if ($row["slot"] == 3) {
            $pflanze3 = $row["pflanze"];
        } else if ($row["slot"] == 4) {
            $pflanze4 = $row["pflanze"];
        } else if ($row["slot"] == 5) {
            $pflanze5 = $row["pflanze"];
        } else if ($row["slot"] == 6) {
            $pflanze6 = $row["pflanze"];
        } else if ($row["slot"] == 7) {
            $pflanze7 = $row["pflanze"];
        } else if ($row["slot"] == 8) {
            $pflanze8 = $row["pflanze"];
        } else if ($row["slot"] == 9) {
            $pflanze9 = $row["pflanze"];
        } else if ($row["slot"] == 10) {
            $pflanze10 = $row["pflanze"];
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
        <script>
        pflanze1 = "<?php echo $pflanze1 ?>";
        pflanze2 = "<?php echo $pflanze2 ?>";
        pflanze3 = "<?php echo $pflanze3 ?>";
        pflanze4 = "<?php echo $pflanze4 ?>";
        pflanze5 = "<?php echo $pflanze5 ?>";
        pflanze6 = "<?php echo $pflanze6 ?>";
        pflanze7 = "<?php echo $pflanze7 ?>";
        pflanze8 = "<?php echo $pflanze8 ?>";
        pflanze9 = "<?php echo $pflanze9 ?>";
        pflanze10 = "<?php echo $pflanze10 ?>";
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
		<script src="js/jquery.min.js"></script>
		<script src="js/drop-down.js"></script>
			<div class=navigation_oben>
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
        </script>
    </body>
</html>

