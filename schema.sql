drop table if exists challengeText;
create table challengeText (
  id integer primary key autoincrement,
  title text not null,
  'text' text not null
);