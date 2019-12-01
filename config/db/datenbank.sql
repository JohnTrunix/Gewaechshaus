SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

CREATE DATABASE IF NOT EXISTS `datenbank` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `datenbank`;

CREATE TABLE `betriebsmodus` (
  `ID` int(11) NOT NULL,
  `parameter_slot` int(11) NOT NULL,
  `programm_status` int(11) NOT NULL,
  `datetime` datetime NOT NULL,
  `programm_datum_ende` date NOT NULL,
  `programm_zeit_ende` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

INSERT INTO `betriebsmodus` (`ID`, `parameter_slot`, `programm_status`, `datetime`, `programm_datum_ende`, `programm_zeit_ende`) VALUES
(1, 1, 0, '0000-00-00 00:00:00', '0000-00-00', '00:00:00');

CREATE TABLE `betriebsmeldungen` (
  `datetime` datetime NOT NULL,
  `meldung` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `parameter` (
  `slot` int(11) NOT NULL,
  `pflanze` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `temperatur` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `lichtstunden` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `wassermenge` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `luftfeuchtigkeit` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

INSERT INTO `parameter` (`slot`, `pflanze`, `temperatur`, `lichtstunden`, `wassermenge`, `luftfeuchtigkeit`) VALUES
(1, 'Slot1', '28', '12', '5', '60'),
(2, 'Slot2', '28', '12', '5', '60'),
(3, 'Slot3', '28', '12', '5', '60'),
(4, 'Slot4', '28', '12', '5', '60'),
(5, 'Slot5', '28', '12', '5', '60'),
(6, 'Slot6', '28', '12', '5', '60'),
(7, 'Slot7', '28', '12', '5', '60'),
(8, 'Slot8', '28', '12', '5', '60'),
(9, 'Slot9', '28', '12', '5', '60'),
(10, 'Slot10', '28', '12', '5', '60');

CREATE TABLE `sensor_bodenfeuchtigkeit_1` (
  `sensorwert` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `datetime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

CREATE TABLE `sensor_licht_1` (
  `sensorwert` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `datetime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

CREATE TABLE `sensor_luftfeuchtigkeit_1` (
  `sensorwert` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `datetime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

CREATE TABLE `sensor_temperatur_1` (
  `sensorwert` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `datetime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

CREATE TABLE `zwischenspeicher` (
  `licht_zaehler` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `zwischenspeicher` (`licht_zaehler`) VALUES
(0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
