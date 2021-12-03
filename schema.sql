drop table if exists challengeText;
create table challengeText (
  id integer primary key autoincrement,
  title text not null,
  'text' text not null
);

drop table if exists users;
CREATE TABLE IF NOT EXISTS users (
    id integer primary key autoincrement,
    username text not null unique,
    password text not null ,
    highscore integer DEFAULT 0,
    isAdmin boolean DEFAULT 0
);

drop table if exists attempts;
CREATE TABLE IF NOT EXISTS attempts (
    id integer primary key autoincrement,
    user text not null references users(username),
    wpm integer not null,
    accuracy integer not null,
    acc_wpm interger not null,
    date text not null
);


