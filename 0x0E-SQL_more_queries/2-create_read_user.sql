-- create database and user
-- user should have select
-- if user exists it should not fail
-- if database exists, it should not fail
CREATE IF NOT EXISTS database hbtn_0d_2;
CREATE USER user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
