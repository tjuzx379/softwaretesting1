import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium import webdriver

import os

os.chdir("C:\\Users\\HUAWEI\\Documents\\Downloads\\chromedriver_win32")
# Open the web browser and navigate to the login page

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")

# Enter a valid username and password
firstname_input = driver.find_element(By.ID, "firstName")
lastname_input = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[1]/div[4]/input")
Email_input = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[2]/div[2]/input")
phoneNumber_input = driver.find_element_by_xpath(
    "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[4]/div[2]/input")
# jump_input = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[3]/span/div")
submit_input = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[11]/div/button")
gender = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[3]/div[2]/div[1]/label")

firstname_input.send_keys("李")
lastname_input.send_keys("华")
Email_input.send_keys("666@example.com")
gender.click()
phoneNumber_input.send_keys("15671405xyz")
time.sleep(5)
# jump_input.click()
submit_input.click()

if driver.find_element(By.XPATH,
                       "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[4]/div[2]/input").text == "":
    print("已显示错误信息")
if driver.find_element(By.XPATH,
                       "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[2]/div[2]/input").text == "":
    print("已显示错误信息")
time.sleep(2)
firstname_input.clear()
lastname_input.clear()
Email_input.clear()
phoneNumber_input.clear()


firstname = driver.find_element(By.ID, "firstName")
lastname = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[1]/div[4]/input")
Email = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[2]/div[2]/input")
phoneNumber= driver.find_element_by_xpath(
    "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[4]/div[2]/input")
# jump_input = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[3]/span/div")
submit = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[11]/div/button")

firstname.send_keys("李")
lastname.send_keys("华")
Email.send_keys("666@example.com")

phoneNumber.send_keys("1567140511")
time.sleep(5)
# jump_input.click()
submit.click()

if driver.find_element(By.XPATH,
                       "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[4]/div[2]/input").text == "":
    print("已显示错误信息")
if driver.find_element(By.XPATH,
                       "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[2]/div[2]/input").text == "":
    print("已显示错误信息")
time.sleep(5)
#driver.quit()
