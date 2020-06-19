# oracle_test.py

# 오라클 패키지 필요 : cx_Oracle
# (윈도우) pip install cx_Oracle

import cx_Oracle as oci

# 1) 연결객체 얻어오기
conn = oci.connect("scott/tiger@192.168.0.18:1521/orcl")
print(conn)

# 2) 커서 얻어오기 (전송객체 역할)
cursor = conn.cursor()

# 3) sql 문장
sql = "SELECT * FROM emp"

# 4) sql 문장 실행
cursor.execute(sql)

data = cursor.fetchall() # 넘겨주는 것을 다 받음
for row in data:
    print(row[0], ">", row[1])
#print(data)

# 5) 커서 닫기
cursor.close()

# 6) 연결 끊기
conn.close()