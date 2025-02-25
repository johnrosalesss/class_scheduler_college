-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Feb 25, 2025 at 03:47 AM
-- Server version: 9.1.0
-- PHP Version: 8.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `class_scheduler_undergrad`
--

-- --------------------------------------------------------

--
-- Table structure for table `rooms`
--

DROP TABLE IF EXISTS `rooms`;
CREATE TABLE IF NOT EXISTS `rooms` (
  `room_id` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  `room_name` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `capacity` int DEFAULT NULL,
  PRIMARY KEY (`room_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `rooms`
--

INSERT INTO `rooms` (`room_id`, `room_name`, `capacity`) VALUES
('R020', 'Room 120', 40),
('R019', 'Room 119', 30),
('R018', 'Room 118', 50),
('R017', 'Room 117', 40),
('R016', 'Room 116', 30),
('R015', 'Room 115', 50),
('R014', 'Room 114', 40),
('R013', 'Room 113', 30),
('R012', 'Room 112', 50),
('R011', 'Room 111', 40),
('R010', 'Room 110', 30),
('R009', 'Room 109', 50),
('R008', 'Room 108', 40),
('R007', 'Room 107', 30),
('R006', 'Room 106', 50),
('R005', 'Room 105', 40),
('R004', 'Room 104', 30),
('R003', 'Room 103', 50),
('R002', 'Room 102', 40),
('R001', 'Room 101', 30),
('R021', 'Room 121', 50),
('R022', 'Room 122', 30),
('R023', 'Room 123', 40),
('R024', 'Room 124', 50),
('R025', 'Room 125', 30),
('R026', 'Room 126', 40),
('R027', 'Room 127', 50),
('R028', 'Room 128', 30),
('R029', 'Room 129', 40),
('R030', 'Room 130', 50),
('R031', 'Room 131', 30),
('R032', 'Room 132', 40),
('R033', 'Room 133', 50),
('R034', 'Room 134', 30),
('R035', 'Room 135', 40),
('R036', 'Room 136', 50),
('R037', 'Room 137', 30),
('R038', 'Room 138', 40),
('R039', 'Room 139', 50),
('R040', 'Room 140', 30),
('R041', 'Room 141', 40),
('R042', 'Room 142', 50),
('R043', 'Room 143', 30),
('R044', 'Room 144', 40),
('R045', 'Room 145', 50),
('R046', 'Room 146', 30),
('R047', 'Room 147', 40),
('R048', 'Room 148', 50),
('R049', 'Room 149', 30),
('R050', 'Room 150', 40),
('R151', 'Room 151', 30),
('R152', 'Room 152', 40),
('R153', 'Room 153', 50),
('R154', 'Room 154', 30),
('R155', 'Room 155', 40),
('R156', 'Room 156', 50),
('R157', 'Room 157', 30),
('R158', 'Room 158', 40),
('R159', 'Room 159', 50),
('R160', 'Room 160', 30),
('R161', 'Room 161', 40),
('R162', 'Room 162', 50),
('R163', 'Room 163', 30),
('R164', 'Room 164', 40),
('R165', 'Room 165', 50),
('R166', 'Room 166', 30),
('R167', 'Room 167', 40),
('R168', 'Room 168', 50),
('R169', 'Room 169', 30),
('R170', 'Room 170', 40),
('R171', 'Room 171', 50),
('R172', 'Room 172', 30),
('R173', 'Room 173', 40),
('R174', 'Room 174', 50),
('R175', 'Room 175', 30),
('R176', 'Room 176', 40),
('R177', 'Room 177', 50),
('R178', 'Room 178', 30),
('R179', 'Room 179', 40),
('R180', 'Room 180', 50),
('R181', 'Room 181', 30),
('R182', 'Room 182', 40),
('R183', 'Room 183', 50),
('R184', 'Room 184', 30),
('R185', 'Room 185', 40),
('R186', 'Room 186', 50),
('R187', 'Room 187', 30),
('R188', 'Room 188', 40),
('R189', 'Room 189', 50),
('R190', 'Room 190', 30),
('R191', 'Room 191', 40),
('R192', 'Room 192', 50),
('R193', 'Room 193', 30),
('R194', 'Room 194', 40),
('R195', 'Room 195', 50),
('R196', 'Room 196', 30),
('R197', 'Room 197', 40),
('R198', 'Room 198', 50),
('R199', 'Room 199', 30),
('R200', 'Room 200', 40),
('R201', 'Room 201', 50),
('R202', 'Room 202', 30),
('R203', 'Room 203', 40),
('R204', 'Room 204', 50),
('R205', 'Room 205', 30),
('R206', 'Room 206', 40),
('R207', 'Room 207', 50),
('R208', 'Room 208', 30),
('R209', 'Room 209', 40),
('R210', 'Room 210', 50),
('R211', 'Room 211', 30),
('R212', 'Room 212', 40),
('R213', 'Room 213', 50),
('R214', 'Room 214', 30),
('R215', 'Room 215', 40),
('R216', 'Room 216', 50),
('R217', 'Room 217', 30),
('R218', 'Room 218', 40),
('R219', 'Room 219', 50),
('R220', 'Room 220', 30),
('R221', 'Room 221', 40),
('R222', 'Room 222', 50),
('R223', 'Room 223', 30),
('R224', 'Room 224', 40),
('R225', 'Room 225', 50),
('R226', 'Room 226', 30),
('R227', 'Room 227', 40),
('R228', 'Room 228', 50),
('R229', 'Room 229', 30),
('R230', 'Room 230', 40),
('R231', 'Room 231', 50),
('R232', 'Room 232', 30),
('R233', 'Room 233', 40),
('R234', 'Room 234', 50),
('R235', 'Room 235', 30),
('R236', 'Room 236', 40),
('R237', 'Room 237', 50),
('R238', 'Room 238', 30),
('R239', 'Room 239', 40),
('R240', 'Room 240', 50),
('R241', 'Room 241', 30),
('R242', 'Room 242', 40),
('R243', 'Room 243', 50),
('R244', 'Room 244', 30),
('R245', 'Room 245', 40),
('R246', 'Room 246', 50),
('R247', 'Room 247', 30),
('R248', 'Room 248', 40),
('R249', 'Room 249', 50),
('R250', 'Room 250', 30);

-- --------------------------------------------------------

--
-- Table structure for table `schedule`
--

DROP TABLE IF EXISTS `schedule`;
CREATE TABLE IF NOT EXISTS `schedule` (
  `id` int NOT NULL AUTO_INCREMENT,
  `block_id` varchar(10) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `subject_code` varchar(10) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `teacher_name` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `room_name` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `day` varchar(10) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `start_time` time DEFAULT NULL,
  `end_time` time DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `subject_code` (`subject_code`),
  KEY `fk_schedule_block` (`block_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1133 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `schedule`
--

INSERT INTO `schedule` (`id`, `block_id`, `subject_code`, `teacher_name`, `room_name`, `day`, `start_time`, `end_time`) VALUES
(1001, 'General-1', 'GENED01', 'T036', 'Room 157', 'Monday', '15:00:00', '16:00:00'),
(1002, 'General-1', 'GENED01', 'T036', 'Room 182', 'Thursday', '09:00:00', '10:00:00'),
(1003, 'General-1', 'GENED01', 'T036', 'Room 218', 'Thursday', '15:00:00', '16:00:00'),
(1004, 'General-1', 'GENED02', 'T036', 'Room 161', 'Wednesday', '16:00:00', '17:00:00'),
(1005, 'General-1', 'GENED02', 'T036', 'Room 243', 'Monday', '16:00:00', '17:00:00'),
(1006, 'General-1', 'GENED02', 'T036', 'Room 115', 'Friday', '16:00:00', '17:00:00'),
(1007, 'General-1', 'GENED03', 'T037', 'Room 109', 'Monday', '09:00:00', '10:00:00'),
(1008, 'General-1', 'GENED03', 'T037', 'Room 235', 'Tuesday', '16:00:00', '17:00:00'),
(1009, 'General-1', 'GENED03', 'T037', 'Room 215', 'Monday', '16:00:00', '17:00:00'),
(1010, 'General-1', 'GENED04', 'T038', 'Room 174', 'Friday', '14:00:00', '15:00:00'),
(1011, 'General-1', 'GENED04', 'T038', 'Room 187', 'Friday', '09:00:00', '10:00:00'),
(1012, 'General-1', 'GENED04', 'T038', 'Room 227', 'Friday', '15:00:00', '16:00:00'),
(1013, 'General-2', 'GENED05', 'T039', 'Room 198', 'Thursday', '15:00:00', '16:00:00'),
(1014, 'General-2', 'GENED05', 'T039', 'Room 125', 'Monday', '09:00:00', '10:00:00'),
(1015, 'General-2', 'GENED05', 'T039', 'Room 169', 'Tuesday', '16:00:00', '17:00:00'),
(1016, 'General-2', 'GENED06', 'T040', 'Room 244', 'Monday', '09:00:00', '10:00:00'),
(1017, 'General-2', 'GENED06', 'T040', 'Room 153', 'Wednesday', '09:00:00', '10:00:00'),
(1018, 'General-2', 'GENED06', 'T040', 'Room 134', 'Saturday', '09:00:00', '10:00:00'),
(1019, 'General-2', 'GENED07', 'T041', 'Room 122', 'Wednesday', '16:00:00', '17:00:00'),
(1020, 'General-2', 'GENED07', 'T041', 'Room 131', 'Friday', '16:00:00', '17:00:00'),
(1021, 'General-2', 'GENED07', 'T041', 'Room 194', 'Thursday', '16:00:00', '17:00:00'),
(1022, 'Computer S', 'CS101', 'T001', 'Room 228', 'Thursday', '14:00:00', '15:00:00'),
(1023, 'Computer S', 'CS101', 'T001', 'Room 101', 'Friday', '16:00:00', '17:00:00'),
(1024, 'Computer S', 'CS101', 'T001', 'Room 248', 'Friday', '16:00:00', '17:00:00'),
(1025, 'Computer S', 'CS102', 'T001', 'Room 194', 'Thursday', '09:00:00', '10:00:00'),
(1026, 'Computer S', 'CS102', 'T001', 'Room 195', 'Saturday', '15:00:00', '16:00:00'),
(1027, 'Computer S', 'CS102', 'T001', 'Room 153', 'Monday', '15:00:00', '16:00:00'),
(1028, 'Computer S', 'CS103', 'T002', 'Room 115', 'Saturday', '15:00:00', '16:00:00'),
(1029, 'Computer S', 'CS103', 'T002', 'Room 228', 'Tuesday', '14:00:00', '15:00:00'),
(1030, 'Computer S', 'CS103', 'T002', 'Room 142', 'Saturday', '16:00:00', '17:00:00'),
(1031, 'Computer S', 'CS104', 'T003', 'Room 164', 'Tuesday', '16:00:00', '17:00:00'),
(1032, 'Computer S', 'CS104', 'T003', 'Room 142', 'Tuesday', '16:00:00', '17:00:00'),
(1033, 'Computer S', 'CS104', 'T003', 'Room 212', 'Wednesday', '09:00:00', '10:00:00'),
(1034, 'Informatio', 'IT101', 'T004', 'Room 242', 'Thursday', '15:00:00', '16:00:00'),
(1035, 'Informatio', 'IT101', 'T004', 'Room 225', 'Monday', '16:00:00', '17:00:00'),
(1036, 'Informatio', 'IT101', 'T004', 'Room 140', 'Friday', '09:00:00', '10:00:00'),
(1037, 'Informatio', 'IT102', 'T005', 'Room 136', 'Monday', '14:00:00', '15:00:00'),
(1038, 'Informatio', 'IT102', 'T005', 'Room 124', 'Monday', '14:00:00', '15:00:00'),
(1039, 'Informatio', 'IT102', 'T005', 'Room 176', 'Thursday', '14:00:00', '15:00:00'),
(1040, 'Informatio', 'IT103', 'T005', 'Room 127', 'Monday', '15:00:00', '16:00:00'),
(1041, 'Informatio', 'IT103', 'T005', 'Room 109', 'Thursday', '14:00:00', '15:00:00'),
(1042, 'Nursing-1', 'BSN101', 'T006', 'Room 212', 'Tuesday', '15:00:00', '16:00:00'),
(1043, 'Nursing-1', 'BSN101', 'T006', 'Room 124', 'Saturday', '09:00:00', '10:00:00'),
(1044, 'Nursing-1', 'BSN101', 'T006', 'Room 238', 'Friday', '14:00:00', '15:00:00'),
(1045, 'Nursing-1', 'BSN102', 'T006', 'Room 237', 'Tuesday', '09:00:00', '10:00:00'),
(1046, 'Nursing-1', 'BSN102', 'T006', 'Room 182', 'Saturday', '09:00:00', '10:00:00'),
(1047, 'Nursing-1', 'BSN102', 'T006', 'Room 229', 'Thursday', '16:00:00', '17:00:00'),
(1048, 'Nursing-2', 'BSN201', 'T007', 'Room 244', 'Thursday', '14:00:00', '15:00:00'),
(1049, 'Nursing-2', 'BSN201', 'T007', 'Room 213', 'Friday', '09:00:00', '10:00:00'),
(1050, 'Nursing-2', 'BSN201', 'T007', 'Room 146', 'Tuesday', '14:00:00', '15:00:00'),
(1051, 'Nursing-2', 'BSN202', 'T008', 'Room 138', 'Wednesday', '15:00:00', '16:00:00'),
(1052, 'Nursing-2', 'BSN202', 'T008', 'Room 164', 'Saturday', '14:00:00', '15:00:00'),
(1053, 'Nursing-2', 'BSN202', 'T008', 'Room 247', 'Friday', '15:00:00', '16:00:00'),
(1054, 'Nursing-3', 'BSN301', 'T009', 'Room 108', 'Wednesday', '14:00:00', '15:00:00'),
(1055, 'Nursing-3', 'BSN301', 'T009', 'Room 105', 'Saturday', '14:00:00', '15:00:00'),
(1056, 'Nursing-3', 'BSN301', 'T009', 'Room 145', 'Friday', '16:00:00', '17:00:00'),
(1057, 'Nursing-4', 'BSN401', 'T010', 'Room 228', 'Friday', '15:00:00', '16:00:00'),
(1058, 'Nursing-4', 'BSN401', 'T010', 'Room 145', 'Tuesday', '16:00:00', '17:00:00'),
(1059, 'Nursing-4', 'BSN401', 'T010', 'Room 142', 'Friday', '15:00:00', '16:00:00'),
(1060, 'Hospitalit', 'HM101', 'T011', 'Room 131', 'Thursday', '16:00:00', '17:00:00'),
(1061, 'Hospitalit', 'HM101', 'T011', 'Room 243', 'Monday', '09:00:00', '10:00:00'),
(1062, 'Hospitalit', 'HM101', 'T011', 'Room 250', 'Thursday', '15:00:00', '16:00:00'),
(1063, 'Hospitalit', 'HM102', 'T012', 'Room 214', 'Tuesday', '16:00:00', '17:00:00'),
(1064, 'Hospitalit', 'HM102', 'T012', 'Room 182', 'Thursday', '16:00:00', '17:00:00'),
(1065, 'Hospitalit', 'HM102', 'T012', 'Room 137', 'Thursday', '14:00:00', '15:00:00'),
(1066, 'Hospitalit', 'HM201', 'T013', 'Room 209', 'Thursday', '16:00:00', '17:00:00'),
(1067, 'Hospitalit', 'HM201', 'T013', 'Room 241', 'Saturday', '16:00:00', '17:00:00'),
(1068, 'Hospitalit', 'HM201', 'T013', 'Room 220', 'Tuesday', '15:00:00', '16:00:00'),
(1069, 'Hospitalit', 'HM301', 'T014', 'Room 168', 'Tuesday', '09:00:00', '10:00:00'),
(1070, 'Hospitalit', 'HM301', 'T014', 'Room 222', 'Thursday', '16:00:00', '17:00:00'),
(1071, 'Hospitalit', 'HM301', 'T014', 'Room 206', 'Saturday', '09:00:00', '10:00:00'),
(1072, 'Hospitalit', 'HM401', 'T015', 'Room 125', 'Wednesday', '15:00:00', '16:00:00'),
(1073, 'Hospitalit', 'HM401', 'T015', 'Room 186', 'Saturday', '15:00:00', '16:00:00'),
(1074, 'Hospitalit', 'HM401', 'T015', 'Room 132', 'Wednesday', '15:00:00', '16:00:00'),
(1075, 'Business A', 'BA101', 'T016', 'Room 209', 'Monday', '16:00:00', '17:00:00'),
(1076, 'Business A', 'BA101', 'T016', 'Room 183', 'Monday', '15:00:00', '16:00:00'),
(1077, 'Business A', 'BA101', 'T016', 'Room 204', 'Saturday', '14:00:00', '15:00:00'),
(1078, 'Business A', 'BA102', 'T017', 'Room 125', 'Thursday', '14:00:00', '15:00:00'),
(1079, 'Business A', 'BA102', 'T017', 'Room 147', 'Friday', '16:00:00', '17:00:00'),
(1080, 'Business A', 'BA201', 'T018', 'Room 156', 'Thursday', '14:00:00', '15:00:00'),
(1081, 'Business A', 'BA201', 'T018', 'Room 250', 'Tuesday', '14:00:00', '15:00:00'),
(1082, 'Business A', 'BA201', 'T018', 'Room 156', 'Tuesday', '15:00:00', '16:00:00'),
(1083, 'Business A', 'BA301', 'T019', 'Room 213', 'Thursday', '16:00:00', '17:00:00'),
(1084, 'Business A', 'BA301', 'T019', 'Room 101', 'Tuesday', '14:00:00', '15:00:00'),
(1085, 'Business A', 'BA301', 'T019', 'Room 240', 'Tuesday', '14:00:00', '15:00:00'),
(1086, 'Accounting', 'BSA101', 'T020', 'Room 129', 'Monday', '14:00:00', '15:00:00'),
(1087, 'Accounting', 'BSA101', 'T020', 'Room 214', 'Thursday', '15:00:00', '16:00:00'),
(1088, 'Accounting', 'BSA101', 'T020', 'Room 182', 'Wednesday', '16:00:00', '17:00:00'),
(1089, 'Accounting', 'BSA102', 'T021', 'Room 204', 'Tuesday', '14:00:00', '15:00:00'),
(1090, 'Accounting', 'BSA102', 'T021', 'Room 218', 'Tuesday', '16:00:00', '17:00:00'),
(1091, 'Accounting', 'BSA102', 'T021', 'Room 237', 'Monday', '09:00:00', '10:00:00'),
(1092, 'Accounting', 'BSA201', 'T022', 'Room 106', 'Friday', '16:00:00', '17:00:00'),
(1093, 'Accounting', 'BSA201', 'T022', 'Room 180', 'Friday', '15:00:00', '16:00:00'),
(1094, 'Accounting', 'BSA201', 'T022', 'Room 113', 'Friday', '09:00:00', '10:00:00'),
(1095, 'Accounting', 'BSA301', 'T023', 'Room 189', 'Wednesday', '15:00:00', '16:00:00'),
(1096, 'Accounting', 'BSA301', 'T023', 'Room 187', 'Friday', '09:00:00', '10:00:00'),
(1097, 'Accounting', 'BSA301', 'T023', 'Room 115', 'Saturday', '09:00:00', '10:00:00'),
(1098, 'Psychology', 'PSY101', 'T024', 'Room 132', 'Thursday', '14:00:00', '15:00:00'),
(1099, 'Psychology', 'PSY101', 'T024', 'Room 159', 'Friday', '14:00:00', '15:00:00'),
(1100, 'Psychology', 'PSY101', 'T024', 'Room 172', 'Wednesday', '14:00:00', '15:00:00'),
(1101, 'Psychology', 'PSY102', 'T025', 'Room 161', 'Monday', '09:00:00', '10:00:00'),
(1102, 'Psychology', 'PSY102', 'T025', 'Room 169', 'Tuesday', '15:00:00', '16:00:00'),
(1103, 'Psychology', 'PSY102', 'T025', 'Room 241', 'Friday', '15:00:00', '16:00:00'),
(1104, 'Psychology', 'PSY201', 'T026', 'Room 138', 'Saturday', '15:00:00', '16:00:00'),
(1105, 'Psychology', 'PSY201', 'T026', 'Room 164', 'Saturday', '09:00:00', '10:00:00'),
(1106, 'Psychology', 'PSY301', 'T027', 'Room 159', 'Saturday', '09:00:00', '10:00:00'),
(1107, 'Psychology', 'PSY301', 'T027', 'Room 204', 'Friday', '09:00:00', '10:00:00'),
(1108, 'Psychology', 'PSY301', 'T027', 'Room 129', 'Saturday', '15:00:00', '16:00:00'),
(1109, 'Engineerin', 'ENG101', 'T028', 'Room 152', 'Tuesday', '15:00:00', '16:00:00'),
(1110, 'Engineerin', 'ENG101', 'T028', 'Room 161', 'Saturday', '09:00:00', '10:00:00'),
(1111, 'Engineerin', 'ENG101', 'T028', 'Room 187', 'Tuesday', '16:00:00', '17:00:00'),
(1112, 'Engineerin', 'ENG102', 'T029', 'Room 241', 'Thursday', '15:00:00', '16:00:00'),
(1113, 'Engineerin', 'ENG102', 'T029', 'Room 220', 'Saturday', '15:00:00', '16:00:00'),
(1114, 'Engineerin', 'ENG102', 'T029', 'Room 132', 'Saturday', '15:00:00', '16:00:00'),
(1115, 'Engineerin', 'ENG201', 'T030', 'Room 153', 'Monday', '16:00:00', '17:00:00'),
(1116, 'Engineerin', 'ENG201', 'T030', 'Room 161', 'Friday', '14:00:00', '15:00:00'),
(1117, 'Engineerin', 'ENG201', 'T030', 'Room 128', 'Wednesday', '14:00:00', '15:00:00'),
(1118, 'Engineerin', 'ENG301', 'T031', 'Room 229', 'Friday', '15:00:00', '16:00:00'),
(1119, 'Engineerin', 'ENG301', 'T031', 'Room 134', 'Monday', '09:00:00', '10:00:00'),
(1120, 'Engineerin', 'ENG301', 'T031', 'Room 167', 'Thursday', '16:00:00', '17:00:00'),
(1121, 'Education-', 'ED101', 'T032', 'Room 202', 'Tuesday', '14:00:00', '15:00:00'),
(1122, 'Education-', 'ED101', 'T032', 'Room 244', 'Tuesday', '15:00:00', '16:00:00'),
(1123, 'Education-', 'ED101', 'T032', 'Room 139', 'Monday', '14:00:00', '15:00:00'),
(1124, 'Education-', 'ED102', 'T033', 'Room 154', 'Wednesday', '16:00:00', '17:00:00'),
(1125, 'Education-', 'ED102', 'T033', 'Room 126', 'Wednesday', '15:00:00', '16:00:00'),
(1126, 'Education-', 'ED102', 'T033', 'Room 124', 'Thursday', '15:00:00', '16:00:00'),
(1127, 'Education-', 'ED201', 'T034', 'Room 134', 'Saturday', '09:00:00', '10:00:00'),
(1128, 'Education-', 'ED201', 'T034', 'Room 163', 'Monday', '15:00:00', '16:00:00'),
(1129, 'Education-', 'ED201', 'T034', 'Room 248', 'Tuesday', '14:00:00', '15:00:00'),
(1130, 'Education-', 'ED301', 'T035', 'Room 200', 'Wednesday', '14:00:00', '15:00:00'),
(1131, 'Education-', 'ED301', 'T035', 'Room 197', 'Saturday', '15:00:00', '16:00:00'),
(1132, 'Education-', 'ED301', 'T035', 'Room 170', 'Monday', '14:00:00', '15:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
CREATE TABLE IF NOT EXISTS `student` (
  `id` int NOT NULL AUTO_INCREMENT,
  `school_aide_id` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `last_name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `first_name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `rfid` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `section` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=1772 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`id`, `school_aide_id`, `last_name`, `first_name`, `rfid`, `section`) VALUES
(114, '2023000145', 'CASIM', 'FRANCE PATRICIA PAMELA DE GUZMAN', '781382499', 'Engineering - 2'),
(202, '2015100032', 'FERNANDEZ', 'ANNA KATRINA ABEJAR', '295072275', 'Nursing - 4'),
(224, '2020200134', 'GARRIDO', 'TRIXIA MAE AGUILAR', '777102691', 'Hospitality Management - 1'),
(261, '2020200265', 'JIAO', 'FRANCHESKA JAYE VILANO', '783575073', 'Accounting - 2'),
(335, '2024000006', 'MATIBAG', 'ANN MARJORIE LAPUZ', '811038439', 'Accounting - 2'),
(434, '2023000009', 'REGIS', 'GIO MARK LANDAYAN', '162086906', 'Computer Science - 1'),
(443, '2024000143', 'ROJAS', 'ROSEANNE JADER', '986211642', 'Education - 3'),
(475, '2021101118', 'SIBAL', 'RODJAN CORDOVA', '162261690', 'Engineering - 1'),
(488, '2022000374', 'SUDARA', 'ERIKA MARI TRIPOLI', '115434481', 'Computer Science - 3'),
(514, '2024000142', 'TRILLANA', 'KATRINA ISABEL VILLANUEVA', '777778753', 'Accounting - 2'),
(524, '2023000064', 'UY', 'JOANNA MARIE PABALAN', '555196755', 'Engineering - 2'),
(538, '2023000003', 'VILLANUEVA', 'FRANCIS JHULIAN VALERIO', '810848023', 'Information Technology - 3'),
(598, '2022200557', 'ACUEZA', 'HANS SHYLLA CORRECES', '289342755', 'Engineering - 1'),
(600, '2021200221', 'ADVINCULA', 'MARY DEI PEREZ', '959048647', 'Psychology - 4'),
(635, '2022200613', 'AMBROSIO', 'AALIYAH JULIANNA SANTOS', '165492625', 'Nursing - 4'),
(640, '2022200346', 'ANDRES', 'LOUIENAIRE CRUZ', '270055955', 'Psychology - 1'),
(644, '2023200201', 'ANGOBUNG', 'ANGEL ANDREA DELA CRUZ', '858671738', 'Computer Science - 1'),
(648, '2021200084', 'ANTIPORDA', 'SOPHIA MICHAELA FRANCISCO', '100961121', 'Hospitality Management - 3'),
(659, '2021200226', 'ARCE', 'ARIANNE RUTH NICOLE SILVA', '463561697', 'Computer Science - 3'),
(668, '2022200548', 'ARUALES', 'NIKKI GEAN', '197733562', 'Accounting - 3'),
(683, '2008501814', 'AZUR', 'ANNA ANOG', '457764577', 'Accounting - 2'),
(693, '2022200294', 'BALAYAN', 'ERYCA ANNE ARCIAGA', '197655914', 'Computer Science - 3'),
(699, '2019200309', 'BALTAZAR', 'JULLIANE MARIE CAYETANO', '115402769', 'Business Administration - 4'),
(710, '2022200361', 'BASE', 'JULIA KLARISSE HERRERA', '276689907', 'Psychology - 1'),
(717, '2021A00011', 'BAUTISTA', 'LORAINE GRACE CARLOS', '117109009', 'Hospitality Management - 3'),
(726, '2021200031', 'BELTRAN', 'CYRILLE DOMINGO', '114855601', 'Information Technology - 3'),
(732, '2023200204', 'BERDOLAGA', 'KIM SAN PEDRO', '300545027', 'Psychology - 2'),
(736, '2021200190', 'BICEN', 'JAMILA JUNTILLA', '491189650', 'Computer Science - 3'),
(743, '2010500250', 'BOBIS', 'RAINE ANTOINETTE MASBAD', '248179731', 'Business Administration - 2'),
(761, '2022200006', 'BRIN', 'ANGELEI MARITHE', '268692467', 'Psychology - 3'),
(766, '2022200602', 'BUAN', 'RAQUEL JACOB', '285213971', 'Nursing - 1'),
(779, '2021200197', 'CABALLES', 'DENISSE ANGELA AGBAYANI', '298474275', 'Engineering - 3'),
(789, '2021200052', 'CALAOAGAN', 'MARY BELINDA BASA', '166458273', 'Hospitality Management - 4'),
(790, '2022200351', 'CALDERON', 'BIANCA MAE ALFONSO', '153287057', 'Computer Science - 4'),
(791, '2022200348', 'CALIANGA', 'BEA ANGELINE GERALDO', '453854689', 'Business Administration - 3'),
(793, '2024200065', 'CALUBAQUIB', 'BIANCA ANGELOU BALUYO', '162209530', 'Hospitality Management - 4'),
(801, '2022200303', 'CANLOBO', 'RIANNE HAZEL UGALDE', '829116087', 'Information Technology - 1'),
(803, '2021200266', 'CANSADO', 'AALIYAH KYLENE REPLAN', '161103802', 'Psychology - 2'),
(813, '2023200285', 'CASTOLO', 'ALYSA MAE MALALUAN', '244072483', 'Nursing - 3'),
(816, '2007501531', 'CASTRO', 'MAXINE CRYSTELLE DEL ROSARIO', '469288417', 'Information Technology - 1'),
(841, '2021200032', 'CONSTANTINO', 'RENAE AUNDREA CENTENO', '987351930', 'Education - 2'),
(851, '2023200042', 'CRESPO', 'DENISE MOIRA CAMARA', '223224995', 'Accounting - 2'),
(870, '2020300079', 'CRUZ', 'KIA FADUL', '863093626', 'Nursing - 1'),
(872, '2023200082', 'CRUZ', 'KRISTIANNA ELOISE ZAPANTA', '111234337', 'Business Administration - 4'),
(875, '2024200140', 'CRUZ', 'MYIESHA KAYIN ARANETA', '736724848', 'Education - 1'),
(876, '2021200195', 'CRUZ', 'NAEOMIE ASHLEY LORENZO', '181418458', 'Hospitality Management - 3'),
(877, '2021200194', 'CRUZ', 'NAEOMIE PATRICE LORENZO', '182413738', 'Accounting - 2'),
(878, '2021200049', 'CRUZ', 'ROSEANNA MICHELLE CLEMENTE', '810461351', 'Psychology - 3'),
(884, '2021200002', 'CUBILLA', 'LEILA TRICIA ABENUMAN', '987838458', 'Information Technology - 3'),
(894, '2022200622', 'DADO', 'AARYANNA JAE NUNEZ', '249351731', 'Hospitality Management - 4'),
(896, '2022200314', 'DALANON', 'SHEEN', '138395041', 'Accounting - 1'),
(901, '2023200016', 'DAR', 'AINGELLE JOHNSHLHYNE KHRINSETH MENDOZA', '858840719', 'Information Technology - 4'),
(902, '2022200612', 'DAUZ', 'CLAIRE DANIELLE BUENO', '235050227', 'Hospitality Management - 2'),
(918, '2022200324', 'DE JESUS', 'MA. CEFERINA EMMA GRANADA', '198144842', 'Information Technology - 3'),
(931, '2023200098', 'DE VERA', 'AALIYAH FRANCESCCA SAGER', '230721699', 'Computer Science - 4'),
(935, '2021200274', 'DEL MUNDO', 'ANN DANNAH LUMADILLA', '959258615', 'Business Administration - 3'),
(941, '2023200070', 'DEL VALLE', 'JULIANNE JAYNE KHO', '866760058', 'Computer Science - 4'),
(944, '2022200320', 'DELA CRUZ', 'DAISY RAIN MANGULABNAN', '289084691', 'Information Technology - 1'),
(949, '2020300058', 'DELA CRUZ', 'SOPHIA MICHAELAH ARABEJO', '181067834', 'Engineering - 4'),
(961, '2023200179', 'DELOS', 'AMA, KEECHEE SIBAYAN', '231234707', 'Engineering - 3'),
(972, '2021200135', 'DIAZ', 'THERESE CARMELA RUBIO', '677134394', 'Business Administration - 1'),
(974, '2021200272', 'DILLENA', 'RITA JANE SABILALA', '462983137', 'Engineering - 1'),
(977, '2022200293', 'DINO', 'ZAMAICA GANADE', '251408371', 'Business Administration - 4'),
(978, '2022200359', 'DIONELA', 'MARION OSIAS', '813893639', 'Business Administration - 4'),
(984, '2022200507', 'DOMINGO', 'FRANCINE MALLARI', '197232538', 'Nursing - 2'),
(985, '2021200198', 'DONATO', 'ZIA LORRAINE GARCIA', '269751587', 'Nursing - 1'),
(990, '2022200335', 'DULOG', 'BEATRIZ ISABELLE', '164883649', 'Psychology - 2'),
(995, '2022200558', 'EBITA', 'ALYSSA JOSH SALVATIERRA', '155391393', 'Hospitality Management - 3'),
(1012, '2022200350', 'ESCAÑO', 'KEETH CORPUZ', '242432835', 'Education - 4'),
(1047, '2022200001', 'FERNANDEZ', 'JONA MA. LAYA DELIMA', '295923987', 'Education - 1'),
(1055, '2021200152', 'FLORES', 'KHIRSTEN RAYNE JARIN', '959555159', 'Accounting - 4'),
(1067, '2023200257', 'FRANCISCO', 'RENALYN PAJAROJA', '863371930', 'Hospitality Management - 3'),
(1077, '2021200218', 'GALVE', 'ATASHA NICOLE FRANCES COLLADO', '829517879', 'Information Technology - 2'),
(1082, '2021200137', 'GAPAS', 'RUZZLE KAIRA', '986252746', 'Psychology - 3'),
(1083, '2021200006', 'GAPIDO', 'MARIA DOMINIQUE SERDON', '497590162', 'Psychology - 3'),
(1086, '2017300076', 'GARCIA', 'ANIKA DIANTHA ALYANA BOBIS', '813884215', 'Information Technology - 4'),
(1088, '2022200419', 'GARCIA', 'JILLIAN CHEYENNE MAÑOSA', '156172673', 'Nursing - 4'),
(1092, '2022200364', 'GARCIA', 'TRISHA STEPHANIE', '183326890', 'Education - 1'),
(1095, '2021200110', 'GATMAYTAN', 'CARMEN ALIYAH MERCEDES REYES', '959518423', 'Business Administration - 4'),
(1118, '2010500013', 'GUINGON', 'TATIANA LINDA RAMONES', '829702343', 'Accounting - 1'),
(1123, '2021200228', 'GUTIERREZ', 'DANICA BEATRIZE CONCEPCION', '695909450', 'Psychology - 1'),
(1129, '2020300097', 'HADJIRUL', 'CHRISTIANNE KELSEY ROQUE', '813668023', 'Accounting - 4'),
(1133, '2022200560', 'HERNANDEZ', 'MA. GABRIELLA BAQUIRAN', '183382330', 'Information Technology - 2'),
(1142, '2022200633', 'IGNACIO', 'RIZZAINE SANTOS', '166510737', 'Business Administration - 2'),
(1143, '2023200017', 'IGNACIO', 'YESHA JANYNNE CRUZ', '864578170', 'Computer Science - 3'),
(1144, '2023200047', 'ILAGAN', 'MIKAELA MAY BITUIN', '858358650', 'Business Administration - 4'),
(1155, '2021200123', 'JAO', 'JAEMARIE REIGN TECSON', '301727763', 'Business Administration - 2'),
(1162, '2021200258', 'JUNSAY', 'NICE CARLENE GAVIOLA', '695453178', 'Engineering - 3'),
(1169, '2021200094', 'KWAN', 'HANNAH DEBORAH MERCADO', '277743907', 'Nursing - 2'),
(1178, '2022200399', 'LAMANO', 'DIANE MARGARETTE NATIVIDAD', '829570487', 'Information Technology - 4'),
(1183, '2022200319', 'LAO', 'SHEAN NATHALIE AMATA', '198071514', 'Engineering - 4'),
(1184, '2010500113', 'LAPESURA', 'CARMELA ADOR', '183379962', 'Psychology - 2'),
(1190, '2022200291', 'LAZARO', 'LEIANNE MEDINA', '974742119', 'Computer Science - 1'),
(1199, '2022200286', 'LEGASPI', 'ROBYNNE GAILE CLEOFAS', '495911570', 'Psychology - 2'),
(1206, '2022200555', 'LIZARDO', 'ASHLEY NICOLE BAUTISTA', '197626666', 'Accounting - 3'),
(1209, '2019A00061', 'LLENA', 'DIANNE CLAIRE BALVERDE', '958661527', 'Education - 2'),
(1224, '2024200293', 'MABUSING', 'ABDUL MUEED ANAM', '857346682', 'Accounting - 1'),
(1232, '2022200549', 'MADRIGAL', 'EIRALIZ GUBI', '157288129', 'Psychology - 1'),
(1238, '2021300026', 'MAGLONZO', 'SHANE MARIE UY', '872044938', 'Computer Science - 2'),
(1241, '2023200102', 'MALAPAD', 'CHARLOTTE ANNE PANGAN', '866958442', 'Accounting - 4'),
(1245, '2022200406', 'MANABAT', 'PAMELA MAE NACIANCENO', '298390803', 'Information Technology - 3'),
(1248, '2009401608', 'MANANGHAYA', 'FELICIA ANTONINA BOLHAYON', '166035889', 'Education - 3'),
(1263, '2019200331', 'MARCOS', 'NICOLE ANDRE VISAYA', '810878743', 'Information Technology - 3'),
(1266, '2012400062', 'MARIANO', 'ANNETTE GUEVARRA', '181689834', 'Accounting - 3'),
(1272, '2015900020', 'MARTINEZ', 'LUCIA FERNANDEZ', '829677943', 'Computer Science - 3'),
(1286, '2022200609', 'MELENDRES', 'SAMANTHA MICKAELA AGUILAR', '295596323', 'Computer Science - 1'),
(1302, '2022200404', 'MINDO', 'RHEVIECHEN ARSZEN MUNGCAL', '288192275', 'Engineering - 2'),
(1308, '2021200245', 'MONJE', 'HANA MARIE VENTURA', '988553194', 'Business Administration - 4'),
(1311, '2020200107', 'MONTON', 'NEA PEREZ', '153882801', 'Business Administration - 2'),
(1313, '2019300165', 'MORALEJO', 'SOPHIA NICOLE PANGILINAN', '999723402', 'Business Administration - 2'),
(1316, '2020200293', 'MORILLO', 'CLAUDETTE SALALIMA', '975669767', 'Accounting - 2'),
(1319, '2022200413', 'MUECO', 'HALLE BEATRICE DOLATRE', '156796577', 'Psychology - 2'),
(1331, '2020200051', 'NARIDA', 'ALYSSA MARIE GADUYON', '286035715', 'Business Administration - 2'),
(1333, '2022200388', 'NATIVIDAD', 'COLLEEN BONDOY', '245925411', 'Education - 4'),
(1339, '2021200050', 'NAVIDA', 'PAULINE LOUISE TAN', '454718673', 'Computer Science - 1'),
(1342, '2008501939', 'NERI', 'PAULINE GOLDA DE GUZMAN', '103931089', 'Hospitality Management - 4'),
(1350, '2023200009', 'NICOLAS', 'ROBERTA MIGUELLA MARIA ALONZO', '872157562', 'Engineering - 2'),
(1366, '2023200148', 'ORDOÑEZ', 'EDRIZA ANGELICA AQUINO', '855830378', 'Accounting - 3'),
(1369, '2024200222', 'ORONCE', 'JOYCE PATRICIA BARTOLOME', '238682691', 'Accounting - 3'),
(1374, '2021200138', 'OSORMAN', 'YCKAH FRANCEZ SALANDANAN', '860200826', 'Engineering - 4'),
(1375, '2022200005', 'PABALAN', 'ELYANNA LOUISSE IBASCO', '197884794', 'Accounting - 1'),
(1383, '2010500173', 'PAHATE', 'NINA ISABELLA GIL', '856740202', 'Computer Science - 3'),
(1385, '2022200529', 'PALARA', 'ALEXIS ANDREE AMORANTO', '959633239', 'Business Administration - 1'),
(1397, '2022200382', 'PARCON', 'ELLA REIGN LORENO', '497915234', 'Nursing - 2'),
(1404, '2015900090', 'PATIGDAS', 'SHANE', '861816186', 'Information Technology - 4'),
(1406, '2020200099', 'PAYUMO', 'MARION ADRIANA ROCCINI', '975636599', 'Nursing - 4'),
(1411, '2023200172', 'PELAGO', 'ROSARIO MARI GARCIA', '223928963', 'Education - 1'),
(1415, '2022200391', 'PEPITO', 'JULLIANNE SANTILLAN', '575216132', 'Education - 3'),
(1419, '2022200334', 'PEREZ', 'KRISHNA ARGONCILLO', '292193027', 'Accounting - 4'),
(1420, '2022200559', 'PHANKWAN', 'DARINEE TRISHIA CRUZ', '290925075', 'Hospitality Management - 4'),
(1425, '2022200566', 'PINLAC', 'FRANCESE THERESE ANDALE', '168299841', 'Business Administration - 2'),
(1430, '2021200097', 'POLICARPIO', 'DOMINIQUE ALTHEA LANDICHO', '986576474', 'Accounting - 4'),
(1431, '2021300004', 'POSAS', 'SELEENA MICHAELA SALAZAR', '241323091', 'Business Administration - 4'),
(1432, '2009502433', 'PRINCIPE', 'MAIE GABRIELLE VILLAROMAN', '737768560', 'Nursing - 4'),
(1437, '2022200318', 'QUA', 'MAI CHESKA YE-SHA BERNABE', '975659495', 'Psychology - 3'),
(1439, '2023200014', 'QUERI', 'ANGELICA NICOLE MEDINA', '810393479', 'Computer Science - 2'),
(1441, '2022200358', 'QUIAMBAO', 'ZARINA FRANCES RUSTIA', '281968915', 'Computer Science - 3'),
(1443, '2021200188', 'QUIJANO', 'MAXINE ISABEL PEREZ', '811615927', 'Hospitality Management - 3'),
(1451, '2021200242', 'RADAZA', 'SHERMILYN FAITH SABANGAN', '959050679', 'Computer Science - 2'),
(1457, '2022200004', 'RAMIRO', 'IVY LORAINE RIBANO', '241346611', 'Hospitality Management - 4'),
(1462, '2021200249', 'RAMOS', 'MAYUMI ISABEL CACHO', '905251542', 'Information Technology - 4'),
(1464, '2022200397', 'RAMOS', 'NISHY SALAZAR', '975526727', 'Nursing - 3'),
(1468, '2009502340', 'RAZA', 'AEZIEN ZERI SADAYA', '155797441', 'Accounting - 3'),
(1469, '2018200229', 'REBUENO', 'KRISTIENNE VICTORIA ENRIQUEZ', '767857077', 'Accounting - 4'),
(1484, '2021200036', 'RIVERA', 'AUBREY BEATRIZ GABAON', '999034138', 'Computer Science - 4'),
(1487, '2023200143', 'RIVERA', 'MIKHAILA KAROLYNE TIU', '108326929', 'Computer Science - 3'),
(1497, '2022200563', 'ROLLOQUE', 'MARIA IVYZA DALA', '497759680', 'Computer Science - 2'),
(1498, '2023200011', 'ROMERO', 'KATREENA DAWN SIASOCO', '858750330', 'Psychology - 2'),
(1504, '2022200345', 'ROQUE', 'JULIANA CHAUNCY BALAGTAS', '285764883', 'Computer Science - 4'),
(1505, '2021200099', 'ROSALES', 'CLARISSA MAE DE GUZMAN', '999474858', 'Engineering - 3'),
(1509, '2023200159', 'ROSLOVTSEV', 'MARIA NATALIA LEE', '230803075', 'Business Administration - 2'),
(1513, '2024200162', 'RUEDA', 'SAMANTHA NICOLE ANDRES', '811294663', 'Psychology - 3'),
(1524, '2022200635', 'SALINAS', 'JULIA VIKTORIA RARELA', '155813057', 'Information Technology - 4'),
(1529, '2021200217', 'SALVADOR', 'JAZMIN FRANCISCO', '300778771', 'Nursing - 3'),
(1530, '2022200342', 'SAMONTE', 'CRYSTAL NICOLE GONZALES', '301928451', 'Business Administration - 3'),
(1536, '2022200299', 'SANCHEZ', 'CLAIRE YVONNE', '959261671', 'Psychology - 1'),
(1539, '2023200185', 'SANGAO', 'MILEVA ALEXANDRIA GARZON', '182729562', 'Psychology - 4'),
(1540, '2023200057', 'SANTA', 'ANA , MARTINA ALEXIE GAN', '228312451', 'Nursing - 1'),
(1542, '2022200516', 'SANTIAGO', 'RIANNA MAE BENITEZ', '165270689', 'Engineering - 3'),
(1544, '2022200310', 'SANTIAGO', 'CHRISTINE JOY MENDOZA', '198036874', 'Business Administration - 1'),
(1545, '2023200100', 'SANTIAGO', 'SOPHIA BIANCA RAMOS', '161345425', 'Hospitality Management - 4'),
(1564, '2021200066', 'SARMIENTO', 'AMANDA ROCIO CARRIEDO', '284326643', 'Psychology - 1'),
(1567, '2008502009', 'SARMIENTO', 'SABYNE MARIA LAMASAN', '577573793', 'Engineering - 2'),
(1574, '2011400062', 'SEGUNDERA', 'SOPHIA MIKAELA SISON', '813685127', 'Hospitality Management - 3'),
(1579, '2023200055', 'SESPEÑE', 'ALGE LYN NALDOZA', '865706874', 'Business Administration - 4'),
(1580, '2009502600', 'SHARMA', 'MEHAK', '182790778', 'Business Administration - 3'),
(1581, '2022200584', 'SIGUAN', 'KRISTINE MARGARETTE GARCHITORENA', '231591811', 'Education - 1'),
(1582, '2022200400', 'SIJERA', 'HANNAH EXUPERY ABID', '197780314', 'Hospitality Management - 3'),
(1584, '2022200411', 'SIKAT', 'CHRISTINE ANN PONCE', '813113063', 'Business Administration - 4'),
(1586, '2021200023', 'SIMEON', 'BRAEDEN GIAN DALE CRUZ', '197614938', 'Information Technology - 3'),
(1593, '2021200041', 'SOLANGON', 'JONNI MAE SUMAYLO', '558205267', 'Psychology - 1'),
(1598, '2022200336', 'SOLLEGUE', 'SENDRICA SIMONE VALDEZ', '287994627', 'Nursing - 3'),
(1604, '2018200259', 'SORIA', 'BIANCA ANGELA ACUÑA', '670929173', 'Psychology - 3'),
(1611, '2022200347', 'SORRIANO', 'EFA MAE GARCIA', '197194026', 'Computer Science - 1'),
(1625, '2022200544', 'SY', 'ALYSSA NICOLE GAVIOLA', '292652035', 'Computer Science - 2'),
(1628, '2023200131', 'TABAGO', 'MARIA ISABELLE PAGTAMA', '154466977', 'Nursing - 3'),
(1630, '2021200009', 'TABUCOL', 'ERIN SAMANTHA VIDAL', '276431651', 'Information Technology - 2'),
(1635, '2023200020', 'TAGUINOD', 'FRANCINE AALIYANAH FLORES', '859745386', 'Education - 1'),
(1636, '2023200037', 'TALABIS', 'LYKA ALECXIS JAVIER', '198978698', 'Hospitality Management - 4'),
(1643, '2022200538', 'TANTE', 'PRINCESS JEBERLYN PICO', '162113953', 'Hospitality Management - 4'),
(1644, '2022200308', 'TANYAG', 'MARGARET OLIVE ESPERANZA', '812995751', 'Hospitality Management - 3'),
(1649, '2021200175', 'TEMPLO', 'PAMELA BEATRICE ROBLES', '987984922', 'Hospitality Management - 3'),
(1650, '2012400113', 'TENDILLA', 'JHUNIZZ YZABHEL RUPA', '858278522', 'Education - 3'),
(1651, '2023200226', 'TENMATAY', 'MONETTE ROSE FERNANDEZ', '223136387', 'Education - 3'),
(1670, '2021200153', 'TORRES', 'MIKHAELA NICOLE', '182108506', 'Engineering - 4'),
(1672, '2024200128', 'TRESPECES', 'MA. ALTHEA YVEZ', '37277626', 'Psychology - 3'),
(1676, '2022200003', 'TUAZON', 'JIZELLE ROSE JOCSON', '197015466', 'Accounting - 3'),
(1679, '2022200375', 'TUMAPAT', 'JULIA ARWEN SOCORIN', '176929809', 'Business Administration - 3'),
(1685, '2023200175', 'UMAYAM', 'ZHARLICE LIM', '226473875', 'Information Technology - 4'),
(1693, '2022200300', 'VALERA', 'DARLA ROSELYN VELASCO', '291655955', 'Hospitality Management - 3'),
(1705, '2023200034', 'VERGARA', 'MIKHAILA DOMINIQUE MARIANO', '104066577', 'Business Administration - 3'),
(1710, '2021200204', 'VERZO', 'ZOE NICOLA MARTINEZ', '151051169', 'Nursing - 4'),
(1722, '2021200183', 'VILLAMOR', 'LAUREN JACQUELINE CAPISTRANO', '576839825', 'Accounting - 1'),
(1723, '2021200018', 'VILLANO', 'PATRICIA SOPHIA TONGSON', '454844897', 'Information Technology - 2'),
(1724, '2022200620', 'VILLANUEVA', 'CAMILLE VICTORIA AQUIAS', '163834001', 'Education - 2'),
(1729, '2021200095', 'VILLANUEVA', 'STEPHANIE AMBER DIZON', '999716298', 'Hospitality Management - 1'),
(1742, '2015900106', 'YADORI', 'AALIYAH MAOWI GERILLA', '101408241', 'Computer Science - 4'),
(1762, '2020200307', 'ZINGALAWA', 'LHY-AR MORALES', '320222054', 'Psychology - 4'),
(1771, '2023200048', 'GONZALES', 'GIANNAH DE VERA', '231017107', 'Education - 1');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
CREATE TABLE IF NOT EXISTS `students` (
  `block_id` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `course` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `year_level` int DEFAULT NULL,
  `num_students` int DEFAULT NULL,
  `section_name` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`block_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`block_id`, `course`, `year_level`, `num_students`, `section_name`) VALUES
('B001', 'Computer Science', 1, 10, 'Computer Science - 1'),
('B002', 'Computer Science', 2, 10, 'Computer Science - 2'),
('B003', 'Computer Science', 3, 10, 'Computer Science - 3'),
('B004', 'Computer Science', 4, 10, 'Computer Science - 4'),
('B005', 'Information Technology', 1, 10, 'Information Technology - 1'),
('B006', 'Information Technology', 2, 10, 'Information Technology - 2'),
('B007', 'Information Technology', 3, 10, 'Information Technology - 3'),
('B008', 'Information Technology', 4, 10, 'Information Technology - 4'),
('B009', 'Nursing', 1, 12, 'Nursing - 1'),
('B010', 'Nursing', 2, 12, 'Nursing - 2'),
('B011', 'Nursing', 3, 12, 'Nursing - 3'),
('B012', 'Nursing', 4, 12, 'Nursing - 4'),
('B013', 'Hospitality Management', 1, 15, 'Hospitality Management - 1'),
('B014', 'Hospitality Management', 2, 15, 'Hospitality Management - 2'),
('B015', 'Hospitality Management', 3, 15, 'Hospitality Management - 3'),
('B016', 'Hospitality Management', 4, 15, 'Hospitality Management - 4'),
('B017', 'Business Administration', 1, 20, 'Business Administration - 1'),
('B018', 'Business Administration', 2, 20, 'Business Administration - 2'),
('B019', 'Business Administration', 3, 20, 'Business Administration - 3'),
('B020', 'Business Administration', 4, 20, 'Business Administration - 4'),
('B021', 'Accounting', 1, 18, 'Accounting - 1'),
('B022', 'Accounting', 2, 18, 'Accounting - 2'),
('B023', 'Accounting', 3, 18, 'Accounting - 3'),
('B024', 'Accounting', 4, 18, 'Accounting - 4'),
('B025', 'Psychology', 1, 22, 'Psychology - 1'),
('B026', 'Psychology', 2, 22, 'Psychology - 2'),
('B027', 'Psychology', 3, 22, 'Psychology - 3'),
('B028', 'Psychology', 4, 22, 'Psychology - 4'),
('B029', 'Engineering', 1, 25, 'Engineering - 1'),
('B030', 'Engineering', 2, 25, 'Engineering - 2'),
('B031', 'Engineering', 3, 25, 'Engineering - 3'),
('B032', 'Engineering', 4, 25, 'Engineering - 4'),
('B033', 'Education', 1, 20, 'Education - 1'),
('B034', 'Education', 2, 20, 'Education - 2'),
('B035', 'Education', 3, 20, 'Education - 3'),
('B036', 'Education', 4, 20, 'Education - 4');

-- --------------------------------------------------------

--
-- Table structure for table `subjects`
--

DROP TABLE IF EXISTS `subjects`;
CREATE TABLE IF NOT EXISTS `subjects` (
  `subject_code` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  `subject_name` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `year_level` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `program` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `lecture_hours` int DEFAULT NULL,
  PRIMARY KEY (`subject_code`)
) ENGINE=MyISAM AUTO_INCREMENT=333 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `subjects`
--

INSERT INTO `subjects` (`subject_code`, `subject_name`, `year_level`, `program`, `lecture_hours`) VALUES
('GENED01', 'English Communication', '1', 'General', 3),
('GENED02', 'Mathematics in the Modern World', '1', 'General', 3),
('GENED03', 'Science, Technology, and Society', '1', 'General', 3),
('GENED04', 'Philippine History', '1', 'General', 3),
('GENED05', 'Ethics', '2', 'General', 3),
('GENED06', 'Rizal’s Life and Works', '2', 'General', 3),
('GENED07', 'Environmental Science', '2', 'General', 3),
('CS101', 'Introduction to Programming', '1', 'Computer Science', 3),
('CS102', 'Data Structures and Algorithms', '2', 'Computer Science', 3),
('CS103', 'Operating Systems', '3', 'Computer Science', 3),
('CS104', 'Software Engineering', '4', 'Computer Science', 3),
('IT101', 'Computer Networks', '2', 'Information Technology', 3),
('IT102', 'Database Systems', '3', 'Information Technology', 3),
('IT103', 'Cybersecurity Fundamentals', '4', 'Information Technology', 3),
('BSN101', 'Fundamentals of Nursing', '1', 'Nursing', 3),
('BSN102', 'Anatomy and Physiology', '1', 'Nursing', 3),
('BSN201', 'Pharmacology', '2', 'Nursing', 3),
('BSN202', 'Medical-Surgical Nursing', '2', 'Nursing', 3),
('BSN301', 'Maternal and Child Nursing', '3', 'Nursing', 3),
('BSN401', 'Community Health Nursing', '4', 'Nursing', 3),
('HM101', 'Introduction to Hospitality Industry', '1', 'Hospitality Management', 3),
('HM102', 'Food and Beverage Management', '2', 'Hospitality Management', 3),
('HM201', 'Housekeeping Operations', '2', 'Hospitality Management', 3),
('HM301', 'Front Office Management', '3', 'Hospitality Management', 3),
('HM401', 'Tourism Planning and Development', '4', 'Hospitality Management', 3),
('BA101', 'Principles of Management', '1', 'Business Administration', 3),
('BA102', 'Financial Accounting', '2', 'Business Administration', 3),
('BA201', 'Marketing Management', '3', 'Business Administration', 3),
('BA301', 'Business Law and Taxation', '4', 'Business Administration', 3),
('BSA101', 'Basic Accounting', '1', 'Accounting', 3),
('BSA102', 'Financial Accounting and Reporting', '2', 'Accounting', 3),
('BSA201', 'Auditing Theory', '3', 'Accounting', 3),
('BSA301', 'Managerial Accounting', '4', 'Accounting', 3),
('PSY101', 'General Psychology', '1', 'Psychology', 3),
('PSY102', 'Developmental Psychology', '2', 'Psychology', 3),
('PSY201', 'Abnormal Psychology', '3', 'Psychology', 3),
('PSY301', 'Industrial-Organizational Psychology', '4', 'Psychology', 3),
('ENG101', 'Engineering Drawing', '1', 'Engineering', 3),
('ENG102', 'Engineering Mathematics', '2', 'Engineering', 3),
('ENG201', 'Structural Analysis', '3', 'Engineering', 3),
('ENG301', 'Hydraulics and Fluid Mechanics', '4', 'Engineering', 3),
('ED101', 'Foundations of Education', '1', 'Education', 3),
('ED102', 'Educational Psychology', '2', 'Education', 3),
('ED201', 'Curriculum Development', '3', 'Education', 3),
('ED301', 'Teaching Internship', '4', 'Education', 3);

-- --------------------------------------------------------

--
-- Table structure for table `teachers`
--

DROP TABLE IF EXISTS `teachers`;
CREATE TABLE IF NOT EXISTS `teachers` (
  `id_num` int NOT NULL AUTO_INCREMENT,
  `teacher_id` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  `teacher_name` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `subject_code` varchar(10) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `type` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id_num`)
) ENGINE=MyISAM AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `teachers`
--

INSERT INTO `teachers` (`id_num`, `teacher_id`, `teacher_name`, `subject_code`, `type`) VALUES
(1, 'T001', 'John Doe', 'CS101', 'Full-Time'),
(2, 'T001', 'John Doe', 'CS102', 'Full-Time'),
(3, 'T002', 'Jane Smith', 'CS103', 'Full-Time'),
(4, 'T003', 'Robert Johnson', 'CS104', 'Full-Time'),
(5, 'T004', 'Emily Davis', 'IT101', 'Full-Time'),
(6, 'T005', 'Michael Brown', 'IT102', 'Part-Time'),
(7, 'T005', 'Michael Brown', 'IT103', 'Part-Time'),
(8, 'T006', 'Sarah Wilson', 'BSN101', 'Full-Time'),
(9, 'T006', 'Sarah Wilson', 'BSN102', 'Full-Time'),
(10, 'T007', 'James Martinez', 'BSN201', 'Full-Time'),
(11, 'T008', 'Patricia Anderson', 'BSN202', 'Full-Time'),
(12, 'T009', 'David Thomas', 'BSN301', 'Part-Time'),
(13, 'T010', 'Barbara White', 'BSN401', 'Full-Time'),
(14, 'T011', 'Charles Harris', 'HM101', 'Full-Time'),
(15, 'T012', 'Susan Clark', 'HM102', 'Full-Time'),
(16, 'T013', 'Christopher Lewis', 'HM201', 'Full-Time'),
(17, 'T014', 'Jessica Walker', 'HM301', 'Full-Time'),
(18, 'T015', 'Matthew Hall', 'HM401', 'Part-Time'),
(19, 'T016', 'Daniel Allen', 'BA101', 'Full-Time'),
(20, 'T017', 'Jennifer Young', 'BA102', 'Full-Time'),
(21, 'T018', 'Joseph Hernandez', 'BA201', 'Full-Time'),
(22, 'T019', 'Lisa King', 'BA301', 'Part-Time'),
(23, 'T020', 'Anthony Scott', 'BSA101', 'Full-Time'),
(24, 'T021', 'Karen Wright', 'BSA102', 'Full-Time'),
(25, 'T022', 'Kevin Lopez', 'BSA201', 'Full-Time'),
(26, 'T023', 'Nancy Green', 'BSA301', 'Part-Time'),
(27, 'T024', 'Brian Adams', 'PSY101', 'Full-Time'),
(28, 'T025', 'Michelle Nelson', 'PSY102', 'Full-Time'),
(29, 'T026', 'Thomas Baker', 'PSY201', 'Full-Time'),
(30, 'T027', 'Donna Carter', 'PSY301', 'Part-Time'),
(31, 'T028', 'George Mitchell', 'ENG101', 'Full-Time'),
(32, 'T029', 'Dorothy Perez', 'ENG102', 'Full-Time'),
(33, 'T030', 'Kenneth Roberts', 'ENG201', 'Full-Time'),
(34, 'T031', 'Betty Campbell', 'ENG301', 'Part-Time'),
(35, 'T032', 'Mark Gonzalez', 'ED101', 'Full-Time'),
(36, 'T033', 'Sandra Rodriguez', 'ED102', 'Full-Time'),
(37, 'T034', 'Paul Martinez', 'ED201', 'Full-Time'),
(38, 'T035', 'Linda Hernandez', 'ED301', 'Part-Time'),
(39, 'T036', 'Steven Moore', 'GENED01', 'Full-Time'),
(40, 'T036', 'Steven Moore', 'GENED02', 'Full-Time'),
(41, 'T037', 'Barbara Taylor', 'GENED03', 'Full-Time'),
(42, 'T038', 'Richard Wilson', 'GENED04', 'Full-Time'),
(43, 'T039', 'Elizabeth Anderson', 'GENED05', 'Part-Time'),
(44, 'T040', 'Charles Thomas', 'GENED06', 'Full-Time'),
(45, 'T041', 'Mary Jackson', 'GENED07', 'Full-Time');

-- --------------------------------------------------------

--
-- Table structure for table `time_slots`
--

DROP TABLE IF EXISTS `time_slots`;
CREATE TABLE IF NOT EXISTS `time_slots` (
  `time_slot_id` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  `day` varchar(10) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `start_time` time DEFAULT NULL,
  `end_time` time DEFAULT NULL,
  PRIMARY KEY (`time_slot_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `time_slots`
--

INSERT INTO `time_slots` (`time_slot_id`, `day`, `start_time`, `end_time`) VALUES
('', 'Monday', '08:00:00', '09:00:00'),
('1', 'Monday', '08:00:00', '09:00:00'),
('2', 'Monday', '09:00:00', '10:00:00'),
('3', 'Monday', '10:00:00', '11:00:00'),
('4', 'Monday', '11:00:00', '12:00:00'),
('5', 'Monday', '13:00:00', '14:00:00'),
('6', 'Monday', '14:00:00', '15:00:00'),
('7', 'Monday', '15:00:00', '16:00:00'),
('8', 'Monday', '16:00:00', '17:00:00'),
('9', 'Tuesday', '08:00:00', '09:00:00'),
('10', 'Tuesday', '09:00:00', '10:00:00'),
('11', 'Tuesday', '10:00:00', '11:00:00'),
('12', 'Tuesday', '11:00:00', '12:00:00'),
('13', 'Tuesday', '13:00:00', '14:00:00'),
('14', 'Tuesday', '14:00:00', '15:00:00'),
('15', 'Tuesday', '15:00:00', '16:00:00'),
('16', 'Tuesday', '16:00:00', '17:00:00'),
('17', 'Wednesday', '08:00:00', '09:00:00'),
('18', 'Wednesday', '09:00:00', '10:00:00'),
('19', 'Wednesday', '10:00:00', '11:00:00'),
('20', 'Wednesday', '11:00:00', '12:00:00'),
('21', 'Wednesday', '13:00:00', '14:00:00'),
('22', 'Wednesday', '14:00:00', '15:00:00'),
('23', 'Wednesday', '15:00:00', '16:00:00'),
('24', 'Wednesday', '16:00:00', '17:00:00'),
('25', 'Thursday', '08:00:00', '09:00:00'),
('26', 'Thursday', '09:00:00', '10:00:00'),
('27', 'Thursday', '10:00:00', '11:00:00'),
('28', 'Thursday', '11:00:00', '12:00:00'),
('29', 'Thursday', '13:00:00', '14:00:00'),
('30', 'Thursday', '14:00:00', '15:00:00'),
('31', 'Thursday', '15:00:00', '16:00:00'),
('32', 'Thursday', '16:00:00', '17:00:00'),
('33', 'Friday', '08:00:00', '09:00:00'),
('34', 'Friday', '09:00:00', '10:00:00'),
('35', 'Friday', '10:00:00', '11:00:00'),
('36', 'Friday', '11:00:00', '12:00:00'),
('37', 'Friday', '13:00:00', '14:00:00'),
('38', 'Friday', '14:00:00', '15:00:00'),
('39', 'Friday', '15:00:00', '16:00:00'),
('40', 'Friday', '16:00:00', '17:00:00'),
('41', 'Saturday', '08:00:00', '09:00:00'),
('42', 'Saturday', '09:00:00', '10:00:00'),
('43', 'Saturday', '10:00:00', '11:00:00'),
('44', 'Saturday', '11:00:00', '12:00:00'),
('45', 'Saturday', '13:00:00', '14:00:00'),
('46', 'Saturday', '14:00:00', '15:00:00'),
('47', 'Saturday', '15:00:00', '16:00:00'),
('48', 'Saturday', '16:00:00', '17:00:00');

-- --------------------------------------------------------

--
-- Stand-in structure for view `weekly_schedule`
-- (See below for the actual view)
--
DROP VIEW IF EXISTS `weekly_schedule`;
CREATE TABLE IF NOT EXISTS `weekly_schedule` (
`subject_code` varchar(10)
,`program` varchar(255)
,`year_level` varchar(50)
,`teacher_name` varchar(100)
,`room_name` varchar(50)
,`day` varchar(10)
,`start_time` time
,`end_time` time
);

-- --------------------------------------------------------

--
-- Structure for view `weekly_schedule`
--
DROP TABLE IF EXISTS `weekly_schedule`;

DROP VIEW IF EXISTS `weekly_schedule`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `weekly_schedule`  AS SELECT `s`.`subject_code` AS `subject_code`, `sub`.`program` AS `program`, `sub`.`year_level` AS `year_level`, `s`.`teacher_name` AS `teacher_name`, `s`.`room_name` AS `room_name`, `s`.`day` AS `day`, `s`.`start_time` AS `start_time`, `s`.`end_time` AS `end_time` FROM (`schedule` `s` join `subjects` `sub` on((`s`.`subject_code` = `sub`.`subject_code`))) ORDER BY `sub`.`program` ASC, `s`.`day` ASC, `s`.`start_time` ASC ;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
