import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument('--ignore-certificate-errors')
# options.add_argument("--disable-cache")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

wait = WebDriverWait(driver, 15, poll_frequency=1)
action = ActionChains(driver)


def test_text_box():
    driver.get("https://demoqa.com/text-box")
    name = ("xpath", '//input[@id ="userName"]')
    email = ('xpath', '//input[@id ="userEmail"]')
    adres = ('xpath', '//textarea[@id ="currentAddress"]')
    permanentAddr = ('xpath', '//textarea[@id ="permanentAddress"]')
    submit_button = ('xpath', '//button[@id = "submit"]')

    driver.find_element(*name).send_keys("Igor")
    driver.find_element(*email).send_keys("igor01@gmail.com")
    driver.find_element(*adres).send_keys("Moscow, Bolshaya Nikitskaya, Dom 13, kv 154")
    driver.find_element(*permanentAddr).send_keys("Moscow, Bolshaya Nikitskaya, Dom 13, kv 154")
    driver.execute_script("window.scrollTo(0,1300)")
    wait.until(EC.visibility_of_element_located(submit_button))
    driver.find_element(*submit_button).click()


