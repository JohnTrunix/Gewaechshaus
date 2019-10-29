<?php
// Die db_config beinhaltet die Verbindungsdaten der Datenbank
// und stellt bei ausführung eine Datenbankverbindung her.

// Verbindungsdaten
//======================================================================
// Datenbank Adresse
$servername = "localhost";
// Benutzername
$username = "datenbank";
// Passwort
$password = "rasp";
// Datenbank
$dbname = "datenbank";
//======================================================================

// Datenbankverbindung herstellen
//======================================================================
$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Datenbank connection failed: " . $conn->connect_error);
}
//======================================================================
