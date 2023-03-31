import time

from selenium import webdriver

import os

os.chdir("C:\\Users\\HUAWEI\\Documents\\Downloads\\chromedriver_win32")

driver = webdriver.Chrome()

driver.get("https://www.imooc.com")
print("base_url:", driver.current_url)

driver.find_element_by_xpath("/html/body/div[3]/div/div/ul/li[2]/a").click()
time.sleep(2)
print('after search: ', driver.current_url)
time.sleep(5)
driver.back()
print('back to: ', driver.current_url)
time.sleep(2)
driver.forward()
print('forward to: ', driver.current_url)

time.sleep(2)
driver.refresh()
print('refresh: ', driver.current_url)

time.sleep(5)
driver.quit()
