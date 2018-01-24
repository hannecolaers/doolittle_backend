-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: unleashed
-- ------------------------------------------------------
-- Server version	5.7.20-log

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add room',7,'add_room'),(20,'Can change room',7,'change_room'),(21,'Can delete room',7,'delete_room'),(22,'Can add space',8,'add_space'),(23,'Can change space',8,'change_space'),(24,'Can delete space',8,'delete_space'),(25,'Can add application',9,'add_application'),(26,'Can change application',9,'change_application'),(27,'Can delete application',9,'delete_application'),(28,'Can add access token',10,'add_accesstoken'),(29,'Can change access token',10,'change_accesstoken'),(30,'Can delete access token',10,'delete_accesstoken'),(31,'Can add grant',11,'add_grant'),(32,'Can change grant',11,'change_grant'),(33,'Can delete grant',11,'delete_grant'),(34,'Can add refresh token',12,'add_refreshtoken'),(35,'Can change refresh token',12,'change_refreshtoken'),(36,'Can delete refresh token',12,'delete_refreshtoken'),(37,'Can add association',13,'add_association'),(38,'Can change association',13,'change_association'),(39,'Can delete association',13,'delete_association'),(40,'Can add code',14,'add_code'),(41,'Can change code',14,'change_code'),(42,'Can delete code',14,'delete_code'),(43,'Can add nonce',15,'add_nonce'),(44,'Can change nonce',15,'change_nonce'),(45,'Can delete nonce',15,'delete_nonce'),(46,'Can add user social auth',16,'add_usersocialauth'),(47,'Can change user social auth',16,'change_usersocialauth'),(48,'Can delete user social auth',16,'delete_usersocialauth'),(49,'Can add partial',17,'add_partial'),(50,'Can change partial',17,'change_partial'),(51,'Can delete partial',17,'delete_partial'),(52,'Can add membership',18,'add_membership'),(53,'Can change membership',18,'change_membership'),(54,'Can delete membership',18,'delete_membership'),(55,'Can add squad',19,'add_squad'),(56,'Can change squad',19,'change_squad'),(57,'Can delete squad',19,'delete_squad'),(58,'Can add habitat',20,'add_habitat'),(59,'Can change habitat',20,'change_habitat'),(60,'Can delete habitat',20,'delete_habitat'),(61,'Can add employee',21,'add_employee'),(62,'Can change employee',21,'change_employee'),(63,'Can delete employee',21,'delete_employee');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(21,'employees','employee'),(7,'floorplan','room'),(8,'floorplan','space'),(20,'habitats','habitat'),(10,'oauth2_provider','accesstoken'),(9,'oauth2_provider','application'),(11,'oauth2_provider','grant'),(12,'oauth2_provider','refreshtoken'),(6,'sessions','session'),(13,'social_django','association'),(14,'social_django','code'),(15,'social_django','nonce'),(17,'social_django','partial'),(16,'social_django','usersocialauth'),(18,'squads','membership'),(19,'squads','squad');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-01-24 15:40:58.621473'),(2,'auth','0001_initial','2018-01-24 15:40:59.936656'),(3,'admin','0001_initial','2018-01-24 15:41:00.222469'),(4,'admin','0002_logentry_remove_auto_add','2018-01-24 15:41:00.237480'),(5,'contenttypes','0002_remove_content_type_name','2018-01-24 15:41:00.416431'),(6,'auth','0002_alter_permission_name_max_length','2018-01-24 15:41:00.575545'),(7,'auth','0003_alter_user_email_max_length','2018-01-24 15:41:00.710717'),(8,'auth','0004_alter_user_username_opts','2018-01-24 15:41:00.727731'),(9,'auth','0005_alter_user_last_login_null','2018-01-24 15:41:00.813784'),(10,'auth','0006_require_contenttypes_0002','2018-01-24 15:41:00.826464'),(11,'auth','0007_alter_validators_add_error_messages','2018-01-24 15:41:00.845585'),(12,'auth','0008_alter_user_username_max_length','2018-01-24 15:41:01.080622'),(13,'auth','0009_alter_user_last_name_max_length','2018-01-24 15:41:01.192530'),(14,'habitats','0001_initial','2018-01-24 15:41:01.250752'),(15,'employees','0001_initial','2018-01-24 15:41:01.422649'),(16,'floorplan','0001_initial','2018-01-24 15:41:01.746276'),(17,'oauth2_provider','0001_initial','2018-01-24 15:41:03.022560'),(18,'oauth2_provider','0002_08_updates','2018-01-24 15:41:03.710872'),(19,'oauth2_provider','0003_auto_20160316_1503','2018-01-24 15:41:04.159548'),(20,'oauth2_provider','0004_auto_20160525_1623','2018-01-24 15:41:04.544496'),(21,'oauth2_provider','0005_auto_20170514_1141','2018-01-24 15:41:08.130592'),(22,'sessions','0001_initial','2018-01-24 15:41:08.211582'),(23,'default','0001_initial','2018-01-24 15:41:08.745648'),(24,'social_auth','0001_initial','2018-01-24 15:41:08.754650'),(25,'default','0002_add_related_name','2018-01-24 15:41:08.904442'),(26,'social_auth','0002_add_related_name','2018-01-24 15:41:08.911430'),(27,'default','0003_alter_email_max_length','2018-01-24 15:41:09.012562'),(28,'social_auth','0003_alter_email_max_length','2018-01-24 15:41:09.019549'),(29,'default','0004_auto_20160423_0400','2018-01-24 15:41:09.038072'),(30,'social_auth','0004_auto_20160423_0400','2018-01-24 15:41:09.045095'),(31,'social_auth','0005_auto_20160727_2333','2018-01-24 15:41:09.101291'),(32,'social_django','0006_partial','2018-01-24 15:41:09.176410'),(33,'social_django','0007_code_timestamp','2018-01-24 15:41:09.305799'),(34,'social_django','0008_partial_timestamp','2018-01-24 15:41:09.422789'),(35,'squads','0001_initial','2018-01-24 15:41:09.856078'),(36,'social_django','0005_auto_20160727_2333','2018-01-24 15:41:09.868171'),(37,'social_django','0003_alter_email_max_length','2018-01-24 15:41:09.875975'),(38,'social_django','0002_add_related_name','2018-01-24 15:41:09.883302'),(39,'social_django','0004_auto_20160423_0400','2018-01-24 15:41:09.890308'),(40,'social_django','0001_initial','2018-01-24 15:41:09.897844');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees_employee`
--

DROP TABLE IF EXISTS `employees_employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employees_employee` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(40) NOT NULL,
  `function` varchar(50) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date DEFAULT NULL,
  `visible_site` tinyint(1) NOT NULL,
  `habitat_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `employees_employee_habitat_id_c6ac9fbd_fk_habitats_habitat_id` (`habitat_id`),
  CONSTRAINT `employees_employee_habitat_id_c6ac9fbd_fk_habitats_habitat_id` FOREIGN KEY (`habitat_id`) REFERENCES `habitats_habitat` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees_employee`
--

LOCK TABLES `employees_employee` WRITE;
/*!40000 ALTER TABLE `employees_employee` DISABLE KEYS */;
/*!40000 ALTER TABLE `employees_employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `floorplan_room`
--

