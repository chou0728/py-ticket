from typing import Tuple
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from datetime import time, datetime, timezone, timedelta
taipei_standard_time = timezone(timedelta(hours=+8), 'TST')


def check_current_time() -> time:
    '''
    Check current time is between 00:00 and 00:15. 
    Returns current time and if it is between begin and end time.
    '''
    dt_now = datetime.now(taipei_standard_time)
    current_time = time(dt_now.hour, dt_now.minute, dt_now.second)
    return current_time


current_time = check_current_time()


# keep browser open
class My_Chrome(uc.Chrome):
    def __del__(self):
        pass


chrome_options = uc.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("user_agent=DN")

driver = My_Chrome(options=chrome_options)
driver.maximize_window()

test_url_1 = 'https://tixcraft.com/activity/detail/23_dna2023'
test_url_2 = 'https://tixcraft.com/activity/detail/22_WuBaiOPR'
url = 'https://tixcraft.com/activity/detail/23_ameiasmr'

driver.implicitly_wait(10)
driver.get(url)
driver.add_cookie({'name': 'OptanonAlertBoxClosed',
                  'value': '2023-01-04T02:01:49.341Z', 'domain': 'tixcraft.com', 'secure': True, })
driver.get(url)

# 1) Google登入會員
# GOOGLE_ACCOUNT = 'xxxx0@gmail.com'
# GOOGLE_PASSWORD = ''

wait = WebDriverWait(driver, 10)

# driver.find_element(By.XPATH, "//a[@href='#login']").click()
# driver.find_element(By.XPATH, "//a[@href='/login/google']").click()
# driver.find_element(
#     By.XPATH, "//input[@type='email']").send_keys(GOOGLE_ACCOUNT)
# driver.find_element(By.XPATH, "//span[text()='繼續']").click()
# wait.until(EC.visibility_of_element_located(
#     (By.XPATH, "//input[@type='password']"))).send_keys(GOOGLE_PASSWORD)
# driver.find_element(By.XPATH, "//span[text()='繼續']").click()


# 2) 登入成功後一直刷新頁面，直到立即購票的按鈕出現
# isClicked = False
# isShow = driver.find_element(By.XPATH, "//div[text()='立即購票']").is_displayed()

# while isShow & isClicked == False:
#     driver.find_element(By.XPATH, "//div[text()='立即購票']").click()
#     isClicked = True
#     print('sdfsd')


# while True:
#     try:
#         print('try')
#         sleep(20)
#         print('try2')
#         # driver.find_element(By.XPATH, "//div[text()='立即購票']").click()
#         break
#     except NoSuchElementException:
#         driver.refresh()
#         print('except  => driver.refresh()')
#         continue

def startBuy():

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[text()='立即購票']"))).click()

    list = wait.until(EC.visibility_of_any_elements_located(
        (By.XPATH, "//input[@value='立即訂購']")))

    list[0].click()

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(text(),'3800')]"))).click()

    select = Select(driver.find_element(By.TAG_NAME, 'select'))

    select.select_by_value('4')

    driver.find_element(By.XPATH, "//label[@for='TicketForm_agree']").click()


check_current_time()

while True:
    if current_time >= time(13, 00, 00):
        driver.refresh()
        print('startBuy...')
        startBuy()
    else:
        print('chekcking...')
        current_time = check_current_time(
        )
    continue
