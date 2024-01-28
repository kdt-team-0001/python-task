from crud_module import *
from connection_module import *
from user.geo import *
from user.address import *
from user.company import *
from user.user import *
from todo.todo import *

if __name__ == '__main__':
    # 우선 할일 4개정도만 추가하기
    save_many_query = "insert into tbl_todo (title, completed, user_id) \
                       values (%s, %s, %s)"
    save_many_params = (
        ("delectus aut autem", False, 2),
        ("quis ut nam facilis et officia qui", False, 2),
        ("et porro tempora", True, 3),
        ("laboriosam mollitia et enim quasi adipisci quia provident illum", True, 4)
    )
    # save_many(save_many_query, save_many_params)

    # 할일 추가하기
    save_query = "insert into tbl_todo (title, completed, user_id) \
                  values (%s, %s, %s)"
    save_params = "quo adipisci enim quam ut ab", True, 5
    # save(save_query, save_params)

    # 할일 전체 조회하기
    find_all_query = "select t.*, u.* from tbl_todo t join tbl_user u on t.user_id = u.id"
    found_todos = find_all(find_all_query)
    todos = []
    for found_todo in found_todos:
        find_by_id_query = "select u.id, u.name, username, email, address_id, phone, website, company_id, a.geo_id, a.id, \
                            a.street, a.suite, a.city, a.zipcode, g.id, g.lat, g.lng, c.id, c.name, c.catch_phrase, c.bs \
                            from tbl_user u join tbl_address a on u.id = %s and a.id = u.address_id \
                            join tbl_geo g on a.geo_id = g.id \
                            join tbl_company c on c.id = u.company_id"
        find_by_id_params = found_todo.get('user_id'),
        found_info = find_by_id(find_by_id_query, find_by_id_params)
        geo = Geo(**found_info)
        address = Address(geo=geo, **found_info)
        company = Company(**found_info)
        user = User(address=address, company=company, **found_info)
        todo = Todo(user=user, **found_todo)
        todos.append(todo)
    for todo in todos:
        print(todo.__dict__)

    # 할일 1개 조회하기
    find_by_id_query = "select t.*, u.* from tbl_todo t join tbl_user u on t.id = %s and t.user_id = u.id"
    find_by_id_params = 1,
    found_todo = find_by_id(find_by_id_query, find_by_id_params)
    find_by_id_query = "select u.id, u.name, username, email, address_id, phone, website, company_id, a.geo_id, a.id, \
                        a.street, a.suite, a.city, a.zipcode, g.id, g.lat, g.lng, c.id, c.name, c.catch_phrase, c.bs \
                        from tbl_user u join tbl_address a on u.id = %s and a.id = u.address_id \
                        join tbl_geo g on a.geo_id = g.id \
                        join tbl_company c on c.id = u.company_id"
    find_by_id_params = found_todo.get('user_id'),
    found_info = find_by_id(find_by_id_query, find_by_id_params)
    geo = Geo(**found_info)
    address = Address(geo=geo, **found_info)
    company = Company(**found_info)
    user = User(address=address, company=company, **found_info)
    todo = Todo(user=user, **found_todo)
    print(todo.__dict__)

    # 할일 수정하기
    # 수정된 할일 객체라고 가정합니다.
    todo.completed = 1
    update_query = "update tbl_todo set completed = %s where id = %s"
    update_params = todo.completed, todo.id
    # update(update_query, update_params)

    # 할일 삭제하기
    delete_query = "delete from tbl_todo where id = %s"
    delete_params = 1,
    # delete(delete_query, delete_params)