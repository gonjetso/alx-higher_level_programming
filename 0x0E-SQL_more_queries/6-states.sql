-- Create database hbtn_0d_usa
-- Create table states in the DB hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT NOT NULL UNIQUE PRIMARY KEY, name VARCHAR(256) NOT NULL);
