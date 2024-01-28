from crud_module import *
from connertion_module import *
from albums import *
from photos import *



if __name__ == '__main__':
    # 앨범 추가하기
    save_album_query ="insert into tbl_albums( title,user_id) \
                       values (%s, %s)"
    save_album_params = ("quam nostrum impedit mollitia quod et dolor", 3)
    # save(save_album_query,save_album_params)

    # 앨범 전체조회하기
    find_all_albums_puery ="select * from tbl_albums"
    find_all(find_all_albums_puery)
    # print(find_all)

    # user_id별로 확인하기
    find_user_id_album_query = ("select * from tbl_albums where user_id = %s")
    find_user_id_album_params = 6
    find_user_id_album_list = find_all_by(find_user_id_album_query,find_user_id_album_params)
    # print(find_user_id_album_list)

    # 앨범 타이틀 확인하면 관련 사진 가져오기
    find_album_in_photo_query = ("select * from tbl_albums a join tbl_photos p where\
                                  p.album_id = a.id and  a.title = %s ")
    find_album_in_photo_params = 'quidem molestiae enim'
    find_album_in_photo_list = find_all_by(find_album_in_photo_query,find_album_in_photo_params)
    print(find_album_in_photo_list)





    # 앨범 중 타이틀 수정하기
    new_album_title = '새로운 타이틀!'
    change_id = 5
    update_album_query = ("update tbl_albums set title = %s where id = %s")
    update_album_params = (new_album_title,change_id)
    # update(update_album_query,update_album_params)

    # 앨범 삭제하기
    delete_album_query = ("delete from tbl_albums where id = %s")
    delete_album_params = 6
    # delete(delete_album_query,delete_album_params)
