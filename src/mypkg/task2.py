from selenium import webdriver
import os

os.chdir("C:\\Users\\HUAWEI\\Documents\\Downloads\\chromedriver_win32")
# Open the web browser and navigate to the login page

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

# Enter a valid username and password
username_input = driver.find_element_by_id("username")
password_input = driver.find_element_by_id("password")
username_input.send_keys("tomsmith")
password_input.send_keys("SuperSecretPassword!")

# Click the login button
login_button = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/button/i")
login_button.click()

# Verify that the user is redirected to the home page
assert driver.current_url == "https://the-internet.herokuapp.com/secure"

# Verify that the user's username is displayed on the home page
welcome_message = driver.find_element_by_xpath("/html/body/div[1]/div/div")
assert welcome_message.text.startswith("You logged into a secure area!")


# Click the logout button
logout_button = driver.find_element_by_xpath("/html/body/div[2]/div/div/a/i")
logout_button.click()

print(driver.current_url)

# Close the web browser
# driver.quit()
