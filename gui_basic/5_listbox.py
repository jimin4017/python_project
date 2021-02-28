from tkinter import *

root = Tk()

root.title("jimin project")  ## 콘솔창 이름 설정

root.geometry("640x480+100+300")  ## tkinter에서 콘솔 크기 설정가로 * 세로  
                                  ## + " x,y" 좌표


listbox = Listbox(root,selectmode="extend",height=0 ) ## extend= 여러개 single= 한개
listbox.insert(0,"사과")
listbox.insert(1,"딸기")
listbox.insert(3,"문어")
listbox.insert(END,"수박")

listbox.pack()

def btncmd() :
    listbox.delete(END) ## 0 은 앞에서 부터 삭제

    # 갯수 확인
    print("리스트에는",listbox.size(),"개가 있어요")
    # 항목 확인
    print("첫번째 부터 3번째까지의 항목 : ",listbox.get(0,2))
    # 선택된 항목 확인
    print("선택된 항목 :")


btn =Button(root,text="클릭",command=btncmd)
btn.pack()


     
   

btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()  ## 계속 루프 돌려 실행

