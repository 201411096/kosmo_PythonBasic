from selenium import webdriver
from bs4 import BeautifulSoup
import time
import storedb


# 웹드라이버 객체 생성
driver = webdriver.Chrome('./webdriver/chromedriver')
driver.implicitly_wait(2)

# url에 접근
driver.get('https://www.mexicana.co.kr:50010/company/find_store.asp')
time.sleep(3)

# driver에서 페이지 소스를 가져옴
html = driver.page_source

# html 부분을 파싱
soup = BeautifulSoup(html, 'html.parser')


# 필요한 데이터들을 감싸고 있는 태그를 가져옴
storelist = soup.select('div.locarea ul .storeLI > a')

storeNameList = []  # db에 저장할 지점들의 이름을 담을 리스트
storeAddrList = []  # db에 저장할 지점들의 주소를 담을 리스트

# 파싱해온 태그의 개수만큼 반복하여 필요한 데이터 추출
for store in storelist:
    name = store.select('.loc_tit')[0].text
    addr = store.select('.loc_lo')[0].text
    storeNameList.append(name)
    storeAddrList.append(addr)

# 이름과 주소를 담은 리스트들을 db에 저장
storedb.insert_data(storeNameList, storeAddrList)


