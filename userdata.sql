create database userInfo;
use userInfo;
create table data(id int auto_increment primary key not null,
	first_name varchar(50) not null, last_name varchar(50), 
    email varchar(50) not null, contact int(10),
    country varchar(10), course varchar(20), 
    password varchar(50));
drop table data;


