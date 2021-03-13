from tkinter import *

root = Tk()

root.title("jimin project")  ## 콘솔창 이름 설정

root.geometry("640x480+100+300")  ## tkinter에서 콘솔 크기 설정가로 * 세로  
                                  ## + " x,y" 좌표

btn1 = Button(root,text="버튼 1")
btn1.pack()

btn2 = Button(root,padx=5 ,pady=10, text ="버튼2") # padx =x 가로 , pady=  y 높이
btn2.pack()
# vs
# btn3 =Button(root,width=10,height=5,text="버튼3")
# btn3.pack()  조금 다름

btn4 = Button(root,fg="red",bg="yellow",text="버튼4") # fg 버튼 배경 bg 버튼색
btn4.pack()


txt = Text(root,width= 30 ,height=5 )
txt.pack()

root.mainloop()  ## 계속 루프 돌려 실행

