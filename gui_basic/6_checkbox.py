from tkinter import *

root = Tk()

root.title("jimin project")  ## 콘솔창 이름 설정

root.geometry("640x480+100+300")  ## tkinter에서 콘솔 크기 설정가로 * 세로  
                                  ## + " x,y" 좌표


chkvar= IntVar() ##chvar에 int 정수 값을 넣는다
chkbox = Checkbutton(root,text="오늘하루  보지 않기",variable=chkvar)
chkbox.pack()

chkvar2 =IntVar()
chkbox =Checkbutton(root,text="일주일동안 보지 않기",variable=chkvar2)


def btncmd() :
    print(chkvar.get())
    print(chvar2.get())
    


btn =Button(root,text="클릭",command=btncmd)
btn.pack()



     
   

btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()  ## 계속 루프 돌려 실행

