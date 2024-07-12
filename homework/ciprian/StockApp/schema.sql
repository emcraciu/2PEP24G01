drop table if exists users;
create table users (
id integer primary key autoincrement,
username text not null,
password text not null,
email text not null,
name text not null
);

drop table if exists cookies;
create table cookies (
id integer primary key autoincrement,
username text not null,
expiry_days integer not null,
sgnkey text not null,
name text not null
);