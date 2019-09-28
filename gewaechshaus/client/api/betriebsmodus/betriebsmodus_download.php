<?php
$servername = "localhost";
$username = "datenbank";
$password = "rasp";
$dbname = "datenbank";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$parameter_slot = '0';
$parameter_name = '0';
$programm_status = '0';
$datetime = '0';

$sql = "SELECT parameter_slot, parameter_name, programm_status, datetime, programm_datum_ende, programm_zeit_ende FROM betriebsmodus";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $parameter_slot = $row["parameter_slot"];
        $parameter_name = $row["parameter_name"];
        $programm_status = $row["programm_status"];
        $datetime = $row["datetime"];
        $programm_datum_ende = $row["programm_datum_ende"];
        $programm_zeit_ende = $row["programm_zeit_ende"];
    }
}
$conn->close();

$get_betriebsmodus_daten = [
    ['parameter_slot' => $parameter_slot, 'parameter_name' => $parameter_name, 'programm_status' => $programm_status, 'datetime' => $datetime, 'programm_datum_ende' => $programm_datum_ende, 'programm_zeit_ende' => $programm_zeit_ende],
];
