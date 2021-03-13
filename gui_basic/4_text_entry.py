from tkinter import *

root = Tk()

root.title("jimin project")  ## 콘솔창 이름 설정

root.geometry("640x480+100+300")  ## tkinter에서 콘솔 크기 설정가로 * 세로  
                                  ## + " x,y" 좌표

txt  = Text(root, width=30, height=5)

txt.pack()

txt.insert(END,"글자를 입력하세요") ## 기본 텍스트 설정

e = Entry(root,width=30)   ## 이건 한줄짜리
e.pack()

e.insert(0, "한줄만 입력하세요")

def btncmd() :
    print(txt.get("1.0", END)) ### 1.0 첫번째 칸 인덱스에서 가져온다는말 거의 고정이라고 봐도 됨
                              ## 1: 첫번째라인,  0:0번째 칼럼
    print(e.get())

    txt.delete("1.0",END)
    e.delete(0,END)
     
   

btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()  ## 계속 루프 돌려 실행

