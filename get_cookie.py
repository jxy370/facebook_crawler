from selenium import webdriver

import time
import MySQLdb
import random


fbusername = ['13161299088']
fbpassword = ['3228932']


def login():
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--disable-notifications")
    # chromeOptions.add_argument('--proxy-server=http://217.12.121.86:80')

    driver = webdriver.Chrome(chrome_options=chromeOptions)
    driver.get("https://www.facebook.com/login.php")
    # #time.sleep(3)
    driver.find_element_by_id("email").send_keys(fbusername[0])
    driver.find_element_by_id("pass").send_keys(fbpassword[0])
    driver.find_element_by_id("loginbutton").click()

    cookies = driver.get_cookies()
    print(str(cookies))
    time.sleep(30)
    # sql = "insert into cookies values(null, %s, %s, %s, null)"
    # values = [fbusername[i], fbpassword[i], str(cookies)]
    # cursor.execute(sql, values)
    # conn.commit()
    driver.quit()
    # cursor.close()
    # conn.close()


def t_cookies(cookies):
    url = "https://www.facebook.com/selina.joey"
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--disable-notifications")
    prefs = {"profile.managed_default_content_settings.images": 2}
    chromeOptions.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=chromeOptions)
    # try:

    driver.get("https://www.facebook.com/login.php")
    for cookie in cookies:
        driver.add_cookie(cookie)
    # print(driver.get_cookies())
    driver.get(url + "/friends")

    # except Exception as e:
    #     print(e)
    time.sleep(3)
    driver.close()
    driver.quit()


login()

# co = [{'domain': '.facebook.com', 'expiry': 1517908529, 'httpOnly': False, 'name': 'wd', 'path': '/', 'secure': True, 'value': '1036x675'}, {'domain': '.facebook.com', 'expiry': 1525079721.460661, 'httpOnly': False, 'name': 'c_user', 'path': '/', 'secure': True, 'value': '100024116122343'}, {'domain': '.facebook.com', 'httpOnly': False, 'name': 'presence', 'path': '/', 'secure': True, 'value': 'EDvF3EtimeF1517303727EuserFA21B24116122343A2EstateFDutF1517303727673CEchF_7bCC'}, {'domain': '.facebook.com', 'expiry': 1580375719.370987, 'httpOnly': True, 'name': 'datr', 'path': '/', 'secure': True, 'value': 'oTdwWq-SL25YDVESq-ikDdR9'}, {'domain': '.facebook.com', 'expiry': 1525079721.460741, 'httpOnly': True, 'name': 'xs', 'path': '/', 'secure': True, 'value': '41%3AEXm8VkcukJBwzA%3A2%3A1517303719%3A-1%3A-1'}, {'domain': '.facebook.com', 'expiry': 1525079721.461033, 'httpOnly': True, 'name': 'pl', 'path': '/', 'secure': True, 'value': 'n'}, {'domain': '.facebook.com', 'expiry': 1517908521, 'httpOnly': False, 'name': 'dpr', 'path': '/', 'secure': True, 'value': '1.25'}, {'domain': '.facebook.com', 'expiry': 1525079721.460923, 'httpOnly': True, 'name': 'fr', 'path': '/', 'secure': True, 'value': '0PxUvJJbrb8Tdx4oD.AWXh4_D6DK8anT2IjLdZd48uLA8.BacDeh.wM.AAA.0.0.BacDen.AWXvqYJd'}, {'domain': '.facebook.com', 'expiry': 1580375721.460478, 'httpOnly': True, 'name': 'sb', 'path': '/', 'secure': True, 'value': 'pzdwWjkr_D2fyZ9kWFjRi9Ye'}]
#
# t_cookies(co)
# for cookies in cookies_list:
#     print(cnt)
#     t_cookies(cookies)
#     cnt = cnt + 1