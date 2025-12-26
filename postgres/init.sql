create table tournaments(
    id serial primary key,
    ema_id int unique not null,
    name text not null,
    place text,
    country text,
    date date not null,
    players int,
    weight numeric(2,1),
    days int
);

create table players(
    id serial primary key,
    ema_number text unique,
    first_name text,
    last_name text,
    country text,
    mers_ranking numeric(6,2),
    rukrs_ranking numeric(6,2)
);

create table tournament_results(
    tournament_id int not null,
    player_id int not null,
    base_rank int,
    primary key (tournament_id, player_id),
    foreign key (tournament_id) references tournaments(id) on delete cascade,
    foreign key (player_id) references players(id) on delete cascade
)

create table player_ranking(
    player_id int not null,
    ranking_date date,
    ranking numeric(6,2),
    primary key (player_id, ranking_date),
    foreign key (player_id) references players(id) on delete cascade
)