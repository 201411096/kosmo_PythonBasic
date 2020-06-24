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
                    select * from buylist order by buylist_id
                """
        cursor.execute(sql1)
        datas = cursor.fetchall()
        for row in datas:
            returnString = returnString + "----------------------------------------------------------------------------------\n"
            returnString = returnString + "주문번호 : " + str(row[0]) + "\n"
            returnString = returnString + "주문날짜 : " + str(row[1]) + "\n"
            returnString = returnString + "----------------------------------------------------------------------------------\n"
            sql2 = "select * from buy where buylist_id = :buylistId"
            print("row0 확인", row[0])
            cursor.execute(sql2, (row[0], ))
            datas2 = cursor.fetchall()
            returnString = returnString + "제품이름\t\t\t" + "제품개수\t\t\t" + " 제품가격" + "\n"
            for row2 in datas2:
                print(row2)
                returnString = returnString + str(row2[3]) + "\t\t\t" + str(row2[4]) + "\t\t\t" + str(row2[2]) + "\n"
                #returnString = returnString + "제품이름 : " + str(row2[3]) + " 제품개수 : " + str(row2[4]) + " 제품가격 :" + str(row2[2]) + "\n"
            returnString = returnString + "----------------------------------------------------------------------------------\n"
            returnString = returnString + "가격총합 : " + str(row[2]) + "\n"
            returnString = returnString + "----------------------------------------------------------------------------------\n"
            returnString = returnString + "\n\n"
        print(returnString)

        cursor.close()
        conn.close()
        return returnString
    @staticmethod
    def delete_buyList(orderListId):
        conn = oci.connect("scott/tiger@192.168.0.18:1521/orcl")
        cursor = conn.cursor()
        sql1 = """
                    DELETE FROM buy where buylist_id = :orderListId
                """
        cursor.execute(sql1, (orderListId,))
        sql2 = """
                    DELETE FROM buylist where buylist_id = :orderListId
                """
        cursor.execute(sql2, (orderListId,))
        cursor.close()
        conn.commit()
        conn.close()
