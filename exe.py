import requests

from bs4 import BeautifulSoup


city = input('Please enter City To Search Weather update For : ')
url = "https://www.google.com/search?q=" + "weather" + city
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
data = str.split('\n')
time = data[0]
sky = data[1]
listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
strd = listdiv[5].text
pos = strd.find('Wind')
other_data = strd[pos:]
x=temp.replace('-','minus ')
x.replace('C',' Centigrade')

# printing all data
print('current weather update for '+city+' and time is ' + time)
print("Temperature . "+ x)

print("Sky Description: "+ sky)