DROP TABLE IF EXISTS `floorplan_room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `floorplan_room` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `type` varchar(30) NOT NULL,
  `color` varchar(8) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `floorplan_room`
--

LOCK TABLES `floorplan_room` WRITE;
/*!40000 ALTER TABLE `floorplan_room` DISABLE KEYS */;
INSERT INTO `floorplan_room` VALUES (1,'EMPTY','Empty','A9A9A9'),(2,'2FREEDOM','Workspace','8A2BE2'),(3,'THE_WORKSHOP','Workspace','FF69B4'),(4,'FINANCE','Workspace','FF8C00'),(5,'CEO','Workspace','8FBC8B'),(6,'PEOPLE','Workspace','E9967A'),(7,'KITCHEN','Kitchen','FF7F50'),(8,'VIKING_DEALS','Workspace','A52A2A'),(9,'JIM_MOBILE','Workspace','483D8B'),(10,'THE_ARENA','Workspace','FF0000'),(11,'STIEVIE','Workspace','4682B4'),(12,'TECHNOLOGY','Workspace','ADFF2F'),(13,'THE_BIG_ROOM','Workspace','4B0082'),(14,'THE_CHAT_ROOM','Workspace','B0C4DE'),(15,'MOBILE_VIKINGS_PRODUCT','Workspace','008B8B'),(16,'THE_SPOTLIGHT','Workspace','FFFF00'),(17,'DESIGN','Workspace','800000'),(18,'MOVILE_VIKINGS_GET_&_RETAIN','Workspace','191970'),(19,'THE_CLOUD','Workspace','0000FF'),(20,'THE_MILKYWAY','Workspace','008000'),(21,'THE_WINDOW_ROOM','Workspace','000080'),(22,'COPYROOM','Workspace','CD853F'),(23,'CUSTOMER_CARE','Workspace','800080');
/*!40000 ALTER TABLE `floorplan_room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `floorplan_space`
--

