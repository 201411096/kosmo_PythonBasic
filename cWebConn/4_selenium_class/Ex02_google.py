'''
1. 크롬웹드라이버로 구글 사이트 열기

2. 실제 크롬창에서 '플레이데이터'라고 검색버튼을 누른다.
    개발자모드(F12)에서 이 부분을 보면
    <input name='q' value='플레이데이터'~~ >
    그리고 'google검색' 버튼이 type='submit' 인거 확인
'''

# [1]
from selenium import webdriver

# 1. webdriver 객체생성
# mvc 구조의 controller때문에 직접 클릭을 해줘야 됨
driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(2) #2초 쉼 (드라이버가 접속할 시간을 주기 위해서)

# 2. 페이지 접근
driver.get('http://www.google.com')
#----------------------------------------------
# [2]

search_bt = driver.find_element_by_name('q')
search_bt.send_keys("파이썬")
search_bt.submit()  #input태그가 하나만 있으면..