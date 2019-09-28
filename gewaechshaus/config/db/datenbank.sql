-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 22. Sep 2019 um 20:32
-- Server-Version: 10.4.6-MariaDB
-- PHP-Version: 7.3.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `datenbank`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `betriebsmodus`
--
-- Erstellt am: 22. Sep 2019 um 14:19
--

CREATE TABLE `betriebsmodus` (
  `ID` int(11) NOT NULL,
  `parameter_slot` int(11) NOT NULL,
  `parameter_name` text COLLATE utf16_bin NOT NULL,
  `programm_status` text COLLATE utf16_bin NOT NULL,
  `datetime` datetime NOT NULL,
  `wasser_gegeben_heute` int(11) NOT NULL,
  `wasser_gegeben_total` int(11) NOT NULL,
  `licht_gegeben_heute` int(11) NOT NULL,
  `licht_gegeben_total` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_bin;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `parameter`
--
-- Erstellt am: 20. Sep 2019 um 18:41
--

CREATE TABLE `parameter` (
  `slot` int(11) NOT NULL,
  `pflanze` text COLLATE utf16_bin NOT NULL,
  `temperatur` int(11) NOT NULL,
  `lichtstunden` int(11) NOT NULL,
  `wassermenge` int(11) NOT NULL,
  `luftfeuchtigkeit` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_bin;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `sensor_bodenfeuchtigkeit_1`
--
-- Erstellt am: 22. Sep 2019 um 18:02
--

CREATE TABLE `sensor_bodenfeuchtigkeit_1` (
  `sensorwert` int(11) NOT NULL,
  `datetime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_bin;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `sensor_licht_1`
--
-- Erstellt am: 22. Sep 2019 um 13:33
--

CREATE TABLE `sensor_licht_1` (
  `sensorwert` int(11) NOT NULL,
  `datetime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_bin;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `sensor_luftfeuchtigkeit_1`
--
-- Erstellt am: 22. Sep 2019 um 13:33
--

CREATE TABLE `sensor_luftfeuchtigkeit_1` (
  `sensorwert` int(11) NOT NULL,
  `datetime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_bin;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `sensor_temperatur_1`
--
-- Erstellt am: 22. Sep 2019 um 13:33
--

CREATE TABLE `sensor_temperatur_1` (
  `sensorwert` int(11) NOT NULL,
  `datetime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_bin;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
