import os
# print(os.getcwd()) # current working directory 현재 작업 공간
# os.chdir("rpa_basic") # rpa_basic 으로 작업 공간 이동
# print(os.getcwd())
# os.chdir("..") # 부모 폴더로 이동
# print(os.getcwd())
# os.chdir("../..") # 조부모 폴더로 이동
# print(os.getcwd())
# os.chdir("c:/") # 주어진 절대 경로로 이동
# print(os.getcwd())



# fiel_path = os.path.join(os.getcwd)
# os.path.join(os.getcwd(),"my_file.txt")


### 파일 목록 가져오기

# print(os.listdir())
# print(os.listdir("rpa_basic"))
# 주어진 폴더 항목 검색

result = os.walk("rpa_basic") ### 폴더랑 파일을 다겨옴

# print(result)

## <generator object walk at 0x0000024B97135040> 라고 출력해줌

# for root, dirs,files in result :
#     print(root, dirs,files ,"\n")
# ## 모든 파일 잘 나옴

## 특정 파일 찾기

# name ="11_file.py"

# result = []

# for root, dirs,files in os.walk(".") :

#     if name in files :
#         result.append(os.path.join(root,name))
## ['.\\rpa_basic\\3_window\\11_file.py']
# for root, dirs,files in os.walk(os.getcwd()) :

#     if name in files :
#         result.append(os.path.join(root,name))
                
# print(result)
## 'C:\\Users\\정지민\\Desktop\\python_project\\python_project\\rpa_basic\\3_window\\11_file.py'

import fnmatch

# patternn = "*.png"
# result = []

# for root, dirs, files in os.walk(".") : 
#     for name in files:
#         if fnmatch.fnmatch(name,patternn) :
#             result.append(os.path.join(root,name))

# print(result)

# ### patternn = "*.png" 라고 하면 끝에 png라고 적힌 파일을 가져옴

# print(os.path.isdir("rpa_basic"))   ## rpa_basic은 폴더인가? True
# print(os.path.isfile("rpa_basic"))  ## rpa_basic은 파일인가? False
# print(os.path.isfile)

## 파일 만들기

# open("new_file.txt","a").close()

import shutil # 파일삭제

shutil.copy("run_btn.png","test_folder")

### run_btn.png 폴더를 fest_folder에 저장



def siyeong () :
    print("웅이")

doong_answer  = 6 

for i in range (,doong_aswer) :
    siyeong()





