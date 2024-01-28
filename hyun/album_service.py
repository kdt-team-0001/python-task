from crud_module import *
from connection_module import *
from user.geo import *
from user.address import *
from user.company import *
from user.user import *
from album.album import *

if __name__ == '__main__':
    # 우선 앨범 4개 정도만 추가
    save_many_query = "insert into tbl_album(user_id, title) \
                       values (%s, %s)"
    save_many_params = (
        (2, "quidem molestiae enim"),
        (2, "sunt qui excepturi placeat culpa"),
        (2, "omnis laborum odio"),
        (3, "quam nostrum impedit mollitia quod et dolor")
    )
    # save_many(save_many_query, save_many_params)

    # 앨범 추가하기
    save_query = "insert into tbl_album(user_id, title) \
                  values (%s, %s)"
    save_params = 3, "nesciunt quia et doloremque"
    # save(save_query, save_params)

    # 앨범 전체 조회하기

    find_all_query = "select a.*, u.* from tbl_album a \
                      join tbl_user u on a.user_id = u.id"
    found_albums = find_all(find_all_query)
    albums = []
    for found_album in found_albums:
        # 유저id로 유저 정보 조회
        find_by_id_query = "select u.id, u.name, username, email, address_id, phone, website, company_id, a.geo_id, a.id, \
                                a.street, a.suite, a.city, a.zipcode, g.id, g.lat, g.lng, c.id, c.name, c.catch_phrase, c.bs \
                                from tbl_user u join tbl_address a on u.id = %s and a.id = u.address_id \
                                join tbl_geo g on a.geo_id = g.id \
                                join tbl_company c on c.id = u.company_id"
        find_by_id_params = found_album.get('user_id'),
        found_info = find_by_id(find_by_id_query, find_by_id_params)
        geo = Geo(**found_info)
        address = Address(geo=geo, **found_info)
        company = Company(**found_info)
        user = User(address=address, company=company, **found_info)
        album = Album(user=user, **found_album)
        albums.append(album)
    for album in albums:
        print(album.__dict__)

    # 앨범 id로 앨범 1개 조회하기
    find_by_id_query = "select a.*, u.* from tbl_album a \
                      join tbl_user u on a.id = %s and a.user_id = u.id"
    find_by_id_params = 5,
    found_album = find_by_id(find_by_id_query, find_by_id_params)
    # 유저id로 유저 정보 조회
    find_by_id_query = "select u.id, u.name, username, email, address_id, phone, website, company_id, a.geo_id, a.id, \
                                    a.street, a.suite, a.city, a.zipcode, g.id, g.lat, g.lng, c.id, c.name, c.catch_phrase, c.bs \
                                    from tbl_user u join tbl_address a on u.id = %s and a.id = u.address_id \
                                    join tbl_geo g on a.geo_id = g.id \
                                    join tbl_company c on c.id = u.company_id"
    find_by_id_params = found_album.get('user_id'),
    found_info = find_by_id(find_by_id_query, find_by_id_params)
    geo = Geo(**found_info)
    address = Address(geo=geo, **found_info)
    company = Company(**found_info)
    user = User(address=address, company=company, **found_info)
    album = Album(user=user, **found_album)
    print(album.__dict__)

    # 앨범 수정하기
    # 수정된 앨범 객체라고 가정합니다.
    album.title = "수정된 앨범 제목1"
    update_query = "update tbl_album set title = %s where id = %s"
    update_params = album.title, album.id
    # update(update_query, update_params)

    # 앨범 삭제하기
    delete_query = "delete from tbl_album where id = %s"
    delete_params = 5,
    # delete(delete_query, delete_params)



