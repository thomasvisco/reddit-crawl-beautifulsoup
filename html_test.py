
import bs4 as BeautifulSoup
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('/home/tav/dev/acc/reddit-crawl-beautifulsoup/reddit.html'), 'html.parser')

#print(soup)

main_table = soup.find('div', attrs={'class':'entry'})

#print(main_table)

links = main_table.find('p', attrs={'class':'title may-blank outbound'})

#print(links)

title = soup.find('p', attrs={'class': 'title'})

print(title)