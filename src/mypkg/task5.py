import time
from selenium import webdriver

import os

os.chdir("C:\\Users\\HUAWEI\\Documents\\Downloads\\chromedriver_win32")
# Open the web browser and navigate to the login page

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_content")

time.sleep(3)
click_input = driver.find_element_by_xpath("/html/body/div[2]/div/div/p[2]/a")
click_input.click()








