-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: rentcar
-- ------------------------------------------------------
-- Server version	8.0.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `uygulama_arac`
--

DROP TABLE IF EXISTS `uygulama_arac`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `uygulama_arac` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `marka` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  `yil` int NOT NULL,
  `fiyat` decimal(10,2) NOT NULL,
  `resim` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `uygulama_arac`
--

LOCK TABLES `uygulama_arac` WRITE;
/*!40000 ALTER TABLE `uygulama_arac` DISABLE KEYS */;
INSERT INTO `uygulama_arac` VALUES (1,'mercedes','g63',2022,2000.00,'arac_resimleri/mercedes_0cjIOFf.jpeg'),(3,'renault','clio',2022,1500.00,'arac_resimleri/renault_a4nGjfl.jpeg'),(4,'peugeot','408',2020,3000.00,'arac_resimleri/pejo.jpeg'),(5,'daica','sandero',2021,750.00,'arac_resimleri/dacia_CXx1hLy.jpeg'),(6,'lamborghini','aventador',2023,8000.00,'arac_resimleri/lamborghini_tRhLFdO.jpeg'),(7,'peugeot','3008',2020,4000.00,'arac_resimleri/peugeot_iZdHiEu.jpeg');
/*!40000 ALTER TABLE `uygulama_arac` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-23 16:30:04
