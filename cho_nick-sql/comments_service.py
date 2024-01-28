from crud_module import *
from connertion_module import *
from comments import *
from post import *

if __name__ == '__main__':

    # comment 작성하기
    save_comment_query = "insert into tbl_comments( name, email, body,post_id) \
                           values(%s, %s, %s, %s)"
    save_comment_params = ("modi ut eos dolores illum nam dolor","Oswald.Vandervort@leanne.org", "expedita maiores dignissimos facilis\nipsum est rem est fugit velit sequi\neum odio dolores dolor totam\noccaecati ratione eius rem velit",2)
    # save(save_comment_query,save_comment_params)

    # 이메일을 통해서 comment 확인하기
    find_email_comment_query = "select * from tbl_comments where email = %s"
    find_email_comment_params = ("Eliseo@gardner.biz")
    find_email_comment_params_list = find_by_id(find_email_comment_query,find_email_comment_params)
    # print(find_email_comment_params_list)

    # post_id 별로 comment 확인하기
    find_post_id_comment_query = "select * from tbl_comments where post_id = %s"
    find_post_id_comment_params = 2
    find_post_id_comment_params_list = find_all_by(find_post_id_comment_query,find_post_id_comment_params)
    # print(find_post_id_comment_params_list)

    # comments 에서 name 입력하면 그에 맞는 post title,body 뽑기
    find_comments_post_query = ("select p.title,p.body from tbl_comments c join test.tbl_post p where\
                                 c.post_id = p.id and c.name = %s")
    find_comments_post_params = ('id labore ex et quam laborum')
    find_comments_post_list = find_all_by(find_comments_post_query,find_comments_post_params)
    print(find_comments_post_list)


    # comment 중 body 수정하기
    new_body = '새로운 내용!'
    change_id = 1
    update_comment_body_query = "update tbl_comments set body = %s where id = %s "
    update_comment_body_params = (new_body,change_id)
    # update(update_comment_body_query,update_comment_body_params)

    # comment 삭제하기
    delete_comment_query = "delete from tbl_comments where id = %s"
    delete_comment_params = 6
    # delete(delete_comment_query,delete_comment_params)