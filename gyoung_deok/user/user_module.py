from study_python.gyoung_deok.crud_module import *
from study_python.gyoung_deok.user.geo import Geo
from study_python.gyoung_deok.user.address import Address
from study_python.gyoung_deok.user.company import Company
from study_python.gyoung_deok.user.user import User


def find_by_user_id(params):
    find_by_id_query = "select u.id, u.name, u.username, u.email, u.phone, u.website, u.address_id, u.company_id, \
                        c.name, c.catch_phrase, c.bs, a.street, a.suite, a.city, a.zipcode, a.geo_id, g.lat, g.lng\
                        from tbl_company c join tbl_user u \
                        on u.id = %s and c.id = u.company_id \
                        join tbl_address a on a.id = u.address_id \
                        join tbl_geo g on g.id = a.geo_id"
    found_user = find_by_id(find_by_id_query, params)

    geo = Geo(
        id=found_user.get("geo_id"),
        lat=found_user.get("lat"),
        lng=found_user.get("lng")
    )

    address = Address(
        id=found_user.get("address_id"),
        street=found_user.get("street"),
        suite=found_user.get("suite"),
        city=found_user.get("city"),
        zipcode=found_user.get("zipcode"),
        geo=geo.__dict__
    )

    company = Company(
        id=found_user.get("company_id"),
        name=found_user.get("c.name"),
        catch_phrase=found_user.get("catch_phrase"),
        bs=found_user.get("bs")
    )

    user = User(
        id=found_user.get("id"),
        name=found_user.get("name"),
        username=found_user.get("username"),
        email=found_user.get("email"),
        phone=found_user.get("phone"),
        website=found_user.get("website"),
        address=address.__dict__,
        company=company.__dict__
    )

    return geo, address, company, user
