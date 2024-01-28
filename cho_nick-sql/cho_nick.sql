use test;


create table tbl_address(
    id bigint auto_increment primary key ,
    street varchar(255) not null ,
    suite varchar(255) not null ,
    city varchar(255) not null ,
    zipcode varchar(255) not null,
    geo_id bigint not null ,
    constraint fk_address_geo foreign key(geo_id)
    references tbl_geo(id)
);
create table tbl_geo(
    id bigint auto_increment primary key ,
    lat double not null,
    lng double not null
);


create table tbl_company(
    id bigint auto_increment primary key,
    name varchar(255) not null ,
    catch_phrase varchar(255) not null ,
    bs varchar(255) not null
);

create table tbl_user(
    id bigint auto_increment primary key,
    username varchar(255) not null ,
    name varchar(255) not null ,
    email varchar(255) not null ,
    address_id bigint not null ,
    phone varchar(255) not null ,
    website varchar(255) not null ,
    company_id bigint not null ,
    constraint fk_user_address foreign key(address_id)
    references tbl_address(id),
    constraint fk_user_company foreign key(company_id)
    references tbl_company(id)
);






insert into tbl_geo(lat,lng)
values (-37.3159,81.1496);

insert into tbl_address(street,suite,city,zipcode,geo_id)
values ('Kulas Light','Apt. 556','Gwenborough','92998-3874',1);

insert into tbl_company(name,catch_phrase,bs)
values ('Romaguera-Crona','Multi-layered client-server neural-net','harness real-time e-markets');

insert into tbl_geo(lat, lng)
values(-43.9509, -34.4618);
insert into tbl_address(street, suite, city, zipcode, geo_id)
values('Victor Plains', 'Suite 879', 'Wisokyburgh', '90566-7771', 2);
insert into tbl_company(name, catch_phrase, bs)
values('Deckow-Crist', 'Proactive didactic contingency', 'synergize scalable supply-chains');

insert into tbl_geo (lat, lng) values (-68.6102, -47.0653);
insert into tbl_company (name, catch_phrase, bs) values ('Romaguera-Jacobson', 'Face to face bifurcated interface', 'e-enable strategic applications');
insert into tbl_address (street, suite, city, zipcode, geo_id) values ('Douglas Extension', 'Suite 847', 'McKenziehaven', '59590-4157', 3);

insert into tbl_geo(lat, lng)
values(29.4572, -164.2990);

insert into tbl_address(street, suite, city, zipcode, geo_id)
values('Hoeger Mall', 'Apt. 692', 'South Elvis', '53919-4257', 4);

insert into tbl_company(name, catch_phrase, bs)
values('Robel-Corkery', 'Multi-tiered zero tolerance productivity', 'transition cutting-edge web services');

insert into tbl_geo (lat, lng)
values (-31.8129, 62.5342);

insert into tbl_address (street, suite, city, zipcode, geo_id)
values ('Skiles Walks', 'Suite 351', 'Roscoeview', '33263', 5);

insert into tbl_company (name, catch_phrase, bs)
values ('Keebler LLC', 'User-centric fault-tolerant solution', 'revolutionize end-to-end systems');


/*                 1번~~~~~ post~~~~~*/

create table tbl_post(
    id bigint auto_increment primary key ,
    title varchar(255) not null ,
    body varchar(255) not null ,
    user_id bigint not null ,
    constraint fk_post_user foreign key(user_id)
    references tbl_user(id)
);

