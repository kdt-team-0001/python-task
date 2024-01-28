from study_python.gyoung_deok.user.user_module import *
from study_python.gyoung_deok.post.post import Post


def find_by_post_id(params):
    find_by_id_query = "select id, title, body, user_id from tbl_post where id = %s"
    found_post = find_by_id(find_by_id_query, params)

    user_id = found_post.get('user_id')
    user = find_by_user_id(user_id).get('user')
    post = Post(user=user, **found_post)

    return post
