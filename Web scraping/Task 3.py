from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np

numberurl = open("table.html")
html=numberurl.read()
soup=BeautifulSoup(html)
tbl=soup.find_all('table')
all_cols=[]
for row in tbl:
    tbl_cols=row.find_all('td')
    all_cols.extend(tbl_cols)
summa=0
for i in all_cols:
    summa=summa+int(i.text)
print('TABLE SUM=',summa, sep='')