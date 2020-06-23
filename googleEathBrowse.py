from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
url = 'https://www.google.com/earth/'
driver = webdriver.Chrome("C:/Users/hashi/webDrivers/chromedriver.exe")
driver.get(url)
#creating an explicit wait using webdriver wait()
wait = WebDriverWait(driver, 10)
#this condition will create an exception and wait for 10sec

launchButton = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/header/div/nav[1]/ul[2]/li[2]/a/span/span')))
launchButton.click()
