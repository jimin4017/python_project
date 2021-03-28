import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?&page="

filename = "시가총액 1-200.csv"
f = open(filename,"w",encoding="utf8")
writer = csv.writer(f)

for page in range(1,5) :
    res= requests.get(url+str(page),newline="")
    # newline= "" 의 효과
    # 줄바꿈을 줄여줌
    # 1번 데이터                 1번데이터
    #                  --->     2번데이터
    # 2번 데이터
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
ddddd
    data_rows= soup.find("table",attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows :
        columns = row.find_all("td")

        if len(columns) <= 1:
            continue
        data = [column.get_text().strip() for column in columns]
        print(data)




    
