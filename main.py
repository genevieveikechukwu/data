from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

url = 'https://cosylab.iiitd.edu.in/recipedb/'

path = Service('C:/Users/dell/Downloads/chromedriver_win32/chromedriver')
chr_options = Options()
chr_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=path, options=chr_options)
driver.get(url)

time.sleep(10)
region = driver.find_element(By.XPATH, "//input[@id='Regs1']")

time.sleep(5)
text = region.send_keys("Northern Africa")

time.sleep(30)
button = driver.find_element(By.XPATH, "//div[@id='test1']/form/div[2]/center/input")

time.sleep(5)
button.click()

time.sleep(30)
rows = driver.find_elements(By.XPATH, "//table/tbody/tr")

title = []

region = []

country = []

serving = []

def get_all_recipes():
    count = 0
    while count < 21:
        rows = driver.find_elements(By.XPATH, "//table/tbody/tr")
        for row in rows:
            title.append(row.find_element(By.XPATH, "./td[1]").text)
            region.append(row.find_element(By.XPATH, "./td[2]").text)
            country.append(row.find_element(By.XPATH, "./td[3]").text)
            serving.append(row.find_element(By.XPATH, "./td[4]").text)

        time.sleep(30)
        next_page = driver.find_element(By.XPATH, "//ul/li[9]") 

        time.sleep(5)
        next_page.click()

        time.sleep(30)
        count += 1
get_all_recipes()

df = pd.DataFrame({'Title': title, 'Region': region, 'Country': country, 'Servings': serving})
df.to_csv('scraped_resipes.csv', index=False)

driver.quit()