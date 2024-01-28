create table tbl_geo(
    id bigint auto_increment primary key,
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
    constraint fk_address_geo foreign key(geo_id)
                        references tbl_geo(id)
);

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



