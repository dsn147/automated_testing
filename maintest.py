from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(r"E:\automated_testing\day01\练习的html\练习的html\main.html")

# 浏览器最大化
driver.maximize_window()

# 跳转到框架页
driver.switch_to.frame("frame")


# 输入不进入
driver.find_element_by_id('input1').send_keys('hello,world!')

# driver.find_element_by_xpath("//*[@id='input1']").send_keys('hello,world!')


time.sleep(2)
driver.quit()
