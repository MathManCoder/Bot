################### open a site in google ########################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

site = input('Enter url : ')
driver = webdriver.Chrome()
driver.get('https://www.google.com')
driver.find_element_by_name('q').send_keys(site)
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').send_keys(Keys.ENTER)
time.sleep(2)
driver.quit()
