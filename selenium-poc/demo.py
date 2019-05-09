from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
elem = driver.find_element(By.XPATH,'//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')
time.sleep(5)
elem.clear()
elem.send_keys("Python")
elem.send_keys(Keys.RETURN)