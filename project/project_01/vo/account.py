import cx_Oracle as oci

class Account:
    def __init__(self, id, password, adminFlag):
        self.id = id
        self.password = password
        self.adminFlag = adminFlag
    @staticmethod
    def select_account(id, pw):
        conn = oci.connect("hrr/hrr@192.168.56.1:1521/xe")
        #       conn = oci.connect("scott/tiger@192.168.0.18:1521/orcl")
        cursor = conn.cursor()
        sql = """
                    SELECT * FROM
                    ACCOUNT
                    WHERE ACCOUNT_ID = :id AND ACCOUNT_PW = :pw
                """
        cursor.execute(sql, (id, pw))
        datas = cursor.fetchall()

        cursor.close()
        conn.close()
        print(datas)
        if not datas:   # 로그인 실패
            print('empty 실행 확인')
            return False
        else:
            print("else 실행 확인")
            returnAccount = Account(datas[0][0], datas[0][1], datas[0][2])
            return returnAccount

# 1. 데이터 받아와서 확인
# account1 = Account.select_account('admin', '1234')
# print(account1.id)

# 1_2. 데이터 받아와서 확인(로그인 실패)
account1 = Account.select_account('admin', '123')
print(account1)