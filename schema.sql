drop table if exists challengeText;
drop table if exists users;
create table challengeText (
  id integer primary key autoincrement,
  title text not null,
  'text' text not null
);


create table users (
    id integer primary key autoincrement,
    username text not null unique,
    password text not null unique 
);