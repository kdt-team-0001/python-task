from study_python.gyoung_deok.post.post_module import *
from study_python.gyoung_deok.comment.comment import Comment

if __name__ == '__main__':
    # 게시글 정보
    # post_id = 1,
    # post = find_by_post_id(post_id)
    # print(post)

    # 댓글 추가
    # save_many_query = "insert into tbl_comment(name, email, body, post_id) \
    #               values (%s, %s, %s, %s)"
    # save_many_params = (
    #     (
    #         "et adipisci aliquam a aperiam ut soluta",
    #         "Cleve@royal.us",
    #         "est officiis placeat\nid et iusto ut fugit numquam\neos aut voluptas ad quia tempore qui quibusdam doloremque\nrecusandae tempora qui",
    #         post.id
    #     ),
    #     (
    #         "blanditiis vel fuga odio qui",
    #         "Donnell@polly.net",
    #         "sequi expedita quibusdam enim ipsam\nbeatae ad eum placeat\nperspiciatis quis in nulla porro voluptas quia\nesse et quibusdam",
    #         post.id
    #     )
    # )
    # save_many(save_many_query, save_many_params)

    # 댓글 목록
    # post_id = 1,
    # post = find_by_post_id(post_id)
    #
    # find_by_all_query = "select id, name, email, body, post_id from tbl_comment where post_id = %s"
    # find_by_all_params = post.id,
    # comments = find_all_by(find_by_all_query, find_by_all_params)
    #
    # for comment in comments:
    #     print(f"게시글 번호: {comment.get('post_id')},\n작성자 이름: {comment.get('name')},\n작성자 이메일: {comment.get('email')},\n댓글 내용: {comment.get('body')}\n")

    # 댓글 수정
    post_id = 1,
    post = find_by_post_id(post_id)
    # 댓글 정보
    find_by_id_query = "select id, name, email, body from tbl_comment where id = %s"
    find_by_id_params = 2,
    found_comment = find_by_id(find_by_id_query, find_by_id_params)
    comment = Comment(post=post, **found_comment)

    # 댓글 작성자만 수정 가능
    comment.email = 'Eliseo@gardner.biz' # comment.email
    comment.name = '수정된 이름'# comment.name
    comment.body = comment.body

    update_query = "update tbl_comment set name = %s, body = %s where id = %s and email = %s"
    update_params = comment.name, comment.body, comment.id, comment.email

    # update(update_query, update_params)
    # print(find_by_id(find_by_id_query, find_by_id_params))
    # print(comment)


    # 댓글 삭제
    delete_query = "delete from tbl_comment where id = %s and email = %s"
    delete_params = 1, comment.email

    # delete(delete_query, delete_params)
