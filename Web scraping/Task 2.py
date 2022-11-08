from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen("https://en.wikipedia.org/wiki/Web_scraping")
html=response.read().decode('utf-8')
#print(html)
soup = BeautifulSoup(html)
#print(soup)

for link in soup.find_all('a'):
  if link.has_attr('href'):
    s=link.get('href')
    if (s.startswith("https")):
      print(link.get('href'))