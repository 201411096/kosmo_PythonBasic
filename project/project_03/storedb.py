import cx_Oracle as oci
import json
import requests
import urllib
connContent = "scott/tiger@192.168.56.1:1521/xe"
#connContent = "scott/tiger@192.168.0.18:1521/orcl"

def insert_data(name, addr):
    # name : db에 담을 지점 이름들이 담긴 리스트
    # addr : db에 담을 지점 주소들이 담긴 리스트
    conn = oci.connect(connContent)
    cursor = conn.cursor()
    sql = """
        INSERT INTO STORE(NAME, ADDR)
        VALUES(:name, :addr)
    """
    for i in range(len(name)): # name 리스트의 길이만큼 반복하여 db에 저장
        cursor.execute(sql, (name[i], addr[i]))
    cursor.close()
    conn.commit()
    conn.close()

def selectOne_data():
    name = str(input("이름 입력"))
    conn = oci.connect(connContent)
    cursor = conn.cursor()
    sql = """
            select * from store where name = :name
        """
    cursor.execute(sql, (name,))
    data = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    return data[0][1]

# db에 저장되어 있는 지정들의 이름과 주소 정보를 읽어 옴
def select_data():
    conn = oci.connect(connContent)
    cursor = conn.cursor()
    sql = """
            select * from store
        """
    cursor.execute(sql)
    datas = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    return datas # (지점 이름, 지점 주소)을 담을 튜플들을 담을 리스트 형태로 반환

# 텍스트파일에 저장되어있는 apikey를 읽어와서 반환
def get_key():
    with open('./properties.txt') as f:
        key =str(f.readline())
    return key

# 주소를 받아서 위도, 경도를 포함한 해당 주소에 대한 정보를 받아옴(Kakao API 이용)
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
    return result.json()
    # .json()
    # Returns the json-encoded content of a response
    # response를 json의 형태로 반환
# Kakao API에서 뽑아온 정보들 중에서 필요한 데이터 추출(주소의 위도, 경도)
def conversion(addr):
    value = kakao_conversion(addr)
    if len(value['documents']) >= 1:    # 해당 주소에 대한 정보가 있는 경우에만 추출
        return value['documents'][0]['address']
    else:
        return None





# 잘 안됨
# def conversion(addr):
#     url = 'https://dapi.kakao.com/v2/local/search/address.json?query='+addr
#     headers = {"Authorization": get_key()}
#     result = json.loads(str(requests.get(url,headers=headers).text))
#     match_first = result['documents'][0]['address']
#     return float(match_first['y']), float(match_first['x'])