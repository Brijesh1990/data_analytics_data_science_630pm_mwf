-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 11, 2026 at 03:26 PM
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

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbl_salesman`
--
ALTER TABLE `tbl_salesman`
  ADD PRIMARY KEY (`id`),
  ADD KEY `indexsalesman` (`salary`),
  ADD KEY `indexsalesman1` (`id`,`name`,`salary`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbl_salesman`
--
ALTER TABLE `tbl_salesman`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
