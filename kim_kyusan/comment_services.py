from crud_module import *
from comment.comment import *

# comment 생성
find_by_id_query = "select id from tbl_post where title = %s "
find_by_id_params ="sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
post_list = find_by_id(find_by_id_query, find_by_id_params)
# print(post_list)

save_many_query = "insert into tbl_comment (post_id, name, email, body) values (%s, %s, %s, %s)"
save_many_params = (
    (post_list.get("id"),"id labore ex et quam laborum", "Eliseo@gardner.biz", "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"),
    (post_list.get("id"), "quo vero reiciendis velit similique earum","Jayne_Kuhic@sydney.com", "est natus enim nihil est dolore omnis voluptatem numquam\net omnis occaecati quod ullam at\nvoluptatem error expedita pariatur\nnihil sint nostrum voluptatem reiciendis et"),
    (post_list.get("id"), "odio adipisci rerum aut animi","Nikita@garfield.biz", "quia molestiae reprehenderit quasi aspernatur\naut expedita occaecati aliquam eveniet laudantium\nomnis quibusdam delectus saepe quia accusamus maiores nam est\ncum et ducimus et vero voluptates excepturi deleniti ratione"),
    (post_list.get("id"), "alias odio sit","Lew@alysha.tv", "non et atque\noccaecati deserunt quas accusantium unde odit nobis qui voluptatem\nquia voluptas consequuntur itaque dolor\net qui rerum deleniti ut occaecati"),
    (post_list.get("id"), "vero eaque aliquid doloribus et culpa","Hayden@althea.biz","harum non quasi et ratione\ntempore iure ex voluptates in ratione\nharum architecto fugit inventore cupiditate\nvoluptates magni quo et")
)
# save_many(save_many_query, save_many_params)

# comment 조회
find_all_query = "select *from tbl_comment"
find_all_params = []
comment_list = find_all(find_all_query)
# for comment in comment_list:
#     print(comment)

# comment 항목 1개 조회
find_by_id_query = "select  p.title as title, name, email, c.body as body from tbl_post p join tbl_comment c on c.post_id = p.id and c.id= %s"
find_by_id_params = 1,
comment_one_list = find_by_id(find_by_id_query, find_by_id_params)
comment_one = Comment(**comment_one_list)
print(comment_one.__dict__)


# comment 항목 중 name 수정
if post_list is not None:
    new_name = input("새로운 이름을 입력하세요: ")
    update_qeury = "update tbl_comment set name = %s where post_id = %s and email = %s"
    update_params = new_name, post_list.get("id"), "Eliseo@gardner.biz"
else:
    print("해당 post는 없습니다.")

# comment 삭제
if post_list is not None:
    delete_query = "delete from tbl_comment where email = %s and name = %s"
    delete_params = "Eliseo@gardner.biz", "id labore ex et quam laborum"
    # delete(delete_query, delete_params)