import requests
from bs4 import BeautifulSoup

url ="https://comic.naver.com/webtoon/weekday.nhn"
res =requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a)
# print(soup.a.attrs)

# print(soup.find(attrs={"class":"Nbtn_upload"}))  ### 클래스가 ="Nbtn_upload"인 a 엘리먼트 찾기

rank1 = soup. find("li",attrs={"class":"rank01"})
# print(rank1.a)
# print(rank1.next_sibling)
# print(rank1.next_sibling.next_sibling)

# print(rank1.parent)
rank1.find_next_sibling("li")

