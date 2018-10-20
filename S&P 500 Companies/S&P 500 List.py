from bs4 import BeautifulSoup
import requests
import pandas as pd

resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
soup = BeautifulSoup(resp.text,'html.parser')

# All data are in table with class wikitable sortable
table = soup.find('table', {'class': 'wikitable sortable'})
tickers=[]


for row in table.findAll('tr')[1:]:
    ticker = row.findAll('td')[0].text
    company = row.findAll('td')[1].text
    tickers.append((ticker,company))

# print (tickers)

df = pd.DataFrame(tickers, columns =['Comapny Ticker','Company Name'])

df.to_csv('E:\Pythoncode\DataScraping\S&P 500 Companies\S&P 500 Company List.csv', index = False)
