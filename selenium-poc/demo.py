from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
elem = driver.find_element_by_link_text('About')
time.sleep(5)
elem.click()
time.sleep(5)
elem = driver.find_element_by_link_text('Our products')
time.sleep(5)
elem.click()