from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')

driver.get('http://google.com')

elem = driver.find_element_by_name('q')
elem.click()
elem.send_keys('کافه بازار')
time.sleep(1)

driver.close()