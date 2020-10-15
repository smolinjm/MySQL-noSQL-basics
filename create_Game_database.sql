
-- source create_Game_database.sql

select 'Create memory db' as '';

drop database if exists memory;

create database memory;

show databases;

use memory;

drop table if exists humans;
drop table if exists Lobby;
drop table if exists Game_Server;
drop table if exists enter_lobby;
drop table if exists join_instance;

create table humans (
	h_id int NOT NULL,
	name varchar(40) NOT NULL,
	email varchar(60) NOT NULL,
	ssn varchar(11),
	birthdate date,
	address varchar(120),
	city varchar(80),
	state varchar(30),
	zipcode varchar(10),
	ipv4 varchar(30),
	card_info varchar(120),
	Primary Key (h_id)
) ;

create table Lobby (
	l_id int NOT NULL,
	size_cap int,
	name varchar(40) NOT NULL,
	Primary Key (l_id)
) ;

create table Game_Server (
	g_id int NOT NULL,
	type int NOT NULL,
	name varchar(60) NOT NULL,
	Primary Key (g_id)
) ;


create table enter_lobby (
	u_id int NOT NULL,
	l_id int NOT NULL,
	Primary Key (u_id,l_id),
	Foreign Key (u_id) references User(u_id),
	Foreign Key (l_id) references Lobby(l_id)
) ;

create table join_instance (
	u_id int NOT NULL,
	g_id int NOT NULL,
	Primary Key (u_id,g_id),
	Foreign Key (u_id) references User(u_id),
	Foreign Key (g_id) references Game_Server(g_id)
) ;



describe humans ;
describe Lobby ;
describe Game_Server ;
describe enter_lobby ;
describe join_instance ;


-- insert into enter_lobby values (55555,301) ;  Foriegn Key ERROR.

-- insert into User values (1000001,"Michael",'smolinski@gmail.com',42,'8556 E Amherst Cir','Denver','CO') ;
-- insert into User values (1000000, Bethany Mccarthy, bethany.mccarthy@hotmail.com, 389-36-4538, 1972-11-04, 3241 Taylor Mountain Apt. 195, Hensleyview, LA, 31931, 192.168.152.45, 30095212734507__10/27__434) ;
 /*
	ipv4 int unsigned,
	card_info varchar(120),
insert into User values (
	1000000,
	Bethany Mccarthy, 
	bethany.mccarthy@hotmail.com, 
	389-36-4538, 
	1972-11-04, 
	3241 Taylor Mountain Apt. 195, 
	Hensleyview, 
	LA, 
	31931, 
	192.168.152.45, 
	30095212734507__10/27__434) ;
*/
-- insert into User values (1000002,"Jeff",'mail@jeffsmolinski.com',42,'8080 Ashgrove Dr','Cincinnati','OH') ;

-- C:/Users/smoli/Dropbox/_ME/school/University of Denver/Course 3421/Homework4/

load data local infile
'game_data.txt'
  into table humans
  fields terminated by ','
  lines terminated by '\n' ;


insert into Lobby values (101,20,'Lobby Deathmatch') ;
insert into Lobby values (201,4,'Lobby 2 vs 2') ;
insert into Lobby values (202,8,'Lobby 4 vs 4') ;
insert into Lobby values (502,16,'Lobby Capture the Flag') ;
insert into Lobby values (301,12,'Lobby Quickplay') ;
insert into Lobby values (401,12,'Lobby Competitive Match') ;
insert into Lobby values (601,3,'Lobby Co-op Campaign') ;

insert into Game_Server values (1001,10,'Deathmatch') ;
insert into Game_Server values (2001,20,'2 vs 2') ;
insert into Game_Server values (2002,30,'4 vs 4') ;
insert into Game_Server values (5002,40,'Capture the Flag') ;
insert into Game_Server values (3001,50,'Quickplay') ;
insert into Game_Server values (4001,60,'Competitive Match') ;
insert into Game_Server values (6001,70,'Co-op Campaign') ;

insert into enter_lobby values (1000001,601) ;

insert into join_instance values (1000002,6001) ;


select * from humans LIMIT 10;
select * from Lobby ;
select * from Game_Server ;
select * from enter_lobby ;
select * from join_instance ;


