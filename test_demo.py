import shelve
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDemo1:
    def setup(self):
        url = "https://ceshiren.com/t/topic/6223/21"
        self.driver = webdriver.Chrome()
        # self.driver.get(url)
        self.driver.get("https://ceshiren.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        sleep(3)

    def teardown(self):
        self.driver.quit()

    def get_own_cookies(self):
        self._username = "XXX"
        self._password = "XXX"

        print("打开界面点击登录按钮")
        self.driver.find_element(By.XPATH, "//*[@id='ember5']/header/div/div/div[2]/span/button[2]/span").click()
        sleep(3)
        print("输入用户名和密码点击登录")
        self.driver.find_element(By.XPATH, '//*[@id="login-account-name"]').send_keys(self._username)
        self.driver.find_element(By.XPATH, '//*[@id="login-account-password"]').send_keys(self._password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]/span').click()
        sleep(7)
        print("获取cookie")
        self.driver.get("https://ceshiren.com/t/topic/4496/2")
        cookies = self.driver.get_cookies()
        print(cookies)
        return cookies

    def handle_cookies(self):
        cookies_test = self.get_own_cookies()
        print(cookies_test)
        db = shelve.open("cookies")
        db["cookie"] = cookies_test
        c = db["cookie"]
        for cookie in c:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
        db.close()
        return c

    def test_login(self):
        db = shelve.open("cookies")
        cookies = db["cookie"]
        db.close()
        print(cookies)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        sleep(3)
        self.driver.get("https://ceshiren.com/t/topic/6223/21")
        sleep(3)
        print(f"***** {self.driver.title}")
        title = self.driver.title
        key = "到课率查询贴"
        if key in title:
            print("cookies有效，登录成功")
            assert key in title
        else:
            print("cookies无效，需要重新获取并存储")
            cookies = self.handle_cookies()
            self.driver.get("https://ceshiren.com/t/topic/6223/21")
            sleep(3)
            title = self.driver.title
            assert key in title
