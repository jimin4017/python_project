import requests
import time
from bs4 import BeautifulSoup


url = "https://play.google.com/store/movies"

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
         ,"Accept-Language":"ko-KR,ko"## 한글페이지 요구      
                }
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

movies = soup.find_all("div",attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))


with open("movie.html","w",encoding="utf8") as f:
    # f.write(res.text)
    f.write(soup.prettify())  ## 예쁘게 나옴

time.sleep(3)
# <div class="wXUyZd"><a href="/store/movies/details/%EC%A1%B0%EC%A0%9C?id=FiwG10w0r7o.P" aria-hidden="true" tabindex="-1" class="poRVub"></a></div>
