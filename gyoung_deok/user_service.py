from study_python.gyoung_deok.crud_module import *
from study_python.gyoung_deok.user.address import *
from study_python.gyoung_deok.user.company import *
from study_python.gyoung_deok.user.user import *

if __name__ == '__main__':
    # 유저 추가
    # find_by_id_query = "select id, lat, lng from tbl_geo where id = %s"
    # find_by_id_params = 1,
    # found_geo = find_by_id(find_by_id_query, find_by_id_params)
    # geo = Geo(**found_geo)
    # find_all_query = "select id, lat, lng from tbl_geo"
    # geos = find_all(find_all_query)

    #
    # find_by_id_query = "select id, street, suite, city, zipcode, geo_id from tbl_address where id = %s"
    # find_by_id_params = 1,
    # found_address = find_by_id(find_by_id_query, find_by_id_params)
    # # found_address의 마지막 키값은 geo_id이지만 Address클래스를 객체화할 때 geo는 객체를 매개 변수로 전달해야 하기 때문에 풀어서 작성한다.
    # address = Address(found_address.get("id"), found_address.get("street"), found_address.get("suite"), found_address.get("city"), found_address.get("zipcode"), geo)
    #
    # find_all_query = "select id, street, suite, city, zipcode, geo_id from tbl_address"
    # addresses = find_all(find_all_query)
    # for i in range(len(addresses)):
    #     addresses[i]['geo'] = Geo(**geos[i])

    # find_by_id_query = "select id, name, catch_phrase, bs from tbl_company where id = %s"
    # find_by_id_params = 1,
    # found_company = find_by_id(find_by_id_query, find_by_id_params)
    # company = Company(**found_company)
    #
    # find_all_query = "select id, name, catch_phrase, bs from tbl_company"
    # companies = find_all(find_all_query)

    # save_many_query = "insert into tbl_user(name, username, email, phone, website, address_id, company_id) \
    #                    values (%s, %s, %s, %s, %s, %s, %s)"
    # save_many_params = (
    #     ("Ervin Howell", "Antonette", "Shanna@melissa.tv", "010-692-6593 x09125", "anastasia.net", addresses[0].get("id"), companies[0].get("id")),
    #     ("Leanne Graham", "Bret", "Sincere@april.biz", "1-770-736-8031 x56442", "hildegard.org", addresses[1].get("id"), companies[1].get("id")),
    #     ("Clementine Bauch", "Samantha", "Nathan@yesenia.net", "1-463-123-4447", "ramiro.info", addresses[2].get("id"), companies[2].get("id")),
    #     ("Chelsey Dietrich", "Kamren", "Lucio_Hettinger@annie.ca", "(254)954-1289", "demarco.info", addresses[3].get("id"), companies[3].get("id")),
    #     ("Patricia Lebsack", "Karianne", "Julianne.OConner@kory.org", "493-170-9623 x156", "kale.biz", addresses[4].get("id"), companies[4].get("id")),
    # )
    # save_many(save_many_query, save_many_params)

    # 마이페이지
    find_by_id_query = "select u.id, u.name, u.username, u.email, u.phone, u.website, u.address_id, u.company_id, \
                        c.name, c.catch_phrase, c.bs, a.street, a.suite, a.city, a.zipcode, a.geo_id, g.lat, g.lng\
                        from tbl_company c join tbl_user u \
                        on u.id = %s and c.id = u.company_id \
                        join tbl_address a on a.id = u.address_id \
                        join tbl_geo g on g.id = a.geo_id"
    find_by_id_params = 1,
    found_user = find_by_id(find_by_id_query, find_by_id_params)

    geo = Geo(
        id=found_user.get("geo_id"),
        lat=found_user.get("lat"),
        lng=found_user.get("lng")
    )

    address = Address(
        id=found_user.get("address_id"),
        street=found_user.get("street"),
        suite=found_user.get("suite"),
        city=found_user.get("city"),
        zipcode=found_user.get("zipcode"),
        geo=geo.__dict__
    )

    company = Company(
        id=found_user.get("company_id"),
        name=found_user.get("c.name"),
        catch_phrase=found_user.get("catch_phrase"),
        bs=found_user.get("bs")
    )

    user = User(
        id=found_user.get("id"),
        name=found_user.get("name"),
        username=found_user.get("username"),
        email=found_user.get("email"),
        phone=found_user.get("phone"),
        website=found_user.get("website"),
        address=address.__dict__,
        company=company.__dict__
    )
    # print(user)

    # 유저정보 수정
    # geo테이블
    # 수정하고자 하는 부분에 값 넣기
    geo.lat = geo.lat
    geo.lng = geo.lng

    update_query = "update tbl_geo set lat=%s, lng=%s where id=%s"
    update_params = geo.lat, geo.lng, geo.id

    find_by_id_query = "select * from tbl_geo where id = %s"
    find_by_id_params = geo.id,
    # update(update_query, update_params)
    # print(find_by_id(find_by_id_query, find_by_id_params))
    # print(user)


    # address테이블
    # 수정하고자 하는 부분에 값 넣기
    find_by_id_query = "select * from tbl_geo where id = %s"
    find_by_id_params = 1,
    change_geo = Geo(**find_by_id(find_by_id_query, find_by_id_params))



    address.street = address.street
    address.suite = address.suite
    address.city = address.city
    address.zipcode = address.zipcode
    if change_geo.id == geo.id:
        address.geo = change_geo.__dict__

    update_query = "update tbl_address \
                    set street = %s, suite = %s, city = %s, zipcode = %s, geo_id = %s \
                    where id=%s"
    update_params = address.street, address.suite, address.city, address.zipcode, address.geo.get("id"), address.id

    find_by_id_query = "select * from tbl_address where id = %s"
    find_by_id_params = address.id,
    # update(update_query, update_params)
    # print(find_by_id(find_by_id_query, find_by_id_params))
    # print(user)

    # company테이블
    # 수정하고자 하는 부분에 값 넣기
    company.name = company.catch_phrase
    company.catch_phrase = company.catch_phrase
    company.bs = company.bs
    update_query = "update tbl_company set name = %s, catch_phrase = %s, bs = %s where id = %s"
    update_params = company.name, company.catch_phrase, company.bs, company.id

    find_by_id_query = "select * from tbl_company where id = %s"
    find_by_id_params = company.id,
    # update(update_query, update_params)
    # print(find_by_id(find_by_id_query, find_by_id_params))
    # print(user)

    # user테이블
    # 수정하고자 하는 부분에 값 넣기
    user.name = user.name
    user.username = user.username
    user.email = user.email
    user.phone = user.phone
    user.website = user.website
    user.address = address.__dict__
    user.company = company.__dict__

    update_query = "update tbl_user \
                    set name = %s, username = %s, email = %s, phone = %s, website = %s \
                    where id = %s"
    update_params = user.name, user.username, user.email, user.phone, user.website
    find_by_id_query = "select * from tbl_user where id = %s"
    find_by_id_params = user.id,
    # update(update_query, update_params)
    # print(find_by_id(find_by_id_query, find_by_id_params))
    # print(user)

    # 삭제
    tbl_names = 'tbl_user', 'tbl_company', 'tbl_address', 'tbl_geo'
    tbl_ids = user.id, user.company.get("id"), user.address.get("id"), user.address["geo"]["id"]
    for tbl_name in tbl_names:
        i = tbl_names.index(tbl_name)
        delete_query = f"delete from {tbl_name} where id = %s"
        delete_params = tbl_ids[i],
        # delete(delete_query, delete_params)
