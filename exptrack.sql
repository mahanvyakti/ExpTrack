-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 29, 2020 at 01:52 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `exptrack`
--

-- --------------------------------------------------------

--
-- Table structure for table `budget`
--

CREATE TABLE `budget` (
  `savings` bigint(20) NOT NULL,
  `budget` bigint(20) NOT NULL,
  `date` datetime NOT NULL,
  `username1` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `budget`
--

INSERT INTO `budget` (`savings`, `budget`, `date`, `username1`) VALUES
(3000, 7000, '0000-00-00 00:00:00', 'dodo'),
(0, 0, '0000-00-00 00:00:00', 'fifi'),
(0, 0, '0000-00-00 00:00:00', 'jay24'),
(600, 400, '0000-00-00 00:00:00', 'koko'),
(300, 700, '0000-00-00 00:00:00', 'popo'),
(800, 200, '0000-00-00 00:00:00', 'tantanu'),
(0, 0, '2020-01-01 00:00:00', 'momo'),
(0, 0, '2020-03-01 00:00:00', 'momo'),
(5000, 20000, '2020-03-06 07:00:00', 'momo'),
(0, 0, '2020-04-01 00:00:00', 'momo'),
(3000, 3000, '2020-04-05 00:00:00', 'goi'),
(6000, 4000, '2020-04-05 00:00:00', 'raju12'),
(2000, 8000, '2020-04-05 10:00:00', 'user'),
(2000, 8000, '2020-04-06 00:00:00', 'aks'),
(3000, 6000, '2020-04-06 00:00:00', 'foi'),
(3000, 12000, '2020-04-15 00:00:00', 'momo');

-- --------------------------------------------------------

--
-- Table structure for table `expense`
--

CREATE TABLE `expense` (
  `category` varchar(20) NOT NULL,
  `mode` varchar(20) NOT NULL,
  `amount` bigint(20) NOT NULL,
  `date` datetime NOT NULL,
  `username` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `expense`
--

INSERT INTO `expense` (`category`, `mode`, `amount`, `date`, `username`) VALUES
('Null', 'Null', 0, '0000-00-00 00:00:00', 'dodo'),
('Null', 'Null', 0, '0000-00-00 00:00:00', 'fifi'),
('0', 'Null', 0, '0000-00-00 00:00:00', 'popo'),
('Null', 'Null', 0, '0000-00-00 00:00:00', 'tantanu'),
('Null', 'Null', 0, '2020-01-01 00:00:00', 'momo'),
('Null', 'Null', 0, '2020-03-01 00:00:00', 'momo'),
('fuel', 'UPI', 2000, '2020-03-10 18:46:22', 'momo'),
('food', 'Cheque', 5000, '2020-03-12 17:47:41', 'momo'),
('hospital', 'Card', 8000, '2020-03-16 20:48:44', 'momo'),
('Null', 'Null', 0, '2020-04-01 00:00:00', 'aks'),
('Null', 'Null', 0, '2020-04-01 00:00:00', 'foi'),
('Null', 'Null', 0, '2020-04-01 00:00:00', 'goi'),
('Null', 'Null', 0, '2020-04-01 00:00:00', 'momo'),
('Null', 'Null', 0, '2020-04-01 00:00:00', 'raju12'),
('Null', 'Null', 0, '2020-04-01 00:00:00', 'user'),
('food', 'Cash', 500, '2020-04-07 07:00:00', 'aks'),
('school', 'UPI', 500, '2020-04-08 09:00:00', 'raju12'),
('food', 'Cash', 5, '2020-04-10 04:00:00', 'raju12'),
('school', 'Card', 2000, '2020-04-13 09:00:00', 'user'),
('school', 'Cheque', 50, '2020-04-14 02:00:00', 'momo'),
('school', 'Cheque', 100, '2020-04-15 06:00:00', 'momo'),
('hospital', 'UPI', 500, '2020-04-17 07:00:00', 'momo'),
('other', 'Card', 100, '2020-04-18 09:00:00', 'momo'),
('fuel', 'Cash', 1000, '2020-04-18 09:00:00', 'raju12'),
('hospital', 'Cheque', 700, '2020-04-18 11:00:00', 'momo'),
('school', 'UPI', 500, '2020-04-19 06:00:00', 'momo'),
('hospital', 'Cheque', 750, '2020-04-20 03:00:00', 'raju12'),
('fuel', 'Cash', 8100, '2020-04-22 00:00:00', 'momo'),
('food', 'Card', 1000, '2020-04-22 07:00:00', 'raju12'),
('food', 'Cash', 300, '2020-04-23 00:00:00', 'momo'),
('fuel', 'Cash', 200, '2020-04-24 00:00:00', 'momo'),
('fuel', 'Card', 200, '2020-04-24 07:00:00', 'momo'),
('food', 'Cash', 1000, '2020-04-25 00:00:00', 'koko'),
('food', 'Cash', 200, '2020-04-25 00:00:00', 'momo'),
('hospital', 'Cash', 400, '2020-04-25 08:00:00', 'momo'),
('food', 'Cash', 0, '2020-04-26 00:00:00', 'momo'),
('food', 'Cash', 300, '2020-04-26 07:00:00', 'momo'),
('food', 'Cash', 200, '2020-04-26 09:30:56', 'momo');

-- --------------------------------------------------------

--
-- Table structure for table `income`
--

CREATE TABLE `income` (
  `amount` bigint(20) NOT NULL,
  `date` datetime NOT NULL,
  `source` varchar(30) NOT NULL,
  `username` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `income`
--

INSERT INTO `income` (`amount`, `date`, `source`, `username`) VALUES
(0, '0000-00-00 00:00:00', 'Null', 'fifi'),
(0, '0000-00-00 00:00:00', 'Null', 'jay24'),
(1000, '2000-02-12 00:00:00', 'business', 'tantanu'),
(0, '2020-01-01 00:00:00', 'Null', 'momo'),
(28000, '2020-01-02 11:00:00', 'salary', 'momo'),
(0, '2020-03-01 00:00:00', 'Null', 'momo'),
(25000, '2020-03-10 04:00:00', 'salary', 'momo'),
(0, '2020-04-01 00:00:00', 'Null', 'aks'),
(0, '2020-04-01 00:00:00', 'Null', 'foi'),
(0, '2020-04-01 00:00:00', 'Null', 'goi'),
(0, '2020-04-01 00:00:00', 'Null', 'momo'),
(0, '2020-04-01 00:00:00', 'Null', 'raju12'),
(0, '2020-04-01 00:00:00', 'Null', 'user'),
(10000, '2020-04-02 00:00:00', 'salary', 'dodo'),
(10000, '2020-04-03 00:00:00', 'business', 'foi'),
(10000, '2020-04-03 00:00:00', 'salary', 'goi'),
(10000, '2020-04-03 08:00:00', 'salary', 'raju12'),
(10000, '2020-04-03 10:00:00', 'salary', 'user'),
(10000, '2020-04-05 00:00:00', 'business', 'aks'),
(5000, '2020-04-05 02:00:00', 'gift voucher', 'momo'),
(10000, '2020-04-12 00:00:00', 'sal', 'momo'),
(15000, '2020-04-15 00:00:00', 'sal', 'momo'),
(1000, '2020-04-22 00:00:00', 'salary', 'koko'),
(1000, '2020-04-23 00:00:00', 'salary', 'popo');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `age` int(3) NOT NULL,
  `email` varchar(40) NOT NULL,
  `address` text NOT NULL,
  `gender` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`username`, `password`, `name`, `age`, `email`, `address`, `gender`) VALUES
('aks', 'patel', 'Akshar', 21, 'aks@gmail.com', 'Kalyan,Thane', 'Male'),
('dodo', 'dodo', 'doo', 28, 'doo@gmail.com', 'mkdasncsanms', 'Male'),
('fifi', 'fifi', 'fi', 78, 'fi@fi.com', 'dlmasma.,sd.as.', 'Female'),
('foi', '1234', 'foii', 25, 'foi@gmail.com', 'dndjdasdkjbkajdbj', 'Male'),
('goi', '1234', 'goi', 47, 'goi@gmail.com', 'enewkfwlfjwfj', 'Male'),
('jay24', '', '', 0, '', '', 'Male'),
('koko', '1234', 'kon', 36, 'kon@gmail.com', 'ewkndkwemwkwe', 'Female'),
('momo', 'monday', 'mohan ', 50, 'mon@gmail.com', 'Dadar,Mumbai,Maharashtra', 'Male'),
('popo', '', 'mon', 0, '', '', 'Male'),
('raju12', 'monday', 'raju', 26, 'raju@gmail.com', 'bhandup,mumbai', 'Male'),
('tantanu', '', '', 0, '', '', 'Male'),
('user', '123`', 'user', 35, 'use@gmail.com', 'lcjndjwndjqkj', 'Male');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `budget`
--
ALTER TABLE `budget`
  ADD PRIMARY KEY (`date`,`username1`),
  ADD KEY `c3` (`username1`);

--
-- Indexes for table `expense`
--
ALTER TABLE `expense`
  ADD PRIMARY KEY (`date`,`username`),
  ADD KEY `c2` (`username`);

--
-- Indexes for table `income`
--
ALTER TABLE `income`
  ADD PRIMARY KEY (`date`,`username`),
  ADD KEY `c1` (`username`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`username`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `budget`
--
ALTER TABLE `budget`
  ADD CONSTRAINT `c3` FOREIGN KEY (`username1`) REFERENCES `user` (`username`);

--
-- Constraints for table `expense`
--
ALTER TABLE `expense`
  ADD CONSTRAINT `c2` FOREIGN KEY (`username`) REFERENCES `user` (`username`);

--
-- Constraints for table `income`
--
ALTER TABLE `income`
  ADD CONSTRAINT `c1` FOREIGN KEY (`username`) REFERENCES `user` (`username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
