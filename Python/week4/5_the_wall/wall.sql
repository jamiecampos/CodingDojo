-- MySQL dump 10.13  Distrib 5.7.12, for osx10.9 (x86_64)
--
-- Host: 127.0.0.1    Database: the_wall
-- ------------------------------------------------------
-- Server version	5.6.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comment` text,
  `created_on` datetime DEFAULT NULL,
  `modified_on` datetime DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `message_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_comments_users1_idx` (`user_id`),
  KEY `fk_comments_messages1_idx` (`message_id`),
  CONSTRAINT `fk_comments_messages1` FOREIGN KEY (`message_id`) REFERENCES `messages` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_comments_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (13,'What are you working on right now?','2016-12-09 13:21:47','2016-12-09 13:21:47',6,18),(15,'Woo hoo!','2016-12-09 13:23:33','2016-12-09 13:23:33',7,19),(16,'Working on Flask & SQL for Python. The project is called the Wall.','2016-12-09 13:24:31','2016-12-09 13:24:31',5,18),(17,'Johnson Auto did a great job when my car was in an accident.','2016-12-09 13:44:59','2016-12-09 13:44:59',5,20),(18,'Stay FAR AWAY from Fields Auto Repair.','2016-12-09 13:45:48','2016-12-09 13:45:48',6,20);
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` text,
  `created_on` datetime DEFAULT NULL,
  `modified_on` datetime DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_messages_users1_idx` (`user_id`),
  CONSTRAINT `fk_messages_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (18,'Having a great time coding!','2016-12-09 13:19:57','2016-12-09 13:19:57',5),(19,'Can\'t wait for the weekend. Big plans.','2016-12-09 13:21:59','2016-12-09 13:21:59',6),(20,'Looking for recommendations. What\'s the best body shop around here?','2016-12-09 13:44:08','2016-12-09 13:44:08',7);
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `modified_on` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (5,'Jamie','Campos','jamie@jamie.com','$2b$12$lHFW6/dUrxNLI1ouvvWLO.yHA3P5SGrI4opY1C0eeX1NGrk1epzGW','2016-12-09 13:19:45','2016-12-09 13:19:45'),(6,'John','Smith','john@john.com','$2b$12$Oh96mnTh3tU0PQOKrXBPu.NtxsaQ8Akycb19DlfGGegH0Lp8Ca6vO','2016-12-09 13:21:37','2016-12-09 13:21:37'),(7,'Jane','Anderson','jane@jane.com','$2b$12$h3qfU9WsHUh/LBr8TCWum.u9BVWmIPQq01/9ggEAum.gCTJDVsrji','2016-12-09 13:23:26','2016-12-09 13:23:26');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-12-09 13:51:52
