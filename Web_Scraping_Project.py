import requests
from bs4 import BeautifulSoup

def beautiful_soup(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")
    return soup

soup = beautiful_soup('https://news.google.com/?hl=en-IN&gl=IN&ceid=IN:en')
all_headlines=soup.find_all('a', {'class': 'VDXfz'})

for headlines in all_headlines:
    print(headlines.find_next('span').text)
