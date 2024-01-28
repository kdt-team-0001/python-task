from crud_module import *
from connection_module import *
from user.geo import *
from user.address import *
from user.company import *
from user.user import *
from post.post import *

if __name__ == '__main__':
    # 게시물 우선 4개 추가해놓고 시작
    save_many_query = "insert into tbl_post(user_id, title, body) \
                  values (%s, %s, %s)"
    save_many_params = (
        (2, "sunt aut facere repellat provident occaecati excepturi optio reprehenderit", "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"),
        (2, "qui est esse", "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"),
        (3, "et ea vero quia laudantium autem", "delectus reiciendis molestiae occaecati non minima eveniet qui voluptatibus\naccusamus in eum beatae sit\nvel qui neque voluptates ut commodi qui incidunt\nut animi commodi"),
        (4, "qui explicabo molestiae dolorem", "rerum ut et numquam laborum odit est sit\nid qui sint in\nquasi tenetur tempore aperiam et quaerat qui in\nrerum officiis sequi cumque quod")
    )
    # save_many(save_many_query, save_many_params)

    # 게시물 작성
    save_query = "insert into tbl_post(user_id, title, body) \
                  values (%s, %s, %s)"
    save_params = 3, "est et quae odit qui non", "similique esse doloribus nihil accusamus\nomnis dolorem fuga consequuntur reprehenderit fugit recusandae temporibus\nperspiciatis cum ut laudantium\nomnis aut molestiae vel vero"
    # save(save_query, save_params)

    # 게시물 및 유저 정보 전체 조회
    find_all_query = "select p.*, u.*, c.*, a.*, g.* \
                      from tbl_post p join tbl_user u \
                      on p.user_id = u.id join tbl_company c on u.company_id = c.id \
                      join tbl_address a on u.address_id = a.id join tbl_geo g on a.geo_id = g.id"
    found_posts = find_all(find_all_query)
    posts = []
    for found_post in found_posts:
        post = Post(user=User(address=Address(geo=Geo(**found_post), **found_post), company=Company(**found_post), **found_post), **found_post)
        posts.append(post)
    # for post in posts:
    #     print(post.__dict__)

    # 게시물 1개 조회
    find_by_id_query = "select p.*, u.*, c.*, a.*, g.* \
                        from tbl_post p join tbl_user u \
                        on p.id = %s and p.user_id = u.id join tbl_company c on u.company_id = c.id \
                        join tbl_address a on u.address_id = a.id join tbl_geo g on a.geo_id = g.id"
    find_by_id_params = 1,
    found_post = find_by_id(find_by_id_query, find_by_id_params)
    post = Post(user=User(address=Address(geo=Geo(**found_post), **found_post), company=Company(**found_post), **found_post), **found_post)
    # print(post.__dict__)

    # 게시물 수정
    # 수정한 객체를 받았다고 가정합니다.
    post = posts[3]
    post.title = "수정된 제목"

    update_query = "update tbl_post set title = %s, body = %s where id = %s"
    update_params = post.title, post.body, post.id
    # update(update_query, update_params)

    # 게시물 삭제
    delete_query = "delete from tbl_post where id = %s"
    delete_params = 1,
    # delete(delete_query, delete_params)

