from tkinter import *

root = Tk()

root.title("jimin project")  ## 콘솔창 이름 설정

root.geometry("640x480+100+300")  ## tkinter에서 콘솔 크기 설정가로 * 세로  
                                  ## + " x,y" 좌표


file_frame = Frame(root)
file_frame.pack()

btn_Add_file = Button(file_frame, text="파일추가")
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, text="선택상자")
btn_del_file.pack(side="right")

list_frame = Frame(root)
list_frame.pack()

list_file = Listbox(list_frame)


root.resizable(True.False)  #x,y 변경 불가

root.mainloop()  ## 계속 루프 돌려 실행

