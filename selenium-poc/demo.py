from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")
elem = driver.find_element_by_tag_name('html')
elem.send_keys(Keys.END)
time.sleep(5)
elem.send_keys(Keys.HOME)