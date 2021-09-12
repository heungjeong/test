from urllib import request, parse
from bs4 import BeautifulSoup
import os
town = input("현재 날씨가 궁금한 동네의 이름을 입력해주세요 : ")
town_weather = parse.quote(town + "+날씨")
print(town_weather)
url = 'https://search.naver.com/search.naver?ie=utf8&query='+ town_weather

html = request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')
print('현재 \'' + town + '\'은 ' + soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text + '도 입니다.', sep = '')
os.system('puase')