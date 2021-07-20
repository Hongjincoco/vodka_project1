from http import HTTPStatus

import sys
sys.path.insert(0, 'tourists/db')
# 1. DB커넥션 가져오기 
from db import get_mysql_connection



def database_update():
    print("--data update--")
    connection = get_mysql_connection()
    print('커넥트 성공')
    # 2. 커서 
    cursor = connection.cursor(dictionary =True)
    print('커서연결')
    # 3. 쿼리문
    query =""" SELECT * FROM A
                order by time desc
                limit 1; """
    # 4. sql 실행
    cursor.execute(query)

    # 5. 데이터를 패치한다.
    records = cursor.fetchall()

    # print(records)


    # 6. 커서와 커넥션을 닫아 준다.
    cursor.close()
    connection.close()
    return records
# # 7. 클라이언트에 리스판스 한다.
# print({'count':len(ret), 'ret':ret})