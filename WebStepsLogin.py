from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

email = input("what is your email?")
password = input("what is your password")
#Calls the chrome driver
#Calls the chrome driver
driveRequest = input("What is your OS, windows, linux or mac?(w/l/m)")
if (driveRequest == "w"):
    driver = webdriver.Chrome(executable_path="Resources/chromedriver.exe")
elif (driveRequest == "l"):
    driver = webdriver.Chrome(executable_path="Resources/chromedriverlinux")
elif(driveRequest == "m"):
    driver = webdriver.Chrome(executable_path="Resources/chromedrivermac")

# Takes you to the website
driver.get("https://mapmanager.steps.me")

#Finds the username and password by there name in the HTML element
element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[5]/button')))
(driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[5]/button')).click()

element2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[3]/input")))

EmailXpath=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[3]/input")
passwordXpath=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[4]/input")

EmailXpath.send_keys(email)
passwordXpath.send_keys(password)

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[6]/div/button").click()

