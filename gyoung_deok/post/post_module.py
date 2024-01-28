from study_python.gyoung_deok.user.user_module import *
from study_python.gyoung_deok.post.post import Post


def find_by_post_id():
    pass


def find_all_post():
    find_all_query = "select title, body, u.username from tbl_user u \
                      join tbl_post p on u.id = p.user_id"

    return find_all(find_all_query)
