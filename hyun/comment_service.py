from crud_module import *
from connection_module import *
from user.geo import *
from user.address import *
from user.company import *
from user.user import *
from post.post import *
from comment.comment import *

if __name__ == '__main__':
    # 우선 댓글 4개만 추가해놓기
    save_many_query = "insert into tbl_comment(post_id, name, email, body) \
                       values(%s, %s, %s, %s)"
    save_many_params = (
        (1, "id labore ex et quam laborum", "Eliseo@gardner.biz", "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"),
        (1, "quo vero reiciendis velit similique earum", "Jayne_Kuhic@sydney.com", "est natus enim nihil est dolore omnis voluptatem numquam\net omnis occaecati quod ullam at\nvoluptatem error expedita pariatur\nnihil sint nostrum voluptatem reiciendis et"),
        (2, "et fugit eligendi deleniti quidem qui sint nihil autem", "Presley.Mueller@myrl.com", "doloribus at sed quis culpa deserunt consectetur qui praesentium\naccusamus fugiat dicta\nvoluptatem rerum ut voluptate autem\nvoluptatem repellendus aspernatur dolorem in"),
        (3, "fugit labore quia mollitia quas deserunt nostrum sunt", "Veronica_Goodwin@timmothy.net", "ut dolorum nostrum id quia aut est\nfuga est inventore vel eligendi explicabo quis consectetur\naut occaecati repellat id natus quo est\nut blanditiis quia ut vel ut maiores ea")
    )
    # save_many(save_many_query, save_many_params)

    # 댓글 작성
    save_query = "insert into tbl_comment(post_id, name, email, body) \
                  values(%s, %s, %s, %s)"
    save_params = 3, "modi ut eos dolores illum nam dolor", "Oswald.Vandervort@leanne.org", "expedita maiores dignissimos facilis\nipsum est rem est fugit velit sequi\neum odio dolores dolor totam\noccaecati ratione eius rem velit"
    # save(save_query, save_params)

    # 게시물 id로 댓글 전체 조회
    # 게시물부터 가져오기
    find_by_id_query = "select p.*, u.*, c.*, a.*, g.* \
                            from tbl_post p join tbl_user u \
                            on p.id = %s and p.user_id = u.id join tbl_company c on u.company_id = c.id \
                            join tbl_address a on u.address_id = a.id join tbl_geo g on a.geo_id = g.id"
    find_by_id_params = 1,
    found_post = find_by_id(find_by_id_query, find_by_id_params)
    post = Post(
        user=User(address=Address(geo=Geo(**found_post), **found_post), company=Company(**found_post), **found_post),
        **found_post)
    # 댓글들 가져오기
    find_all_by_query = "select id, post_id, name, email, body from tbl_comment \
                         where post_id = %s"
    find_all_by_params = 1,
    found_comments = find_all_by(find_all_by_query, find_all_by_params)
    comments = []
    for found_comment in found_comments:
        comment = Comment(post=post, **found_comment)
        comments.append(comment)
    for comment in comments:
        print(comment.__dict__)

    # 댓글 수정
    # 수정된 댓글 객체라고 가정하겠습니다.
    comment = comments[1]
    comment.name = "수정된 댓글 이름1"
    # print(comment.__dict__)

    update_query = "update tbl_comment set name = %s, email = %s, body = %s where id = %s"
    update_params = comment.name, comment.email, comment.body, comment.id
    update(update_query, update_params)

    # 댓글 삭제
    delete_query = "delete from tbl_comment where id = %s"
    delete_params = 1,
    # delete(delete_query, delete_params)

