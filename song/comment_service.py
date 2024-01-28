from user import *
from post import *
from comment import *
from crud_module import *

# post_id, id, name, email, body

if __name__ == '__main__':
    # 댓글 정보
    save_many_query = "insert into tbl_comment (post_id, name, email, body) \
                    values (%s, %s, %s, %s)"
    save_many_params = (
        (1, 'id labore ex et quam laborum', 'Eliseo@gardner.biz', 'laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium'),
        (1, 'quo vero reiciendis velit similique earum', 'Jayne_Kuhic@sydney.com', 'est natus enim nihil est dolore omnis voluptatem numquam\net omnis occaecati quod ullam at\nvoluptatem error expedita pariatur\nnihil sint nostrum voluptatem reiciendis et'),
        (1, 'odio adipisci rerum aut animi', 'Nikita@garfield.biz', 'quia molestiae reprehenderit quasi aspernatur\naut expedita occaecati aliquam eveniet laudantium\nomnis quibusdam delectus saepe quia accusamus maiores nam est\ncum et ducimus et vero voluptates excepturi deleniti ratione'),
        (1, 'alias odio sit', 'Lew@alysha.tv', 'non et atque\noccaecati deserunt quas accusantium unde odit nobis qui voluptatem\nquia voluptas consequuntur itaque dolor\net qui rerum deleniti ut occaecati')
    )
    # save_many(save_many_query, save_many_params)

    # 댓글 추가
    comment = Comment(post_id=1, name='vero eaque aliquid doloribus et culpa', email='Hayden@althea.biz', body='harum non quasi et ratione\ntempore iure ex voluptates in ratione\nharum architecto fugit inventore cupiditate\nvoluptates magni quo et')
    save_query = "insert into tbl_comment (post_id, name, email, body) \
                    values (%s, %s, %s, %s)"
    save_params = (comment.post_id, comment.name, comment.email, comment.body)
    # save(save_query, save_params)


    # 댓글 조회
    find_all_query = "select post_id, id, name, email, body from tbl_comment"
    found_comments = find_all(find_all_query)
    print(found_comments)

    # 유저별 댓글 조회
    find_by_id_query = "select post_id, id, name, email, body from tbl_comment where id = %s"
    find_by_id_params = 1,
    found_comment = find_by_id(find_by_id_query, find_by_id_params)
    print(found_comment)

    # 댓글 수정
    update_query = "update from tbl_comment set body = 'test body' where id = %s"
    update_params = 1,
    # update(update_query, update_params)

    # 댓글 삭제
    delete_query = "delete from tbl_comment where id = %s"
    delete_params = 1,
    # delete(delete_query, delete_params)