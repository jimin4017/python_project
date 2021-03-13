import time
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *


root = Tk()

root.title("jimin project")  ## 콘솔창 이름 설정

root.geometry("640x480+100+300")  ## tkinter에서 콘솔 크기 설정가로 * 세로  
                                  ## + " x,y" 좌표

txt = Text(root,width= 30 ,height=5 )
txt.grid(row=0, column=0)



def create_new_file() :
    text_file = open("score.txt","a",encoding="uft8")
    txt.insert(END,text_file)

menu = Menu(root)

menu_file = Menu(menu,tearoff=0)
menu_file.add_command(label="New File",command=create_new_file)
menu_file.add_command(label="New window" )
menu_file.add_separator()
menu_file.add_command(label="Open File....")
menu.add_cascade(label="File", menu=menu_file)

txt.pack()

root.config(menu=menu)

root.mainloop()  ## 계속 루프 돌려 실행
