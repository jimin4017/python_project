import tkinter.ttk as ttk
from tkinter import *


root = Tk()

root.title("jimin project")  ## 콘솔창 이름 설정

root.geometry("640x480+100+300")  ## tkinter에서 콘솔 크기 설정가로 * 세로  
                                   ## + " x,y" 좌표


file_frame = Frame(root)
file_frame.pack()

btn_Add_file = Button(file_frame,padx=5,pady=5,width=12,text="파일추가")
btn_Add_file.pack(side="left")

btn_del_file = Button(file_frame,padx=5,pady=5,width=12, text="선택삭제")
btn_del_file.pack(side="right")

###############################################  밑에 메모장처럼 글자 넣는곳
list_frame = Frame(root)
list_frame.pack(fill="both") 

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right",fill="y")

list_file = Listbox(list_frame, selectmode="extended",height= 15,yscrollcommand=scrollbar.set)
list_file.pack(side="left",fill="both",expand=True)
scrollbar.config(command=list_file.yview)


# 저장경로 프레임
path_frame = LabelFrame(root,text="저장경로")
path_frame.pack()


txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left",fill="both")

btn_dest_path = Button(path_frame,text="찾아보기",width=10)
btn_dest_path.pack(side="right")

# 옵션 프레임
frame_option = LabelFrame(root,text="옵션")
frame_option.pack()

# 1. 가로 넓이 옵션
# 가로 넓이 레이블
lbl_width = Label(frame_option, text="가로넓이",)




# ## 가로 넓이 콤보

# opt_width = ["원본유지","1024","800","640"]
# cmb_width = ttk.Combobox(frame_option,state="readonly",values=opt_width)
# cmb_width.current()
# cmb_width.pack(side="left")





root.resizable(False,False)  #x,y 변경 불가

root.mainloop()  ## 계속 루프 돌려 실행

