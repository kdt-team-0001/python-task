from study_python.gyoung_deok.user.user_module import *
from study_python.gyoung_deok.album.album import Album
from study_python.gyoung_deok.photo.photo import Photo


if __name__ == '__main__':
    # 사진 추가
    # user_id = 1,
    # user = find_by_user_id(user_id).get("user")
    #
    # find_by_id_query = "select id, title from tbl_album where id = %s and user_id = %s"
    # find_by_id_params = 1, user.id
    # found_album = find_by_id(find_by_id_query, find_by_id_params)
    # album = Album(user=user, **found_album)
    #
    # save_many_query = "insert into tbl_photo(title, url, thumbnail_url, album_id) \
    #                    values (%s, %s, %s, %s)"
    # save_many_params = (
    #     (
    #         "quod culpa hic unde consequuntur est est",
    #         "https://via.placeholder.com/600/e979a4",
    #         "https://via.placeholder.com/150/e979a4",
    #         album.id
    #     ),
    #     (
    #         "delectus in aut",
    #         "https://via.placeholder.com/600/ce7227",
    #         "https://via.placeholder.com/150/ce7227",
    #         album.id
    #     ),
    # )
    # save_many(save_many_query, save_many_params)

    # 사진 목록
    # user_id = 1,
    # user = find_by_user_id(user_id).get("user")
    #
    # find_by_id_query = "select id, title from tbl_album where id = %s and user_id = %s"
    # find_by_id_params = 1, user.id
    # found_album = find_by_id(find_by_id_query, find_by_id_params)
    # album = Album(user=user, **found_album)
    #
    # find_all_by_query = "select p.title, p.url, p.thumbnail_url from tbl_album a join tbl_photo p \
    #                      on a.id = %s and a.id = p.album_id \
    #                      where a.user_id = %s"
    # find_all_by_params = album.id, user.id
    # photos = find_all_by(find_all_by_query, find_all_by_params)
    #
    # for photo in photos:
    #     print(f"사진 제목: {photo.get('title')}\n사진 경로: {photo.get('url')}\n사진 썸네일 경로: {photo.get('thumbnail_url')}\n")

    # 사진 상세보기
    user_id = 1,
    user = find_by_user_id(user_id).get("user")

    find_by_id_query = "select id, title from tbl_album where id = %s and user_id = %s"
    find_by_id_params = 1, user.id
    found_album = find_by_id(find_by_id_query, find_by_id_params)
    album = Album(user=user, **found_album)

    find_by_id_query = "select id, title, url, thumbnail_url from tbl_photo where id = %s and album_id = %s"
    find_by_id_params = 1, album.id
    found_photo = find_by_id(find_by_id_query, find_by_id_params)
    photo = Photo(album=album, **found_photo)
    # print(photo)

    # 사진 수정
    photo.title = "수정된 사진 제목"
    update_query = "update tbl_photo set title = %s where id = %s and album_id = %s"
    update_params = photo.title, 1, album.id
    # update(update_query, update_params)
    # print(find_by_id(find_by_id_query, find_by_id_params))
    # print(photo)

    # 사진 삭제
    delete_query = "delete from tbl_photo where id = %s"
    delete_params = 1,
    # delete(delete_query, delete_params)