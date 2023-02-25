
from bs4 import BeautifulSoup
import requests

date = input("In which year do you want to travel in ? Enter the date in format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
charts = response.text

soup = BeautifulSoup(charts, 'html.parser')
songs = soup.find_all(name="h3", class_="a-no-trucate")
song =[song.getText().strip() for song in songs]
print(song)