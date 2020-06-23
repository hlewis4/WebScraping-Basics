from selenium import webdriver
driver = webdriver.Chrome("C:/Users/hashi/webDrivers/chromedriver.exe")
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('Hello World')
showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()

#test2
addField1 = driver.find_element_by_xpath('//*[@id="sum1"]')
addField1.send_keys('10')
addField2 = driver.find_element_by_xpath('//*[@id="sum2"]')
addField2.send_keys('20')
addButton = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
addButton.click()