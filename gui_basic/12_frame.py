import time
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()

root.title("jimin project")  ## 콘솔창 이름 설정

root.geometry("640x480+100+300")  ## tkinter에서 콘솔 크기 설정가로 * 세로  
                                  ## + " x,y" 좌표

frame_burger = Frame(root,relife="solid",bd=1)
frame_burger.pack()

Button(frame_burger,text="햄버거").pack()
Button(frame_burger,text="치즈버거").pack()
Button(frame_burger,text="치킨버거").pack()
root.mainloop()  ## 계속 루프 돌려 실행

