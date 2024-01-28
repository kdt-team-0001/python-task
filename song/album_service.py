from user import *
from album import *
from photo import *
from crud_module import *

if __name__ == '__main__':
    # 앨범 추가
    save_many_query = "insert into tbl_album (user_id, title)\
                        values(%s, %s)"
    save_many_params = (
        (1, 'quidem molestiae enim'),
        (1, 'sunt qui excepturi placeat culpa'),
        (1, 'omnis laborum odio'),
        (1, 'non esse culpa molestiae omnis sed optio')
    )
    # save_many(save_many_query, save_many_params)

    # 앨범 생성
    album = Album(user_id=1, title='eaque aut omnis a')
    save_query = "insert into tbl_album (user_id, title) \
                    values(%s, %s)"
    save_params = (album.user_id, album.title)
    # save(save_query, save_params)

    # 앨범 목록
    find_all_query = "select user_id, id, title from tbl_album"
    found_albums = find_all(find_all_query)
    print(found_albums)

    # 앨범 수정
    update_query = "update tbl_album \
                    set title = 'test album' \
                    where id = %s"
    update_params = 1,
    # update(update_query, update_params)

    # 앨범 삭제
    delete_query = "delete from tbl_album where id = %s"
    delete_params = 1,
    # delete(delete_query, delete_params)
