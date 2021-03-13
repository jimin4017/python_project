from tkinter import *

root = Tk()

root.title("jimin project")  ## 콘솔창 이름 설정

root.geometry("640x480+100+300")  ## tkinter에서 콘솔 크기 설정가로 * 세로  
                                  ## + " x,y" 좌표

burger_var = IntVar()
btn_burger1 = Radiobutton(root,text="불고기 버거",value=1,variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root,text="치즈 버거",value=2,variable=burger_var)
btn_burger3 = Radiobutton(root,text="햄치즈 버거",value=3,variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()


def btncmd() :
    print(burger_var.get())
    print(drink_var.get())
    
btn = Button(root,text="주문",command=btncmd)
btn.pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root,text="사이다",value="사이다",variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root,text="콜라",value=2,variable=drink_var)     
btn_drink3 = Radiobutton(root,text="사이다",value=3,variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

root.mainloop()  ## 계속 루프 돌려 실행

