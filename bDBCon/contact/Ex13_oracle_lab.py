"""
0. DB에 저장할 테이블 생성
1. Contact 클래스 생성하고 출력 확인
2. 사용자 입력 받아 확인
3. 메인메뉴 구성
4. 연락처 입력 받기
5. 연락처 출력하기
6. 연락처 삭제하기
"""
import cx_Oracle as oci

class Contact:
    def __init__(self, name, phone_number, email, addr):
        self.name=name
        self.phone_name=phone_number
        self.email=email
        self.addr=addr

    def print_info(self):
        print("이름:", self.name)
        print("전화번호:", self.phone_name)
        print("이메일:", self.email)
        print("주소;", self.addr)

def print_menu():
    print('1. 연락처 입력')
    print('2. 연락처 출력')
    print('3. 연락처 삭제')
    print('4. 종료')
    menu=input('메뉴선택:')
    return int(menu)

def set_contact():
    # (3)
    # 이름, 전화번호, 이메일, 주소를 입력받아
    name = input("이름 입력 : ")
    tel = input("전화번호 입력 : ")
    email = input("이메일 입력 : ")
    addr = input("주소 입력 : ")
    conn = oci.connect("scott/tiger@192.168.0.18:1521/orcl")
    cursor = conn.cursor()
    sql = """
        INSERT INTO CONTACT(CONTACT_NAME, PHONE, EMAIL, ADDR) 
        VALUES(:name, :tel, :email, :addr )
    """
    cursor.execute(sql, (name, tel, email, addr))
    cursor.close()
    conn.commit()
    conn.close()

def print_contact():
    conn = oci.connect("scott/tiger@192.168.0.18:1521/orcl")
    cursor = conn.cursor()
    sql = "SELECT * FROM CONTACT"
    cursor.execute(sql)
    datas = cursor.fetchall()  # 데이터를 전부 다 받음
    for index, row in enumerate(datas):
        print("-----", index+1, "번째 사람의 연락처-----")
        print("이름 :", row[0])
        print("전화번호 :", row[1])
        print("이메일 :", row[2])
        print("주소 :", row[3])
    cursor.close()
    conn.close()

def delete_contact(name):
    conn = oci.connect("scott/tiger@192.168.0.18:1521/orcl")
    cursor = conn.cursor()
    print("name 확인", name)
    sql = "delete from CONTACT where CONTACT_NAME = :name"
    cursor.execute(sql, (name,))
    cursor.close()
    conn.commit()
    conn.close()

def run():
    while True:
        menu=print_menu()
        if menu==4:  # 종료를 선택하면
            break
        elif menu==1: # 입력을 선택하면
            contact = set_contact()
        elif menu==2: # 출력을 선택하면
            print_contact()
        elif menu==3: # 삭제를 선택하면
            name = input('삭제할 이름은?')
            delete_contact(name)


if __name__ == "__main__":
    run()
