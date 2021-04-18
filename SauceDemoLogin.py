from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import platform

platString = (str(platform.platform()))

#if this is your first time, run DriverInstaller first

#Checks if either the chromedriver or chromedriver.exe files exist in your files


if "Window" in platString:
    driver = webdriver.Chrome(executable_path="Resources/chromedriver.exe")
else:
    driver = webdriver.Chrome(executable_path="Resources/chromedriver")




# Takes you to the website
driver.get("http://saucedemo.com/")

#Finds the username and password by there name in the HTML element
username=driver.find_element_by_name("user-name")
password=driver.find_element_by_name("password")

#Sends keystrokes that make the username and password to said elements
username.send_keys("standard_user")
password.send_keys("secret_sauce")

#Presses the Login button
login=driver.find_element_by_id("login-button").click()


#Waits until the element "product_sort_container" is visible inside the html code to start the next portion
element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container")))

#Finds the dropdown menu by its xpath
dropDown = Select(driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div[2]/span/select'))

#select the "lohi" value of said dropdown menu
dropDown.select_by_value('lohi')

#Clicks the baby shirt, then purchase, then back one, all through the xpath, waiting isnt needed because they are all done at once
(driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div')).click()
(driver.find_element_by_xpath('//*[@id="add-to-cart-sauce-labs-onesie"]')).click()
(driver.find_element_by_xpath('//*[@id="back-to-products"]')).click()

#Finds shopping cart and continues via id and xpath respectively
driver.find_element_by_id("shopping_cart_container").click()
driver.find_element_by_id("checkout").click()

#Finds the first name, last name, and postal code boxes via the element names
first_name = driver.find_element_by_id("first-name")
last_name = driver.find_element_by_id("last-name")
postal_code = driver.find_element_by_id("postal-code")

#Sends the name keys
first_name.send_keys("Test")
last_name.send_keys("Name")
postal_code.send_keys("330l7h")

#presses continue and finish
driver.find_element_by_id("continue").click()
driver.find_element_by_id("finish").click()

#closes the driver
driver.close()