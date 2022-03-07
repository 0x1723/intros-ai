-- Drop the database if it exists, this will error out if it doesn't but it's not harmful as it doesn't stop the script execution
DROP DATABASE `intros-ai`;

-- This was generated using MySQLWorkbench
CREATE DATABASE `intros-ai` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

-- Use the database and then create the only table needed for the project
USE `intros-ai`;
CREATE TABLE tasks (
	id INT AUTO_INCREMENT PRIMARY KEY,
    description TINYTEXT,
    completed BOOLEAN DEFAULT false
);