insert into tbl_post(title,body,user_id)
values ('sunt aut facere repellat provident occaecati excepturi optio reprehenderit','quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto
',6);

insert into tbl_post(title,body,user_id)
values ('qui est esse','est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla',6);

insert into tbl_post(title,body,user_id)
values ('ea molestias quasi exercitationem repellat qui ipsa sit aut','et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut',6);

insert into tbl_post(title,body,user_id)
values ('eum et est occaecati','ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit',6);

insert into tbl_post(title,body,user_id)
values ('nesciunt quas odio','repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque',6);

/*                 -----------2 번  ------------------*/

create table tbl_comments(
    id bigint auto_increment primary key ,
    name varchar(255) not null ,
    email varchar(255) not null ,
    body varchar(255) not null ,
    post_id bigint not null ,
    constraint fk_comments_post foreign key(post_id)
    references tbl_post(id)

);

insert into tbl_comments(name,email,body,post_id)
values ('id labore ex et quam laborum','Eliseo@gardner.biz','laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium',1);
insert into tbl_comments(name,email,body,post_id)
values ('quo vero reiciendis velit similique earum','Jayne_Kuhic@sydney.com','est natus enim nihil est dolore omnis voluptatem numquam\net omnis occaecati quod ullam at\nvoluptatem error expedita pariatur\nnihil sint nostrum voluptatem reiciendis et',1);
insert into tbl_comments(name,email,body,post_id)
values ('odio adipisci rerum aut animi','Nikita@garfield.biz','quia molestiae reprehenderit quasi aspernatur\naut expedita occaecati aliquam eveniet laudantium\nomnis quibusdam delectus saepe quia accusamus maiores nam est\ncum et ducimus et vero voluptates excepturi deleniti ratione',1);
insert into tbl_comments(name,email,body,post_id)
values ('alias odio sit','Lew@alysha.tv','non et atque\noccaecati deserunt quas accusantium unde odit nobis qui voluptatem\nquia voluptas consequuntur itaque dolor\net qui rerum deleniti ut occaecati',1);
insert into tbl_comments(name,email,body,post_id)
values ('vero eaque aliquid doloribus et culpa','Hayden@althea.biz','harum non quasi et ratione\ntempore iure ex voluptates in ratione\nharum architecto fugit inventore cupiditate\nvoluptates magni quo et',1);





/*                 -----------3 번  ------------------*/

create table tbl_albums(
    id bigint auto_increment primary key ,
    title varchar(255) not null ,
    user_id bigint not null ,
    constraint fk_albums_user foreign key(user_id)
    references tbl_user(id)
);

insert into tbl_albums(title,user_id)
values ('quidem molestiae enim',6);
insert into tbl_albums(title,user_id)
values ('sunt qui excepturi placeat culpa',6);
insert into tbl_albums(title,user_id)
values ('omnis laborum odio',6);
insert into tbl_albums(title,user_id)
values ('non esse culpa molestiae omnis sed optio',6);
insert into tbl_albums(title,user_id)
values ('eaque aut omnis a',6);

/*~~~~~~~~~~~~~~~4번 포토~~~~~~`*/


create table tbl_photos(
    id bigint auto_increment primary key ,
    title varchar(255) not null ,
    url varchar(255) not null ,
    thumbnail_url varchar(255) not null ,
    album_id bigint not null ,
    constraint fk_albums_albums foreign key(album_id)
    references tbl_albums(id)
);

insert into tbl_photos(title, url, thumbnail_url, album_id)
values ('accusamus beatae ad facilis cum similique qui sunt','https://via.placeholder.com/600/92c952','https://via.placeholder.com/150/92c952',1);
insert into tbl_photos(title, url, thumbnail_url, album_id)
values ('reprehenderit est deserunt velit ipsam','https://via.placeholder.com/600/771796','https://via.placeholder.com/150/771796',1);
insert into tbl_photos(title, url, thumbnail_url, album_id)
values ('officia porro iure quia iusto qui ipsa ut modi','https://via.placeholder.com/600/24f355','https://via.placeholder.com/150/24f355',1);
insert into tbl_photos(title, url, thumbnail_url, album_id)
values ('culpa odio esse rerum omnis laboriosam voluptate repudiandae','https://via.placeholder.com/600/d32776','https://via.placeholder.com/150/d32776',1);
insert into tbl_photos(title, url, thumbnail_url, album_id)
values ('natus nisi omnis corporis facere molestiae rerum in','https://via.placeholder.com/600/f66b97','https://via.placeholder.com/150/f66b97',1);

/*~~~~~~~ 5번~~~~~~~~~~ todos*/

create table tbl_todos(
    id bigint auto_increment primary key ,
    title varchar(255) not null ,
    completed varchar(255) not null ,
    user_id bigint not null ,
    constraint fk_todos_user foreign key(user_id)
    references tbl_user(id)
);

insert into tbl_todos(title, completed, user_id)
values ('delectus aut autem','false',6);
insert into tbl_todos(title, completed, user_id)
values ('quis ut nam facilis et officia qui','false',6);
insert into tbl_todos(title, completed, user_id)
values ('fugiat veniam minus','false',6);
insert into tbl_todos(title, completed, user_id)
values ('et porro tempora','true',6);
insert into tbl_todos(title, completed, user_id)
values ('laboriosam mollitia et enim quasi adipisci quia provident illum','false',6);


DELETE FROM tbl_todos WHERE id = 6;
