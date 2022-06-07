-- Table structure for table `player`
DROP TABLE IF EXISTS `player_games`;
DROP TABLE IF EXISTS `matches`;
DROP TABLE IF EXISTS `player`;
CREATE TABLE `player` (
  `id` int(64) NOT NULL AUTO_INCREMENT,
  `username` varchar(25) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `permissions` int(64) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`)
);
-- Dumping data for table `player`
INSERT INTO `player` VALUES (1,'JohnSmith','MrSmith@google.com','g4m3r',0),(2,'CrazyGamer','thecrazygamer@google.com','g4m3r',0),(3,'Travler','TGump@verizon.net','g4m3r',0);


-- Table structure for table `games`
DROP TABLE IF EXISTS `games`;
CREATE TABLE `games` (
  `id` int(64) NOT NULL AUTO_INCREMENT,
  `gameName` varchar(255) NOT NULL,
  `category` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
);
-- Dumping data for table `games`
INSERT INTO `games` VALUES (1,'Apex Legends','Battle Royale'),(2,'Fall Guys','Battle Royale'),(3,'Fortnite','Battle Royale'),(4,'Battlefield','FPS'),(5,'Call of Duty','FPS'),(6,'Halo','FPS'),(7,'Dead Space','Horror'),(8,'Resident Evil','Horror'),(9,'Silent Hill','Horror'),(10,'Crash Bandicoot','Platformer'),(11,'Shovel Knight','Platformer'),(12,'Super Mario Bros','Platformer'),(13,'Elder Scrolls','RPG'),(14,'Final Fantasy','RPG'),(15,'Fire Emblem','RPG'),(16,'FIFA','Sports'),(17,'Madden NFL','Sports'),(18,'NBA 2K','Sports');

-- Table structure for table `player_games`
CREATE TABLE `player_games` (
  `id` int(64) NOT NULL AUTO_INCREMENT,
  `userId` int(64) NOT NULL,
  `gameId` int(64) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (userId) REFERENCES player (id),
  FOREIGN KEY (gameId) REFERENCES games (id)
);
-- Dumping data for table `player_games`
INSERT INTO `player_games` VALUES (1,1,1),(2,1,17),(3,1,5),(4,2,12),(5,2,15),(6,2,2),(7,3,9),(8,3,4),(9,3,16);


-- Table structure for table `matches`
CREATE TABLE `matches` (
  `id` int(64) NOT NULL AUTO_INCREMENT,
  `userId` int(64) NOT NULL,
  `likedId` int(64) NOT NULL, 
  `matched` int(32) NOT NULL DEFAULT 0,
  `timeOfLike` date NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (userId) REFERENCES player (id),
  FOREIGN KEY (likedId) REFERENCES player (id)
);
-- Dumping data for table `matches`
INSERT INTO `matches` VALUES (1,1,2,0,'2022-03-29'),(2,1,3,0,'2022-03-29'),(3,3,2,1,'2022-04-01'); 
