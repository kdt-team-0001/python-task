from a_mac.study_python.kim_kyusan.todo.todo import *
from crud_module import *

find_by_id_query = "select id from tbl_user where id = %s"
find_by_id_params = 1,
user_info = find_by_id(find_by_id_query, find_by_id_params)

# todo항목 추가
save_query = "insert into tbl_todo (user_id, title, completed) values (%s, %s, %s)"
save_params = (user_info.get("id"), "delecturs aut autem", False)
# save(save_query, save_params)

save_many_query = "insert into tbl_todo (user_id, title, completed) values (%s, %s, %s)"
save_many_params = (
    (user_info.get("id"), "quis ut nam facilis et officia qui", False),
    (user_info.get("id"), "fugiat veniam minus", False),
    (user_info.get("id"), "et porro tempora", True),
    (user_info.get("id"), "laboriosam mollitia et enim quasi adipisci quia provident illum", True),
)
# save_many(save_many_query,save_many_params)

# todo리스트 1개 항목 조회
find_by_id_query = "select id, user_id, title, completed from tbl_todo where user_id = %s"
find_by_id_params = 1,
todo_one_list = find_all_by(find_by_id_query, find_by_id_params)
# print(todo_one_list)

# todo리스트 전체 조회
find_all_query = "select *from tbl_todo"
todo_list = find_all(find_all_query)
for todo in todo_one_list:
    todo_one = Todo(**todo)
    # print(todo_one.__dict__)

# todo항목 중 comleted 수정
find_by_id_query= "select id, user_id, title, completed from tbl_todo where title = %s"
find_by_id_params = "delecturs aut autem",
todo_title_list =find_by_id(find_by_id_query, find_by_id_params)
print(todo_title_list.get("completed"))

if todo_title_list is not None:
    if todo_title_list.get("completed") is False:
        update_query = "update tbl_todo set completed = True where title =%s"
        update_params = "delecturs aut autem"
        # update(update_query, update_params)
    else:
        print("completed 값은 현재 True 입니다.")
else:
    print("선택한 앨범이 없습니다")


# todo리스트 삭제
if todo_one_list is not None:
    delete_query ="delete from tbl_todo where id = %s"
    delete_params = todo_title_list.get('id')
    delete(delete_query, delete_params)
