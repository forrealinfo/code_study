import sys
import io
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

chrome_options = Options()

# headless 옵션 설정
chrome_options.add_argument('--headless')

chrome_options.add_argument('--log-level=3')
#driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:/section3/webdriver/chrome/chromedriver')
driver = webdriver.Chrome('c:/Coding/testRepo/driver/chromedriver')

driver.set_window_size(1920, 1080)

driver.implicitly_wait(3)
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

time.sleep(5)
driver.implicitly_wait(3)

driver.find_element_by_name('id').send_keys('아이디')

driver.implicitly_wait(3)
driver.find_element_by_name('pw').send_keys('비번')

driver.implicitly_wait(3)
# # 로그인

# xpath 관련 참고사이트 : https://devyurim.github.io/python/crawler/2018/08/11/crawler-2.html
driver.find_element_by_xpath('//*[@id="log.login"]').click()

driver.implicitly_wait(1)
driver.save_screenshot('c:/Coding/testRepo/login.png')

driver.quit()
