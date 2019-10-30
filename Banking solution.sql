/*
SQLyog - Free MySQL GUI v5.17
Host - 5.0.45-community-nt : Database - dbbank
*********************************************************************
Server version : 5.0.45-community-nt
*/


SET NAMES utf8;

SET SQL_MODE='';

create database if not exists `dbbank`;

USE `dbbank`;

SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO';

/*Table structure for table `tbadmin` */

DROP TABLE IF EXISTS `tbadmin`;

CREATE TABLE `tbadmin` (
  `admid` varchar(50) NOT NULL,
  `admpwd` varchar(50) default NULL,
  `admname` varchar(50) default NULL,
  `admsecques` varchar(50) default NULL,
  `admsecans` varchar(50) default NULL,
  `admgender` varchar(10) default NULL,
  `admaddress` varchar(50) default NULL,
  `admphno` int(11) default NULL,
  PRIMARY KEY  (`admid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `tbadmin` */

insert into `tbadmin` (`admid`,`admpwd`,`admname`,`admsecques`,`admsecans`,`admgender`,`admaddress`,`admphno`) values ('aa@gmail.com','123','sumit','what is your college name?','gndu','male','fzr',2147483647);

/*Table structure for table `tbtransaction` */

DROP TABLE IF EXISTS `tbtransaction`;

CREATE TABLE `tbtransaction` (
  `transid` int(11) NOT NULL,
  `transaccno` int(11) default NULL,
  `transtype` varchar(50) default NULL,
  `transamt` int(11) default NULL,
  `transdate` varchar(50) default NULL,
  `transtime` varchar(50) default NULL,
  PRIMARY KEY  (`transid`),
  KEY `FK_tbtransaction` (`transaccno`),
  CONSTRAINT `tbtransaction_ibfk_1` FOREIGN KEY (`transaccno`) REFERENCES `tbuser` (`accno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `tbtransaction` */

insert into `tbtransaction` (`transid`,`transaccno`,`transtype`,`transamt`,`transdate`,`transtime`) values (1,101,'withdraw',200,'15-07-2018','06:27:16');
/*Table structure for table `tbuser` */

DROP TABLE IF EXISTS `tbuser`;

CREATE TABLE `tbuser` (
  `accno` int(11) NOT NULL,
  `cname` varchar(50) default NULL,
  `caddress` varchar(50) default NULL,
  `cgender` varchar(50) default NULL,
  `cphno` bigint(15) default NULL,
  `cemail` varchar(50) default NULL,
  `odate` varchar(50) default NULL,
  `cbalance` int(11) default NULL,
  PRIMARY KEY  (`accno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `tbuser` */


insert into `tbuser` (`accno`,`cname`,`caddress`,`cgender`,`cphno`,`cemail`,`odate`,`cbalance`) values (101,'sps','fzr','male',98,'sumit65pal','14-07-2018',20800);
SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
