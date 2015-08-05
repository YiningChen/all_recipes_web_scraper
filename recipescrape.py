import urllib.request
from bs4 import BeautifulSoup


def scrape( url ):
# data file names
  dataFileName = 'data.txt'
  ingredientsFileName = 'ingredients.txt'
# opens files
  ingredOutf = open(ingredientsFileName,'a')
  dataOutf = open(dataFileName,'a')

# Gets html from URL
  try:
    print("Getting Data from "+url)
    data = urllib.request.urlopen(url).read()
  except URLError as e:
    if hasattr(e, 'reason'):
      print('We failed to reach a server.')
      print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
      print('The server couldn\'t fulfill the request.')
      print('Error code: ', e.code)

# Starting Beautiful Soup
  try:
    bs = BeautifulSoup(data)

# BS gets all ingredients used and saves them to ingredients.txt
    try:
      ingreds = bs.find_all('span', {'class': 'ingredient-name'})
      ingreds = [s.getText().strip() for s in ingreds]
      ingredOutf.write('\n'.join(ingreds))
    except:
      print("beautiful soup ingredient problems")

# BS gets nutritional information and saves to list
    try:
      dataList = []
      dataList.append((bs.find('h1', {'id': 'itemTitle'})).getText().strip())
      dataList.append((bs.find('span', {'id': 'litCalories'})).getText().strip())
      dataList.append((bs.find('span', {'itemprop': 'sodiumContent'})).getText().strip())
      dataList.append((bs.find('span', {'itemprop': 'carbohydrateContent'})).getText().strip())
      nutrients = ['Potassium', 'Protein', 'Vitamin A', 'Vitamin C']

      for nutrient in nutrients:
        try:
          nutrientLabel = bs.find('span', text = nutrient)
          if "Vitamin" in nutrient:
            dataList.append((nutrientLabel.findNextSibling('span', {'class':'right'})).getText().strip())
          else:
            dataList.append((nutrientLabel.next_sibling.next_sibling).getText().strip())
#       Sometimes there are double asterix because not nutrition info may not be accurate
#       due to lack of info from ingredient list. I still want to capture the value.
#       However I also want to make a note of it incase I later want to throw out the value
        except:
          try:
            nutrientLabel = bs.find('span', text = ('** '+nutrient))
            if "Vitamin" in nutrient:
              dataList.append('*'+(nutrientLabel.findNextSibling('span', {'class':'right'})).getText().strip())
            else:
              dataList.append('*'+(nutrientLabel.next_sibling.next_sibling).getText().strip())
          except:
            print("tried with asterix, failed again")

#     Writes nutritional info to data.txt
#     ---HELP---: BETTER WAY OF ADDING THE NEW LINE?
      try:
        dataOutf.write('\n')
        dataOutf.write('\t'.join(dataList))
      except:
        print('data writing failed')
    except:
      print("beautiful soup data problems")
  except:
    print("beautiful soup basic problemo")

# Closing all Files
  ingredOutf.close()
  return


def main():
# for loop that scrapes data from first 10 pages of most popular main dishes
  for i in range (0,11):
    url = 'http://allrecipes.com/recipes/main-dish/main.aspx?evt19=1&st=p&p34=HR_SortByPopularity&vm=l&Page='+str(i)+'#recipes'

#   Gets info from for each page's URL
    try:
      print("Getting pages from: "+url)
      data = urllib.request.urlopen(url).read()
    except URLError as e:
      if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
      elif hasattr(e, 'code'):
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)

#   Starting Beautiful Soup
    try:
      bs = BeautifulSoup(data)
    except:
      print("beautiful soup basic problemo")

#   Calls scrape method for all recipes listed on current page
    try:
      links = bs.find_all('h3', {'class': 'resultTitle'})
      for link in links:
        scrape( link.find_next('a').get('href') )
    except:
      print("link scrape error on page: "+i)

main()
