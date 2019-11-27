-- phpMyAdmin SQL Dump
-- version 4.6.6deb4
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Erstellungszeit: 27. Nov 2019 um 23:30
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

CREATE TABLE `betriebsmodus` (
  `ID` int(11) NOT NULL,
  `parameter_slot` int(11) NOT NULL,
  `programm_status` int(11) NOT NULL,
  `datetime` datetime NOT NULL,
  `programm_datum_ende` date NOT NULL,
  `programm_zeit_ende` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Daten für Tabelle `betriebsmodus`
--

INSERT INTO `betriebsmodus` (`ID`, `parameter_slot`, `programm_status`, `datetime`, `programm_datum_ende`, `programm_zeit_ende`) VALUES
(1, 2, 1, '2019-11-27 23:27:47', '2019-11-28', '14:00:00');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `parameter`
--

CREATE TABLE `parameter` (
  `slot` int(11) NOT NULL,
  `pflanze` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `temperatur` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `lichtstunden` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `wassermenge` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `luftfeuchtigkeit` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Daten für Tabelle `parameter`
--

INSERT INTO `parameter` (`slot`, `pflanze`, `temperatur`, `lichtstunden`, `wassermenge`, `luftfeuchtigkeit`) VALUES
(3, 'Default3', '26', '8', '6', '56'),
(4, 'Default4', '31', '15', '6', '51'),
(5, 'Default5', '29', '15', '6', '64'),
(7, 'Default7', '28', '6', '6', '54'),
(2, 'Default2', '31', '14', '4', '64'),
(1, 'Default1', '30', '14', '3', '64'),
(6, 'Default6', '32', '16', '4', '65'),
(8, 'Default8', '33', '14', '7', '71'),
(9, 'Default9', '29', '13', '8', '52'),
(10, 'Default10', '27', '12', '9', '77');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `sensor_bodenfeuchtigkeit_1`
--

CREATE TABLE `sensor_bodenfeuchtigkeit_1` (
  `sensorwert` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `datetime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `sensor_licht_1`
--

CREATE TABLE `sensor_licht_1` (
  `sensorwert` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `datetime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `sensor_luftfeuchtigkeit_1`
--

CREATE TABLE `sensor_luftfeuchtigkeit_1` (
  `sensorwert` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `datetime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `sensor_temperatur_1`
--

CREATE TABLE `sensor_temperatur_1` (
  `sensorwert` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `datetime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `zwischenspeicher`
--

CREATE TABLE `zwischenspeicher` (
  `licht_zaehler` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `zwischenspeicher`
--

INSERT INTO `zwischenspeicher` (`licht_zaehler`) VALUES
(2);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
