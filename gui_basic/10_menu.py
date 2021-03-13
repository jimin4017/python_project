import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()

root.title("jimin project")  ## 콘솔창 이름 설정

root.geometry("640x480+100+300")  ## tkinter에서 콘솔 크기 설정가로 * 세로  
                                  ## + " x,y" 좌표


# progressbar = ttk.Progressbar(root,maximum=100,mode="determinate")
# # indeterminate == 값이 정해져있지 않음
# # determinate   == 값이 맥시멈 까지 정해져있음
# progressbar.start(30)  # 30ms 마다 움직임
# progressbar.pack()
# def btncmd() :
#     pass



# btn = Button(root,text="주문",command=btncmd)
# btn.pack()
def create_new_file() :
    print("새 파일을 만듭니다. ")

# 메뉴
menu = Menu(root)

menu_file = Menu(menu,tearoff=0)
menu_file.add_command(label="New File",command=create_new_file)
menu_file.add_command(label="New window" )
menu_file.add_separator()
menu_file.add_command(label="Open File....")

menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable") # 비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

# exit 메뉴
menu.add_cascade(label="Edit")

# language 메뉴 추가 (radio 벝느을 톡해서 1택) 
menu_lang = Menu(menu,tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language",menu=menu_lang)

# view 메뉴
menu_view = Menu(menu,tearoff=0)
menu_view.add_checkbutton(label="Python")
menu.add_cascade(label="Language",menu=menu_view)
root.config(menu=menu)
root.mainloop()  ## 계속 루프 돌려 실행

