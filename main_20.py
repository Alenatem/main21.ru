from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option(name='detach', value=True)

driver = webdriver.Chrome(options=options)


def set_up():
    driver.get('http://www.saucedemo.com/')
    driver.maximize_window()


def login():
    user_name = driver.find_element(By.ID, "user-name")
    user_name.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")


    login_button = driver.find_element(By.XPATH, '//input[@id="login-button"]')
    login_button.click()

set_up()
login()

select = Select(driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select'))
sleep(2)
select.select_by_visible_text("Price (low to high)")