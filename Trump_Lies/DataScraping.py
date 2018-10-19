# request library is used to get data from webpage !
import requests as req

# .get is used to get a webpage
r = req.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')

# print first 500 character of HTML
# print (r.text[0:500])


from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text,'html.parser')

# This is the format of HTML from which I have to parse the text
# <span class="short-desc"><strong> Date </strong> Lie <span class="short-truth"><a href="URL" target="_blank"> Explanation </a></span></span>
# Datas to be parsed "Date", "Lie", "URL", "Explanation"

results = soup.find_all('span', attrs = {'class':'short-desc'})
#print(len(results))

# Creating and empty record array
record = []

for result in results:
    Date = (result.find('strong').text[0:-1] + ',2017')  
    Lie = (result.contents[1][1:-2])
    Explanation = (result.contents[2].find('a').text[1:-1])
    URL = (result.contents[2].find('a')['href'])
    record.append((Date,Lie,Explanation,URL))


import pandas as pd

# using pandas DataFrame function to record data from array to df 
df = pd.DataFrame(record, columns =['Date', 'Lie', 'Explanation', 'URL'])

# converting string Date to datetime format using pandas to_datetime function
df['Date'] = pd.to_datetime(df['Date'])

df.to_csv('E:\Pythoncode\DataScraping\Trump_Lies\TrumpLies.csv', index = False)
    
