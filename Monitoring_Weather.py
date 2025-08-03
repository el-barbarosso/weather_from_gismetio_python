import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://www.gismeteo.ru/weather-mariupol-5104/now/"
headers = {
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
   }
response = requests.get(url, timeout=10, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
nowtime = datetime.now().strftime("%d.%m.%Y %H:00")
if response.status_code == 200:
    temp_tag = soup.find("temperature-value")
    temperature = temp_tag.get('value')
    weather_report = soup.find(class_="now-desc").text
    temperature_feeling = soup.find(class_="now-feel").find("temperature-value")
    temp_feel = temperature_feeling.get("value")
    print(f"Погода в городе Мариуполь в {nowtime} \nсоставляет {temperature}, \nпо ощущению {temp_feel}, \nа погода {weather_report}")
    
else:
    print(f"Код {response.status_code}")