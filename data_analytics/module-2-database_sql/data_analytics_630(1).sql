-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 11, 2026 at 03:27 PM
-- Server version: 8.0.40
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `data_analytics_630`
--

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `empid` int NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `salary` int DEFAULT NULL,
  `manager_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`empid`, `name`, `salary`, `manager_id`) VALUES
(1, 'brijesh', 15500, 1),
(2, 'kavish', 25500, 1),
(3, 'noorie', 26500, 2),
(4, 'khushali', 15500, 1),
(5, 'jay', 35500, 2),
(6, 'mitesh', 45500, 1),
(7, 'sanket', 25500, 1);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_categories`
--

CREATE TABLE `tbl_categories` (
  `catid` int NOT NULL,
  `catname` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `tbl_categories`
--

INSERT INTO `tbl_categories` (`catid`, `catname`) VALUES
(1, 'electronics'),
(2, 'furniture'),
(3, 'toys'),
(4, 'clothes'),
(5, 'watches'),
(6, 'jwellery');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_department`
--

CREATE TABLE `tbl_department` (
  `depid` int NOT NULL,
  `depname` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `tbl_department`
--

INSERT INTO `tbl_department` (`depid`, `depname`) VALUES
(1, 'IT'),
(2, 'CSE'),
(3, 'EC'),
(4, 'EE'),
(5, 'HR'),
(6, 'BANKING');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_employee`
--

CREATE TABLE `tbl_employee` (
  `empid` int NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `firstname` varchar(200) DEFAULT NULL,
  `lastname` varchar(200) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL,
  `mobile` bigint DEFAULT NULL,
  `salary` decimal(10,2) DEFAULT NULL,
  `upload_image` varchar(200) DEFAULT NULL,
  `gender` enum('male','female','other') DEFAULT NULL,
  `address` text,
  `status` enum('active','inactive') DEFAULT NULL,
  `added_date_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_products`
--

CREATE TABLE `tbl_products` (
  `pid` int NOT NULL,
  `pname` varchar(255) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `catid` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `tbl_products`
--

INSERT INTO `tbl_products` (`pid`, `pname`, `price`, `catid`) VALUES
(1, 'oppo f7', 25000, 1),
(2, 'samsung galaxy', 36500, 1),
(3, 'single table', 22500, 2),
(4, 'relaxing chair', 6500, 2),
(5, 'asus laptop', 48500, 1),
(6, 'samsung galaxy', 25000, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_reviews`
--

CREATE TABLE `tbl_reviews` (
  `rid` int NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` bigint DEFAULT NULL,
  `rating` enum('*','**','***','****','*****') DEFAULT NULL,
  `comment` text,
  `added_date_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_salesman`
--

CREATE TABLE `tbl_salesman` (
  `id` int NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `mobile` bigint DEFAULT NULL,
  `address` text,
  `salary` decimal(10,2) DEFAULT NULL,
  `department` varchar(255) DEFAULT NULL,
  `create_at` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `tbl_salesman`
--

INSERT INTO `tbl_salesman` (`id`, `name`, `age`, `mobile`, `address`, `salary`, `department`, `create_at`) VALUES
(1, 'brijesh', 36, 952125962, 'near pandeypur churaha behind over bridge varansi', 115000.00, 'CSE', '01/09/2026 10:56'),
(2, 'noori', 24, 9121812, '150 feet ring road rajkot', 26800.00, 'HR', '31/08/2026 18:52'),
(3, 'khushali', 25, 888853656, '150 feet ring road rajkot', 27800.00, 'HR', '31/08/2026 18:52'),
(4, 'kavish', 23, 9121812645, '150 feet ring road rajkot', 27800.00, 'IT', '31/08/2026 18:52'),
(5, 'jay', 26, 9655121864, '150 feet ring road rajkot', 27800.00, 'CSE', '31/08/2026 18:52'),
(6, 'prakruti', NULL, 9122312135, NULL, NULL, NULL, NULL),
(7, 'sanket', NULL, 78460166, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Stand-in structure for view `tbl_salesman_view`
-- (See below for the actual view)
--
CREATE TABLE `tbl_salesman_view` (
`id` int
,`name` varchar(255)
,`mobile` bigint
);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_users`
--

CREATE TABLE `tbl_users` (
  `id` int NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `mobile` bigint DEFAULT NULL,
  `address` text,
  `appointmentdate_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `tbl_users`
--

INSERT INTO `tbl_users` (`id`, `name`, `email`, `password`, `mobile`, `address`, `appointmentdate_time`) VALUES
(3, 'nimesh', 'nimesh@gmail.com', 'n56454', 9998003879, 'rjt', '2026-09-02 18:00:58'),
(4, 'mitesh', 'nimesh007@gmail.com', 'k545454', 9998003871, 'ahmd', '2026-09-02 18:00:58');

-- --------------------------------------------------------

--
-- Structure for view `tbl_salesman_view`
--
DROP TABLE IF EXISTS `tbl_salesman_view`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `tbl_salesman_view`  AS SELECT `tbl_salesman`.`id` AS `id`, `tbl_salesman`.`name` AS `name`, `tbl_salesman`.`mobile` AS `mobile` FROM `tbl_salesman` WHERE (`tbl_salesman`.`id` in (1,3,4)) ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`empid`);

--
-- Indexes for table `tbl_categories`
--
ALTER TABLE `tbl_categories`
  ADD PRIMARY KEY (`catid`);

--
-- Indexes for table `tbl_department`
--
ALTER TABLE `tbl_department`
  ADD PRIMARY KEY (`depid`);

--
-- Indexes for table `tbl_employee`
--
ALTER TABLE `tbl_employee`
  ADD PRIMARY KEY (`empid`),
  ADD UNIQUE KEY `email` (`email`,`mobile`);

--
-- Indexes for table `tbl_products`
--
ALTER TABLE `tbl_products`
  ADD PRIMARY KEY (`pid`),
  ADD KEY `catid` (`catid`);

--
-- Indexes for table `tbl_reviews`
--
ALTER TABLE `tbl_reviews`
  ADD PRIMARY KEY (`rid`);

--
-- Indexes for table `tbl_salesman`
--
ALTER TABLE `tbl_salesman`
  ADD PRIMARY KEY (`id`),
  ADD KEY `indexsalesman` (`salary`),
  ADD KEY `indexsalesman1` (`id`,`name`,`salary`);

--
-- Indexes for table `tbl_users`
--
ALTER TABLE `tbl_users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`,`mobile`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `empid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `tbl_categories`
--
ALTER TABLE `tbl_categories`
  MODIFY `catid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `tbl_department`
--
ALTER TABLE `tbl_department`
  MODIFY `depid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `tbl_employee`
--
ALTER TABLE `tbl_employee`
  MODIFY `empid` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_products`
--
ALTER TABLE `tbl_products`
  MODIFY `pid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `tbl_reviews`
--
ALTER TABLE `tbl_reviews`
  MODIFY `rid` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_salesman`
--
ALTER TABLE `tbl_salesman`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `tbl_users`
--
ALTER TABLE `tbl_users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tbl_products`
--
ALTER TABLE `tbl_products`
  ADD CONSTRAINT `catid` FOREIGN KEY (`catid`) REFERENCES `tbl_categories` (`catid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
