from selenium import webdriver
from bs4 import BeautifulSoup
import time
import cx_Oracle as oci


def insert_data(name, addr):
    conn = oci.connect("scott/tiger@192.168.0.18:1521/orcl")
    cursor = conn.cursor()
    sql = """
        INSERT INTO STORE(NAME, ADDR)
        VALUES(:name, :addr)
    """
    cursor.execute(sql, (name, addr))
    cursor.close()
    conn.commit()
    conn.close()


# -------------------------------1. 웹 페이지 접근
# 웹드라이버 객체 생성
driver = webdriver.Chrome('./webdriver/chromedriver')
driver.implicitly_wait(2)

driver.get('https://www.mexicana.co.kr:50010/company/find_store.asp')
time.sleep(3)
html = driver.page_source  # driver에서 페이지 소스를 가져옴

soup = BeautifulSoup(html, 'html.parser')
storelist = soup.select('div.locarea ul .storeLI > a')

storeNameList = []
storeAddrList = []

for store in storelist:
    name = store.select('.loc_tit')[0].text
    addr = store.select('.loc_lo')[0].text
    storeNameList.append(name)
    storeAddrList.append(addr)
    print(name)
    print(addr)
    insert_data(name, addr) # 커넥션을 여러번 열어서 문제가 생기는듯
    # ORA-12516: TNS:리스너가 프로토콜 스택과 일치하는 처리기를 찾을 수 없습니다
    # 동시 처리 가능한 Processes parameter 값을 초과했기 때문에 발생하는 문제
#insert_data(storeNameList, storeAddrList)


