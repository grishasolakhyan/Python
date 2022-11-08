import csv 
from urllib.request import urlopen 
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Galilean_moons' 

html = urlopen(url) 
soup = BeautifulSoup(html, 'html.parser') 

table = soup.find_all('table')[0] 
rows = table.find_all('tr') 

File = open('my_html_data_to_csv.csv', 'wt+',encoding='utf-8') 
Data = csv.writer(File) 
try: 
    for row in rows: 
        FilteredRow = [] 
        for cell in row.find_all(['td', 'th']): 
            FilteredRow.append(cell.get_text().strip(' ').strip('\n')) 
            Data.writerow(FilteredRow) 
        print(FilteredRow,"\n") 
finally: 
    File.close()