from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import pandas as pd
import time

website = "https://www.allrecipes.com/recipes/226/world-cuisine/african/"
path = Service('C:/Users/dell/Downloads/chromedriver_win32/chromedriver')

chr_options = Options()
chr_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=path, options=chr_options)
driver.get(website)
# count = 0
# final_count = 63
# while count <= final_count:
all_recipe_card = driver.find_element('xpath', "//div[@class='card__content']")
# for card in all_recipe_card:
all_recipe_card.click()
# count += 1

time.sleep(30)
article = driver.find_element(By.TAG_NAME, "article")
ingredient_for_cooking = article.find_elements('xpath', "./div[3]/div[3]/div[4]/div/ul/li")
directions = article.find_elements('xpath', './div[3]/div[3]/div[5]/div/ol/li')

title = []
image = []
serving = []
preparation_time = []
cook_time = []
course = []
cuisine = []
ingredients = []
instructions = []


# find title
title.append(article.find_element(By.XPATH, "./div[2]/h1").text)
print(title)

# find image
time.sleep(60)
picture = driver.find_element('xpath', "//div[@class='figure-media']/div/img").get_attribute("srcset")
time.sleep(60)
image.append(picture)
print(picture)

# # find serving
recipe_prep = driver.find_element(By.XPATH, '//*[@id="recipe-details_1-0"]/div[1]')
serving.append(recipe_prep.find_element(By.XPATH, './div[4]/div[2]').text)

# find prep_time
preparation_time.append(recipe_prep.find_element(By.XPATH, './div[1]/div[2]').text)

# find cook_time
cook_time.append(recipe_prep.find_element(By.XPATH, './div[2]/div[2]').text)

# find course
course.append("Main")
# print(course)

# find cuisine
cuisine.append("Morrocan")

# find ingredient
for ingredient in ingredient_for_cooking:
    ingredients.append(ingredient.text)
    # print(ingredient.text)

# find Instruction
for direction in directions:
    instructions.append(direction.text)
    # print(direction.text)


a = {'Title': title, 'Image': image, 'Servings': serving, 'Preparation Time': preparation_time,
 'Cook Time': cook_time, 'Course': course, 'Cuisine': cuisine, 
 'Ingredients': ingredients, 'Instructions': instructions}
df = pd.DataFrame.from_dict(a, orient='index')
df = df.transpose()
df.to_csv('recipes.csv', index=False)
# driver.quit()