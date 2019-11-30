<?php
// Die API regelt die gesamte Kommunikation von Front- und Backend der Software.
// Requests welche Daten lesen enden mit _read
// Requests welche Daten schreiben enden mit _write

// Import der Datenbank Verbindungskonfiguration und der Variablen.
//======================================================================
require 'db_config.php';
require 'variablen.php';
//======================================================================

// Lese Betriebsmodus Daten
//======================================================================
if (isset($_GET['betriebsmodus_read'])) {
    $sql = "SELECT parameter_slot, programm_status, datetime, programm_datum_ende, programm_zeit_ende FROM betriebsmodus";
    $result = $conn->query($sql);
    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            $parameter_slot = $row["parameter_slot"];
            $programm_status = $row["programm_status"];
            $datetime = $row["datetime"];
            $programm_datum_ende = $row["programm_datum_ende"];
            $programm_zeit_ende = $row["programm_zeit_ende"];
        }
    }
    $conn->close();
    $get_betriebsmodus_daten = [
        ['parameter_slot' => $parameter_slot, 'programm_status' => $programm_status, 'datetime' => $datetime, 'programm_datum_ende' => $programm_datum_ende, 'programm_zeit_ende' => $programm_zeit_ende],
    ];
    echo json_encode($get_betriebsmodus_daten);
}
//======================================================================

// Schreibe Betriebsmodus Daten
//======================================================================
elseif (isset($_GET['betriebsmodus_write'])) {
    $parameter_slot = $_GET['parameter_slot'];
    $programm_status = $_GET['programm_status'];
    $datetime = date('Y-m-d H:i:s');
    $programm_datum_ende = $_GET['programm_datum_ende'];
    $programm_zeit_ende = $_GET['programm_zeit_ende'];
    if ($parameter_slot < 1 || $number > 10) {
        header("Location: /index.html?fehler");
        die();
    }
    $sql1 = "DELETE FROM betriebsmodus WHERE ID = '1'";
    $sql2 .= "INSERT INTO betriebsmodus (ID, parameter_slot, programm_status, datetime, programm_datum_ende, programm_zeit_ende)
	VALUES ('1', '$parameter_slot', '$programm_status', '$datetime', '$programm_datum_ende', '$programm_zeit_ende')";
    if (mysqli_query($conn, $sql1) && mysqli_query($conn, $sql2)) {
        header("Location: /index.html?erfolgreich");
    } else {
        header("Location: /index.html?fehler");
        die();
    }
    mysqli_close($conn);
}
//======================================================================

// Lese Parameter
//======================================================================
elseif (isset($_GET['parameter_read'])) {
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
    echo json_encode($get_parameter_daten);
}
//======================================================================

// Schreibe Parameter
//======================================================================
elseif (isset($_GET['parameter_write'])) {
    $slot = $_GET['slot'];
    $pflanze = $_GET['name'];
    $temperatur = $_GET['temperatur'];
    $lichtstunden = $_GET['lichtstunden'];
    $wassermenge = $_GET['wassermenge'];
    $luftfeuchtigkeit = $_GET['luftfeuchtigkeit'];
    if ($slot < 1 || $number > 10) {
        header("Location: /einstellungen.html?fehler");
        die();
    }
    $sql1 = "DELETE FROM parameter WHERE slot = '$slot'";
    $sql2 .= "INSERT INTO parameter (slot, pflanze, temperatur, lichtstunden, wassermenge, luftfeuchtigkeit)
	VALUES ('$slot', '$pflanze', '$temperatur', '$lichtstunden', '$wassermenge', '$luftfeuchtigkeit')";
    if (mysqli_query($conn, $sql1) && mysqli_query($conn, $sql2)) {
        header("Location: /einstellungen.html?erfolgreich");
    } else {
        header("Location: /einstellungen.html?fehler");
        die();
    }
    mysqli_close($conn);
}
//======================================================================

// Lese neueste Bodenfeuchtigkeit
//======================================================================
elseif (isset($_GET['bodenfeuchtigkeit_read'])) {
    $sql_sensor_bodenfeuchtigkeit_1 = "SELECT sensorwert FROM sensor_bodenfeuchtigkeit_1 ORDER BY datetime DESC LIMIT 1;";
    $result = $conn->query($sql_sensor_bodenfeuchtigkeit_1);
    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            $sensor_bodenfeuchtigkeit_1 = $row["sensorwert"];
        }
    }
    echo "$sensor_bodenfeuchtigkeit_1";
}
//======================================================================

// Lese neueste Lichtstärke
//======================================================================
elseif (isset($_GET['lichtstaerke_read'])) {
    $sql_sensor_licht_1 = "SELECT sensorwert FROM sensor_licht_1 ORDER BY datetime DESC LIMIT 1;";
    $result = $conn->query($sql_sensor_licht_1);
    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            $sensor_licht_1 = $row["sensorwert"];
        }
    }
    echo "$sensor_licht_1";
}
//======================================================================

// Lese neueste Luftfeuchtigkeit
//======================================================================
elseif (isset($_GET['luftfeuchtigkeit_read'])) {
    $sql_sensor_luftfeuchtigkeit_1 = "SELECT sensorwert FROM sensor_luftfeuchtigkeit_1 ORDER BY datetime DESC LIMIT 1;";
    $result = $conn->query($sql_sensor_luftfeuchtigkeit_1);
    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            $sensor_luftfeuchtigkeit_1 = $row["sensorwert"];
        }
    }
    echo "$sensor_luftfeuchtigkeit_1";
}
//======================================================================

// Lese neueste Temperatur
//======================================================================
elseif (isset($_GET['temperatur_read'])) {
    $sql_sensor_temperatur_1 = "SELECT sensorwert FROM sensor_temperatur_1 ORDER BY datetime DESC LIMIT 1;";
    $result = $conn->query($sql_sensor_temperatur_1);
    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            $sensor_temperatur_1 = $row["sensorwert"];
        }
    }
    echo "$sensor_temperatur_1";
}
//======================================================================

// Lese IP Adresse
//======================================================================
elseif (isset($_GET['ip_adresse_read'])) {
    echo $_SERVER['HTTP_HOST'];
}
//======================================================================

// Falscher API Request
//======================================================================
else {
    echo "falscher api request!";
}
//======================================================================
