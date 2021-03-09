import shelve
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestDemo1:
    # get_cookies 登录后获取token的方法
    def get_cookies(self):
        url = "https://ceshiren.com/t/topic/6223/21"
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        sleep(3)
        print("打开界面点击登录按钮")
        self.driver.find_element(By.XPATH, "//*[@id='ember5']/header/div/div/div[2]/span/button[2]/span").click()
        sleep(3)

        print("输入用户名和密码点击登录")
        self.driver.find_element(By.XPATH, '//*[@id="login-account-name"]').send_keys("username") # 写自己的账户名
        self.driver.find_element(By.XPATH, '//*[@id="login-account-password"]').send_keys("password")# 写自己的密码
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]/span').click()
        sleep(7)

        print("获取cookie")
        self.driver.get("https://ceshiren.com/t/topic/4496/2")
        cookies = self.driver.get_cookies()
        print(cookies)
        return cookies
    # 处理token，存储到小型数据库shelve
    def handle_cookies(self):
        cookies_test = self.get_cookies()
        print(cookies_test)
        db = shelve.open("cookies")
        db["cookie"] = cookies_test
        c = db["cookie"]
        db.close()
        return c

    # test_login测试代码
    # 先将1-3行注释，将第4行打开，去获取并存储cookie
    # 然后将1-3打开，第4行注释，从本地获取token去登录即可，在cookie有效期内使用即可
    def test_login(self):
        db = shelve.open("cookies")
        cookies = db["cookie"]
        db.close()
        # cookies = self.handle_cookies()
        sleep(10)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://ceshiren.com")
        self.driver.implicitly_wait(5)
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        print(cookies)
        sleep(3)
        self.driver.get("https://ceshiren.com/t/topic/6223/21")
        sleep(3)
        print(f"***** {self.driver.title}")
        b = self.driver.title
        assert "到课率查询贴" in b
        self.driver.quit()
