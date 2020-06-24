import cx_Oracle as oci

class buyList:
    @staticmethod
    def insert_buyList(buyListTotalPrice, orderList, price):
        conn = oci.connect("scott/tiger@192.168.0.18:1521/orcl")
        cursor = conn.cursor()
        sql1 = """
            INSERT INTO buyList(buylist_id, buylist_date, buylist_totalprice) 
            VALUES (seq_buylist_pk.nextval, sysdate, :buyListTotalPrice)
        """
        cursor.execute(sql1, (buyListTotalPrice,))
        for product in orderList.keys():
            tempPrice = int(price[product])
            cnt = int(orderList[product])
            print(tempPrice)
            print(cnt)
            sql2 = """
                INSERT INTO buy(buy_id, buylist_id, buy_price, buy_productname, buy_cnt)
                VALUES (seq_buy_pk.nextval, seq_buylist_pk.currval, :price, :product, :cnt) 
            """
            cursor.execute(sql2, (tempPrice, product, cnt))
        cursor.close()
        conn.commit()
        conn.close()
    @staticmethod
    def select_buyList():
        returnString = ''
        conn = oci.connect("scott/tiger@192.168.0.18:1521/orcl")
        cursor = conn.cursor()
        sql1 = """
                    select * from buylist
                """
        cursor.execute(sql1)
        datas = cursor.fetchall()
        returnString = returnString + "------------------------------------------------------------\n"
        for row in datas:
            returnString = returnString + "------------------------------------------------------------\n"
            returnString = returnString + "주문리스트번호 : " + str(row[0]) + " 주문날짜 : " + str(row[1]) + " 주문가격 : " + str(row[2]) + "\n"
            returnString = returnString + "------------------------------------------------------------\n"
            sql2 = "select * from buy where buylist_id = :buylistId"
            print("row0 확인", row[0])
            cursor.execute(sql2, (row[0], ))
            datas2 = cursor.fetchall()
            for row2 in datas2:
                print(row2)
                returnString = returnString + "주문리스트번호 : " + str(row2[1]) + " 구매번호 : " + str(row2[0]) + " 제품가격 : " + str(row2[2]) + " 제품이름 : " + str(row2[3])+ " 제품 개수 :" + str(row2[4]) + "\n"
            # print("주문번호 :", row[0])
            # print("주문날짜 :", row[1])
            # print("주문가격 :", row[2])
        print(returnString)

        cursor.close()
        conn.close()
buyList.select_buyList()