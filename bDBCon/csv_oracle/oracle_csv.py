#oracle_csv.py

import cx_Oracle as oci

def createTable():
    # 1. 연결객체 얻어오기
    conn = oci.connect("scott/tiger@192.168.0.18:1521/orcl")
    # 2. 커서 얻어오기
    cursor = conn.cursor()
    # 3. sql 문장
    # csv의 column 내용과 맞추면서 공백은 "_"로 맞춰야됨 
    sql = """
        CREATE TABLE supply(
            id  integer     primary key,
            Supplier_Name   varchar2(30),
            Invoice_Number  varchar2(30),
            Part_Number     varchar2(30),
            Cost            integer,
            Purchase_Date   date
        )
    """
    # 4. sql 실행
    cursor.execute(sql)
    
    # 시퀀스 생성하는 sql 만들어서 실행
    sql2 = "CREATE SEQUENCE seq_supply_id"
    cursor.execute(sql2)

    # 5. 커서 닫기
    cursor.close()
    # 6. 연결 닫기
    conn.close()

if __name__ == "__main__":  # 이부분은 이 파일을 실행할 경우에만 실행되는 부분임
    createTable()
    