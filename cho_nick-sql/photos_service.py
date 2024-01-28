from crud_module import *
from connertion_module import *
from photos import *
from albums import *


if __name__ == '__main__':
    # 사진 추가하기
    add_photo_query = ("insert into tbl_photos(title, url, thumbnail_url, album_id) \
                        values (%s,%s,%s,%s)")
    add_photo_params = ('totam voluptas iusto deserunt dolores','"https://via.placeholder.com/600/ea51da','https://via.placeholder.com/150/ea51da',2)
    # save(add_photo_query,add_photo_params)


    # 사진 넘버로 가져오기
    find_one_photo_query = "select id, title, url, thumbnail_url, album_id from tbl_photos where id =%s "
    find_one_photo_params = 1
    photo_list = find_by_id (find_one_photo_query,find_one_photo_params)
    # print(photo_list)

    # 앨범에 있는 사진 다 가져오기

    photo_all_query = "select * from tbl_photos where album_id =%s "
    photo_all_params = 1
    all_album_photos_list = find_all_by(photo_all_query,photo_all_params)
    # print(all_album_photos_list)

    # 앨범 타이틀 관련 정보도 다 가져오기
    photo_album_query = ("select * from tbl_photos p join tbl_albums a where\
                          p.album_id = a.id and p.album_id = %s")
    photo_album_params = 1
    photo_album_list = find_all_by(photo_album_query,photo_album_params)
    # print(photo_album_list)

    # 사진 타이틀 바꿔주기
    new_title = '타이틀 1'
    update_id = 1
    update_photo_query = "update tbl_photos set title = %s where id = %s"
    update_photo_params = (new_title,update_id)
    # update(update_photo_query,update_photo_params)


    # 사진 삭제하기
    delete_photo_query = "delete from tbl_photos where id = %s"
    delete_photo_params = 6
    # delete(delete_photo_query, delete_photo_params)

