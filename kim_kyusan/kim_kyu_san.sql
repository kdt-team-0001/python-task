


create table tbl_geo (
    id bigint auto_increment primary key ,
    lat double,
    lng double
);

create table tbl_address(
    id bigint auto_increment primary key,
    street varchar(255),
    suite varchar(255),
    city varchar(255),
    zipcode varchar(255),
    geo_id bigint,
    constraint fk_address_geo_id foreign key (geo_id) references tbl_geo(id)
);

create table tbl_company (
    id bigint auto_increment primary key,
    name varchar(255),
    catch_phrase varchar(255),
    bs varchar(255)
);
create table tbl_user(
    id bigint primary key auto_increment,
    name varchar(255) not null,
    username varchar(255),
    email varchar(255) not null,
    phone varchar(255),
    website varchar(255),
    address_id bigint,
    company_id bigint,
    constraint fk_user_address foreign key (address_id) references tbl_address(id),
    constraint fk_user_company foreign key (company_id) references tbl_company(id)
);


create table tbl_todo (
    user_id bigint,
    id bigint auto_increment primary key ,
    title varchar(255),
    completed tinyint,
    constraint fk_todo_user foreign key (user_id) references tbl_user(id)
);

create table tbl_album (
    user_id bigint,
    id bigint auto_increment primary key ,
    title varchar(255),
    constraint fk_album_user foreign key (user_id) references tbl_user(id)
);

create table tbl_photo (
    album_id bigint,
    id bigint auto_increment primary key,
    title varchar(255),
    url varchar(255),
    thumbnail_url varchar(255),
    constraint fk_photo_album foreign key (album_id) references tbl_album(id)
);

create table tbl_post (
    user_id bigint,
    id bigint auto_increment primary key ,
    title varchar(255),
    body varchar(255),
    constraint fk_post_user foreign key (user_id) references tbl_user(id)
);

create table tbl_comment (
    post_id bigint,
    id bigint auto_increment primary key ,
    name varchar(255),
    email varchar(255),
    body varchar(255),
    constraint fk_comment_post foreign key (post_id) references tbl_post(id)
);



# user의 필요한 기본 데이터는 insert 항목으로 작성 (geo, company, address)

# insert into tbl_geo (lat, lng) values (-68.6102, -47.0653);
# insert into tbl_company (name, catch_phrase, bs) values ('Romaguera-Jacobson', 'Face to face bifurcated interface', 'e-enable strategic applications');
# insert into tbl_address (street, suite, city, zipcode, geo_id) values ('Douglas Extension', 'Suite 847', 'McKenziehaven', '59590-4157', 1);
#

# insert into tbl_geo(lat, lng) values(-43.9509, -34.4618);
# insert into tbl_address(street, suite, city, zipcode, geo_id) values('Victor Plains', 'Suite 879', 'Wisokyburgh', '90566-7771', 2);
# insert into tbl_company(name, catchPhrase , bs) values('Deckow-Crist', 'Proactive didactic contingency', 'synergize scalable supply-chains');
#
# insert into tbl_geo(lat,lng) values (-37.3159,81.1496);
# insert into tbl_address(street,suite,city,zipcode,geo_id) values ('Kulas Light','Apt. 556','Gwenborough','92998-3874',3);
# insert into tbl_company(name,catchPhrase,bs) values ('Romaguera-Crona','Multi-layered client-server neural-net','harness real-time e-markets');
#
# insert into tbl_geo(lat, lng) values(29.4572, -164.2990);
# insert into tbl_address(street, suite, city, zipcode, geo_id) values('Hoeger Mall', 'Apt. 692', 'South Elvis', '53919-4257', 4);
# insert into tbl_company(name, catchPhrase, bs) values('Robel-Corkery', 'Multi-tiered zero tolerance productivity', 'transition cutting-edge web services');
#
# insert into tbl_geo(lat, lng)
# values(-43.9509, -34.4618);
# insert into tbl_address(street, suite, city, zipcode, geo_id)
# values('Victor Plains', 'Suite 879', 'Wisokyburgh', '90566-7771', 5);
# insert into tbl_company(name, catchPhrase, bs)
# values('Deckow-Crist', 'Proactive didactic contingency', 'synergize scalable supply-chains');


select a.id,g.lat, g.lng from tbl_geo g join tbl_address a
on a.geo_id = g.id;

select c.id , c.name, c.catch_phrase, c.bs From tbl_company c;

select uc.name, uc.username, uc.email, uc.phone, uc.website, uc.c_name,uc.catch_phrase, uc.bs,
ag.street, ag.suite, ag.city, ag.zipcode, ag.lng, ag.lat
from
(select u.id, u.name, u.username, u.email, u.phone,u.website,u.address_id, c.name as c_name, c.catch_phrase, c.bs
from tbl_user u join tbl_company c
on u.company_id = c.id) uc join
(select a.id,g.lat, g.lng, a.street, a.suite, a.city, a.zipcode from tbl_geo g join tbl_address a
on a.geo_id = g.id) ag
on uc.address_id = ag.id
;

select *from tbl_todo;

select *from tbl_post;

select a.title as "album_title", p.title, p.url, p.thumbnail_url  from tbl_photo p join tbl_album a on p.album_id = a.id and p.id =1
