-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 28. Sep 2019 um 19:34
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

CREATE TABLE `betriebsmodus` (
  `ID` int(11) NOT NULL,
  `parameter_slot` int(11) NOT NULL,
  `parameter_name` text COLLATE utf16_bin NOT NULL,
  `programm_status` text COLLATE utf16_bin NOT NULL,
  `datetime` datetime NOT NULL,
  `programm_datum_ende` date NOT NULL,
  `programm_zeit_ende` time NOT NULL,
  `wasser_gegeben_heute` int(11) NOT NULL,
  `wasser_gegeben_total` int(11) NOT NULL,
  `licht_gegeben_heute` int(11) NOT NULL,
  `licht_gegeben_total` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_bin;

--
-- Daten für Tabelle `betriebsmodus`
--

INSERT INTO `betriebsmodus` (`ID`, `parameter_slot`, `parameter_name`, `programm_status`, `datetime`, `programm_datum_ende`, `programm_zeit_ende`, `wasser_gegeben_heute`, `wasser_gegeben_total`, `licht_gegeben_heute`, `licht_gegeben_total`) VALUES
(1, 1, 'Saas', 'start', '2019-09-28 19:32:51', '2019-09-29', '14:00:00', 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `parameter`
--

CREATE TABLE `parameter` (
  `slot` int(11) NOT NULL,
  `pflanze` text COLLATE utf16_bin NOT NULL,
  `temperatur` int(11) NOT NULL,
  `lichtstunden` int(11) NOT NULL,
  `wassermenge` int(11) NOT NULL,
  `luftfeuchtigkeit` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_bin;

--
-- Daten für Tabelle `parameter`
--

INSERT INTO `parameter` (`slot`, `pflanze`, `temperatur`, `lichtstunden`, `wassermenge`, `luftfeuchtigkeit`) VALUES
(1, 'Saas', 14, 17, 3, 71);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `sensor_bodenfeuchtigkeit_1`
--

CREATE TABLE `sensor_bodenfeuchtigkeit_1` (
  `sensorwert` int(11) NOT NULL,
  `datetime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_bin;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `sensor_licht_1`
--

CREATE TABLE `sensor_licht_1` (
  `sensorwert` int(11) NOT NULL,
  `datetime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_bin;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `sensor_luftfeuchtigkeit_1`
--

CREATE TABLE `sensor_luftfeuchtigkeit_1` (
  `sensorwert` int(11) NOT NULL,
  `datetime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_bin;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `sensor_temperatur_1`
--

CREATE TABLE `sensor_temperatur_1` (
  `sensorwert` int(11) NOT NULL,
  `datetime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_bin;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
