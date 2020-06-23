from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome("C:/Users/hashi/webDrivers/chromedriver.exe")
driver.maximize_window()
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
source = driver.find_element_by_xpath('//*[@id="box3"]')
dest = driver.find_element_by_xpath('//*[@id="box103"]')
#to use drag and drop you need action chain library
actions = ActionChains(driver)
actions.drag_and_drop(source,dest).perform()