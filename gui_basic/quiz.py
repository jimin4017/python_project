import time
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
import os


root = Tk()

root.title("jimin project")  ## 콘솔창 이름 설정

root.geometry("640x480+100+300")  ## tkinter에서 콘솔 크기 설정가로 * 세로  
                                  ## + " x,y" 좌표


filename = "mynote.txt"

def create_new_file() :  ## 파일이 있으면 TRUE 
    if os.path.isfile(mynote.txt) :
        with open(filename,"r",encoding=="uft8") as file:
            txt.insert(END,file.read())

def save_file() :   # 모든 내용 가져오기
    with open (filename,"w",encoding="utf8")  as file :
        file.write(txt.get("1.0",END))

menu = Menu(root)

menu_file = Menu(menu,tearoff=0)
menu_file.add_command(label="New File",command=create_new_file)
menu_file.add_command(label="New window" )
menu_file.add_separator()
menu_file.add_command(label="Open File....")
menu.add_cascade(label="File", menu=menu_file)

txt= Text(root)


# 스크롤바

Scrollbar = Scrollbar(root)
Scrollbar.pack(side="right",fill="y")

txt.pack(side="left" ,fill="both",expand=TRUE)

root.config(menu=menu)

root.mainloop()  ## 계속 루프 돌려 실행
