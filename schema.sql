drop table if exists songs;
create table songs (
  id integer primary key autoincrement,
  title text not null,
  link text not null,
  votes integer
);
