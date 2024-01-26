import requests
from bs4 import BeautifulSoup

url = "https://ncrtc.in/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
print(soup.prettify())

#!!!!warning!!!!
#still in developmental stage
