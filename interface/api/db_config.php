<?php
// Datenbank Verbindungsdaten
//======================================================================
$servername = "localhost";
$username = "datenbank";
$password = "rasp";
$dbname = "datenbank";
//======================================================================

// Datenbankverbindung herstellen
//======================================================================
$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Datenbank connection failed: " . $conn->connect_error);
}
//======================================================================
