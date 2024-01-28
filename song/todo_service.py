from user import *
from todo import *
from crud_module import *


if __name__ == '__main__':
    # 할 일 추가
    find_all_query = "select t.user_id, t.id, title, completed \
                    from tbl_todo t join tbl_user u \
                    on t.user_id = u.id"
    save_many_query = "insert into tbl_todo (user_id, title) \
                        values (%s, %s)"
    save_many_params = (
        (1, 'delectus aut autem'),
        (2, 'quis ut nam facilis et officia qui'),
        (3, 'fugiat veniam minus'),
        (4, 'et porro tempora'),
        (5, 'laboriosam mollitia et enim quasi adipisci quia provident illum')
    )
    # save_many(save_many_query, save_many_params)

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


    # 할 일 완료
    update_query = ("update tbl_todo \
                    set completed = 1 \
                    where id = %s")
    update_params = 1,
    # update(update_query, update_params)

    # 할 일 삭제
    delete_query = "delete from tbl_todo where id = %s"
    delete_params = 1,
    # delete(delete_query, delete_params)