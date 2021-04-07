import pyautogui

# file_menu = pyautogui.locateOnScreen("menu.png")
# print(file_menu)
# pyautogui.click(file_menu)


# # 출력문 Box(left=659, top=191, width=50, height=22)
# # Ctrl win alt space

# trash_icon =pyautogui.locateOnScreen("trash.png")
# print(trash_icon)
# pyautogui.moveTo(trash_icon)

# 1. gray scle  
# trash_icon = pyautogui.locateOnScreen("trash.png",grayscale=True)  ### grayscale = 이미지를 흑백으로 만들어 속도 개선 조금 빨라지나 정확도 낮아짐
# pyautogui.moveTo(trash_icon)

 
# 2. 범위 선정  속도 개빨라짐 개굿굿

# trash_icon = pyautogui.locateOnScreen("trash.png",region=(1802,820,1861-1802,880-820)) 
# pyautogui.moveTo(trash_icon)jimi

# pyautogui.moveTo(trash_icon) 
#   1828,847 204,204,204 #CCCCCC


# 3. 정확  pip intall opencv-python
# run_btn =pyautogui.locateOnScreen("run_btn.png",confidence=0.6) ## 60퍼 정도 일치
# pyautogui.moveTo(run_btn)

# test = pyautogui.locateOnScreen("test_fish.png",confidence=0.7)
# pyautogui.moveTo(1000,200)
#  959,532 49,115,208 #3173D0


# pyautogui.moveTo(trash_icon) 
#   1828,847 204,204,204 #CCCCCC


# 좌표 얻어 두기
# 1802,820 30,30,30 #1E1E1E
# 1861,880 30,30,30 #1E1E1E



# 자동화 대상이 바로 보여지지 않는 경우
# 1. 계속 기다리기
file_menu_notepad = pyautogui.locateOnScreen("test_fish.png")
# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)
# else:
#     print("발견 실패")


# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("test_fish.png")
#     print("발견 실패")
#pyautogui.click(file_menu_notepad)

# 2. 일정 시간동안 기다리기 (TimeOut)
import time
import sys

timeout = 10 # 10초 대기
start = time.time() # 시작 시간 설정
file_menu_notepad = None
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     end = time.time() # 종료 시간 설정
#     if end - start > timeout: # 지면정한 10초를 초과하
#         print("시간 종료")
#         sys.exit()

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
        print("잡혔다!")
        sys.exit()   ## 프로그램 끝나는거

#pyautogui.click(file_menu_notepad)

my_click("fish.png", 10)
