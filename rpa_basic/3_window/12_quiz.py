import pyautogui
import time
import pyperclip
import sys

def my_write(text):
    pyperclip.copy(text)
    time.sleep(1)
    pyautogui.hotkey("ctrl", "v")
def find_target(img_file, timeout=30):  ## 타겟 찾기 
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target
def my_click(img_file, timeout=30):    ## 타겟 클릭

    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program.")
        
        sys.exit()   ## 프로그램 끝나는거
    

pyautogui.hotkey("win", "r") # 클립보드에 있는 내용을 붙여넣기
pyautogui.write("mspaint")
pyautogui.hotkey("enter") 

time.sleep(1)
text_menu = pyautogui.locateOnScreen("txt_img.png",confidence=0.7)
if text_menu:
    pyautogui.doubleClick(text_menu)


   

pyautogui.click( 700 , 530)

my_write("ㅇㅁ라ㅣ믄ㅇ;라ㅣㅡ마ㅣ")


time.sleep(2)
my_click("Exit.png", 10)

my_click("close.png", 10)




# 마우스 좌표
#693,525 255,255,255 #FFFFFF


## 

