<?php
$servername = "localhost";
$username = "datenbank";
$password = "rasp";
$dbname = "datenbank";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sensor_bodenfeuchtigkeit_1 = '0';

$sql_sensor_bodenfeuchtigkeit_1 = "SELECT sensorwert FROM sensor_bodenfeuchtigkeit_1 ORDER BY datetime DESC LIMIT 1;";

$result = $conn->query($sql_sensor_bodenfeuchtigkeit_1);
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $sensor_bodenfeuchtigkeit_1 = $row["sensorwert"];
    }
}

echo "$sensor_bodenfeuchtigkeit_1";
