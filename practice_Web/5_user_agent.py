import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
####"User-Agent":"여기에 자신의 user agent"

res = requests.get(url,headers=headers)
res.raise_for_status()



# with open("mygoogle.html", "w", encoding="utf8") as f:
#     f.write(res.text)
# import requests
# url = "http://nadocoding.tistory.com"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
# res = requests.get(url, headers=headers)
# res.raise_for_status()
# with open("nadocoding.html", "w", encoding="utf8") as f:
#     f.write(res.text)