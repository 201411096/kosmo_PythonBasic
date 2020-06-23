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
            sql2 = """
                INSERT INTO buy(buy_id, buylist_id, buy_price, buy_productname, buy_cnt)
                VALUES (seq_buy_pk.nextval, seq_buylist_pk.currval, :price, :product, :cnt) 
            """
            cursor.execute(sql2, (tempPrice, product, cnt))
        cursor.close()
        conn.commit()
        conn.close()