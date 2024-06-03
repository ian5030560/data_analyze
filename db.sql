-- --------------------------------------------------------
-- 主機:                           127.0.0.1
-- 伺服器版本:                        11.2.2-MariaDB - mariadb.org binary distribution
-- 伺服器作業系統:                      Win64
-- HeidiSQL 版本:                  12.3.0.6589
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- 傾印 data_analyze 的資料庫結構
CREATE DATABASE IF NOT EXISTS `data_analyze` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `data_analyze`;

-- 傾印  資料表 data_analyze.cpi 結構
CREATE TABLE IF NOT EXISTS `cpi` (
  `year` int(11) NOT NULL AUTO_INCREMENT,
  `value` float DEFAULT NULL,
  PRIMARY KEY (`year`)
) ENGINE=InnoDB AUTO_INCREMENT=113 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 正在傾印表格  data_analyze.cpi 的資料：~22 rows (近似值)
INSERT INTO `cpi` (`year`, `value`) VALUES
	(91, 81.76),
	(92, 81.53),
	(93, 82.84),
	(94, 84.75),
	(95, 85.26),
	(96, 86.79),
	(97, 89.86),
	(98, 89.07),
	(99, 89.93),
	(100, 91.21),
	(101, 92.97),
	(102, 93.71),
	(103, 94.83),
	(104, 94.54),
	(105, 95.86),
	(106, 96.45),
	(107, 97.76),
	(108, 98.3),
	(109, 98.07),
	(110, 100),
	(111, 102.95),
	(112, 105.51);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
