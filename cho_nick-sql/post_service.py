from crud_module import *
from connertion_module import *
from post import *
from comments import *

if __name__ == '__main__':

    # post 추가하기
    save_post_query = "insert into tbl_post( title, body,user_id) \
                       values (%s, %s, %s)"
    save_post_params =("est et quae odit qui non", "similique esse doloribus nihil accusamus\nomnis dolorem fuga consequuntur reprehenderit fugit recusandae temporibus\nperspiciatis cum ut laudantium\nomnis aut molestiae vel vero",3)
    save(save_post_query,save_post_params)

    # post title로 조회하기

    find_post_title_query = "select * from tbl_post where title = %s"
    find_post_title_params =("nesciunt quas odio")
    find_post_title_list = find_by_id(find_post_title_query,find_post_title_params)
    # print(find_post_title_list)

    # post user_id 별로 조회하기
    find_post_user_id_query = "select * from tbl_post where user_id = %s"
    find_post_user_id_params = 6
    find_post_user_id_list = find_all_by(find_post_user_id_query,find_post_user_id_params)
    # print(find_post_user_id_list)

    #post에서 title 을 입력하면 comments에서 사용한 애들 다 출력
    find_post_comment_query = ("select  c.* from tbl_post p join tbl_comments c where\
                                 c.post_id = p.id and p.title = %s")
    find_post_comment_params = ('sunt aut facere repellat provident occaecati excepturi optio reprehenderit')
    find_post_comment_list = find_all_by(find_post_comment_query,find_post_comment_params)
    print(find_post_comment_list)




    # post body 수정하기
    new_body = '새로운 내용!'
    chacnge_id = 5
    update_post_body_query = "update tbl_post set body = %s where id =%s"
    update_post_body_params = (new_body,chacnge_id)
    # update(update_post_body_query,update_post_body_params)

    # post 삭제하기
    delete_post_query = "delete from tbl_post where id =%s"
    delete_post_params = 7
    # delete(delete_post_query,delete_post_params)