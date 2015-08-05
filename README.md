## All Recipes Web Scraper
scraped top 200 recipes from all recipes.com and saved ingredients + nutritional info for data analysis

##Breakdown of Files:
**￼recipescrape.py**
script that took nutritional information from the 200 most popular main dishes on allrecipes.com and stored them in a text file
(It also stored all the ingredients so I can play around with text analysis later)

**cleanrecipe.py**
script that then cleans the data above.

**Popular Recipes Nutrition.xlsx**
quick statistical calculations

**data.txt**
original data scraped via recipescrape.py 

**cleandata.txt**
cleaned data (removed ‘mg’s and g’s)

**ingredients.txt**
all ingredients from every recipe. Hope to play around with this later - maybe counts for most common ingredient

#￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼Statistics:
Average Calories per Serving: 422

￼￼￼￼Average Sodium per Serving:890 mg

Average Vitamin C per serving: 21% of daily serving

Min Calories per Serving: 135

Max Calories per Serving: 1109

