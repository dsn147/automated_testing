from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(r"E:\automated_testing\day01\练习的html\练习的html\frame.html")

driver.maximize_window()

driver.find_element_by_id('input1').send_keys('hello,world!')

time.sleep(2)
driver.quit()

