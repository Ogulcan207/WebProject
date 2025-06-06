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
-- Table structure for table `uygulama_admin`
--

DROP TABLE IF EXISTS `uygulama_admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `uygulama_admin` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(800) NOT NULL,
  `email` varchar(100) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `uygulama_admin`
--

LOCK TABLES `uygulama_admin` WRITE;
/*!40000 ALTER TABLE `uygulama_admin` DISABLE KEYS */;
INSERT INTO `uygulama_admin` VALUES (5,'yigit','pbkdf2_sha256$720000$8mlDNq5WFopDpeVyP7Aisn$PqEQGFWz0x5sx0Hn4L4O/Tb4QXqOPlojKaoUZPo5hKE=','yigit.dikbas@hotmail.com',1),(6,'yigit12','pbkdf2_sha256$720000$qMDXeouzsghjDkPlHztRYd$+hFUafPhxUZeiqD6NXaQMWylS64EoThw4zMzAL8hqsY=','yigit.dikbas12@hotmail.com',1),(7,'yigit123','pbkdf2_sha256$720000$ijKyZ1qBRKUX7G2YpquWfj$1G/iuhTlu/uF5QsB5/8ac8sYOeAnbCagu5XEqbLeKd4=','yigit.dikbas123@hotmail.com',1),(8,'yigit1234','pbkdf2_sha256$720000$y5rQqFMpSkJXtAs3is7nwn$pG8b6CYZPyj/EBWZvnTjMwJqRJNB4K/SSDxVQE/EDfA=','yigit.dikbas1234@hotmail.com',1);
/*!40000 ALTER TABLE `uygulama_admin` ENABLE KEYS */;
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
