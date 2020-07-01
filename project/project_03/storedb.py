import cx_Oracle as oci
import json
import requests
def insert_data(name, addr):
    conn = oci.connect("scott/tiger@192.168.0.18:1521/orcl")
    cursor = conn.cursor()
    sql = """
        INSERT INTO STORE(NAME, ADDR)
        VALUES(:name, :addr)
    """
    for i in range(len(name)):
        cursor.execute(sql, (name[i], addr[i]))
    cursor.close()
    conn.commit()
    conn.close()
def select_data():
    conn = oci.connect("scott/tiger@192.168.0.18:1521/orcl")
    cursor = conn.cursor()
    sql = """
            select * from store
        """
    cursor.execute(sql)
    datas = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    return datas

def selectOne_data(name):
    print('지점 이름 입력')
    conn = oci.connect("scott/tiger@192.168.0.18:1521/orcl")
    cursor = conn.cursor()
    sql = """
            select * from store where name = :name
        """
    cursor.execute(sql, (name,))
    data = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    return data

def conversion(addr):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query='+addr
    headers = {"Authorization": "ec8f6fd46ab832e10395eecfabaa2c5a"}
    result = json.loads(str(requests.get(url,headers=headers).text))
    match_first = result['documents'][0]['address']
    return float(match_first['y']), float(match_first['x'])