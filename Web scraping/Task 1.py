from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

x=10
y=10
arr1 = [[0 for j in range(1,y+1)] for i in range(1,x+1)]
for i in range(1,x+1):
    for j in range(1,y+1):
        arr1[i-1][j-1]=i*j
print(arr1)
arr2=np.array(arr1)
print(arr2)

fout=open("SITE.html", 'w', encoding='utf8')

print('''<!DOCTYPE html>
      <head>
      <title>TABLE</title>
      </head>
      <body>
      <p1>ТАБЛИЦА ССЫЛОК</p1>
      <table>''', file=fout)

for i in range(arr2.shape[0]):
    print('''<tr>''', file=fout)
    for j in range(arr2.shape[1]):
        print('<td>',"<a href=http://"+str(arr2[i][j])+".ru>"+"<B>"+str(arr2[i][j])+"</B>"+"</a>",'</td>', file=fout)
print('''</table>
      </body>
      </html>''', file=fout)
fout.close()