<?php
$servername = "localhost";
$username = "datenbank";
$password = "rasp";
$dbname = "datenbank";

$conn = mysqli_connect($servername, $username, $password, $dbname);

if (!$conn) {
    header("Location: /index.php?fehler");
    die();
}

$parameter_slot = $_GET['parameter_slot'];
$parameter_name = $_GET['parameter_name'];
$programm_datum_ende = $_GET['programm_datum_ende'];
$programm_zeit_ende = $_GET['programm_zeit_ende'];
$programm_status = $_GET['programm_status'];
$datetime = date('Y-m-d H:i:s');

if ($parameter_slot < 1 || $number > 10) {
    header("Location: /index.php?fehler");
    die();
}

$sql1 = "DELETE FROM betriebsmodus WHERE ID = '1'";

$sql2 .= "INSERT INTO betriebsmodus (ID, parameter_slot, parameter_name, programm_status, datetime, programm_datum_ende, programm_zeit_ende)
VALUES ('1', '$parameter_slot', '$parameter_name', '$programm_status', '$datetime', '$programm_datum_ende', '$programm_zeit_ende')";

if (mysqli_query($conn, $sql1) && mysqli_query($conn, $sql2)) {
    header("Location: /index.php?erfolgreich");
} else {
    header("Location: /index.php?fehler");
    die();
}

mysqli_close($conn);
