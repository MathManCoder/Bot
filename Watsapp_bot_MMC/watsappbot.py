# ################# Watsapp Bot ###############################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

names = input('Enter the name with cama : (name1,name2,...)')
a = names.split(',')
names = list(a)
msg = input('Enter a message : ')
count = int(input('How many send : '))
input('Enter Any thing ')
for name in names:
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_35EW6')
        button.click()