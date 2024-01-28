from album import *
from photo import *
from crud_module import *

# 포토 생성
find_by_id_qeury = "select *from tbl_album where id = %s"
find_by_id_params = 1,
album_list = find_by_id(find_by_id_qeury, find_by_id_params)

save_many_query = "insert into tbl_photo (album_id, title, url, thumbnail_url) values (%s, %s, %s, %s)"
save_many__params = (
    (1,"accusamus beatae ad facilis cum similique qui sunt","https://via.placeholder.com/600/92c952", "https://via.placeholder.com/150/92c952"),
    (1,"reprehenderit est deserunt velit ipsam", "https://via.placeholder.com/600/771796", "https://via.placeholder.com/150/771796"),
    (1,"officia porro iure quia iusto qui ipsa ut modi","https://via.placeholder.com/600/24f355","https://via.placeholder.com/150/24f355"),
    (1,"culpa odio esse rerum omnis laboriosam voluptate repudiandae", "https://via.placeholder.com/600/d32776","https://via.placeholder.com/150/d32776"),
    (1,"natus nisi omnis corporis facere molestiae rerum in","https://via.placeholder.com/600/f66b97", "https://via.placeholder.com/150/f66b97"),
)
save_many


# 포토 조회
# 포토 타이틀 수정
# 포토 삭제
