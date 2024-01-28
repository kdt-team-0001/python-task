from user import *
from todo import *
from crud_module import *


if __name__ == '__main__':
    # 할 일 추가
    find_all_query = "select t.user_id, t.id, title, completed \
                    from tbl_todo t join tbl_user u \
                    on t.user_id = u.id"
    save_many_query = "insert into tbl_todo (user_id, title, completed) \
                        values (%s, %s, %s)"
    save_many_params = (
        (1, 'delectus aut autem', False),
        (2, 'quis ut nam facilis et officia qui', False),
        (3, 'fugiat veniam minus', False),
        (4, 'et porro tempora', False)
    )
    save_many(save_many_query, save_many_params)

    # 할 일 추가
    todo_add = Todo(user_id=5, title='laboriosam mollitia et enim quasi adipisci quia provident illum', completed=False)
    save_query = "insert into tbl_todo (user_id, title, completed) \
                    values (%s, %s, %s)"
    save_params = (todo_add.user_id, todo_add.title, todo_add.completed)
    save(save_many_query, save_many_params)

    # 유저 별 할 일 조회
    find_by_id_query = "select u.id, t.id, title, completed \
                        from tbl_todo t join tbl_user u \
                        on t.user_id = u.id and u.id = %s"
    find_by_id_params = 2,
    found_todo = find_by_id(find_by_id_query, find_by_id_params)
    print(found_todo)

    # 할 일 수정
    update_query = ("update tbl_todo \
                    set title = 'test todo'\
                    where id = %s")
    update_params = 1,
    # update(update_query, update_params)


    # 완료
    update_query = ("update tbl_todo \
                    set completed = True \
                    where id = %s")
    update_params = 4,
    # update(update_query, update_params)

    # 할 일 삭제
    delete_query = "delete from tbl_todo where id = %s"
    delete_params = 1,
    # delete(delete_query, delete_params)