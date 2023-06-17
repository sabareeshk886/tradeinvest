/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.6.12-log : Database - final project
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`final project` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `final project`;

/*Table structure for table `account_details` */

DROP TABLE IF EXISTS `account_details`;

CREATE TABLE `account_details` (
  `aid` int(11) NOT NULL AUTO_INCREMENT,
  `acc_no` varchar(200) DEFAULT NULL,
  `pvt_key` varchar(200) DEFAULT NULL,
  `lid` int(11) DEFAULT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `account_details` */

insert  into `account_details`(`aid`,`acc_no`,`pvt_key`,`lid`) values 
(1,'0xB9B4112Ee943255796E6650691858167d70bf958','0x4d3cbdd196fdb681257f26d57c5ba376c3147761b5b22f0112baf559e5569094',2),
(2,'0x5DCbc44D79d32cED902feEfAb5a7C9Db554f2720','0x8c9d6511eb3db793f1bcd580e60ed84ff36ea5c97519980bc49233ebe79a6f7b',8),
(3,'0xA1EFEBAaE95FE7F307273CBE8E0D3A9653593fA9','0x7fc3217172fa511377fb2b598d89e2bdd3333c90d2063838612c2e29084d86ec',10),
(4,'0x8375190CBAFce47178485540BCCeC22bD4ef34F4','0x4ae477f1359536137622376ebdf5b37174e72f3907ecb59886d0f3abfd83046a',13);

/*Table structure for table `company` */

DROP TABLE IF EXISTS `company`;

CREATE TABLE `company` (
  `C_id` int(11) NOT NULL AUTO_INCREMENT,
  `l_id` int(11) DEFAULT NULL,
  `base_price` varchar(100) DEFAULT NULL,
  `c_graph` varchar(200) DEFAULT NULL,
  `logo` varchar(200) DEFAULT NULL,
  `c_name` varchar(30) DEFAULT NULL,
  `tax_id` varchar(30) DEFAULT NULL,
  `legal_status` varchar(30) DEFAULT NULL,
  `field_of_business` varchar(30) DEFAULT NULL,
  `registered_office` varchar(30) DEFAULT NULL,
  `state` varchar(30) DEFAULT NULL,
  `region` varchar(30) DEFAULT NULL,
  `muncipality` varchar(30) DEFAULT NULL,
  `postcode` int(11) DEFAULT NULL,
  `street` varchar(30) DEFAULT NULL,
  `phone_number` int(11) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `telephone` int(11) DEFAULT NULL,
  `fax` varchar(30) DEFAULT NULL,
  `postal_address` varchar(30) DEFAULT NULL,
  `city` varchar(30) DEFAULT NULL,
  `country` varchar(30) DEFAULT NULL,
  `bank_name` varchar(30) DEFAULT NULL,
  `bank_number` bigint(30) DEFAULT NULL,
  `ifsc_code` varchar(30) DEFAULT NULL,
  `director_name` varchar(30) DEFAULT NULL,
  `director_title` varchar(30) DEFAULT NULL,
  `director_surname` varchar(30) DEFAULT NULL,
  `director_dob` varchar(30) DEFAULT NULL,
  `bankguarantee` varchar(200) DEFAULT NULL,
  `proof_of_financialeligibility` varchar(30) DEFAULT NULL,
  `status` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`C_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `company` */

insert  into `company`(`C_id`,`l_id`,`base_price`,`c_graph`,`logo`,`c_name`,`tax_id`,`legal_status`,`field_of_business`,`registered_office`,`state`,`region`,`muncipality`,`postcode`,`street`,`phone_number`,`email`,`telephone`,`fax`,`postal_address`,`city`,`country`,`bank_name`,`bank_number`,`ifsc_code`,`director_name`,`director_title`,`director_surname`,`director_dob`,`bankguarantee`,`proof_of_financialeligibility`,`status`) values 
(1,2,'5','/static/company/LOGO/graph.jpg','/static/company/LOGO/company_logo.jpg','TRADE CHAIN','4565454','approved','TRADING','kochi','KERALA','india','kochi',676102,'kakkanad',2147483647,'abc@gmail.com',2147483647,'53654','abc,kakkanad,kochi','kochi','INDIA','pnb',45632514125689,'punb01563','sabareesh','sabareesh','sabareesh','sabareesh','/static/company/BANK_PROOF/20230406-124849.jpg','','approved'),
(4,3,NULL,NULL,'/static/company/LOGO/20230521-214452.jpg','UNLISTED','25553','12','IT','KOCHI','KERALA','0','0',647571,'0',989898855,'2',8,'8','8','5','INDIA','8687686',76786768,'7678676','78686','76786','76786','2023-05-11','/static/company/PROOF/20230521-214452.jpg','/static/company/BANK_PROOF/202','approved'),
(5,0,NULL,NULL,'/static/company/LOGO/20230617-113610.jpg','OYO (Oravel Stays Ltd)','45681','CONFIRM','HOSPITALITY','Gurugram','Haryana',' India','Gurugram',652457,'GURUGAM',2147483647,'oyoindia.com',547547,'1231E1','OYO GURUGRAM INDIA','G','INDIA','PNB',12542565241545,'PUNB010015','Ritesh Agarwal','CEO','S','1996-01-01','/static/company/PROOF/20230617-113610.jpg','/static/company/BANK_PROOF/202',NULL),
(6,0,NULL,NULL,'/static/company/LOGO/20230617-114158.jpg','Cochin International Airport L','145652','CONFIRM','TRAVEL','KOCHI','KERALA','KERALA','KOCHI',678425,'ALUVA',2147483647,'sabareeshk55@gmail.com',56452,'4546','CIAL KOCHI','TIRUR','INDIA','PNB',123423242424244545,'PUNB0100153','sarthak','CEO','k','1998-01-09','/static/company/PROOF/20230617-114158.jpg','/static/company/BANK_PROOF/202',NULL),
(7,10,NULL,NULL,'/static/company/LOGO/20230617-120417.jpg','Tata Technologies Limited','658987','CONFIRM','Engineering & Manufacturing','DELHI','DELHI','INDIA','SECTOR2',568745,'SECTOR 1',2147483647,'sabareeshk886@gmail.com',5632145,'45HG','TATA INDIA DELH','DELHI','INDIA','sbi',21345432678976,'sbi4321','ratan','ceo','tata','1989-01-02','/static/company/PROOF/20230617-120417.jpg','/static/company/BANK_PROOF/202',NULL);

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `complaint` varchar(500) DEFAULT NULL,
  `reply` varchar(500) DEFAULT NULL,
  `status` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`date`,`user_id`,`complaint`,`reply`,`status`) values 
(3,'2023-04-21',8,'NETWORK ISSUE','pending','pending'),
(4,'2023-04-27',8,'WALLET ISSUE','pending','pending'),
(5,'2023-06-17',8,'error','pending','pending');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `date` date DEFAULT NULL,
  `feedback` varchar(250) DEFAULT NULL,
  `rating` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`user_id`,`date`,`feedback`,`rating`) values 
(4,8,'2023-04-21','GOOD SERVICE','4.5');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`user_name`,`password`,`type`) values 
(1,'admin','123','admin'),
(2,'vishnuvprt@gmail.com','123','company'),
(8,'sadeed.abdulla@gmail.com','sadeed123','trader'),
(10,'sabareeshk886@gmail.com','7774793','company'),
(12,'001entertain@gmail.com','sri123','trader'),
(13,'nadasafeer12@gmail.com','krish123','trader');

/*Table structure for table `newsfeed` */

DROP TABLE IF EXISTS `newsfeed`;

CREATE TABLE `newsfeed` (
  `newsfeed_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(2000) DEFAULT NULL,
  `news_content` varchar(2000) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`newsfeed_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `newsfeed` */

insert  into `newsfeed`(`newsfeed_id`,`title`,`news_content`,`date`) values 
(1,'Should investors blindly follow the trend and invest in unlisted shares? Factors investors should consider?','The popularity of unlisted shares has grown as a result of the competition between new-age companies to reach the necessary threshold for being listed on the stock market. The majority of unlisted stocks are related to start-ups or small businesses. Evidently, small businesses have a smaller basis and hence expand more quickly than well-established businesses.Investment in unlisted stocks comes with its own share of risks and rewards. Every investor must know the risks and returns associated with every type of investment before choosing to invest. This will help them plan their finances better and set realistic investment goals.','24 Nov 2022, 03:31 PM IST');

/*Table structure for table `orders` */

DROP TABLE IF EXISTS `orders`;

CREATE TABLE `orders` (
  `order_id` int(11) NOT NULL AUTO_INCREMENT,
  `c_id` varchar(50) DEFAULT NULL,
  `available_lots` varchar(50) DEFAULT NULL,
  `total_price` int(11) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `orders` */

insert  into `orders`(`order_id`,`c_id`,`available_lots`,`total_price`,`quantity`) values 
(1,'1','5',200,10),
(2,'2','55',500,55),
(3,'3',NULL,NULL,NULL);

/*Table structure for table `portifolio` */

DROP TABLE IF EXISTS `portifolio`;

CREATE TABLE `portifolio` (
  `position` varchar(11) DEFAULT NULL,
  `history` varchar(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `portifolio` */

insert  into `portifolio`(`position`,`history`) values 
('hi','hello');

/*Table structure for table `trader` */

DROP TABLE IF EXISTS `trader`;

CREATE TABLE `trader` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `l_id` int(11) DEFAULT NULL,
  `user_name` varchar(30) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `pan` varchar(50) DEFAULT NULL,
  `dob` varchar(50) DEFAULT NULL,
  `contact` bigint(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `marital_status` varchar(50) DEFAULT NULL,
  `annual_income` int(50) DEFAULT NULL,
  `trading_experience` varchar(50) DEFAULT NULL,
  `occuppation` varchar(50) DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  `accountholder_name` varchar(50) DEFAULT NULL,
  `ifsc_code` varchar(50) DEFAULT NULL,
  `account_number` int(11) DEFAULT NULL,
  `account_type` varchar(50) DEFAULT NULL,
  `signature` varchar(150) DEFAULT NULL,
  `photo` varchar(200) DEFAULT NULL,
  `location` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `trader` */

insert  into `trader`(`user_id`,`l_id`,`user_name`,`address`,`pan`,`dob`,`contact`,`email`,`gender`,`marital_status`,`annual_income`,`trading_experience`,`occuppation`,`country`,`accountholder_name`,`ifsc_code`,`account_number`,`account_type`,`signature`,`photo`,`location`) values 
(4,8,'SADEED','MARAKATHEL (H), MARANCHERI (P.O)','MBCTY1234D','07/02/2000',9037462002,'sadeed.abdulla@gmail.com','Male','Single',0,NULL,'GOVERNMENT SECTOR','india','','FDRL0001706',2147483647,'Savings',NULL,'/static/trader/proof/20230617142639.jpg','INDIA'),
(7,13,'krish',NULL,NULL,'2000-06-17',7654324567,'nadasafeer12@gmail.com','Male','Married',0,NULL,'GOVERNMENT SECTOR','Afghanistan','Krishnan','sbi1234',987654321,'Savings',NULL,'/static/trader/proof/20230617142639.jpg','India');

/*Table structure for table `watchlist` */

DROP TABLE IF EXISTS `watchlist`;

CREATE TABLE `watchlist` (
  `watch_id` int(11) NOT NULL AUTO_INCREMENT,
  `c_id` int(11) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  PRIMARY KEY (`watch_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `watchlist` */

insert  into `watchlist`(`watch_id`,`c_id`,`uid`) values 
(1,0,8),
(3,3,8);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
