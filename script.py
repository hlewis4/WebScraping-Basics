#WEB SCRAPING ON ONE WEB PAGE
import requests
from bs4 import BeautifulSoup
url = 'http://quotes.toscrape.com/'
response = requests.get(url)

#parsing the response with lxml parser
soup = BeautifulSoup(response.text, 'lxml')
# print("HI")
# print(soup)

#find where your required content is by inspecting your html
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_ = 'tags')

# for q in quotes:
#     print(q.text )

#print author and corresponding quote
for i in range(0,len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quoteTags = tags[i].find_all('a', class_='tag')
    for quoteTag in quoteTags:
        print(quoteTag.text)
