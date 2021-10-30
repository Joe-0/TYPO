drop table if exists challengeText;
create table challengeText (
  id integer primary key autoincrement,
  title text not null,
  'text' text not null
);

drop table if exists users;
create table users (
    id integer primary key autoincrement,
    username text not null unique,
    password text not null unique 
);

drop table if exists attempts;
create table attempts (
    id integer primary key autoincrement,
    user text not null references users(username),
    wpm integer not null,
    accuracy integer not null
);