from selenium import webdriver
from selenium.webdriver.common.keys import Keys

usr = ''
pwd = ''

# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdriver/chromedriver')
driver.implicitly_wait(3) # 암묵적으로 자원로드될 때까지 3초 기다림

# 네이버로그인 하기 -[결론] 네이버 보안에 걸림
# 보안에 안걸렸으면 로그인된 상태로 많은 정보를 가져올 수 있다
driver.get('https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F')
driver.find_element_by_name('id').send_keys(usr)
driver.find_element_by_name('pw').send_keys(pwd)
driver.find_element_by_id('loginBtn').click()