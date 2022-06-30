# import libraries 
from bs4 import BeautifulSoup
import requests

# Connect to the Website and pull in data
URL = 'https://www.atptour.com/en/players/rafael-nadal/n409/overview'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
page = requests.get(URL, headers=headers)
response = BeautifulSoup(page.content, "html.parser")
soup =  BeautifulSoup(response.prettify(), "html.parser")

# extracet data from html
# full name
name = soup.find('div', class_="player-profile-hero-name")
first_name = soup.find('div', class_="first-name").text.strip()
last_name = soup.find('div', class_="last-name").text.strip()

# country
country = soup.find('div', class_="player-flag")
flag = country.find("div", class_="player-flag-img").find("img", alt="Country Flag").get("src")
flag = "https://www.atptour.com" + flag
name = country.find("div", class_="player-flag-code").text.strip()

# personnel information
age = soup.find('div', class_="table-big-value").text.strip()[:2]
Weight = soup.find('span', class_="table-weight-lbs").text.strip()
Height = soup.find('span', class_="table-height-ft").text.strip()
information = soup.find_all('div', class_="table-value")
birth_place = information[0]
plays = information[1]
coach = information[2]

# PLAYER EQUIPMENT
equipments = soup.find_all('div', class_="equipment-item-image-wrapper")
racket = print(equipments[0].find('a').get('href'))
t_shirt = print(equipments[1].find('a').get('href'))
shoe = print(equipments[2].find('a').get('href'))