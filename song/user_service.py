from user.geo import *
from user.address import *
from user.company import *
from user.user import *
from crud_module import *


if __name__ == '__main__':
    # 위치 정보
    # find_by_id_query = "select id, lat, lng from tbl_geo where id = %s"
    # find_by_id_params = 1,
    # found_geo = find_by_id(find_by_id_query, find_by_id_params)
    # geo = Geo(**found_geo)
    # print(geo.__dict__)
    #
    # # 주소 정보
    # find_by_id_query = "select id, street, suite, city, zipcode from tbl_address where id = %s"
    # find_by_id_params = 1,
    # found_address = find_by_id(find_by_id_query, find_by_id_params)
    # address = Address(geo=geo, **found_address)
    # # print(address.__dict__)
    # # print(address.__dict__.get('geo').lat)
    #
    # # 회사 정보
    # find_by_id_query = "select id, name, catch_phrase, bs from tbl_company where id = %s"
    # find_by_id_params = 1,
    # found_company = find_by_id(find_by_id_query,find_by_id_params)
    # company = Company(**found_company)
    # # print(company.__dict__)

    # 유저 정보
    save_many_query = "insert into tbl_user(name, username, email, address_id, phone, website, company_id)\
                        values (%s, %s, %s, %s, %s, %s, %s)"
    save_many_params = (
        ('Leanne Graham', 'Bret', 'Sincere@april.biz', 1, '1-770-736-8031 x56442', 'hildegard.org', 1),
        ('Ervin Howell', 'Antonette', 'Shanna@melissa.tv', 2, '010-692-6593 x09125', 'anastasia.net', 2),
        ('Clementine Bauch', 'Samantha', 'Nathan@yesenia.net', 3, '1-463-123-4447', 'ramiro.info', 3),
        ('Patricia Lebsack', 'Karianne', 'Julianne.OConner@kory.org', 4, '493-170-9623 x156', 'kale.biz', 4),
    )
    # save_many(save_many_query, save_many_params)

    # 회원 가입
    user = User(name='Chelsey Dietrich', username='Kamren', email='Lucio_Hettinger@annie.ca', address=5, phone='(254)954-1289', website='demarco.info', company=5)
    save_query = "insert into tbl_user(name, username, email, address_id, phone, website, company_id)\
                    values(%s, %s, %s, %s, %s, %s, %s)"
    save_params = (user.name, user.username, user.email, user.address, user.phone, user.website, user.company)
    # save(save_query, save_params)

    # user 정보 조회(마이페이지)
    find_by_id_query = "select id, name, username, email, address_id, phone, website, company_id\
                            from tbl_user where id = %s"
    find_by_id_params = 2,
    found_info = find_by_id(find_by_id_query, find_by_id_params)
    print(found_info)

    # 전체 정보 조회(마이페이지)
    find_by_id_query = "select u.id, u.name, username, email, address_id, phone, website, company_id, \
                            a.id, a.street, a.suite, a.city, a.zipcode, a.geo_id, \
                            g.id, g.lat, g.lng, \
                            c.id, c.name, c.catch_phrase, c.bs from tbl_user u join tbl_address a on u.id = %s and a.id = u.address_id\
                            join tbl_geo g on g.id = a.geo_id \
                            join tbl_company c on c.id = u.company_id"
    find_by_id_params = 2,
    found_info = find_by_id(find_by_id_query, find_by_id_params)
    geo = Geo(**found_info)
    address = Address(geo=geo, **found_info)
    company = Company(**found_info)
    user = User(address=address, company=company, **found_info)
    print(user.__dict__)

    # 회원 정보 수정
    update_query = "update tbl_user \
                    set name = 'song' \
                    where id = %s"
    update_params = 5,
    # update_user = update(update_query, update_params)

    # 탈퇴
    delete_query = "delete from tbl_user where id = %s"
    delete_params = 5,
    # delete_user = delete(delete_query, delete_params)