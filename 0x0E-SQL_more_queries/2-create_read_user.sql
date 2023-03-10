-- create database and user
-- user should have select
-- if user exists it should not fail
-- if database exists, it should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT 0N hbtn_0d_2.* T0 user_0d_2@localhost;
