<?php
$servername = "localhost";
$username = "datenbank";
$password = "rasp";
$dbname = "datenbank";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$slot1 = 1;
$pflanze1 = 0;
$temperatur1 = 0;
$lichtstunden1 = 0;
$wassermenge1 = 0;
$luftfeuchtigkeit1 = 0;
$slot2 = 2;
$pflanze2 = 0;
$temperatur2 = 0;
$lichtstunden2 = 0;
$wassermenge2 = 0;
$luftfeuchtigkeit2 = 0;
$slot3 = 3;
$pflanze3 = 0;
$temperatur3 = 0;
$lichtstunden3 = 0;
$wassermenge3 = 0;
$luftfeuchtigkeit3 = 0;
$slot4 = 4;
$pflanze4 = 0;
$temperatur4 = 0;
$lichtstunden4 = 0;
$wassermenge4 = 0;
$luftfeuchtigkeit4 = 0;
$slot5 = 5;
$pflanze5 = 0;
$temperatur5 = 0;
$lichtstunden5 = 0;
$wassermenge5 = 0;
$luftfeuchtigkeit5 = 0;
$slot6 = 6;
$pflanze6 = 0;
$temperatur6 = 0;
$lichtstunden6 = 0;
$wassermenge6 = 0;
$luftfeuchtigkeit6 = 0;
$slot7 = 7;
$pflanze7 = 0;
$temperatur7 = 0;
$lichtstunden7 = 0;
$wassermenge7 = 0;
$luftfeuchtigkeit7 = 0;
$slot8 = 8;
$pflanze8 = 0;
$temperatur8 = 0;
$lichtstunden8 = 0;
$wassermenge8 = 0;
$luftfeuchtigkeit8 = 0;
$slot9 = 9;
$pflanze9 = 0;
$temperatur9 = 0;
$lichtstunden9 = 0;
$wassermenge9 = 0;
$luftfeuchtigkeit9 = 0;
$slot10 = 10;
$pflanze10 = 0;
$temperatur10 = 0;
$lichtstunden10 = 0;
$wassermenge10 = 0;
$luftfeuchtigkeit10 = 0;

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

$get_parameter_daten = [
    ['pflanze' => $pflanze1, 'temperatur' => $temperatur1, 'lichtstunden' => $lichtstunden1, 'wassermenge' => $wassermenge1, 'luftfeuchtigkeit' => $luftfeuchtigkeit1],
    ['pflanze' => $pflanze2, 'temperatur' => $temperatur2, 'lichtstunden' => $lichtstunden2, 'wassermenge' => $wassermenge2, 'luftfeuchtigkeit' => $luftfeuchtigkeit2],
    ['pflanze' => $pflanze3, 'temperatur' => $temperatur3, 'lichtstunden' => $lichtstunden3, 'wassermenge' => $wassermenge3, 'luftfeuchtigkeit' => $luftfeuchtigkeit3],
    ['pflanze' => $pflanze4, 'temperatur' => $temperatur4, 'lichtstunden' => $lichtstunden4, 'wassermenge' => $wassermenge4, 'luftfeuchtigkeit' => $luftfeuchtigkeit4],
    ['pflanze' => $pflanze5, 'temperatur' => $temperatur5, 'lichtstunden' => $lichtstunden5, 'wassermenge' => $wassermenge5, 'luftfeuchtigkeit' => $luftfeuchtigkeit5],
    ['pflanze' => $pflanze6, 'temperatur' => $temperatur6, 'lichtstunden' => $lichtstunden6, 'wassermenge' => $wassermenge6, 'luftfeuchtigkeit' => $luftfeuchtigkeit6],
    ['pflanze' => $pflanze7, 'temperatur' => $temperatur7, 'lichtstunden' => $lichtstunden7, 'wassermenge' => $wassermenge7, 'luftfeuchtigkeit' => $luftfeuchtigkeit7],
    ['pflanze' => $pflanze8, 'temperatur' => $temperatur8, 'lichtstunden' => $lichtstunden8, 'wassermenge' => $wassermenge8, 'luftfeuchtigkeit' => $luftfeuchtigkeit8],
    ['pflanze' => $pflanze9, 'temperatur' => $temperatur9, 'lichtstunden' => $lichtstunden9, 'wassermenge' => $wassermenge9, 'luftfeuchtigkeit' => $luftfeuchtigkeit9],
    ['pflanze' => $pflanze10, 'temperatur' => $temperatur10, 'lichtstunden' => $lichtstunden10, 'wassermenge' => $wassermenge10, 'luftfeuchtigkeit' => $luftfeuchtigkeit10],
];