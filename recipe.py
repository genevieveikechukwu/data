from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import json
import pandas as pd
import time

# website = "https://www.allrecipes.com/recipes/226/world-cuisine/african/"
path = Service('C:/Users/dell/Downloads/chromedriver_win32/chromedriver')

chr_options = Options()
chr_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=path, options=chr_options)
# driver.get(website)



title = []
image = []
serving = []
preparation_time = []
cook_time = []
course = []
cuisine = []
ingredients = []
instructions = []
links = []
count = 0

# Looping through the whole cards

website = "https://www.allrecipes.com/recipes/226/world-cuisine/african/"
driver.get(website)
time.sleep(30)
all_recipe_card = driver.find_elements('xpath', "//div[@data-chunk='36']/a")

for card in all_recipe_card:
    time.sleep(1)
    links.append(card.get_attribute("href"))
    # print(links)
for link in links:
    website = link
    driver.get(website)
    count += 1
    if count < 3:
        time.sleep(5)
        article = driver.find_element(By.TAG_NAME, "article")

        time.sleep(5)
        ingredient_for_cooking = article.find_elements('xpath', "./div[3]/div[3]/div[4]/div/ul/li")

        time.sleep(3)
        directions = article.find_elements('xpath', './div[3]/div[3]/div[5]/div/ol/li')
        # find title

        time.sleep(3)
        title.append(article.find_element(By.XPATH, "./div[2]/h1").text)
        print(title)

        # find image
        time.sleep(5)
        try:
            picture = driver.find_element('xpath', "//div[@class='figure-media']/div/img").get_attribute("srcset")

            time.sleep(3)
            image.append(picture)
            print(image)
        except:
            image.append('none')
            print(image)

        # # find serving
        time.sleep(5)
        recipe_prep = driver.find_element(By.XPATH, '//*[@id="recipe-details_1-0"]/div[1]')

        time.sleep(3)
        serving.append(recipe_prep.find_element(By.XPATH, './div[4]/div[2]').text)

        # find prep_time
        time.sleep(2)
        preparation_time.append(recipe_prep.find_element(By.XPATH, './div[1]/div[2]').text)

        # find cook_time
        time.sleep(3)
        cook_time.append(recipe_prep.find_element(By.XPATH, './div[2]/div[2]').text)

        # find course
        time.sleep(3)
        course.append("Meal")
        # print(course)

        # find cuisine
        time.sleep(5)
        try:
            country = driver.find_element(By.XPATH, '//*[@id="mntl-text-link_2-0-3"]/span')
            cuisine.append(country.text)
        except:
            cuisine.append("African")

        # find ingredient
        for ingredient in ingredient_for_cooking:
            time.sleep(5)
            ingredients.append(ingredient.text)
            # print(ingredient.text)

        # find Instruction
        for direction in directions:
            time.sleep(5)
            instructions.append(direction.text)
            time.sleep(5)
    
        
            # print(direction.text)



        recipe_dict = {'Title': title, 'Image': image, 'Servings': serving, 'Preparation Time': preparation_time,
        'Cook Time': cook_time, 'Course': course, 'Cuisine': cuisine, 
        'Ingredients': ingredients, 'Instructions': instructions}


        with open("recipes.json", "w") as r:
            json.dump(recipe_dict, r, indent=4)
    else:
        driver.quit()



"""
Keeping the code below for reference
"""
# # # df = pd.DataFrame.from_dict(a, orient='index')
# # # df = df.transpose()
# # # df.to_csv('recipes.csv', index=False)
# driver.quit()