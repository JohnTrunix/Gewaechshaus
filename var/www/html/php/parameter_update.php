<?php
$servername = "localhost";
$username = "datenbank";
$password = "rasp";
$dbname = "datenbank";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
    header("Location: /einstellungen.php?fehler");
    die();
}

$slot = $_GET['slot'];
$pflanze = $_GET['name'];
$temperatur = $_GET['temperatur'];
$lichtstunden = $_GET['lichtstunden'];
$wassermenge = $_GET['wassermenge'];
$luftfeuchtigkeit = $_GET['luftfeuchtigkeit'];

if ($slot < 1 || $number > 10) {
    header("Location: /einstellungen.php?fehler");
    die();
}

$sql1 = "DELETE FROM parameter WHERE slot = '$slot'";

$sql2 .= "INSERT INTO parameter (slot, pflanze, temperatur, lichtstunden, wassermenge, luftfeuchtigkeit)
VALUES ('$slot', '$pflanze', '$temperatur', '$lichtstunden', '$wassermenge', '$luftfeuchtigkeit')";

if (mysqli_query($conn, $sql1) && mysqli_query($conn, $sql2)) {
    header("Location: /einstellungen.php?erfolgreich");
} else {
    header("Location: /einstellungen.php?fehler");
    die();
}

mysqli_close($conn);
