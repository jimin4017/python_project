from tkinter import *

root = Tk()

root.title("jimin project")  ## 콘솔창 이름 설정

root.geometry("640x480+100+300")  ## tkinter에서 콘솔 크기 설정가로 * 세로  
                                  ## + " x,y" 좌표

label1 = Label(root,text=" 안녕하세요")
label1.pack()



# photo = PhotoImage(file="C:/Users/정지민/Desktop/python_project/python_project/pygame_basic/background.png")
# label2 =Label(root,image=photo)
# label2.pack()



def change() :
     label1.config(text="또 만나요") ## 안에있는 text 변경

     global photo2
     photo2 =PhotoImage(file="gui_basic/img2.png")
     label1.config(Image=photo2)


btn  = Button(root,text="클릭",command=change)
btn.pack()Q

root.mainloop()  ## 계속 루프 돌려 실행

