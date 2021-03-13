import tkinter.ttk as ttk
from tkinter import *

root = Tk()

root.title("jimin project")  ## 콘솔창 이름 설정

root.geometry("640x480+100+300")  ## tkinter에서 콘솔 크기 설정가로 * 세로  
                                  ## + " x,y" 좌표

values= [str(i) + "일"for i in range(1,32)]
combobox = ttk.Combobox(root,height=5,values=values )
combobox.pack()
combobox.set("카드 결제일")  ## 초기 뜨는 값

readonly_combobox = ttk.Combobox(root,height=5,values=values,state="readonly" )
readonly_combobox.current(0)  ## 0번째 인덱스 값 선택
readonly_combobox.pack()
readonly_combobox.set("카드 결제일")  ## 초기 뜨는 값

def btncmd() :
    print(combobox.get())
    print(readonly_combobox.get())
 
    
btn = Button(root,text="주문",command=btncmd)
btn.pack()



root.mainloop()  ## 계속 루프 돌려 실행

