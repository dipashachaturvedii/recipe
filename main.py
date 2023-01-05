#install all the requirements
#pip install bs4 requests html5lib

import requests
from bs4 import BeautifulSoup
url ="https://www.vegrecipesofindia.com/recipes/?fwp_recipe_cuisines=indian"
#get html
r = requests.get(url)
htmlContent = r.content
print(htmlContent)

#parse html
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify)

#traverse tree
#commonly used types of object
#1. Tag print(type(title))
#2. NavigableString print(type(title.string))
#3. BeautifulSoup print(type(soup))
#4. Comment markup = "<p><!--this is a comment--></p>"
#soup2 = BeautifulSoup(markup)
#print(type(soup2.p.string))
#exit()

title = soup.title
print(title)
#get all anchor tags or script
paras = soup.find_all('p')
print(paras)

#print(soup.find('p').get_text)
#print(soup.find('p')['class'])
#find elements that have lead class
#print(soup.find_all("p", class_="lead"))

#get all links of page
anchors = soup.find_all('a')
print(anchors)
print(soup.title)
# Getting the name of the tag
print(soup.title.name)
 
# Getting the name of parent tag
print(soup.title.parent.name)

all_links = set()
for link in anchors:
       linkText = "https://www.vegrecipesofindia.com" + link.get('href')
       all_links.add(linkText)
       print(linkText)
