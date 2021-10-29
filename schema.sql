drop table if exists challengeText;
create table challengeText (
  id integer primary key autoincrement,
  title text not null,
  'text' text not null
);

create table users (
    id primary key autoincrement,
    username text not null,
    password text not null
);