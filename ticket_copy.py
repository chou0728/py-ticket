# import webdriver
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# chrome options ( keep browser open)
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# options.add_argument("--disable-extensions")
# options.add_argument("--disable-popup-blocking")
# options.add_argument("--profile-directory=Default")
# options.add_argument("--ignore-certificate-errors")
# options.add_argument("--disable-plugins-discovery")
# options.add_argument("--incognito")
# options.add_argument("user_agent=DN")


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


cookies = [
    {
        "domain": ".tixcraft.com",
        "expirationDate": 1707363047.48554,
        "hostOnly": False,
        "httpOnly": False,
        "name": "_ga",
        "path": "/",
        "sameSite": "None",
        "secure": False,
        "session": False,
        "storeId": "1",
        "value": "GA1.1.1113947880.1672802229",
        "id": 1
    },
    {
        "domain": ".tixcraft.com",
        "expirationDate": 1707363047.485152,
        "hostOnly": False,
        "httpOnly": False,
        "name": "_ga_C3KRPGTSF6",
        "path": "/",
        "sameSite": "None",
        "secure": False,
        "session": False,
        "storeId": "1",
        "value": "GS1.1.1672802228.1.1.1672803047.0.0.0",
        "id": 2
    },
    {
        "domain": ".tixcraft.com",
        "expirationDate": 1704338233,
        "hostOnly": False,
        "httpOnly": False,
        "name": "OptanonAlertBoxClosed",
        "path": "/",
        "sameSite": "Lax",
        "secure": False,
        "session": False,
        "storeId": "1",
        "value": "2023-01-04T03:17:13.326Z",
        "id": 3
    },
    {
        "domain": ".tixcraft.com",
        "expirationDate": 1704339047,
        "hostOnly": False,
        "httpOnly": False,
        "name": "OptanonConsent",
        "path": "/",
        "sameSite": "Lax",
        "secure": False,
        "session": False,
        "storeId": "1",
        "value": "isGpcEnabled=0&datestamp=Wed+Jan+04+2023+11%3A30%3A47+GMT%2B0800+(%E5%8F%B0%E5%8C%97%E6%A8%99%E6%BA%96%E6%99%82%E9%96%93)&version=202209.1.0&isIABGlobal=False&hosts=&consentId=f0012d6e-f2a8-4b0f-b9fa-759c5c00e7da&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A0%2CC0002%3A0%2CC0004%3A0&geolocation=TW%3BNWT&AwaitingReconsent=False",
        "id": 4
    },
    {
        "domain": "tixcraft.com",
        "hostOnly": True,
        "httpOnly": True,
        "name": "CSRFTOKEN",
        "path": "/",
        "sameSite": "None",
        "secure": True,
        "session": True,
        "storeId": "1",
        "value": "d38b0c21324d6e7cea6be2d27414b36a16a84229s%3A88%3A%22TWE5dXRVcn5LSE5LZklHak5HMmZNVzhtcEh2X35-WlDHensdUokFBT209w1pb7g0Tr4my3N5b9uyTsVawluVSA%3D%3D%22%3B",
        "id": 5
    },
    {
        "domain": "tixcraft.com",
        "hostOnly": True,
        "httpOnly": False,
        "name": "gameHash",
        "path": "/activity/detail",
        "sameSite": "None",
        "secure": False,
        "session": True,
        "storeId": "1",
        "value": "",
        "id": 6
    },
    {
        "domain": "tixcraft.com",
        "hostOnly": True,
        "httpOnly": True,
        "name": "lang",
        "path": "/",
        "sameSite": "None",
        "secure": True,
        "session": True,
        "storeId": "1",
        "value": "1a73f0317e76f38c9adb36e69bdc73613602f560s%3A5%3A%22zh_tw%22%3B",
        "id": 7
    },
    {
        "domain": "tixcraft.com",
        "hostOnly": True,
        "httpOnly": True,
        "name": "SID",
        "path": "/",
        "sameSite": "None",
        "secure": True,
        "session": True,
        "storeId": "1",
        "value": "6bod3q42ojgov5pu7u9u64v0c4",
        "id": 8
    },
    {
        "domain": "tixcraft.com",
        "hostOnly": True,
        "httpOnly": False,
        "name": "tagHash",
        "path": "/activity/detail",
        "sameSite": "None",
        "secure": False,
        "session": True,
        "storeId": "1",
        "value": "",
        "id": 9
    }
]


# open browser
# driver = webdriver.Chrome(chrome_options=options)
driver = My_Chrome(options=chrome_options)

driver.maximize_window()
driver.get('https://tixcraft.com/activity/detail/23_projectx')
# driver.add_cookie({'name':'OptanonAlertBoxClosed', 'value': '2023-01-04T02:01:49.341Z', 'domain': 'tixcraft.com', 'secure': True })
# driver.add_cookie({'name':'CSRFTOKEN', 'value': '4e83e9dfaa60d6b081a73fd817cbeb326fd9c3f3s%3A88%3A%22X29MZEVnfkhVeDVZNTFVQ1lRUlRYdFJraGRpM04yT3rZkJWw6aRfqVUsgXZgVUxtmWGEX6kAXgD9XbTPUusrhw%3D%3D%22%3B', 'domain': 'tixcraft.com', 'secure': True })
# driver.add_cookie({'name':'SID', 'value': 'et20r9meca0qe2nur47cbd8vid', 'domain': 'tixcraft.com', 'secure': True })

# for item in cookies:
#     driver.add_cookie(item)

# driver.get('https://tixcraft.com/activity/detail/23_projectx')

WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "//button[text()='接受所有 Cookie']"))).click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "//div[text()='立即購票']"))).click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "//input[@value='立即訂購']"))).click()

# OptanonAlertBoxClosed
# 2023-01-04T02:01:49.341Z

# CSRFTOKEN

# 4e83e9dfaa60d6b081a73fd817cbeb326fd9c3f3s%3A88%3A%22X29MZEVnfkhVeDVZNTFVQ1lRUlRYdFJraGRpM04yT3rZkJWw6aRfqVUsgXZgVUxtmWGEX6kAXgD9XbTPUusrhw%3D%3D%22%3B

# SID

# et20r9meca0qe2nur47cbd8vid
