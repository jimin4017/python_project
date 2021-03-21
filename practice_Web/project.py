import requests
from bs4 import BeautifulSoup

def scrape_weather():
    print([오늘의 날씨])
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%A7%88%EC%82%B0%EB%82%A0%EC%94%A8&oquery=%EB%8B%A4%EB%82%98%EC%99%80&tqi=haUcJlp0J1ZssC9KC6RssssssFN-302946"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")

if __name__ == "__main__":
    scrape_weather() 


