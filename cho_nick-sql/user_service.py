from crud_module import *
from geo import *
from address import *
from company import *
from user import *
from albums import *
from comments import *
from photos import  *
from post import  *
from todos import *


if __name__ == '__main__':
    # geo 찾아오기
    # find_geo_query = 'select * from tbl_geo where id = %s'
    # find_geo_params = 5
    # geo = find_by_id(find_geo_query,find_geo_params)

    # address찾아오기
    # find_address_query = 'select * from tbl_address where id =%s '
    # find_address_params = geo.get('id')
    # address = find_by_id(find_address_query,find_address_params)
    # print(address.get('street'))

    # 회사정보 가져오기
    # find_company_query = 'select * from tbl_company where id =%s'
    # find_company_params = 5
    # company = find_by_id(find_company_query,find_company_params)
    # print(company.get('name'))



    # save_query = 'insert into  tbl_user(name,username,email,phone,website,address_id,company_id)\
    #                values (%s,%s,%s,%s,%s,%s,%s)'
    # save_prams =  ('Chelsey Dietrich','Kamren','Lucio_Hettinger@annie.ca','(254)954-1289','demarco.info',address.get('id'),company.get('id'))
    # save(save_query,save_prams)


    # 마이페이지
    # find_user_query = 'select * from tbl_user where id = %s '
    # find_user_params = 6
    # user = find_by_id(find_user_query,find_user_params)
    # find_company_query = 'select * from tbl_company where id =%s'
    # find_company_params = user.get('company_id')
    # company = find_by_id(find_company_query,find_company_params)
    # find_address_query = 'select * from tbl_address where id =%s '
    # find_address_params = user.get('address_id')
    # address = find_by_id(find_address_query, find_address_params)
    # find_geo_query = 'select * from tbl_geo where id = %s'
    # find_geo_params = address.get('geo_id')
    # geo = find_by_id(find_geo_query, find_geo_params)
    # print(user, company,address,geo)


    # 정보 바꾸기
    new_name = 'cho'
    update_query = 'update tbl_user set name = %s,username = %s ,email= %s, phone= %s, website = %s where id = %s'
    update_params =  [new_name,6]
    # update(update_query, update_params)

    #회원삭제
    delete_query = 'delete from tbl_user where id = %s'
    delete_params = 7
    # delete(delete_query,delete_params)


    # join 쓰기
    # join 사용하여 마이페이지 가기
    find_by_id_query = "select u.id, u.name, username, email, address_id, phone, website, company_id, a.geo_id, a.id, \
                        a.street, a.suite, a.city, a.zipcode, g.id, g.lat, g.lng, c.id, c.name, c.catch_phrase, c.bs \
                        from tbl_user u join tbl_address a on u.id = %s and a.id = u.address_id \
                        join tbl_geo g on a.geo_id = g.id \
                        join tbl_company c on c.id = u.company_id"
    find_by_id_params = 6
    found_info = find_by_id(find_by_id_query, find_by_id_params)
    geo = Geo(**found_info)
    address = Address(geo=geo, **found_info)
    company = Company(**found_info)
    user = User(address=address, company=company, **found_info)
    print(user.__dict__)