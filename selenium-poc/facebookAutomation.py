from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')
emailElement = driver.find_element(By.XPATH,'.//*[@id="email"]')
emailElement.send_keys('xyz@gmail.com')
passwordElement = driver.find_element(By.XPATH,'.//*[@id="pass"]')
passwordElement.send_keys('xxx')

elem = driver.find_element(By.XPATH,'.//*[@id="u_0_8"]')
elem.click()