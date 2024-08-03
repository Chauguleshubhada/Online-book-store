CREATE DATABASE  IF NOT EXISTS `onlinebookstore` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `onlinebookstore`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: onlinebookstore
-- ------------------------------------------------------
-- Server version	8.1.0

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
-- Table structure for table `book_category`
--

DROP TABLE IF EXISTS book_category;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE book_category (
  category_Id int NOT NULL AUTO_INCREMENT,
  category_name varchar(50) DEFAULT NULL,
  PRIMARY KEY (category_Id)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_category`
--

LOCK TABLES book_category WRITE;
/*!40000 ALTER TABLE book_category DISABLE KEYS */;
INSERT INTO book_category VALUES (20,'Education'),(24,'Story Books'),(26,'education'),(27,'novel');
/*!40000 ALTER TABLE book_category ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS books;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE books (
  Book_id int NOT NULL AUTO_INCREMENT,
  Book_name varchar(50) DEFAULT NULL,
  Price int DEFAULT NULL,
  Author_name varchar(50) DEFAULT NULL,
  `Description` varchar(100) DEFAULT NULL,
  Book_img varchar(100) DEFAULT NULL,
  category_Id int DEFAULT NULL,
  PRIMARY KEY (Book_id),
  KEY category_Id (category_Id),
  CONSTRAINT books_ibfk_1 FOREIGN KEY (category_Id) REFERENCES book_category (category_Id)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES books WRITE;
/*!40000 ALTER TABLE books DISABLE KEYS */;
INSERT INTO books VALUES (1,'C Programming',200,' E Balagurusamy ','Programming in Ansi C 8th Ed Book By E. Balagurusamy','Images/c.jpg',20),(2,'Java',300,'E. Balagurusamy','Programming in Java Book By E. Balagurusamy','Images/Java.jpg',20),(3,'OOP',300,'E. Balagurusamy','Programming in OOP Book By E. Balagurusamy','Images/object oriented programming.jpg',20),(4,'Magic Drum',300,'Sudha Murty','Story Book by Sudha Murty','Images/Magic drum.jpg',24),(5,'Grandma\'s bag of stories',200,'Sudha Murty','Story Book by Sudha Murty','Images/grandma\'s bag of stories.jpg',24),(6,'How the onions got its layers',300,'Sudha Murty','Story Book by Sudha Murty','Images/how the onions got its layers.jpg',24),(7,'The magic of lost temple',300,'Sudha Murty','Story Book by Sudha Murty','Images/The magic of lost temple.jpg',24),(9,'me to',200,'wwe','helooooooooooooooooo','Images/One Indian Girl.jpg',26),(10,'One Indian Girl',300,'Chetan Bhagt','story book by chetan bhagt','Images/One Indian Girl.jpg',27);
/*!40000 ALTER TABLE books ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `books_vw`
--

DROP TABLE IF EXISTS books_vw;
/*!50001 DROP VIEW IF EXISTS books_vw*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `books_vw` AS SELECT 
 1 AS book_id,
 1 AS book_name,
 1 AS price,
 1 AS author_name,
 1 AS description,
 1 AS book_img,
 1 AS category_name,
 1 AS cat_id*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `cart_vw`
--

DROP TABLE IF EXISTS cart_vw;
/*!50001 DROP VIEW IF EXISTS cart_vw*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `cart_vw` AS SELECT 
 1 AS book_id,
 1 AS book_name,
 1 AS price,
 1 AS book_img,
 1 AS qty,
 1 AS username,
 1 AS subtotal*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `contact`
--

DROP TABLE IF EXISTS contact;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE contact (
  `name` varchar(30) DEFAULT NULL,
  email varchar(30) DEFAULT NULL,
  mobile_number varchar(15) DEFAULT NULL,
  message varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact`
--

LOCK TABLES contact WRITE;
/*!40000 ALTER TABLE contact DISABLE KEYS */;
INSERT INTO contact VALUES ('shubhada chaugule','shubhada20@gmail.com','8698110103','hello'),('shubhada chaugule','shubhada20@gmail.com','8698110103','hh'),('shubhada chaugule','shubhada20@gmail.com','8698110103','hh'),('shubhada chaugule','shubhada20@gmail.com','8698110103','q'),('shubhada chaugule','shubhada20@gmail.com','8698110103','y'),('shubhada chaugule','shubhada20@gmail.com','8698110103','tt'),('shubhada chaugule','shubhada20@gmail.com','8698110103','s'),('shubhada chaugule','shubhada20@gmail.com','8698110103','m'),('shubhada chaugule','shubhada20@gmail.com','8698110103','n'),('shubhada chaugule','shubhada20@gmail.com','8698110103','3'),('shubhada chaugule','shubhada20@gmail.com','8698110103','helloo shubhada'),('Siddhi Raut','siddhi20@gmail.com','8698110103','Hello');
/*!40000 ALTER TABLE contact ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mycart`
--

DROP TABLE IF EXISTS mycart;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE mycart (
  id int NOT NULL AUTO_INCREMENT,
  book_id int DEFAULT NULL,
  username varchar(20) DEFAULT NULL,
  qty int DEFAULT NULL,
  PRIMARY KEY (id),
  KEY book_id (book_id),
  KEY username (username),
  CONSTRAINT mycart_ibfk_1 FOREIGN KEY (book_id) REFERENCES books (Book_id),
  CONSTRAINT mycart_ibfk_2 FOREIGN KEY (username) REFERENCES userinfo (username)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mycart`
--

LOCK TABLES mycart WRITE;
/*!40000 ALTER TABLE mycart DISABLE KEYS */;
/*!40000 ALTER TABLE mycart ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment`
--

DROP TABLE IF EXISTS payment;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE payment (
  cardno varchar(16) NOT NULL,
  cvv varchar(4) DEFAULT NULL,
  expiry varchar(10) DEFAULT NULL,
  balance float DEFAULT NULL,
  PRIMARY KEY (cardno)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment`
--

LOCK TABLES payment WRITE;
/*!40000 ALTER TABLE payment DISABLE KEYS */;
INSERT INTO payment VALUES ('4111111111111111','567','12/2030',47900),('5111111111111111','123','12/2031',7100);
/*!40000 ALTER TABLE payment ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_likes`
--

DROP TABLE IF EXISTS user_likes;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE user_likes (
  id int NOT NULL AUTO_INCREMENT,
  book_id int DEFAULT NULL,
  username varchar(20) DEFAULT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_likes`
--

LOCK TABLES user_likes WRITE;
/*!40000 ALTER TABLE user_likes DISABLE KEYS */;
INSERT INTO user_likes VALUES (3,2,'shubhada'),(4,7,'shubhada'),(5,9,'shubhada');
/*!40000 ALTER TABLE user_likes ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userinfo`
--

DROP TABLE IF EXISTS userinfo;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE userinfo (
  username varchar(20) NOT NULL,
  `password` varchar(20) DEFAULT NULL,
  email_id varchar(100) DEFAULT NULL,
  `role` varchar(30) DEFAULT NULL,
  PRIMARY KEY (username)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userinfo`
--

LOCK TABLES userinfo WRITE;
/*!40000 ALTER TABLE userinfo DISABLE KEYS */;
INSERT INTO userinfo VALUES ('admin','admin1','admin@gmail.co','admin'),('shubhada','Shubhada11','shubhada20@gmail.com','user'),('siddhi','new','siddhi20@gmail.com','user'),('Vrushali','Vrushali','vrushali@gmail.com','user');
/*!40000 ALTER TABLE userinfo ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `userlikes_vw`
--

DROP TABLE IF EXISTS userlikes_vw;
/*!50001 DROP VIEW IF EXISTS userlikes_vw*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `userlikes_vw` AS SELECT 
 1 AS book_id,
 1 AS book_name,
 1 AS price,
 1 AS book_img,
 1 AS username*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `books_vw`
--

/*!50001 DROP VIEW IF EXISTS books_vw*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = cp850 */;
/*!50001 SET character_set_results     = cp850 */;
/*!50001 SET collation_connection      = cp850_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=root@localhost SQL SECURITY DEFINER */
/*!50001 VIEW books_vw AS select b.Book_id AS book_id,b.Book_name AS book_name,b.Price AS price,b.Author_name AS author_name,b.`Description` AS `description`,b.Book_img AS book_img,cat.category_name AS category_name,cat.category_Id AS cat_id from (books b join book_category cat on((b.category_Id = cat.category_Id))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `cart_vw`
--

/*!50001 DROP VIEW IF EXISTS cart_vw*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = cp850 */;
/*!50001 SET character_set_results     = cp850 */;
/*!50001 SET collation_connection      = cp850_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=root@localhost SQL SECURITY DEFINER */
/*!50001 VIEW cart_vw AS select b.Book_id AS book_id,b.Book_name AS book_name,b.Price AS price,b.Book_img AS book_img,mycart.qty AS qty,mycart.username AS username,(mycart.qty * b.Price) AS subtotal from (books b join mycart on((b.Book_id = mycart.book_id))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `userlikes_vw`
--

/*!50001 DROP VIEW IF EXISTS userlikes_vw*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = cp850 */;
/*!50001 SET character_set_results     = cp850 */;
/*!50001 SET collation_connection      = cp850_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=root@localhost SQL SECURITY DEFINER */
/*!50001 VIEW userlikes_vw AS select b.Book_id AS book_id,b.Book_name AS book_name,b.Price AS price,b.Book_img AS book_img,user_likes.username AS username from (books b join user_likes on((b.Book_id = user_likes.book_id))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-03 19:35:49
