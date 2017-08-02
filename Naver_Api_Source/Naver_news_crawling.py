from bs4 import BeautifulSoup
from urllib.request import urlopen



url = 'http://news.naver.com'
response = urlopen(url)
point_text = response.read()
soup = BeautifulSoup(point_text,'html.parser')

for news in soup.find_all('div',class_='newsnow_tx_inner'):
    print(news)