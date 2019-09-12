<?php
$servername = "localhost";
$username = "datenbank";
$password = "rasp";
$dbname = "datenbank";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT slot, pflanze, temperatur, lichtstunden, wassermenge, luftfeuchtigkeit FROM parameter";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
      $slot = $row["slot"];
      $pflanze = $row["pflanze"];
      $temperatur = $row["temperatur"];
      $lichtstunden = $row["lichtstunden"];
      $wassermenge = $row["wassermenge"];
      $luftfeuchtigkeit = $row["luftfeuchtigkeit"];
    }

  echo $slot;
  echo $pflanze;
  echo $temperatur;
  echo $lichtstunden;
  echo $wassermenge;
  echo $luftfeuchtigkeit;

} else {
    echo "FEHLER!!!";
}
$conn->close();
?>