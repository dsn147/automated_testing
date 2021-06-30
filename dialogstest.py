from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(r"E:\automated_testing\day01\练习的html\练习的html\弹框的验证\dialogs.html")

driver.maximize_window()

driver.find_element_by_id("alert").click()
time.sleep(1)
driver.switch_to.alert.dismiss()
time.sleep(2)

driver.find_element_by_xpath("//*[@id='confirm']").click()
time.sleep(1)
driver.switch_to.alert.dismiss()
time.sleep(2)

driver.quit()
