from study_python.gyoung_deok.user.user_module import *
from study_python.gyoung_deok.album.album import Album


if __name__ == '__main__':
    # 엘범 추가
    # 회원 정보 가져오기
    user_id = 1,
    user = find_by_user_id(user_id).get("user")

    save_many_query = "insert into tbl_album(title, user_id) \
                       values(%s, %s)"
    save_many_params = (
        ("ea voluptates maiores eos accusantium officiis tempore mollitia consequatur", user.id),
        ("tenetur explicabo ea", user.id)
    )
    # save_many(save_many_query, save_many_params)

    # 엘범 목록(엘범 안의 사진 개수도 함께)
    # find_all_by_query = "select distinct a.title, ifnull(count(p.id), 0) photo_count from tbl_album a\
    #                      left outer join tbl_photo p on a.id = p.album_id \
    #                      where a.user_id = %s \
    #                      group by a.id"
    # find_all_by_params = 1,
    # albums = find_all_by(find_all_by_query, find_all_by_params)
    #
    # for album in albums:
    #     print(f"엘범 제목: {album.get('title')}\n사진 개수: {album.get('photo_count')}")

    # 엘범 상세보기
    find_by_id_query = "select id, title from tbl_album where id = %s and user_id = %s"
    find_by_id_params = 1, user.id
    found_album = find_by_id(find_by_id_query, find_by_id_params)
    album = Album(user=user, **found_album)

    # 엘범 수정
    album.title = "수정된 엘범 제목"
    update_query = "update tbl_album set title = %s where id = %s and user_id = %s"
    update_params = album.title, 1, user.id
    # update(update_query, update_params)
    # print(find_by_id(find_by_id_query, find_by_id_params))
    # print(album)

    # 엘범 삭제
    delete_query = "delete from tbl_album where id = %s"
    delete_params = 1,
    # delete(delete_query, delete_params)
