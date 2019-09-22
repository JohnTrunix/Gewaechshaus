<?php
$servername = "localhost";
$username = "datenbank";
$password = "rasp";
$dbname = "datenbank";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sensor_luftfeuchtigkeit_1 = '0';

$sql_sensor_luftfeuchtigkeit_1 = "SELECT sensorwert FROM sensor_luftfeuchtigkeit_1 ORDER BY datetime DESC LIMIT 1;";

$result = $conn->query($sql_sensor_luftfeuchtigkeit_1);
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $sensor_luftfeuchtigkeit_1 = $row["sensorwert"];
    }
}

echo "$sensor_luftfeuchtigkeit_1";
