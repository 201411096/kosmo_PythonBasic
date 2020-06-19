#oracle_csv.py
import csv
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

def insertTable(data):
    conn = oci.connect("scott/tiger@192.168.0.18:1521/orcl")
    cursor = conn.cursor()
    sql = """
    INSERT INTO supply
    (id, Supplier_Name, Invoice_Number, Part_Number, Cost, Purchase_Date)
    VALUES(seq_supply_id.nextval, :v_name, :v_invoice, :v_part, :v_cost, :v_date)
    """
    v_name = data[0]
    v_invoice = data[1]
    v_part = data[2]
    v_cost = data[3]
    v_date = data[4]
    cursor.execute(sql, (v_name, v_invoice, v_part, v_cost, v_date)) # :0,:1,:2,:3,:4 에 해당하는 데이터를 넣음
    cursor.close()
    conn.commit()  # commit 필요
    conn.close()

def viewTable(table):
    conn = oci.connect("scott/tiger@192.168.0.18:1521/orcl")
    cursor = conn.cursor()
    sql = "SELECT * FROM {}".format(table)
    cursor.execute(sql)
    datas = cursor.fetchall() # 데이터를 전부 다 받음
    for row in datas:
        print(row)
    cursor.close()
    conn.close()
if __name__ == "__main__":  # 이부분은 이 파일을 실행할 경우에만 실행되는 부분임
    # (1) db에 테이블 생성
    #createTable()
    # (2) csv 읽어서 DB에 입력
    # file_name = "../files/supply.csv"
    # file = open(file_name, 'r')
    # datas = csv.reader(file, delimiter=',') # ,를 기준으로 데이터를 자름
    # header = next(datas, None)  # 컬럼들을 뽑아옴
    # print(header)
    # print("-"*50)
    # 
    # for row in datas:
    #     print(row)
    #     print("a")
    #     insertTable(row)
    
    # (3) db 값을 가져와서 보여주기
    viewTable('supply')