<?php
$servername = "localhost";
$username = "datenbank";
$password = "rasp";
$dbname = "datenbank";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT parameter_slot, parameter_name, programm_status, datetime FROM betriebsmodus";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $parameter_slot = $row["parameter_slot"];
        $parameter_name = $row["parameter_name"];
        $programm_status = $row["programm_status"];
        $datetime = $row["datetime"];
    }
}
$conn->close();

$get_betriebsmodus_daten = [
    ['parameter_slot' => $parameter_slot, 'parameter_name' => $parameter_name, 'programm_status' => $programm_status, 'datetime' => $datetime],
];
