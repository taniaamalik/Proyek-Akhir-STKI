import requests
from bs4 import BeautifulSoup

# import requests

cookies = {
    'ccsid': '816-4785021-9980172',
    '__qca': 'P0-59280284-1587618929146',
    '__gads': 'ID=a25e1e146646c364:T=1587618929:S=ALNI_MaAFRKvkzlmsvqdELKnvKQ93O_4Dw',
    'never_show_interstitial': 'true',
    '__utmz': '250562704.1587631663.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    'p': 'MKsFRYcLD20vI4_-JpeaUFHBW3MGE20Yjfvwb9XmJs6BjKk0',
    'locale': 'en',
    '__utmc': '250562704',
    'blocking_sign_in_interstitial': 'true',
    'u': 'VUA9pzIpUaiyEPOsT-nSW5bEtZ3aeT8evfxnCgspVZy49zzY',
    '_session_id2': '8a9750ba527499d79b8608b8a9aec6cd',
    '__utma': '250562704.625867263.1587618928.1587738336.1587748717.7',
    '__utmb': '250562704.3.10.1587748717',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'id,en-US;q=0.9,en;q=0.8',
    'If-None-Match': 'W/"ec9c265abc834a0723ced0b5db71eefa"',
}

params = (
    ('page', '9'),
)

# response = requests.get('https://www.goodreads.com/shelf/show/indonesian-literature', headers=headers, params=params, cookies=cookies)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.goodreads.com/shelf/show/indonesian-literature?page=9', headers=headers, cookies=cookies)


# response = requests.get('https://www.goodreads.com/shelf/show/indonesian-literature', headers=headers, params=params, cookies=cookies)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.goodreads.com/shelf/show/indonesian-literature?page=9', headers=headers, cookies=cookies)




def getSoup(search):
    url = 'https://www.goodreads.com'+search
    r = requests.get(url, headers=headers, params=params, cookies=cookies)
    request = r.content
    return BeautifulSoup(request, 'html.parser')

# r = requests.get('https://www.goodreads.com/shelf/show/indonesian-literature', headers=headers, params=params, cookies=cookies)
# request = r.content
search = '/shelf/show/indonesian-literature'
soup = getSoup(search)

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
