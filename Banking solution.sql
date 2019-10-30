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
insert into `tbtransaction` (`transid`,`transaccno`,`transtype`,`transamt`,`transdate`,`transtime`) values (2,101,'deposit',50000,'15-07-2018','06:27:33');
insert into `tbtransaction` (`transid`,`transaccno`,`transtype`,`transamt`,`transdate`,`transtime`) values (3,101,'Transfer',3000,'15-07-2018','06:28:01');
insert into `tbtransaction` (`transid`,`transaccno`,`transtype`,`transamt`,`transdate`,`transtime`) values (4,102,'Transfer',3000,'15-07-2018','06:28:02');
insert into `tbtransaction` (`transid`,`transaccno`,`transtype`,`transamt`,`transdate`,`transtime`) values (5,101,'withdraw',5000,'15-07-2018','06:30:26');
insert into `tbtransaction` (`transid`,`transaccno`,`transtype`,`transamt`,`transdate`,`transtime`) values (6,101,'Transfer',5000,'15-07-2018','06:30:50');
insert into `tbtransaction` (`transid`,`transaccno`,`transtype`,`transamt`,`transdate`,`transtime`) values (7,102,'Transfer',5000,'15-07-2018','06:30:51');
insert into `tbtransaction` (`transid`,`transaccno`,`transtype`,`transamt`,`transdate`,`transtime`) values (8,101,'Transfer',10000,'15-07-2018','06:36:40');
insert into `tbtransaction` (`transid`,`transaccno`,`transtype`,`transamt`,`transdate`,`transtime`) values (9,102,'Transfer',10000,'15-07-2018','06:36:41');
insert into `tbtransaction` (`transid`,`transaccno`,`transtype`,`transamt`,`transdate`,`transtime`) values (10,105,'withdraw',600,'16-07-2018','15:22:24');
insert into `tbtransaction` (`transid`,`transaccno`,`transtype`,`transamt`,`transdate`,`transtime`) values (11,101,'Transfer',6000,'16-07-2018','15:23:19');
insert into `tbtransaction` (`transid`,`transaccno`,`transtype`,`transamt`,`transdate`,`transtime`) values (12,105,'Transfer',6000,'16-07-2018','15:23:20');

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

insert into `tbuser` (`accno`,`cname`,`caddress`,`cgender`,`cphno`,`cemail`,`odate`,`cbalance`) values (101,'sumit','afs','dsaf',123,'asdf','13-07-2018',22301);
insert into `tbuser` (`accno`,`cname`,`caddress`,`cgender`,`cphno`,`cemail`,`odate`,`cbalance`) values (102,'sumit','fzr','male',98,'sumit','14-07-2018',20800);
insert into `tbuser` (`accno`,`cname`,`caddress`,`cgender`,`cphno`,`cemail`,`odate`,`cbalance`) values (103,'sumit','asr','male',12,'saddA','14-07-2018',654);
insert into `tbuser` (`accno`,`cname`,`caddress`,`cgender`,`cphno`,`cemail`,`odate`,`cbalance`) values (104,'sumit','bti','male',64565,'sdf','14-07-2018',5646);
insert into `tbuser` (`accno`,`cname`,`caddress`,`cgender`,`cphno`,`cemail`,`odate`,`cbalance`) values (105,'harnam singh','fzr','m',123456789,'asdffghb','16-07-2018',10400);
insert into `tbuser` (`accno`,`cname`,`caddress`,`cgender`,`cphno`,`cemail`,`odate`,`cbalance`) values (106,'ravneet kaur','ferozepur','female',8437655565,'ravneetkr96@gmail.com','16-07-2018',6000);
insert into `tbuser` (`accno`,`cname`,`caddress`,`cgender`,`cphno`,`cemail`,`odate`,`cbalance`) values (107,'fdg1kh','kh','hkhk',6546,'ag','16-07-2018',64864);

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
