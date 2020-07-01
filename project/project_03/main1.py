from selenium import webdriver
from bs4 import BeautifulSoup
import time
import storedb

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
storedb.insert_data(storeNameList, storeAddrList)


