-- create database and table
CREATE database IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_od_usa.cities(
	id INT NOT NULL AUTO-INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256),
	PRIMARY KEY(id),
	FOREIGN KEY(state_id) REFERENCES states(id)
);
