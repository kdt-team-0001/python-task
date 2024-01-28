from user import *
from post import *
from comment import *
from crud_module import *

# user_id, id, title, body

if __name__ == '__main__':
    # 게시글 추가
    save_many_query = "insert into tbl_post (user_id, title, body) values (%s, %s, %s)"
    save_many_params = (
        (1, 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'),
        (1, 'qui est esse', 'est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla'),
        (1, 'ea molestias quasi exercitationem repellat qui ipsa sit aut', 'et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut'),
        (1, 'eum et est occaecati', 'ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit')
    )
    # save_many(save_many_query, save_many_params)

    # 게시글 작성
    post_add = Post(user_id=1, title='nesciunt quas odio', body='repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque')
    save_query = "insert into tbl_post (user_id, title, body) values (%s, %s, %s)"
    save_params = (post_add.user_id, post_add.title, post_add.body)
    # save(save_query, save_params)

    # 게시글 목록
    find_all_query = "select user_id, id, title from post"
    post_list = find_all(find_all_query)
    print(post_list)

    # 게시글 조회
    find_by_id_query = "select p.user_id, p.id, p.title, p.body, \
                        c.post_id, c.id, c.name, c.email, c.body \
                        from tbl_post p join tbl_comment c \
                        on p.id = c.post_id and p.id = %s"
    find_by_id_params = 1,
    found_post = find_by_id(find_by_id_query, find_by_id_params)
    comment = Comment(**found_post)
    post = Post(comment=comment, **found_post)
    print(post)

    # 게시글 조회
    find_by_id_query = "select user_id, id, title, body \
                        from post \
                        where id %s"
    find_by_id_params = 1,
    post = find_by_id(find_by_id_query, find_by_id_params)
    print(post)

    # 게시글 수정
    update_query = "update from tbl_post \
                    set title = 'test title' \
                    where id = %s"
    update_params = 1,
    # update(update_query, update_params)


    # 게시글 삭제
    delete_query = "delete from tbl_post where id = %s"
    delete_params = 1,
    # delete(delete_query, delete_params)
