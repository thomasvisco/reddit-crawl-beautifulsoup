
import bs4 as BeautifulSoup
from bs4 import BeautifulSoup
import html.parser

html = open('/home/roc/dev/acc_python/reddit-crawl-beautifulsoup/reddit.html')

soup = BeautifulSoup(html, 'html.parser')

print(soup)

#main_table = soup.find('div', attrs={'class':'entry'})

#print(main_table)

#links = main_table.find('p', attrs={'class':'title may-blank outbound'})

#print(links)

#title = soup.find('p', attrs={'class': 'title'})

#print(title)
