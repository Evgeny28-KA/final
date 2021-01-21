from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome('ChromeDriver\chromedriver.exe')
driver.get("https://tmall.ru/")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="nav-user-account"]/div[1]/div/span[1]/a[1]').click()
time.sleep(2)
driver.find_element_by_id('fm-login-id').send_keys("nachalniksas@mail.ru")
driver.find_element_by_id('fm-login-password').send_keys('qwertyui1r')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="login-form"]/div[5]/button').click()