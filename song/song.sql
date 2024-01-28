use test;

# user
create table tbl_geo(
    id bigint auto_increment primary key,
    lat double,
    lng double
);

create table tbl_address(
    id bigint auto_increment primary key,
    street varchar(255),
    city varchar(255),
    zipcode varchar(255),
    geo_id bigint,
    constraint fk_address_geo foreign key(geo_id)
                        references tbl_geo(id)
);

alter table tbl_address add suite varchar(255);

create table tbl_company(
    id bigint auto_increment primary key,
    name varchar(255),
    catch_phrase varchar(255),
    bs varchar(255)
);

create table tbl_user(
    id bigint auto_increment primary key,
    name varchar(255),
    username varchar(255),
    email varchar(255),
    address_id bigint,
    phone varchar(255),
    website varchar(255),
    company_id bigint,
    constraint fk_user_address foreign key(address_id)
                     references tbl_address(id),
    constraint fk_user_company foreign key(company_id)
                     references tbl_company(id)
);


# todos
create table tbl_todo(
    id bigint auto_increment primary key,
    user_id bigint,
    title varchar(255),
    completed tinyint,
    constraint fk_todos_user foreign key(user_id)
                      references tbl_user(id)
);

# albums
create table tbl_album(
    user_id bigint,
    id bigint auto_increment primary key,
    title varchar(255),
    constraint fk_albums_user foreign key(user_id)
                       references tbl_user(id)
);

# photos
    create table tbl_photo(
        album_id bigint,
        id bigint auto_increment primary key,
        title varchar(255),
        url varchar(255),
        thumbnail_url varchar(255),
        constraint fk_photos_albums foreign key(album_id)
                           references tbl_album(id)
    );

# posts
create table tbl_post(
    user_id bigint,
    id bigint auto_increment primary key,
    title varchar(255),
    body varchar(255),
    constraint fk_posts_user foreign key(user_id)
                      references tbl_user(id)
);

# comments
create table tbl_comment(
    post_id bigint,
    id bigint auto_increment primary key,
    name varchar(255),
    email varchar(255),
    body varchar(255),
    constraint fk_comments_posts foreign key(post_id)
                         references tbl_post(id)
);


# 1번
insert into tbl_geo(lat,lng)
values (-37.3159, 81.1496);

insert into tbl_address(street,suite,city,zipcode,geo_id)
values ('Kulas Light','Apt. 556','Gwenborough','92998-3874',1);

insert into tbl_company(name,catch_phrase,bs)
values ('Romaguera-Crona','Multi-layered client-server neural-net','harness real-time e-markets');


# 2번
insert into tbl_geo(lat, lng)
values(-43.9509, -34.4618);

insert into tbl_address(street, suite, city, zipcode, geo_id)
values('Victor Plains', 'Suite 879', 'Wisokyburgh', '90566-7771', 2);

insert into tbl_company(name, catch_phrase, bs)
values('Deckow-Crist', 'Proactive didactic contingency', 'synergize scalable supply-chains');


# 3번
insert into tbl_geo (lat, lng)
values (-68.6102, -47.0653);

insert into tbl_company (name, catch_phrase, bs)
values ('Romaguera-Jacobson', 'Face to face bifurcated interface', 'e-enable strategic applications');

insert into tbl_address (street, suite, city, zipcode, geo_id)
values ('Douglas Extension', 'Suite 847', 'McKenziehaven', '59590-4157', 3);


# user 4번
insert into tbl_geo(lat, lng)
values (29.4572, -164.2990);

insert into tbl_address(street, suite, city, zipcode, geo_id)
values('Hoeger Mall', 'Apt. 692', 'South Elvis', '53919-4257', 4);

insert into tbl_company(name, catch_phrase, bs)
values('Robel-Corkery', 'Multi-tiered zero tolerance productivity', 'transition cutting-edge web services');


# user 5번
insert into tbl_geo (lat, lng)
values (-31.8129, 62.5342);

insert into tbl_address (street, suite, city, zipcode, geo_id)
values ('Skiles Walks', 'Suite 351', 'Roscoeview', '33263', 5);

insert into tbl_company (name, catch_phrase, bs)
values ('Keebler LLC', 'User-centric fault-tolerant solution', 'revolutionize end-to-end systems');