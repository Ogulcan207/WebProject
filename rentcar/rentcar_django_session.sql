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
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('47khuy3ol4b1uiymn832j1s2o2jk3r4s','.eJxVjMEOwiAQRP-FsyHA0kU8eu83kIVFqRqalPZk_Hdp0oMe5jLvzbxFoG0tYWt5CROLi9Di9NtFSs9cd8APqvdZprmuyxTlrsiDNjnOnF_Xw_07KNRKX8cEoAwiYfRgtXXeo_Um6zMpSsTMxkV3gyEC-57BYFJAyEgdeBCfL88XN5k:1sawYY:R4n3p9EttROTHheSqtTmzO_54SFPfczqtnD-TJgIhuI','2024-08-19 12:11:18.468132'),('5t2g2eqacwmd2qhq519vub0809gswwgs','.eJxVj8sOgyAQRf-FtSFDEdQuu-83mAGGah9iAJvYpv9eNS7a7b3nnsy8WYtT7topUWx7x45MsuI3M2hvNKyFu-JwCdyGIcfe8BXhe5v4OTi6n3b2T9Bh6pa1aBzKRlOlhal1LcAp6Ul5KFErA97YxksSQtWuosqQVujBl8p6PDQI61WbLs8jLbrHlDLFfkkjvSg-Mc1h2B6QomA5ZLy3Y-ztwkoA4PD5AnlhTXM:1tHMRL:OCyVrKtfpZk9zqTEtBH3YwPb50KUInSerUzUyScR-gQ','2024-12-14 12:19:11.520882'),('b43jrs3ezp4roczumdwr9krh6c3lh9hi','eyJzdGFydF9kYXRlIjoiIiwiZW5kX2RhdGUiOiIifQ:1siAg7:brKgULnPzNPQXapaL_CzZSP7h0GcRQGyWi9G-d8-MrY','2024-09-08 10:40:59.771890'),('vk4ugq49yryftkjhjmz72lor2baaoba1','.eJxVjMsOwiAQRf-FtSGVx0Bduu83kBkGpGogKe3K-O_apAvd3nPOfYmA21rC1tMSZhYXocTpdyOMj1R3wHestyZjq-syk9wVedAup8bpeT3cv4OCvXzrDOMwsIma2GLSWbFHDxGyVQwEyZI3Z--IsjajN8pFyimSc2SQwJF4fwD-zTjS:1savcH:XbvN6tC_LRJjRrYb2Yy9nIwdbQOl87jqOtJW9JOlhco','2024-08-19 11:11:05.546147');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
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
