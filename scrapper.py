import requests
from bs4 import BeautifulSoup

url = 'http://fapl.ru'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
block_news_list = soup.find_all('div', {'class': 'block news'})

with open('news.txt', 'w', encoding='utf-8') as f:
    for block_news in block_news_list:
        h3_tag = block_news.find('h3')
        if h3_tag is not None:
            f.write(h3_tag.text.strip() + '\n' + '++++++++++' + '\n')