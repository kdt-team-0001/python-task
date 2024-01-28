from user import *
from album import *
from photo import *
from crud_module import *

# album_id, id, title, url, thumbnail_url

if __name__ == '__main__':
    # 사진 추가
    find_all_query = "select p.album_id, p.id, title, url, thumbnail_url \
                        from tbl_photo p join tbl_album a \
                        on p.album_id = a.id"
    save_many_query = "insert into tbl_photo (album_id, title, url, thumbnail_url) \
                        values (%s, %s, %s, %s)"
    save_many_params = (
        (1, 'accusamus beatae ad facilis cum similique qui sunt', 'https://via.placeholder.com/600/92c952', 'https://via.placeholder.com/150/92c952'),
        (1, 'reprehenderit est deserunt velit ipsam', 'https://via.placeholder.com/600/771796', 'https://via.placeholder.com/150/771796'),
        (1, 'officia porro iure quia iusto qui ipsa ut modi', 'https://via.placeholder.com/600/24f355', 'https://via.placeholder.com/150/24f355'),
        (1, 'culpa odio esse rerum omnis laboriosam voluptate repudiandae', 'https://via.placeholder.com/600/d32776', 'https://via.placeholder.com/150/d32776'),
        (1, 'natus nisi omnis corporis facere molestiae rerum in', 'https://via.placeholder.com/600/f66b97', 'https://via.placeholder.com/150/f66b97')
    )
    save_many(save_many_query, save_many_params)

    # 사진 조회
    find_by_id_query = "select album_id, id, title, url, thumbnail_url \
                                from tbl_todo \
                                on id = %s"
    find_by_id_params = 1,
    found_photo = find_by_id(find_by_id_query, find_by_id_params)
    print(found_photo)

    # 사진 수정
    update_query = "update tbl_todo \
                    set album_id = 2 \
                    where id = %s"
    update_params = 1,
    # update(update_query, update_params)

    # 사진 삭제
    delete_query = "delete from tbl_todo where id = %s"
    delete_params = 1,
    # delete(delete_query, delete_params)

