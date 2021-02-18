import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

PATH = "D:\chromeEngine\chromedriver.exe"

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
#option.add_argument("--headless")
#option.add_argument("disable-gpu")

driver = webdriver.Chrome(PATH,options=option)

data = ['Yash','1000','yashbakshi3@gmail.com','address']

driver.get('https://docs.google.com/forms/d/e/1FAIpQLScpv_m8QR3jO87snxpWse3VzBQBhkLtOO4WSkbP4e6Sed0tGA/viewform?usp=sf_link')

#actions = ActionChains(driver)

#nameX = '/html/body/div/div[3]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
# rollX = '/html/body/div/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
# emailX = '/html/body/div/div[3]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
# addressX = '/html/body/div/div[3]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea'

count=0

# textboxes = driver.find_elements_by_class_name('quantumWizTextinputPaperinputInput')
# for value in textboxes:
#      value.send_keys(data[count])
#      count += count

# textareaboxes = driver.find_elements_by_class_name("quantumWizTextinputPapertextareaInput")

# for value in textareaboxes:
#     value.send_keys(data[count])
#     count += count

namebox = driver.find_element_by_name('Name')
rollbox = driver.find_element_by_name('Roll no.')
emailbox = driver.find_element_by_name('Email')
addressbox = driver.find_element_by_name('Address')

elementslist = [namebox,rollbox,emailbox,addressbox]

for element in elementslist:
    element.send_keys(data[count])
    count+= count


driver.close()