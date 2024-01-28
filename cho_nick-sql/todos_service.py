from crud_module import *
from connertion_module import *
from todos import *

if __name__ == '__main__':

    # todos 생성하기
    save_todos_query = "insert into tbl_todos (title, completed, user_id) \
                        values (%s, %s, %s)"
    save_todos_params = ("quo adipisci enim quam ut ab", 'true', 3)
    # save(save_todos_query,save_todos_params)

    # todos 전체 조회하기
    find_todos_query = "select * from tbl_todos"
    find_all_todos = find_all(find_todos_query)
    # print(find_all_todos)

    # todos true만 조회하기
    find_todos_completed_query = "select * from tbl_todos where completed =%s"
    find_todos_completed_params = "true"
    find_todos_completed_list = find_all_by(find_todos_completed_query,find_todos_completed_params)
    # print(find_todos_completed_list)

    # todos 에서 false를 true로 바꿔주기
    new_completed = 'true'
    change_id = 5
    update_todos_completed_query = "update tbl_todos set completed=%s where id=%s"
    update_todos_completed_params = (new_completed, change_id)
    # update(update_todos_completed_query,update_todos_completed_params)


    # todos 삭제하기
    delete_todos_query = "delete from tbl_todos where id = %s"
    delete_todos_params = 7
    # delete(delete_todos_query,delete_todos_params)