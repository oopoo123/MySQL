# 1) DB가 설치된 컴퓨터의 IP주소(내 컴퓨터에 DB가 설치되어있으면 localhost)
# 2) DB의 계정 root(실무에서는 ID나 비번 알려줌)
# 3) DB의 비밀번호 12345
# 4) DB(스키마)의 이름(ex:testdb)

import pymysql

conn = pymysql.connect(host='localhost', user='root', password='12345', db='memberdb')
# DB와 파이썬파일 사이의 연결통로가 생성

sql = "SELECT * FROM member"
# sql문 생성하여 문자열로 저장
#sql = "INSERT INTO member VALUES('blackcat', '12345', '박영길', '010-8899-9988', '경기도 안산시', 61)"
# 데이터 베이스에 추가

cur = conn.cursor() # 커서 생성
cur.execute(sql) # SQL문 실행

result = cur.fetchall()

for member in result:
    print(member[2]) # 회원들의 이름만 출력

cur.close()
conn.commit() # insert, delete, update sql문을 사용한 경우에는 commit을 반드시 해줘야 함!
conn.close()



