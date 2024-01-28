from post_module import *
from post import Post

if __name__ == '__main__':
    # post 작성하기
    find_by_user_id_params = 5,
    user = find_by_user_id(find_by_user_id_params)[3]
    post = Post(
        41,
        "non est facere",
        "molestias id nostrum\nexcepturi molestiae dolore omnis repellendus quaerat saepe\nconsectetur iste quaerat tenetur asperiores accusamus ex ut\nnam quidem est ducimus sunt debitis saepe",
        user.__dict__
    )
    save_query = "insert into tbl_post(id, title, body, user_id) values(%s, %s, %s, %s)"
    save_params = (post.id, post.title, post.body, post.user.get("id"))
    # save(save_query, save_params)

    # post 목록보기
    # posts = find_all_post()
    # for post in posts:
    #     print(f"제목: {post.get('title')},\n내용: {post.get('body')},\n작성자: {post.get('username')}\n")

    # post 상세보기


    # post 수정하기
    # post 삭제하기
