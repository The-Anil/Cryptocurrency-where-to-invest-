import bs4 as bs
import urllib.request
import pandas as pd

sauce = urllib.request.urlopen('https://coinmarketcap.com/').read()

soup = bs.BeautifulSoup(sauce, 'lxml')

#print(soup.find_all('p'))
global t_data,table

for t_data in soup.find_all('td'):
    #print(t_data)
    for table in t_data.find_all('a',class_= 'currency-name-container'):
        print(table.text+" : \t",end="")

    for table in t_data.find_all('a', class_='price'):
        print(table.text)
