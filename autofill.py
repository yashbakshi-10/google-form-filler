from os import times
import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
import time


PATH = "D:\chromeEngine\chromedriver.exe"

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
# option.add_argument("--headless")
# option.add_argument("disable-gpu")

driver = webdriver.Chrome(PATH, options=option)

data = ['Yash', '1000', 'yashbakshi3@gmail.com', 'address']

driver.get('https://docs.google.com/forms/d/e/1FAIpQLScpv_m8QR3jO87snxpWse3VzBQBhkLtOO4WSkbP4e6Sed0tGA/viewform?usp=sf_link')


boxes = driver.find_elements_by_class_name(
    'quantumWizTextinputPaperinputInput')
addressbox = driver.find_element_by_class_name(
    'quantumWizTextinputPapertextareaInput')

# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "element"))


for i in range(0, 3):
    boxes[i].send_keys(data[i])

addressbox.send_keys(data[3])
# for element in elementslist:
#     element.send_keys(data[count])
#     count += count

time.sleep(10)

driver.close()
