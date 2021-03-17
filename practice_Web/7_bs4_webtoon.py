import requests
from bs4 import BeautifulSoup

url ="https://comic.naver.com/webtoon/weekday.nhn"
res =requests.get(url)
res.raise_for_status()

# soup = BeautifulSoup(res.text,"lxml")

# cartoons = soup.find_all("a",attrs={"class":"title"})
# for cartoon in cartoons :
#     print(cartoon.get_text())

###############################################  웹툰 이름 타이틀 가져오기

for car





