from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time


username = input('Enter your username : ')
password = input('Enter your password : ')
hasht = input('Enter your Hashtags for exmaple ; Hashtag_1 , Hashtag_2 , ... : ')
hashtag = hasht.split(',')

class InstagramBot:
    def __init__(self , username , password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def CloseBrowser(self):
        self.driver.close()

    def Login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(2)
        username_box = driver.find_element_by_xpath('//input[@name="username"]')
        username_box.clear()
        username_box.send_keys(self.username)

        password_box = driver.find_element_by_xpath('//input[@name="password"]')
        password_box.clear()
        password_box.send_keys(self.password)

        Login_bottun = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')
        Login_bottun.click() ## password_box.send_keys(Key.ENTER)
        time.sleep(5)
        driver.get(f'https://www.instagram.com/{self.username}/')


    def Like_pthoto(self , hashtag):
        driver = self.driver
        driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
        time.sleep(2)
        pic_hrefs = []
        for i in range(1,4):
            try:
                driver.execute_script('window.scrollTo(0 , document.body.scrollHeight)')
                time.sleep(2)
                all_hrefs = driver.find_elements_by_tag_name('a')
                pic_hrefs = [elem.get_attribute('href') for elem in all_hrefs if '.com/p/' in elem.get_attribute('href')]
        
            except Exception:
                continue

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(2)
            try:
                time.sleep(random.randint(1,3))
                driver.find_element_by_class_name("_8-yf5").click()           

            except Exception as e:
                time.sleep(2)


userbot_1 = InstagramBot(username , password)
userbot_1.Login()


while True:
    try:
        tag = random.choice(hashtag)
        userbot_1.Like_pthoto(tag)
    except Exception:
        userbot_1.CloseBrowser()
        time.sleep(30)
        userbot_1 = InstagramBot(username , password)

