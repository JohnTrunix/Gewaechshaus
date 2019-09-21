<!DOCTYPE html>
<html>
    <head>
        <title>Gewaechshaus Raspberry Pi 3B+</title>
        <link rel="stylesheet" href="style.css">
        <meta http-equiv="refresh" content="20">
    </head>
    <body>
        <div class="menu_bar">
            <p class="menu_titel">Live Werte</p>
            <div class="sensorwert sensorwert_1">
                <img src="img/idea.svg" class="sensor_icon">
                <?php
                    $link = mysqli_connect("localhost", "datenbank", "rasp", "datenbank");
                    $str2="Lux";
                    $sql = "SELECT sensorwert FROM sensor_licht_1 ORDER BY zeit DESC LIMIT 1;";
                    if($result = mysqli_query($link, $sql)){
                        if(mysqli_num_rows($result) > 0){
                            while($row = mysqli_fetch_array($result)){
                                echo "<a class='sensor_zahl'>";
                                echo $row['sensorwert'] . " " . $str2;
                                echo "</a>";
                            }
                            mysqli_free_result($result);
                        }
                    }
                    ?>
                <a class="sensor_beschreibung">Lichtstärke</a>
            </div>
            <div class="sensorwert sensorwert_2">
                <img src="img/breeze.svg" class="sensor_icon">
                <?php
                    $link = mysqli_connect("localhost", "datenbank", "rasp", "datenbank");
                    $str2="%";
                    $sql = "SELECT sensorwert FROM sensor_luftfeuchtigkeit_1 ORDER BY zeit DESC LIMIT 1;";
                    if($result = mysqli_query($link, $sql)){
                        if(mysqli_num_rows($result) > 0){
                            while($row = mysqli_fetch_array($result)){
                                echo "<a class='sensor_zahl'>";
                                echo $row['sensorwert'] . " " . $str2;
                                echo "</a>";
                            }
                            mysqli_free_result($result);
                        }
                    }
                    ?>
                <a class="sensor_beschreibung">Luftfeuchtigkeit</a>
            </div>
            <div class="sensorwert sensorwert_3">
                <img src="img/thermometer.svg" class="sensor_icon">
                <?php
                    $link = mysqli_connect("localhost", "datenbank", "rasp", "datenbank");
                    $str2="°C";
                    $sql = "SELECT sensorwert FROM sensor_temperatur_1 ORDER BY zeit DESC LIMIT 1;";
                    if($result = mysqli_query($link, $sql)){
                        if(mysqli_num_rows($result) > 0){
                            while($row = mysqli_fetch_array($result)){
                                echo "<a class='sensor_zahl'>";
                                echo $row['sensorwert'] . " " . $str2;
                                echo "</a>";
                            }
                            mysqli_free_result($result);
                        }
                    }
                    ?>
                <a class="sensor_beschreibung">Temperatur</a>
            </div>
		</div>
    </body>
</html>

