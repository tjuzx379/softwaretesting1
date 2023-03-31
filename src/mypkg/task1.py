from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os


os.chdir("C:\\Users\\HUAWEI\\Documents\\Downloads\\chromedriver_win32")
# Open the web browser and navigate to the login page

driver = webdriver.Chrome()
driver.get("https://www.google.com")
search_input = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
search_input.send_keys("selenium")
# Click the search button
search_input.send_keys(Keys.ENTER)

