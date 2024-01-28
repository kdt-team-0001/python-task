from study_python.gyoung_deok.todo.todo import Todo
from study_python.gyoung_deok.user.user_module import *


if __name__ == '__main__':
    # 할일 추가
    # user_id = 1,
    # user = find_by_user_id(user_id).get("user")
    #
    # save_many_query = "insert into tbl_todo(title, completed, user_id) \
    #                    values (%s, %s, %s)"
    # save_many_params = (
    #     ("suscipit qui totam", 1, user.id),
    #     ("voluptates eum voluptas et dicta", 0, user.id),
    #     ("quidem at rerum quis ex aut sit quam", 1, user.id),
    # )
    # save_many(save_many_query, save_many_params)

    # 할일 목록
    # user_id = 1,
    # user = find_by_user_id(user_id).get("user")
    #
    # find_all_by_query = "select title, completed from tbl_todo where user_id = %s"
    # find_all_by_params = user.id
    # todos = find_all_by(find_all_by_query, find_all_by_params)
    #
    # for todo in todos:
    #     print(f"할일 제목: {todo.get('title')}\n완료 여부: {'완료' if todo.get('completed') else '미완료'}\n")

    # 할일 상세보기
    user_id = 1,
    user = find_by_user_id(user_id).get("user")

    find_by_id_query = "select id, title, completed from tbl_todo where id = %s and user_id = %s"
    find_by_id_params = 1, user.id
    found_photo = find_by_id(find_by_id_query, find_by_id_params)
    todo = Todo(user=user, **found_photo)
    print(todo)

    # 할일 수정
    todo.title = todo.title
    todo.completed = 1
    update_query = "update tbl_todo set title = %s, completed = %s where id = %s and user_id = %s"
    update_params = todo.title, todo.completed, todo.id, user.id
    update(update_query, update_params)
    print(find_by_id(find_by_id_query, find_by_id_params))
    print(todo)

    # 할일 삭제
    delete_query = "delete from tbl_todo where id = %s"
    delete_params = 1,
    # delete(delete_query, delete_params)
