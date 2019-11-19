-- phpMyAdmin SQL Dump
-- version 4.6.6deb4
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Erstellungszeit: 19. Nov 2019 um 21:21
-- Server-Version: 10.1.38-MariaDB-0+deb9u1
-- PHP-Version: 7.0.33-0+deb9u6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
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
-- Erstellt am: 19. Nov 2019 um 20:18
--

CREATE TABLE `betriebsmodus` (
  `ID` int(11) NOT NULL,
  `parameter_slot` int(11) NOT NULL,
  `programm_status` text COLLATE utf8_bin NOT NULL,
  `datetime` datetime NOT NULL,
  `programm_datum_ende` date NOT NULL,
  `programm_zeit_ende` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Daten für Tabelle `betriebsmodus`
--

INSERT INTO `betriebsmodus` (`ID`, `parameter_slot`, `programm_status`, `datetime`, `programm_datum_ende`, `programm_zeit_ende`) VALUES
(1, 1, 'stop', '2019-11-03 20:35:06', '0000-00-00', '00:00:00');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `parameter`
--
-- Erstellt am: 19. Nov 2019 um 20:18
--

CREATE TABLE `parameter` (
  `slot` int(11) NOT NULL,
  `pflanze` text COLLATE utf8_bin NOT NULL,
  `temperatur` text COLLATE utf8_bin NOT NULL,
  `lichtstunden` text COLLATE utf8_bin NOT NULL,
  `wassermenge` text COLLATE utf8_bin NOT NULL,
  `luftfeuchtigkeit` text COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Daten für Tabelle `parameter`
--

INSERT INTO `parameter` (`slot`, `pflanze`, `temperatur`, `lichtstunden`, `wassermenge`, `luftfeuchtigkeit`) VALUES
(1, 'Default1', '27', '4.8', '0.3', '56'),
(2, 'Default2', '26', '5.3', '1', '56'),
(3, 'Default3', '30', '19.1', '0.3', '70'),
(4, 'Default4', '25', '5.9', '0.2', '55'),
(5, 'Default5', '25', '5.2', '0.2', '59'),
(6, 'Default6', '24', '23.6', '0.2', '63'),
(7, 'Default7', '24', '19', '0.3', '60'),
(8, 'Default8', '27', '6.3', '1', '61'),
(9, 'Default9', '27', '5.2', '0.1', '54'),
(10, 'Default10', '28', '7.8', '0.1', '68');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `sensor_bodenfeuchtigkeit_1`
--
-- Erstellt am: 19. Nov 2019 um 20:18
--

CREATE TABLE `sensor_bodenfeuchtigkeit_1` (
  `sensorwert` text COLLATE utf8_bin NOT NULL,
  `datetime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `sensor_licht_1`
--
-- Erstellt am: 19. Nov 2019 um 20:18
--

CREATE TABLE `sensor_licht_1` (
  `sensorwert` text COLLATE utf8_bin NOT NULL,
  `datetime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `sensor_luftfeuchtigkeit_1`
--
-- Erstellt am: 19. Nov 2019 um 20:18
--

CREATE TABLE `sensor_luftfeuchtigkeit_1` (
  `sensorwert` text COLLATE utf8_bin NOT NULL,
  `datetime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `sensor_temperatur_1`
--
-- Erstellt am: 19. Nov 2019 um 20:18
--

CREATE TABLE `sensor_temperatur_1` (
  `sensorwert` text COLLATE utf8_bin NOT NULL,
  `datetime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
