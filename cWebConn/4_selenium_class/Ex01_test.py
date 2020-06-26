"""
 간단하게 크롬 브라우저를 실행하여 페이지 열기
"""

from selenium import webdriver

# 1. webdriver 객체생성
# mvc 구조의 controller때문에 직접 클릭을 해줘야 됨
driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(2) #2초 쉼 (드라이버가 접속할 시간을 주기 위해서)

# 2. 페이지 접근
driver.get('http://www.google.com')

# 3. 화면을 캡처해서 저장하기
driver.save_screenshot('Website.png')