
from bs4 import BeautifulSoup

html = open('/home/roc/dev/acc_python/reddit-crawl-beautifulsoup/reddit.html')

soup = BeautifulSoup(html, 'html.parser')

main_table = soup.find('div', attrs={'class':'entry'})

links = main_table.find('p', attrs={'class':'title may-blank outbound'})    #not working

title = soup.find('p', attrs={'class': 'title'})

print(title)
