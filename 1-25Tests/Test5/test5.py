from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome('ChromeDriver\chromedriver.exe')
driver.get("https://tmall.ru/")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="search-key"]').send_keys('ваормзырвзм2134')
driver.find_element_by_xpath('//*[@id="form-searchbar"]/div[1]/input').click()