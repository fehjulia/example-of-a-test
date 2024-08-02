from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.google.com/')
sleep(10)

driver.find_element('xpath','//*[@id="APjFqb"]').send_keys('teste')
driver.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

input()