from user import *
from album import *
from crud_module import *

# 앨범 추가

find_by_id_query = "select id from tbl_user where id = %s"
find_by_id_params = 1,
user_info = find_by_id(find_by_id_query, find_by_id_params)

save_many_query= "insert into tbl_album (user_id, title) values (%s, %s)"
save_many_params= (
(user_info.get("id"), "quidem molestiae enim"),
(user_info.get("id"), "sunt qui excepturi placeat culpa"),
(user_info.get("id"), "omnis laborum odio"),
(user_info.get("id"), "non esse culpa molestiae omnis sed optio"),
(user_info.get("id"), "eaque aut omnis a"),
)
# save_many(save_many_query, save_many_params)

# 앨범 전체 조회
find_all_by_query = "select * from tbl_album"
find_all_by_params= []
album_list = find_all_by(find_all_by_query, find_all_by_params)
# for album in album_list:
#     print(album)

# 앨범 title 수정 => 타이틀 명칭이 똑같은 걸 찾은 후 해당 타이틀을 변경해야 함

find_by_id_query = "select * from tbl_album where title = %s"
find_by_id_params= input("타이틀을 입력하세요: ") # quidem molestiae enim
album_list = find_by_id(find_by_id_query, find_by_id_params)
delete_album_list = find_by_id(find_by_id_query, find_by_id_params)

if album_list is not None:
    new_title = input("새로운 타이틀을 입력하세요: ")
    update_query = "select * from tbl_album where title = %s"
    update_params = new_title,
    # update(update_query, update_params)
    print("타이틀이 변경되었습니다.")
else:
    print("해당 앨범이 없습니다.")

# 앨범  삭제
if delete_album_list is not None:
    delete_query = "delete from tbl_album where title = %s"
    delete_params = delete_album_list,
    # delete(delete_query, delete_params)
else:
    print("해당 앨범이 없습니다.")

