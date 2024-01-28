from study_python.gyoung_deok.post.post_module import *
from study_python.gyoung_deok.post.post import Post

if __name__ == '__main__':
    # post 작성하기
    find_by_user_id_params = 1,
    user = find_by_user_id(find_by_user_id_params).get("user")

    post = Post(
        id=1, title='sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
        body="quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto",
        user=user
    )

    save_query = "insert into tbl_post(id, title, body, user_id) values(%s, %s, %s, %s)"
    save_params = (post.id, post.title, post.body, post.user.get("id"))
    # save(save_query, save_params)

    # post 목록보기
    find_all_query = "select title, body, u.username from tbl_user u \
                      join tbl_post p on u.id = p.user_id"
    posts = find_all(find_all_query)
    # for post in posts:
    #     print(f"제목: {post.get('title')},\n내용: {post.get('body')},\n작성자: {post.get('username')}\n")

    # post 상세보기
    post_id = 1,
    post = find_by_post_id(post_id)
    # print(post)

    # post 수정하기
    # 로그인 되어있는 회원의 정보 조회
    find_by_user_id_params = 1,
    user = find_by_user_id(find_by_user_id_params).get("user")

    post.title = '수정된 제목'
    post.body = post.body
    update_query = "update tbl_post \
                    set title = %s, body =%s \
                    where id = %s and user_id = %s"
    update_params = (post.title, post.body, post.id, user.id)
    # update(update_query, update_params)
    #
    find_by_id_query = "select id, title, body, user_id from tbl_post where id = %s"
    # print(find_by_id(find_by_id_query,post.id))
    # print(post)

    # post 삭제하기
    find_by_user_id_params = 1,
    user = find_by_user_id(find_by_user_id_params).get("user")

    delete_query = "delete from tbl_post where id = %s and user_id = %s"
    delete_params = (post.id, user.id)
    # delete(delete_query, delete_params)
