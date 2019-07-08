-- MySQL dump 10.13  Distrib 8.0.13, for macos10.14 (x86_64)
--
-- Host: localhost    Database: tracks
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tracks_survey20tracks`
--

DROP TABLE IF EXISTS `tracks_survey20tracks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tracks_survey20tracks` (
  `name` varchar(100) NOT NULL,
  `id` varchar(30) NOT NULL,
  `artist_name` varchar(100) NOT NULL,
  `artist_id` varchar(30) NOT NULL,
  `preview_url` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tracks_survey20tracks`
--

LOCK TABLES `tracks_survey20tracks` WRITE;
/*!40000 ALTER TABLE `tracks_survey20tracks` DISABLE KEYS */;
INSERT INTO `tracks_survey20tracks` VALUES ('Give Me Something','1au9q3wiWxIwXTazIjHdfF','Seafret','4Ly0KABsxlx4fNj63zJTrF','https://p.scdn.co/mp3-preview/4d7625d9a01acca6647e8f92cb5dd338978da2e1?cid=774b29d4f13844c495f206cafdad9c86\n'),('The Lazy Song','1ExfPZEiahqhLyajhybFeS','Bruno Mars','0du5cEVh5yTK9QJze8zA0C','https://p.scdn.co/mp3-preview/6dda0f582db7db112f377d36df313cf04e706f27?cid=774b29d4f13844c495f206cafdad9c86\n'),('Given Up','1fLlRApgzxWweF1JTf8yM5','Linkin Park','6XyY86QOPPrYVGvF9ch6wz','https://p.scdn.co/mp3-preview/ab38812ac47dbfe4d4d70abc375311bd8a2511a6?cid=774b29d4f13844c495f206cafdad9c86\n'),('November Night','1pSIQWMFbkJ5XvwgzKfeBv','Groove Coverage','1yWjNh9SRE7C59A3LDIwVW','https://p.scdn.co/mp3-preview/c52cc53bcf0ff8916107c89ebf8507758cb0e21d?cid=774b29d4f13844c495f206cafdad9c86'),('Old Flame','1UMJ5XcJPmH6ZbIRsCLY5F','Tom Speight','02U4dXZhGSo07f66l8JZ91','https://p.scdn.co/mp3-preview/155fe54c1186c043df3701ff2b0e13d2ea286bb8?cid=774b29d4f13844c495f206cafdad9c86\n'),('Spit It Out','2W2eaLVKv9NObcLXlYRZZo','Slipknot','05fG473iIaoy82BF1aGhL8','https://p.scdn.co/mp3-preview/56871b651b171ed29ebb1d6630952fc164c1dc75?cid=774b29d4f13844c495f206cafdad9c86\n'),('I\'m Yours','3S0OXQeoh0w6AY8WQVckRW','Jason Mraz','4phGZZrJZRo4ElhRtViYdl','https://p.scdn.co/mp3-preview/c58f1bc9160754337b858a4eb824a6ac2321041d?cid=774b29d4f13844c495f206cafdad9c86\n'),('Vain','3wF0zyjQ6FKLK4vFxcMojP','KIRBY','5lcDGoJUr5WY5bCFAfYbCU','https://p.scdn.co/mp3-preview/606a06399ab185681386a6cffef192690857a2fc?cid=774b29d4f13844c495f206cafdad9c86\n'),('Hero','4FCb4CUbFCMNRkI6lYc1zI','Mariah Carey','4iHNK0tOyZPYnBU7nGAgpQ','https://p.scdn.co/mp3-preview/cc03494b6954237706d6f2ac7b9ce189014f840a?cid=774b29d4f13844c495f206cafdad9c86\n'),('Skinny Love','4RL77hMWUq35NYnPLXBpih','Birdy','2WX2uTcsvV5OnS0inACecP','https://p.scdn.co/mp3-preview/fa2ee949327d85e7bd22385f00737744ebf87d60?cid=774b29d4f13844c495f206cafdad9c86\n'),('Thunderstruck','52UWtKlYjZO3dHoRlWuz9S','AC/DC','711MCceyCBcFnzjGY4Q7Un','https://p.scdn.co/mp3-preview/2d9544a444030dbf6f506c4c9bd5ae5708bc59f8?cid=774b29d4f13844c495f206cafdad9c86\n'),('Happy','5b88tNINg4Q4nrRbrCXUmg','Pharrell Williams','2RdwBSPQiwcmiDo9kixcl8','https://p.scdn.co/mp3-preview/67cffdcb7e3c82a5eb2e5f0bb235d377ccc94eeb?cid=774b29d4f13844c495f206cafdad9c86\n'),('Homesick','5E5MqaS6eOsbaJibl3YeMZ','Dua Lipa','6M2wZ9GZgrQXHCFfjv46we','https://p.scdn.co/mp3-preview/47eb20c4409683df486f8bb518b2e6abf4e617a5?cid=774b29d4f13844c495f206cafdad9c86\n'),('Say You Won\'t Let Go','5uCax9HTNlzGybIStD3vDh','James Arthur','4IWBUUAFIplrNtaOHcJPRM','https://p.scdn.co/mp3-preview/00825cb1779b31d68964eda6f2a7911fc2ae96c6?cid=774b29d4f13844c495f206cafdad9c86\n'),('I\'ll Be Good','5WLSak7DN3LY1K71oWYuoN','Jaymes Young','6QrQ7OrISRYIfS5mtacaw2','https://p.scdn.co/mp3-preview/0c94dde2f13273e3ed1eec72cb184537d0ae77d2?cid=774b29d4f13844c495f206cafdad9c86\n'),('The Downfall of Us All','6G7URf5rGe6MvNoiTtNEP7','A Day To Remember','4NiJW4q9ichVqL1aUsgGAN','https://p.scdn.co/mp3-preview/f094559ec555e9cf67cca13261458be4df2ef4a5?cid=774b29d4f13844c495f206cafdad9c86\n'),('Someone Like You','6QPKYGnAW9QozVz2dSWqRg','Adele','4dpARuHxo51G3z768sgnrY','https://p.scdn.co/mp3-preview/ba52dd35393f5936ed277cf375128feecd111d26?cid=774b29d4f13844c495f206cafdad9c86\n'),('I Hate Everything About You','6rUp7v3l8yC4TKxAAR5Bmx','Three Days Grace','2xiIXseIJcq3nG7C8fHeBj','https://p.scdn.co/mp3-preview/8893669447625edf76339cdd67a338dad034a7ea?cid=774b29d4f13844c495f206cafdad9c86\n'),('Jekyll and Hyde','7qjbpdk0IYijcSuSYWlXO6','Five Finger Death Punch','5t28BP42x2axFnqOOMg3CM','https://p.scdn.co/mp3-preview/776ba6ac560da4be1c441b1a2cafbb7a78413d31?cid=774b29d4f13844c495f206cafdad9c86\n'),('Mr. Know It All','7uRznL3LcuazKpwCTpDltz','Kelly Clarkson','3BmGtnKgCSGYIUhmivXKWX','https://p.scdn.co/mp3-preview/0af54fd78b3b5e2c115b75aa43d0567eefe0a137?cid=774b29d4f13844c495f206cafdad9c86\n');
/*!40000 ALTER TABLE `tracks_survey20tracks` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-15 14:42:36
