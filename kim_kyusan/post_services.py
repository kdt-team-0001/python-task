from post import *
from user import *
from crud_module import *

# post 생성
find_by_id_query = "select id from tbl_user where email = %s"
find_by_id_params = "Sincere@april.biz"
user_list = find_by_id(find_by_id_query, find_by_id_params)

save_many_query = "insert into tbl_post (user_id, title, body)  values (%s,%s,%s)"
save_many_params = (
    (user_list.get("id"), "sunt aut facere repellat provident occaecati excepturi optio reprehenderit","quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"),
    (user_list.get("id"),"qui est esse", "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"),
    (user_list.get("id"),"ea molestias quasi exercitationem repellat qui ipsa sit aut","et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"),
    (user_list.get("id"), "eum et est occaecati","ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit"),
    (user_list.get("id"),"nesciunt quas odio","repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque")
)
# save_many(save_many_query, save_many_params)

# post 조회
find_by_id_query = "select user_id, id, title, body from tbl_post where title = %s"
find_by_id_params = "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
post_list = find_by_id(find_by_id_query,find_by_id_params)
# post , body 수정
if post_list is not None:
    new_body = input("새로운 내용을 입력하세요: ")
    update_query = "update tbl_post set body = %s where title = %s"
    update_params = new_body, post_list.get("title")
    # update(update_query, update_params)
else:
    print("해당 post가 존재하지 않습니다.")

# post 삭제
if post_list is not None:
    delete_query = "delete from tbl_post where id = %s"
    delete_params = post_list.get("id")
    delete(delete_query, delete_params)
else:
    print("해당 post가 존재하지 않습니다.")