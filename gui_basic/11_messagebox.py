import time
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()

root.title("jimin project")  ## 콘솔창 이름 설정

root.geometry("640x480+100+300")  ## tkinter에서 콘솔 크기 설정가로 * 세로  
                                  ## + " x,y" 좌표
def info() :
    msgbox.showinfo("알림","정상적으로 예매에 완료되었습니다.")
    ##### 첫번째칸 버튼의 이름 , 두번째칸 눌렸을때 뜨는 메시지칸

def warn() :
    msgbox.showwarning("경고","해당 좌석은 매진되었습니다.")

def error() :
    msgbox.showerror("에러","에러가 났습니다.")
def okcancel() :
    msgbox.askokcancel("확인/취소","해당 좌석은 유아동반석입니다. 예매하시겠습니까?")
def recycle() :
    msgbox.askretrycancel("재시도/ 취소","일시적인 오류입니다. 다시 시도 하겠습니까?")
def yesno() :
    msgbox.askyesno("예/ 아니오","일시적인 오류입니다. 다시 시도 하겠습니까?")
def retrycancel() :
    response = msgbox.askretrycancel("재시도/취소","일시적인 오류입니다")
    if response == 1: # 재시도
        print("재시도")
    elif response == 0 :#취소
    print("취소")



Button(root,command=info,text="알림").pack()
Button(root,command=warn,text="경고").pack()
Button(root,command=error,text="에러").pack()

Button(root,command=okcancel,text="재시도 확인").pack()
Button(root,command=recycle,text="확인").pack()
Button(root,command=yesno,text="예/아니오").pack()
Button(root,command=retrycancel,text="retry").pack()


root.mainloop()  ## 계속 루프 돌려 실행

