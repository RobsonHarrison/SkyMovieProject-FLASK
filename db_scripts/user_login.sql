USE skymovie_christmas;

#CREATE DATASBASE user_login;

#use user_login;

CREATE TABLE users(
user_id int unique not null auto_increment,
user_name VARCHAR(30) unique not null,
_password VARCHAR(30) not null,
email_address VARCHAR(50) not null unique,
first_name VARCHAR (30),
last_name VARCHAR(30),
address1 VARCHAR(30),
address2 VARCHAR(30),
address3 VARCHAR(30),
postcode VARCHAR(8),
primary key(user_id));

insert into users(user_name, _password, email_address, first_name, last_name) Values("LukeSky", "wordpass", "Red5@hotmail.co.uk", "Luke", "Skywalker");