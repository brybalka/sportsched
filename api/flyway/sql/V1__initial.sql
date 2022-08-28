create table ufc_event(
  id serial primary key,
  name varchar,
  date DATE not null,
  status varchar
);

create table ufc_fight(
  id serial primary key,  
  fighter_1 varchar,
  fighter_2 varchar,
  ufc_event integer references ufc_event(id),
  status varchar
);