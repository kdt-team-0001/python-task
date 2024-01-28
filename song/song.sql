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
    completed tinyint default 0,
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
