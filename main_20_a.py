#from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option(name='detach', value=True)

driver = webdriver.Chrome(options=options)

driver.get('https://www.lambdatest.com/selenium-playground/jquery-dropdown-search-demo')
driver.maximize_window()

click_drop = driver.find_element(By.XPATH, '//*[@id="__next"]/div/section[2]/div/div/div/div[1]/div[2]/span/span[1]')
click_drop.click()
click_drop = driver.find_element(By.XPATH, '/html/body/span/span/span[1]/input')
click_drop.send_keys('India')
click_drop.send_keys(Keys.ENTER)