DROP TABLE IF EXISTS `floorplan_space`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `floorplan_space` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `x` int(11) NOT NULL,
  `y` int(11) NOT NULL,
  `employee_id` int(11) DEFAULT NULL,
  `room_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `floorplan_space_room_id_5b0c60d6_fk_floorplan_room_id` (`room_id`),
  CONSTRAINT `floorplan_space_room_id_5b0c60d6_fk_floorplan_room_id` FOREIGN KEY (`room_id`) REFERENCES `floorplan_room` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=664 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `floorplan_space`
--

LOCK TABLES `floorplan_space` WRITE;
/*!40000 ALTER TABLE `floorplan_space` DISABLE KEYS */;
INSERT INTO `floorplan_space` VALUES (1,0,12,0,2),(2,1,12,1,2),(3,2,12,1,2),(4,3,12,0,2),(5,4,12,0,2),(6,5,12,1,2),(7,6,12,1,2),(8,7,12,0,2),(9,8,12,0,2),(10,9,12,1,2),(11,10,12,1,2),(12,11,12,0,2),(13,12,12,0,2),(14,13,12,1,2),(15,14,12,1,2),(16,15,12,0,2),(17,16,12,0,3),(18,17,12,0,3),(19,18,12,0,3),(20,19,12,0,3),(21,20,12,0,3),(22,21,12,0,3),(23,22,12,0,3),(24,23,12,0,3),(25,24,12,0,4),(26,25,12,0,4),(27,26,12,0,4),(28,27,12,0,4),(29,28,12,0,4),(30,29,12,0,4),(31,30,12,0,4),(32,31,12,0,4),(33,32,12,0,5),(34,33,12,0,5),(35,34,12,0,5),(36,35,12,0,5),(37,36,12,0,5),(38,37,12,0,6),(39,38,12,0,6),(40,39,12,0,6),(41,40,12,0,6),(42,41,12,0,6),(43,42,12,0,6),(44,43,12,0,6),(45,44,12,0,7),(46,45,12,0,7),(47,46,12,0,7),(48,47,12,0,7),(49,48,12,0,7),(50,49,12,0,7),(51,50,12,0,7),(52,0,11,0,2),(53,1,11,1,2),(54,2,11,1,2),(55,3,11,0,2),(56,4,11,0,2),(57,5,11,1,2),(58,6,11,1,2),(59,7,11,0,2),(60,8,11,0,2),(61,9,11,1,2),(62,10,11,1,2),(63,11,11,0,2),(64,12,11,0,2),(65,13,11,1,2),(66,14,11,1,2),(67,15,11,0,2),(68,16,11,0,3),(69,17,11,0,3),(70,18,11,0,3),(71,19,11,0,3),(72,20,11,0,3),(73,21,11,0,3),(74,22,11,0,3),(75,23,11,0,3),(76,24,11,0,4),(77,25,11,0,4),(78,26,11,1,4),(79,27,11,1,4),(80,28,11,1,4),(81,29,11,1,4),(82,30,11,1,4),(83,31,11,0,4),(84,32,11,0,5),(85,33,11,1,5),(86,34,11,1,5),(87,35,11,1,5),(88,36,11,0,5),(89,37,11,0,6),(90,38,11,1,6),(91,39,11,1,6),(92,40,11,1,6),(93,41,11,1,6),(94,42,11,1,6),(95,43,11,0,6),(96,44,11,0,7),(97,45,11,0,7),(98,46,11,0,7),(99,47,11,0,7),(100,48,11,0,7),(101,49,11,0,7),(102,50,11,0,7),(103,0,10,0,2),(104,1,10,1,2),(105,2,10,1,2),(106,3,10,0,2),(107,4,10,0,2),(108,5,10,1,2),(109,6,10,1,2),(110,7,10,0,2),(111,8,10,0,2),(112,9,10,1,2),(113,10,10,1,2),(114,11,10,0,2),(115,12,10,0,2),(116,13,10,1,2),(117,14,10,1,2),(118,15,10,0,2),(119,16,10,0,3),(120,17,10,0,3),(121,18,10,0,3),(122,19,10,0,3),(123,20,10,0,3),(124,21,10,0,3),(125,22,10,0,3),(126,23,10,0,3),(127,24,10,0,4),(128,25,10,0,4),(129,26,10,0,4),(130,27,10,0,4),(131,28,10,0,4),(132,29,10,0,4),(133,30,10,0,4),(134,31,10,0,4),(135,32,10,0,5),(136,33,10,0,5),(137,34,10,0,5),(138,35,10,0,5),(139,36,10,0,5),(140,37,10,0,6),(141,38,10,0,6),(142,39,10,0,6),(143,40,10,0,6),(144,41,10,0,6),(145,42,10,0,6),(146,43,10,0,6),(147,44,10,0,7),(148,45,10,0,7),(149,46,10,0,7),(150,47,10,0,7),(151,48,10,0,7),(152,49,10,0,7),(153,50,10,0,7),(154,0,9,0,1),(155,1,9,0,1),(156,2,9,0,1),(157,3,9,0,1),(158,4,9,0,1),(159,5,9,0,1),(160,6,9,0,1),(161,7,9,0,1),(162,8,9,0,1),(163,9,9,0,1),(164,10,9,0,1),(165,11,9,0,1),(166,12,9,0,1),(167,13,9,0,1),(168,14,9,0,1),(169,15,9,0,1),(170,16,9,0,1),(171,17,9,0,1),(172,18,9,0,1),(173,19,9,0,1),(174,20,9,0,1),(175,21,9,0,1),(176,22,9,0,1),(177,23,9,0,1),(178,24,9,0,1),(179,25,9,0,1),(180,26,9,0,1),(181,27,9,0,1),(182,28,9,0,1),(183,29,9,0,1),(184,30,9,0,1),(185,31,9,0,1),(186,32,9,0,1),(187,33,9,0,1),(188,34,9,0,1),(189,35,9,0,1),(190,36,9,0,1),(191,37,9,0,1),(192,38,9,0,1),(193,39,9,0,1),(194,40,9,0,1),(195,41,9,0,1),(196,42,9,0,7),(197,43,9,0,7),(198,44,9,0,7),(199,45,9,0,7),(200,46,9,0,7),(201,47,9,0,7),(202,48,9,0,7),(203,49,9,0,7),(204,50,9,0,7),(205,0,8,0,1),(206,1,8,0,1),(207,2,8,0,1),(208,3,8,0,1),(209,4,8,0,1),(210,5,8,0,1),(211,6,8,0,1),(212,7,8,0,1),(213,8,8,0,1),(214,9,8,0,1),(215,10,8,0,1),(216,11,8,0,1),(217,12,8,0,1),(218,13,8,0,1),(219,14,8,0,1),(220,15,8,0,1),(221,16,8,0,1),(222,17,8,0,1),(223,18,8,0,1),(224,19,8,0,1),(225,20,8,0,1),(226,21,8,0,1),(227,22,8,0,1),(228,23,8,0,1),(229,24,8,0,1),(230,25,8,0,1),(231,26,8,0,1),(232,27,8,0,1),(233,28,8,0,1),(234,29,8,0,1),(235,30,8,0,1),(236,31,8,0,1),(237,32,8,0,1),(238,33,8,0,1),(239,34,8,0,1),(240,35,8,0,1),(241,36,8,0,1),(242,37,8,0,1),(243,38,8,0,1),(244,39,8,0,1),(245,40,8,0,1),(246,41,8,0,1),(247,42,8,0,7),(248,43,8,0,7),(249,44,8,0,7),(250,45,8,0,7),(251,46,8,0,7),(252,47,8,0,7),(253,48,8,0,7),(254,49,8,0,7),(255,50,8,0,7),(256,0,7,0,8),(257,1,7,1,8),(258,2,7,1,8),(259,3,7,0,8),(260,4,7,0,9),(261,5,7,1,9),(262,6,7,1,9),(263,7,7,0,9),(264,8,7,0,1),(265,9,7,0,1),(266,10,7,0,10),(267,11,7,0,10),(268,12,7,0,10),(269,13,7,0,10),(270,14,7,0,10),(271,15,7,0,11),(272,16,7,1,11),(273,17,7,1,11),(274,18,7,0,11),(275,19,7,0,1),(276,20,7,0,12),(277,21,7,1,12),(278,22,7,1,12),(279,23,7,0,12),(280,24,7,0,12),(281,25,7,1,12),(282,26,7,1,12),(283,27,7,0,12),(284,28,7,0,12),(285,29,7,1,12),(286,30,7,1,12),(287,31,7,0,12),(288,32,7,0,12),(289,33,7,1,12),(290,34,7,1,12),(291,35,7,0,12),(292,36,7,0,13),(293,37,7,0,13),(294,38,7,0,13),(295,39,7,0,13),(296,40,7,0,14),(297,41,7,0,14),(298,42,7,0,7),(299,43,7,0,7),(300,44,7,0,7),(301,45,7,0,7),(302,46,7,0,7),(303,47,7,0,7),(304,48,7,0,7),(305,49,7,0,7),(306,50,7,0,7),(307,0,6,0,8),(308,1,6,1,8),(309,2,6,1,8),(310,3,6,0,8),(311,4,6,0,9),(312,5,6,1,9),(313,6,6,1,9),(314,7,6,0,9),(315,8,6,0,1),(316,9,6,0,1),(317,10,6,0,10),(318,11,6,0,10),(319,12,6,0,10),(320,13,6,0,10),(321,14,6,0,10),(322,15,6,0,11),(323,16,6,1,11),(324,17,6,1,11),(325,18,6,0,11),(326,19,6,0,1),(327,20,6,0,12),(328,21,6,1,12),(329,22,6,1,12),(330,23,6,0,12),(331,24,6,0,12),(332,25,6,1,12),(333,26,6,1,12),(334,27,6,0,12),(335,28,6,0,12),(336,29,6,1,12),(337,30,6,1,12),(338,31,6,0,12),(339,32,6,0,12),(340,33,6,1,12),(341,34,6,1,12),(342,35,6,0,12),(343,36,6,0,13),(344,37,6,0,13),(345,38,6,0,13),(346,39,6,0,13),(347,40,6,0,14),(348,41,6,0,14),(349,42,6,0,7),(350,43,6,0,7),(351,44,6,0,7),(352,45,6,0,7),(353,46,6,0,7),(354,47,6,0,7),(355,48,6,0,7),(356,49,6,0,7),(357,50,6,0,7),(358,0,5,0,8),(359,1,5,1,8),(360,2,5,1,8),(361,3,5,0,8),(362,4,5,0,1),(363,5,5,0,1),(364,6,5,0,1),(365,7,5,0,1),(366,8,5,0,1),(367,9,5,0,1),(368,10,5,0,10),(369,11,5,0,10),(370,12,5,0,10),(371,13,5,0,10),(372,14,5,0,10),(373,15,5,0,11),(374,16,5,1,11),(375,17,5,1,11),(376,18,5,0,11),(377,19,5,0,1),(378,20,5,0,1),(379,21,5,0,1),(380,22,5,0,1),(381,23,5,0,1),(382,24,5,0,12),(383,25,5,1,12),(384,26,5,1,12),(385,27,5,0,12),(386,28,5,0,1),(387,29,5,0,1),(388,30,5,0,1),(389,31,5,0,1),(390,32,5,0,12),(391,33,5,1,12),(392,34,5,1,12),(393,35,5,0,12),(394,36,5,0,13),(395,37,5,0,13),(396,38,5,0,13),(397,39,5,0,13),(398,40,5,0,14),(399,41,5,0,14),(400,42,5,0,7),(401,43,5,0,7),(402,44,5,0,7),(403,45,5,0,7),(404,46,5,0,7),(405,47,5,0,7),(406,48,5,0,7),(407,49,5,0,7),(408,50,5,0,7),(409,0,4,0,1),(410,1,4,0,1),(411,2,4,0,1),(412,3,4,0,1),(413,4,4,0,1),(414,5,4,0,1),(415,6,4,0,1),(416,7,4,0,1),(417,8,4,0,1),(418,9,4,0,1),(419,10,4,0,1),(420,11,4,0,1),(421,12,4,0,1),(422,13,4,0,1),(423,14,4,0,1),(424,15,4,0,1),(425,16,4,0,1),(426,17,4,0,1),(427,18,4,0,1),(428,19,4,0,1),(429,20,4,0,1),(430,21,4,0,1),(431,22,4,0,1),(432,23,4,0,1),(433,24,4,0,1),(434,25,4,0,1),(435,26,4,0,1),(436,27,4,0,1),(437,28,4,0,1),(438,29,4,0,1),(439,30,4,0,1),(440,31,4,0,1),(441,32,4,0,1),(442,33,4,0,1),(443,34,4,0,1),(444,35,4,0,1),(445,36,4,0,1),(446,37,4,0,1),(447,38,4,0,1),(448,39,4,0,1),(449,40,4,0,1),(450,41,4,0,1),(451,42,4,0,7),(452,43,4,0,7),(453,44,4,0,7),(454,45,4,0,7),(455,46,4,0,7),(456,47,4,0,7),(457,48,4,0,7),(458,49,4,0,7),(459,50,4,0,7),(460,0,3,0,1),(461,1,3,0,1),(462,2,3,0,1),(463,3,3,0,1),(464,4,3,0,1),(465,5,3,0,1),(466,6,3,0,1),(467,7,3,0,1),(468,8,3,0,1),(469,9,3,0,1),(470,10,3,0,1),(471,11,3,0,1),(472,12,3,0,1),(473,13,3,0,1),(474,14,3,0,1),(475,15,3,0,1),(476,16,3,0,1),(477,17,3,0,1),(478,18,3,0,1),(479,19,3,0,1),(480,20,3,0,1),(481,21,3,0,1),(482,22,3,0,1),(483,23,3,0,1),(484,24,3,0,1),(485,25,3,0,1),(486,26,3,0,1),(487,27,3,0,1),(488,28,3,0,1),(489,29,3,0,1),(490,30,3,0,1),(491,31,3,0,1),(492,32,3,0,1),(493,33,3,0,1),(494,34,3,0,1),(495,35,3,0,1),(496,36,3,0,1),(497,37,3,0,1),(498,38,3,0,1),(499,39,3,0,1),(500,40,3,0,1),(501,41,3,0,1),(502,42,3,0,7),(503,43,3,0,7),(504,44,3,0,7),(505,45,3,0,7),(506,46,3,0,7),(507,47,3,0,7),(508,48,3,0,7),(509,49,3,0,7),(510,50,3,0,7),(511,0,2,0,15),(512,1,2,1,15),(513,2,2,1,15),(514,3,2,0,15),(515,4,2,0,15),(516,5,2,1,15),(517,6,2,1,15),(518,7,2,0,15),(519,8,2,0,16),(520,9,2,0,16),(521,10,2,0,16),(522,11,2,0,16),(523,12,2,0,16),(524,13,2,0,16),(525,14,2,0,16),(526,15,2,0,17),(527,16,2,1,17),(528,17,2,1,17),(529,18,2,0,17),(530,19,2,0,18),(531,20,2,1,18),(532,21,2,1,18),(533,22,2,0,18),(534,23,2,0,19),(535,24,2,0,19),(536,25,2,0,19),(537,26,2,0,19),(538,27,2,0,19),(539,28,2,0,19),(540,29,2,0,19),(541,30,2,0,19),(542,31,2,0,20),(543,32,2,0,20),(544,33,2,0,21),(545,34,2,0,21),(546,35,2,0,21),(547,36,2,0,21),(548,37,2,0,22),(549,38,2,0,22),(550,39,2,0,23),(551,40,2,1,23),(552,41,2,1,23),(553,42,2,1,23),(554,43,2,1,23),(555,44,2,1,23),(556,45,2,0,23),(557,46,2,1,23),(558,47,2,1,23),(559,48,2,1,23),(560,49,2,1,23),(561,50,2,1,23),(562,0,1,0,15),(563,1,1,1,15),(564,2,1,1,15),(565,3,1,0,15),(566,4,1,0,15),(567,5,1,1,15),(568,6,1,1,15),(569,7,1,0,15),(570,8,1,0,16),(571,9,1,0,16),(572,10,1,0,16),(573,11,1,0,16),(574,12,1,0,16),(575,13,1,0,16),(576,14,1,0,16),(577,15,1,0,17),(578,16,1,1,17),(579,17,1,1,17),(580,18,1,0,17),(581,19,1,0,18),(582,20,1,1,18),(583,21,1,1,18),(584,22,1,0,18),(585,23,1,0,19),(586,24,1,0,19),(587,25,1,0,19),(588,26,1,0,19),(589,27,1,0,19),(590,28,1,0,19),(591,29,1,0,19),(592,30,1,0,19),(593,31,1,0,20),(594,32,1,0,20),(595,33,1,0,21),(596,34,1,0,21),(597,35,1,0,21),(598,36,1,0,21),(599,37,1,0,22),(600,38,1,0,22),(601,39,1,0,23),(602,40,1,0,23),(603,41,1,0,23),(604,42,1,0,23),(605,43,1,0,23),(606,44,1,0,23),(607,45,1,0,23),(608,46,1,0,23),(609,47,1,0,23),(610,48,1,0,23),(611,49,1,0,23),(612,50,1,0,23),(613,0,0,0,15),(614,1,0,1,15),(615,2,0,1,15),(616,3,0,0,15),(617,4,0,0,15),(618,5,0,1,15),(619,6,0,1,15),(620,7,0,0,15),(621,8,0,0,16),(622,9,0,0,16),(623,10,0,0,16),(624,11,0,0,16),(625,12,0,0,16),(626,13,0,0,16),(627,14,0,0,16),(628,15,0,0,17),(629,16,0,1,17),(630,17,0,1,17),(631,18,0,0,17),(632,19,0,0,18),(633,20,0,1,18),(634,21,0,1,18),(635,22,0,0,18),(636,23,0,0,19),(637,24,0,0,19),(638,25,0,0,19),(639,26,0,0,19),(640,27,0,0,19),(641,28,0,0,19),(642,29,0,0,19),(643,30,0,0,19),(644,31,0,0,20),(645,32,0,0,20),(646,33,0,0,21),(647,34,0,0,21),(648,35,0,0,21),(649,36,0,0,21),(650,37,0,0,22),(651,38,0,0,22),(652,39,0,0,23),(653,40,0,0,23),(654,41,0,0,23),(655,42,0,0,23),(656,43,0,0,23),(657,44,0,0,23),(658,45,0,0,23),(659,46,0,0,23),(660,47,0,0,23),(661,48,0,0,23),(662,49,0,0,23),(663,50,0,0,23);
/*!40000 ALTER TABLE `floorplan_space` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `habitats_habitat`
--

DROP TABLE IF EXISTS `habitats_habitat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `habitats_habitat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `habitats_habitat`
--

LOCK TABLES `habitats_habitat` WRITE;
/*!40000 ALTER TABLE `habitats_habitat` DISABLE KEYS */;
/*!40000 ALTER TABLE `habitats_habitat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_accesstoken`
--

DROP TABLE IF EXISTS `oauth2_provider_accesstoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oauth2_provider_accesstoken` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `token` varchar(255) NOT NULL,
  `expires` datetime(6) NOT NULL,
  `scope` longtext NOT NULL,
  `application_id` bigint(20) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `oauth2_provider_accesstoken_token_8af090f8_uniq` (`token`),
  KEY `oauth2_provider_accesstoken_user_id_6e4c9a65_fk_auth_user_id` (`user_id`),
  KEY `oauth2_provider_accesstoken_application_id_b22886e1_fk` (`application_id`),
  CONSTRAINT `oauth2_provider_accesstoken_application_id_b22886e1_fk` FOREIGN KEY (`application_id`) REFERENCES `oauth2_provider_application` (`id`),
  CONSTRAINT `oauth2_provider_accesstoken_user_id_6e4c9a65_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_accesstoken`
--

LOCK TABLES `oauth2_provider_accesstoken` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_accesstoken` DISABLE KEYS */;
/*!40000 ALTER TABLE `oauth2_provider_accesstoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_application`
--

DROP TABLE IF EXISTS `oauth2_provider_application`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oauth2_provider_application` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `client_id` varchar(100) NOT NULL,
  `redirect_uris` longtext NOT NULL,
  `client_type` varchar(32) NOT NULL,
  `authorization_grant_type` varchar(32) NOT NULL,
  `client_secret` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `skip_authorization` tinyint(1) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `client_id` (`client_id`),
  KEY `oauth2_provider_application_client_secret_53133678` (`client_secret`),
  KEY `oauth2_provider_application_user_id_79829054_fk_auth_user_id` (`user_id`),
  CONSTRAINT `oauth2_provider_application_user_id_79829054_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_application`
--

LOCK TABLES `oauth2_provider_application` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_application` DISABLE KEYS */;
/*!40000 ALTER TABLE `oauth2_provider_application` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_grant`
--

DROP TABLE IF EXISTS `oauth2_provider_grant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oauth2_provider_grant` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `code` varchar(255) NOT NULL,
  `expires` datetime(6) NOT NULL,
  `redirect_uri` varchar(255) NOT NULL,
  `scope` longtext NOT NULL,
  `application_id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `oauth2_provider_grant_code_49ab4ddf_uniq` (`code`),
  KEY `oauth2_provider_grant_application_id_81923564_fk` (`application_id`),
  KEY `oauth2_provider_grant_user_id_e8f62af8_fk_auth_user_id` (`user_id`),
  CONSTRAINT `oauth2_provider_grant_application_id_81923564_fk` FOREIGN KEY (`application_id`) REFERENCES `oauth2_provider_application` (`id`),
  CONSTRAINT `oauth2_provider_grant_user_id_e8f62af8_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_grant`
--

LOCK TABLES `oauth2_provider_grant` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_grant` DISABLE KEYS */;
/*!40000 ALTER TABLE `oauth2_provider_grant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_refreshtoken`
--

DROP TABLE IF EXISTS `oauth2_provider_refreshtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oauth2_provider_refreshtoken` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `token` varchar(255) NOT NULL,
  `access_token_id` bigint(20) NOT NULL,
  `application_id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `access_token_id` (`access_token_id`),
  UNIQUE KEY `oauth2_provider_refreshtoken_token_d090daa4_uniq` (`token`),
  KEY `oauth2_provider_refreshtoken_application_id_2d1c311b_fk` (`application_id`),
  KEY `oauth2_provider_refreshtoken_user_id_da837fce_fk_auth_user_id` (`user_id`),
  CONSTRAINT `oauth2_provider_refreshtoken_access_token_id_775e84e8_fk` FOREIGN KEY (`access_token_id`) REFERENCES `oauth2_provider_accesstoken` (`id`),
  CONSTRAINT `oauth2_provider_refreshtoken_application_id_2d1c311b_fk` FOREIGN KEY (`application_id`) REFERENCES `oauth2_provider_application` (`id`),
  CONSTRAINT `oauth2_provider_refreshtoken_user_id_da837fce_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_refreshtoken`
--

LOCK TABLES `oauth2_provider_refreshtoken` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_refreshtoken` DISABLE KEYS */;
/*!40000 ALTER TABLE `oauth2_provider_refreshtoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_association`
--

DROP TABLE IF EXISTS `social_auth_association`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `social_auth_association` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `server_url` varchar(255) NOT NULL,
  `handle` varchar(255) NOT NULL,
  `secret` varchar(255) NOT NULL,
  `issued` int(11) NOT NULL,
  `lifetime` int(11) NOT NULL,
  `assoc_type` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `social_auth_association_server_url_handle_078befa2_uniq` (`server_url`,`handle`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_association`
--

LOCK TABLES `social_auth_association` WRITE;
/*!40000 ALTER TABLE `social_auth_association` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_association` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_code`
--

DROP TABLE IF EXISTS `social_auth_code`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `social_auth_code` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `code` varchar(32) NOT NULL,
  `verified` tinyint(1) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `social_auth_code_email_code_801b2d02_uniq` (`email`,`code`),
  KEY `social_auth_code_code_a2393167` (`code`),
  KEY `social_auth_code_timestamp_176b341f` (`timestamp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_code`
--

LOCK TABLES `social_auth_code` WRITE;
/*!40000 ALTER TABLE `social_auth_code` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_code` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_nonce`
--

DROP TABLE IF EXISTS `social_auth_nonce`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `social_auth_nonce` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `server_url` varchar(255) NOT NULL,
  `timestamp` int(11) NOT NULL,
  `salt` varchar(65) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `social_auth_nonce_server_url_timestamp_salt_f6284463_uniq` (`server_url`,`timestamp`,`salt`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_nonce`
--

LOCK TABLES `social_auth_nonce` WRITE;
/*!40000 ALTER TABLE `social_auth_nonce` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_nonce` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_partial`
--

DROP TABLE IF EXISTS `social_auth_partial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `social_auth_partial` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `token` varchar(32) NOT NULL,
  `next_step` smallint(5) unsigned NOT NULL,
  `backend` varchar(32) NOT NULL,
  `data` longtext NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `social_auth_partial_token_3017fea3` (`token`),
  KEY `social_auth_partial_timestamp_50f2119f` (`timestamp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_partial`
--

LOCK TABLES `social_auth_partial` WRITE;
/*!40000 ALTER TABLE `social_auth_partial` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_partial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_auth_usersocialauth`
--

DROP TABLE IF EXISTS `social_auth_usersocialauth`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `social_auth_usersocialauth` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `provider` varchar(32) NOT NULL,
  `uid` varchar(255) NOT NULL,
  `extra_data` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `social_auth_usersocialauth_provider_uid_e6b5e668_uniq` (`provider`,`uid`),
  KEY `social_auth_usersocialauth_user_id_17d28448_fk_auth_user_id` (`user_id`),
  CONSTRAINT `social_auth_usersocialauth_user_id_17d28448_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_auth_usersocialauth`
--

LOCK TABLES `social_auth_usersocialauth` WRITE;
/*!40000 ALTER TABLE `social_auth_usersocialauth` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_auth_usersocialauth` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `squads_membership`
--

DROP TABLE IF EXISTS `squads_membership`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `squads_membership` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `employee_id` int(11) NOT NULL,
  `squad_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `squads_membership_employee_id_squad_id_ec9ab8f7_uniq` (`employee_id`,`squad_id`),
  KEY `squads_membership_squad_id_92f35eb8_fk_squads_squad_id` (`squad_id`),
  CONSTRAINT `squads_membership_employee_id_dcb8b8de_fk_employees_employee_id` FOREIGN KEY (`employee_id`) REFERENCES `employees_employee` (`id`),
  CONSTRAINT `squads_membership_squad_id_92f35eb8_fk_squads_squad_id` FOREIGN KEY (`squad_id`) REFERENCES `squads_squad` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `squads_membership`
--

LOCK TABLES `squads_membership` WRITE;
/*!40000 ALTER TABLE `squads_membership` DISABLE KEYS */;
/*!40000 ALTER TABLE `squads_membership` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `squads_squad`
--

DROP TABLE IF EXISTS `squads_squad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `squads_squad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `squads_squad`
--

LOCK TABLES `squads_squad` WRITE;
/*!40000 ALTER TABLE `squads_squad` DISABLE KEYS */;
/*!40000 ALTER TABLE `squads_squad` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-01-24 16:47:57
