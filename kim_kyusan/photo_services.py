from album import *
from photo import *
from crud_module import *

# 포토 생성
find_by_id_qeury = "select *from tbl_album where id = %s"
find_by_id_params = 1,
album_list = find_by_id(find_by_id_qeury, find_by_id_params)

save_many_query = "insert into tbl_photo (album_id, title, url, thumbnail_url) values (%s, %s, %s, %s)"
save_many__params = (
    (1,"accusamus beatae ad facilis cum similique qui sunt","https://via.placeholder.com/600/92c952", "https://via.placeholder.com/150/92c952"),
    (1,"reprehenderit est deserunt velit ipsam", "https://via.placeholder.com/600/771796", "https://via.placeholder.com/150/771796"),
    (1,"officia porro iure quia iusto qui ipsa ut modi","https://via.placeholder.com/600/24f355","https://via.placeholder.com/150/24f355"),
    (1,"culpa odio esse rerum omnis laboriosam voluptate repudiandae", "https://via.placeholder.com/600/d32776","https://via.placeholder.com/150/d32776"),
    (1,"natus nisi omnis corporis facere molestiae rerum in","https://via.placeholder.com/600/f66b97", "https://via.placeholder.com/150/f66b97"),
)
# save_many(save_many_query, save_many__params)

# 포토 조회
find_by_id_qeury = "select album_id, id, title, url, thumbnail_url from tbl_photo where title = %s"
find_by_id_params = "accusamus beatae ad facilis cum similique qui sunt"
photo_list = find_by_id(find_by_id_qeury, find_by_id_params)
# print(photo_list)

find_by_id_qeury = "select  id,title from tbl_album where title = %s"
find_by_id_params = "quidem molestiae enim"
album_list = find_by_id(find_by_id_qeury, find_by_id_params)
print(album_list.get('id'))

# 포토 title 수정
if album_list is not None:
    if photo_list is not None:
        new_title = input("새로운 title 을 입력하세요: ")
        update_query = "update tbl_photo set title = %s where album_id =%s and title = %s"
        update_params = album_list.get("id") , photo_list.get("title")
        # update(update_query, update_params)
    else:
        print("phote title이 존재하지 않습니다.")
else:
    print("앨범이 존재하지 않습니다.")

# 포토 삭제
if photo_list is not None:
    delete_query = "delete from tbl_photo where title = %s"
    delete_params = album_list.get("title")
    # delete(delete_query, delete_params)
else:
    print("삭제할 항목이 없습니다.")