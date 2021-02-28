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

p_var2 = DoubleVar() ## 실수를 위해 Double
 
progressbar2 = ttk.Progressbar(root,maximum = 100,length=150,variable=p_var2)
progressbar2.pack()

def btncmd2() :
    for i in range(1,101) :
        time.sleep(0.01) # 0.01초 대기

        p_var2.set(i)
        progressbar2.update()
        print(p_var2.get())
    

btn = Button(root,text="시작",command=btncmd2)
btn.pack()

root.mainloop()  ## 계속 루프 돌려 실행

