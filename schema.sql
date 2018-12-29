drop table if exists transition_data;
  create table transition_data (
    id integer primary key autoincrement,
    a_song text not null,
    b_song text not null,
    info text not null
  );
