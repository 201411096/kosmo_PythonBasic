"""
    [연습] 페이스북에 접속해서 로그인 하기

        로그인 후에 보안창은 없는데 안 넘어가서

        from selenium.webdriver.common.keys import Keys

        아이디와 패스워드 지정후에
        elem.send_keys(Keys.RETURN)

"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

usr=''
pwd=''













driver = webdriver.Chrome('./webdriver/chromedriver')
driver.implicitly_wait(3) # 암묵적으로 자원로드될 때까지 3초 기다림


driver.get('https://www.facebook.com')
driver.find_element_by_name('email').send_keys(usr)
driver.find_element_by_name('pass').send_keys(pwd)
#driver.send_keys(Keys.RETURN)
driver.find_element_by_id('u_0_e').click()
#driver.submit()