drop table if exists challengeText;
create table challengeText (
  id integer primary key autoincrement,
  title text not null,
  'text' text not null
);


CREATE TABLE IF NOT EXISTS users (
    id integer primary key autoincrement,
    username text not null unique,
    password text not null unique,
    isAdmin boolean
);

CREATE TABLE IF NOT EXISTS attempts (
    id integer primary key autoincrement,
    user text not null references users(username),
    wpm integer not null,
    accuracy integer not null
);


