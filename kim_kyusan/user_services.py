from a_mac.study_python.kim_kyusan.user.geo import *
from a_mac.study_python.kim_kyusan.user.company import *
from a_mac.study_python.kim_kyusan.user.address import *
from crud_module import *

if __name__ == '__main__':
# 사용자 아이디 등록
# 1. 위치, 주소, 회사의 값을 선행 확인 후 생성이 가능

    # 위치 정보 가져오기
    find_by_id_qeury= "select id, lat, lng from tbl_geo where id = %s"
    find_by_id_params= 1,
    find_geo = find_by_id(find_by_id_qeury, find_by_id_params)
    geo = Geo(**find_geo)
    find_all_by_query ="select id, lat, lng from tbl_geo"
    find_all_by_params = []
    find_all_geo = find_all_by(find_all_by_query,find_all_by_params)

    # 주소 아이디 찾기
    find_by_id_qeury = "select a.id, a.street, a.suite, a.city, a.zipcode from tbl_address a, tbl_geo g \
                        where a.geo_id = g.id and g.id = %s"
    find_by_id_params = find_geo.get('id')
    find_address = find_by_id(find_by_id_qeury, find_by_id_params)
    address = Address(**find_address)

    find_all_by_query = "select a.id, a.street, a.suite, a.city, a.zipcode, g.lat, g.lng from tbl_address a, tbl_geo g \
                        where a.geo_id = g.id "
    find_all_by_params = []
    find_all_address = find_all_by(find_all_by_query,find_all_by_params)


    # 회사 아이디 찾기
    find_by_id_qeury = "select name, catch_phrase, bs from tbl_company where id = %s"
    find_by_id_params = 1,
    find_company = find_by_id(find_by_id_qeury, find_by_id_params)
    company = Company(**find_company)
    find_all_by_query = "select name, catch_phrase, bs from tbl_company"
    find_all_by_params = []
    find_all_company = find_all_by(find_all_by_query,find_all_by_params)


    # 사용자 추가
    save_query = "insert into tbl_user (name, username, email, phone, website, address_id, company_id) \
                   values(%s, %s, %s, %s, %s, %s, %s)"
    save_many_params = (
        ("Leanne Graham", "Bret", "Sincere@april.biz", '1-770-736-8031 x56442', 'hildegard.org',2,2),
        ("Ervin Howell", "Antonette","Shanna@melissa.tv","010-692-6593 x09125","anastasia.net",1,1 ),
        ("Clementine Bauch", "Samantha", "Nathan@yesenia.net", "1-463-123-4447", "ramiro.info", find_address.get('id'), find_address.get('id')),
        ("Patricia Lebsack","Karianne","Julianne.OConner@kory.org", "493-170-9623 x156","kale.biz",4,4),
        ("Chelsey Dietrich", "Kamren","Lucio_Hettinger@annie.ca","(254)954-1289","demarco.info",5,5)
    )
    # save_many(save_query, save_many_params)


    # 사용자 전체 정보 출력
    find_all_by_query = "select uc.name, uc.username, uc.email, uc.phone, uc.website, uc.c_name,uc.catch_phrase, uc.bs, \
                        ag.street, ag.suite, ag.city, ag.zipcode, ag.lng, ag.lat \
                        from \
                        (select u.id, u.name, u.username, u.email, u.phone,u.website,u.address_id, c.name as c_name, c.catch_phrase, c.bs \
                        from tbl_user u join tbl_company c \
                        on u.company_id = c.id) uc join \
                        (select a.id,g.lat, g.lng, a.street, a.suite, a.city, a.zipcode from tbl_geo g join tbl_address a \
                        on a.geo_id = g.id) ag \
                        on uc.address_id = ag.id"
    find_all_by_param= []
    users = find_all_by(find_all_by_query,find_all_by_param)
    # for user in users:
        # print(user)

    #사용자 업데이트
    # 1. 사용자 계정 유무 체크
    choice_update_service = int(input("변경할 정보 입력 \n 1. phone, 2. address\n 숫자를 입력하세요"))
    check_user_email = input("이메일을 입력하세요: ")
    find_by_id_query = "select u.id, u.address_id from tbl_user u, tbl_address a where u.address_id= a.id and u.email = %s"
    find_by_id_params = check_user_email
    user_info = find_by_id(find_by_id_query,find_by_id_params)
    # print(user_info)

    if user_info is not None:
        if choice_update_service == 1:
            update_phone = input("변경하고 싶은 핸드폰 번호를 입력하세요: ")
            update_query = "update tbl_user set phone = %s where id = %s"
            update_params = update_phone, user_info.get("id")
            # update(update_query,update_params)

        elif choice_update_service == 2:
            update_address_city = input("변경하고 싶은 주소(도시)를 입력하세요: ")
            update_query = "update tbl_address set city = %s where id = %s"
            update_params = update_address_city, user_info.get("address_id")
            # update(update_query, update_params)
        else:
            print("잘못된 숫자를 입력하였습니다")
    else:
        print("없는 이메일 입니다.")

    # 사용자 삭제
    # 1. 사용자 계정 있을 때만 삭제
    if user_info is not None:
        delete_query = "delete from tbl_user where email = %s"
        delete_params = user_info.get("email")
        # delete(delete_query, delete_params)
    else:
        print("없는 이메일 입니다.")




