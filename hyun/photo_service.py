from crud_module import *
from connection_module import *
from user.geo import *
from user.address import *
from user.company import *
from user.user import *
from album.album import *
from photo.photo import *

if __name__ == '__main__':
    # 일단 photo 4개정도만 넣기
    save_many_query = "insert into tbl_photo (album_id, title, url, thumbnailurl) \
                       values (%s, %s, %s, %s)"
    save_many_params = (
        (5, "accusamus beatae ad facilis cum similique qui sunt", "https://via.placeholder.com/600/92c952", "https://via.placeholder.com/150/92c952"),
        (5, "reprehenderit est deserunt velit ipsam", "https://via.placeholder.com/600/771796", "https://via.placeholder.com/150/771796"),
        (6, "tenetur minus voluptatum et", "https://via.placeholder.com/600/c96cad", "https://via.placeholder.com/150/c96cad"),
        (7, "expedita rerum eaque", "https://via.placeholder.com/600/4d564d", "https://via.placeholder.com/150/4d564d")
    )
    # save_many(save_many_query, save_many_params)

    # 사진 추가하기
    save_query = "insert into tbl_photo (album_id, title, url, thumbnailurl) \
                  values (%s, %s, %s, %s)"
    save_params = 8, "totam voluptas iusto deserunt dolores", "https://via.placeholder.com/600/ea51da", "https://via.placeholder.com/150/ea51da"
    # save(save_query, save_params)

    # 사진 전체 목록 가져오기
    find_all_query = "select p.*, a.* from tbl_photo p join tbl_album a on p.album_id = a.id"
    found_photos = find_all(find_all_query)
    photos = []
    for found_photo in found_photos:
        # 앨범 id로 앨범 정보 조회
        find_by_id_query = "select a.*, u.* from tbl_album a \
                              join tbl_user u on a.id = %s and a.user_id = u.id"
        find_by_id_params = found_photo.get('album_id'),
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
        photo = Photo(album=album, **found_photo)
        photos.append(photo)
    for photo in photos:
        print(photo.__dict__)

    # 사진 id로 1개 가져오기

    find_by_id_query = "select p.*, a.* from tbl_photo p join tbl_album a on p.id = %s and p.album_id = a.id"
    find_by_id_params = 1,
    found_photo = find_by_id(find_by_id_query, find_by_id_params)
    # 앨범id로 앨범 정보 조회
    find_by_id_query = "select a.*, u.* from tbl_album a \
                                  join tbl_user u on a.id = %s and a.user_id = u.id"
    find_by_id_params = found_photo.get('album_id'),
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
    photo = Photo(album=album, **found_photo)
    print(photo.__dict__)

    # 사진 수정
    # 수정된 사진 객체라고 가정합니다.
    photo.title = "수정된 사진 제목1"
    update_query = "update tbl_photo set title = %s where id = %s"
    update_params = photo.title, photo.id
    update(update_query, update_params)

    # 사진 삭제
    delete_query = "delete from tbl_photo where id = %s"
    delete_params = 1,
    # delete(delete_query, delete_params)

