import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0]

w.activate()  ## 메모장 깜빡깜빡 활성화
pyautogui.write("12345")
pyautogui.write("12345",interval=0.1)
##### pyautogui.write("한글")
##### 한글을 쓰면 인식이 아노딤

pyautogui.write(["t","e","s","t","left","left","right","l","a","enter"], interval=0.25)
# t e s t 순서대로 적고 왼쪽 방향키 2번, 오른쪽 방향키 2번, l a 순서대로 적고 enter 입력


# import pyautogui
# w = pyautogui.getWindowsWithTitle("제목 없음")[0] # 메모장 1개 띄운 상태에서 가져옴
# w.activate()

# pyautogui.write("12345")
# pyautogui.write("NadoCoding", interval=0.25)
# pyautogui.write("나도코딩")
