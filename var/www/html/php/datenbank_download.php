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
    while ($row = $result->fetch_assoc()) {
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
