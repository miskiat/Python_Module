import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
       url = 'https://buybetter.ng/product-category/bath-body/page/' + str(page)
       source_code = requests.get(url)
       plain_text = source_code.text
       soup = BeautifulSoup(plain_text)
       for link in soup.findAll('a', {'class': 'product-title'}):
           href = link.get('herf')
           print(href)
       page += 1

trade_spider(1)




