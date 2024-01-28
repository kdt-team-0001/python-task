import pymysql
from pymysql.cursors import Cursor


def connect():
    conn = pymysql.connect(host='13.124.193.4', user='mysql', password='1234', db='test', charset='utf8', autocommit=True)
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    return conn, cursor


def execute(crud):
    result = None

    def manage(*args):
        nonlocal result
        # conn 은 파이썬이랑연결된 각종 정보들을 담고있음 cursor는 진짜 모르겠음...
        conn, cursor = connect()
        try:

            #            cursor ???? // args는 query , params 를 받아주고
            result = crud(cursor, *args)
            #  connect열어서 commit 해줍니다
            conn.commit()
        # 만약 실페하게 된다면 connect에서 rollback 해서 마지막 저장한 commit으로 간다.
        #  Exception은 대표적인 예외처리 방법, 이거를 alias로 e에 담아둠
        except Exception as e:
            print(e.__str__())
            conn.rollback()
        #  뭔일이 있더라도 열린문은 닫아주고 1.2 순으로 열었으니 2.1 순으로 닫는다.
        finally:
            cursor.close()
            conn.close()

        return result

    return manage
