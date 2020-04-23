import requests
from bs4 import BeautifulSoup

def getSoup(search):
    url = 'https://www.goodreads.com'+search
    r = requests.get(url)
    request = r.content
    return BeautifulSoup(request, 'html.parser')

url = '/shelf/show/indonesian-literature?page=1'
soup = getSoup(url)

title = soup.find_all('a', attrs={'class' : 'bookTitle'})
author = soup.find_all('a', attrs={'class' : 'authorName'})

count = 0
sinopsis = []
for t in range(0, 2):#len(title)):
    count += 1
    print("{0}. {1}\nPenulis : {2}"
    .format(count, title[t].text.strip(), author[t].text.strip()))
    url2 = title[t]['href']
    # print(url2)
    soup2 = getSoup(url2)
    sinopsis.append(soup2.find('span', attrs={'style' : 'display:none'}))
    print(str(sinopsis[t].text.strip())+"\n")
