from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
elem = driver.find_element_by_name('q')
time.sleep(5)
elem.clear()
elem.send_keys("Python")
elem.send_keys(Keys.RETURN)