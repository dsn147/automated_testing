from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get(r"E:\automated_testing\day01\练习的html\练习的html\上传文件和下拉列表\autotest.html")
driver.maximize_window()

driver.find_element_by_xpath("//*[@id='accountID']").send_keys("杜少楠")

driver.find_element_by_xpath("//*[@id='passwordID']").send_keys("asd111")

driver.find_element_by_xpath("//*[@id='areaID']").send_keys("天津市")

driver.find_element_by_xpath("//*[@id='sexID1']").click()

driver.find_element_by_xpath("//*[@value='spring']").click()

driver.find_element_by_xpath("//*[@value='Auterm']").click()

driver.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r"D:\桌面\图片\mine mad_002.jpg")

driver.find_element_by_xpath("//*[@id='buttonID' and @type='button']").click()

time.sleep(2)
# 弹窗点击确定
driver.switch_to.alert.dismiss()  # accept()确定  dismiss


time.sleep(1)
driver.quit()



