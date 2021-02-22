#from bs4 import BeautifulSoup
#soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
#print(soup.prettify())

#import glob # 경로내의 폴더 파일 목록 조회
#print(glob.glob("*.py") )## 확장자가 .py 인거다

import os
print(os.getcwd())

folder = "sample_dir"

if os.path.exists(folder) :
    print("이미 존재하는 파일 입니다.")
else:
    os.makedirs(folder)
    print(folder,"폴더를 생성하였습니다.")


import time
print(time.localtime())