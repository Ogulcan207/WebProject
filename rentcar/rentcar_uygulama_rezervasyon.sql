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
-- Table structure for table `uygulama_rezervasyon`
--

DROP TABLE IF EXISTS `uygulama_rezervasyon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `uygulama_rezervasyon` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `baslangic_tarihi` date NOT NULL,
  `bitis_tarihi` date NOT NULL,
  `arac_id` bigint NOT NULL,
  `musteri_id` bigint NOT NULL,
  `fiyat` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `uygulama_rezervasyon_arac_id_2b4ca760_fk_uygulama_arac_id` (`arac_id`),
  KEY `uygulama_rezervasyon_musteri_id_68750486_fk_uygulama_musteri_id` (`musteri_id`),
  CONSTRAINT `uygulama_rezervasyon_arac_id_2b4ca760_fk_uygulama_arac_id` FOREIGN KEY (`arac_id`) REFERENCES `uygulama_arac` (`id`),
  CONSTRAINT `uygulama_rezervasyon_musteri_id_68750486_fk_uygulama_musteri_id` FOREIGN KEY (`musteri_id`) REFERENCES `uygulama_musteri` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `uygulama_rezervasyon`
--

LOCK TABLES `uygulama_rezervasyon` WRITE;
/*!40000 ALTER TABLE `uygulama_rezervasyon` DISABLE KEYS */;
INSERT INTO `uygulama_rezervasyon` VALUES (18,'2024-08-13','2024-08-22',1,1,18000.00),(20,'2024-08-05','2024-08-15',6,1,80000.00),(25,'2024-08-05','2024-08-22',4,2,51000.00),(26,'2024-08-20','2024-08-25',5,1,3750.00),(30,'2024-08-31','2024-09-07',6,1,56000.00),(31,'2024-11-28','2024-11-30',3,2,3000.00);
/*!40000 ALTER TABLE `uygulama_rezervasyon` ENABLE KEYS */;
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
