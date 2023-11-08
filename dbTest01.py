import pymysql

# 1) DB가 설치된 컴퓨터의 IP주소(내 컴퓨터에 DB가 설치되어있으면 localhost)
# 2) DB의 계정 root(실무에서는 ID나 비번 알려줌)
# 3) DB의 비밀번호 12345
# 4) DB의 이름(ex:testdb)

conn = pymysql.connect(host="localhost", user="root", password="12345", db="testdb")
# DB와의 커넥션 생성

sql = "SELECT * FROM member"

cur = conn.cursor()

cur.execute(sql) # SQL문 실행

# row = cur.fetchone() # 레코드 중의 첫줄이 튜플구조로 반환됨
#
# print(row)

rows = cur.fetchall() # 해당 테이블의 모든 레코드가 튜플구조로 반환됨

print(rows)

print(rows[1])

cur.close()