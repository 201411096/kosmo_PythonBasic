import cx_Oracle as oci
import json
import requests
import urllib
def insert_data(name, addr):
    conn = oci.connect("scott/tiger@192.168.56.1:1521/xe")
    #conn = oci.connect("scott/tiger@192.168.0.18:1521/orcl")
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
    conn = oci.connect("scott/tiger@192.168.56.1:1521/xe")
    #conn = oci.connect("scott/tiger@192.168.0.18:1521/orcl")
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
    conn = oci.connect("scott/tiger@192.168.56.1:1521/xe")
    #conn = oci.connect("scott/tiger@192.168.0.18:1521/orcl")
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


def get_key():
    with open('properties.txt') as f:
        key =str(f.readline())
    return key

def conversion(addr):
    value = kakao_conversion(addr)
    print('conversion 확인', value)
    return value['documents'][0]['address']

def kakao_conversion(addr):
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'KakaoAK {}'.format(get_key())
    }
    address = addr.encode("utf-8")

    p = urllib.parse.urlencode(
        {
            'query': address
        }
    )
    result = requests.get("https://dapi.kakao.com/v2/local/search/address.json", headers=headers, params=p)
    print(type(result))
    return result.json()
    # .json()
    # Returns the json-encoded content of a response
    # response를 json의 형태로 반환




# 잘 안됨
# def conversion(addr):
#     url = 'https://dapi.kakao.com/v2/local/search/address.json?query='+addr
#     headers = {"Authorization": get_key()}
#     result = json.loads(str(requests.get(url,headers=headers).text))
#     match_first = result['documents'][0]['address']
#     return float(match_first['y']), float(match_first['x'])