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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-07-26 07:19:13.937667'),(2,'auth','0001_initial','2024-07-26 07:19:14.590050'),(3,'admin','0001_initial','2024-07-26 07:19:14.756582'),(4,'admin','0002_logentry_remove_auto_add','2024-07-26 07:19:14.764579'),(5,'admin','0003_logentry_add_action_flag_choices','2024-07-26 07:19:14.772474'),(6,'contenttypes','0002_remove_content_type_name','2024-07-26 07:19:14.844699'),(7,'auth','0002_alter_permission_name_max_length','2024-07-26 07:19:14.905720'),(8,'auth','0003_alter_user_email_max_length','2024-07-26 07:19:14.932699'),(9,'auth','0004_alter_user_username_opts','2024-07-26 07:19:14.937718'),(10,'auth','0005_alter_user_last_login_null','2024-07-26 07:19:14.985701'),(11,'auth','0006_require_contenttypes_0002','2024-07-26 07:19:14.988704'),(12,'auth','0007_alter_validators_add_error_messages','2024-07-26 07:19:14.994722'),(13,'auth','0008_alter_user_username_max_length','2024-07-26 07:19:15.048718'),(14,'auth','0009_alter_user_last_name_max_length','2024-07-26 07:19:15.099719'),(15,'auth','0010_alter_group_name_max_length','2024-07-26 07:19:15.112719'),(16,'auth','0011_update_proxy_permissions','2024-07-26 07:19:15.118700'),(17,'auth','0012_alter_user_first_name_max_length','2024-07-26 07:19:15.173703'),(18,'sessions','0001_initial','2024-07-26 07:19:15.222720'),(19,'uygulama','0001_initial','2024-07-26 07:19:15.238738'),(20,'uygulama','0002_arac_resim','2024-07-26 08:45:28.753811'),(21,'uygulama','0003_alter_arac_resim_rezervasyon','2024-07-26 11:16:41.800255'),(22,'uygulama','0004_alter_arac_resim','2024-07-26 11:22:18.078864'),(23,'uygulama','0005_alter_arac_resim','2024-07-26 11:37:31.652239'),(24,'uygulama','0006_musteri_alter_arac_resim','2024-07-29 05:18:15.690716'),(25,'uygulama','0005_musteri','2024-07-29 06:21:07.397053'),(26,'uygulama','0006_rezervasyon_musteri_rezervasyon_tc','2024-07-29 06:35:18.416292'),(27,'uygulama','0007_musteri_kullanici_adi_musteri_sifre','2024-07-29 08:32:41.722069'),(28,'uygulama','0008_alter_musteri_kullanici_adi_alter_musteri_sifre_and_more','2024-07-29 12:04:08.878329'),(29,'uygulama','0009_remove_rezervasyon_tc_rezervasyon_fiyat_and_more','2024-07-30 06:34:46.400638'),(30,'uygulama','0010_admin','2024-08-01 11:17:22.013102'),(31,'uygulama','0010_musteri_email_musteri_telefon','2024-08-02 11:06:30.706190'),(32,'uygulama','0011_admin','2024-08-02 11:08:29.205863'),(33,'uygulama','0012_alter_admin_password','2024-08-02 11:51:15.187781'),(34,'uygulama','0010_musteri_email','2024-08-05 07:30:01.348763'),(35,'uygulama','0011_contactmessage','2024-08-07 05:55:52.623459');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-23 16:30:05
