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
        $parameter_slot = $row["parameter_slot"];
        $pflanze1 = $row["pflanze"];
        $temperatur1 = $row["temperatur"];
        $lichtstunden1 = $row["lichtstunden"];
        $wassermenge1 = $row["wassermenge"];
        $luftfeuchtigkeit1 = $row["luftfeuchtigkeit"];
    }
}
$conn->close();

$arr = [
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
