import pyautogui

# fw = pyautogui.getActiveWindow()


# print(fw.title) # 창의 제목 정보
# print(fw.size)  # 창의 크기 정보 
# print(fw.left , fw.top, fw.right, fw.bottom) # 창의 좌표


# pyautogui.click(fw.left + 25 , fw.top + 20)

# for w in pyautogui.getAllWindows():
#     print(w)

# <Win32Window left="-32000", top="-32000", width="160", height="28", title="Blitz">
# <Win32Window left="-32000", top="-32000", width="160", height="28", title="#general - Discord">
# <Win32Window left="0", top="0", width="1920", height="1080", title="">
# <Win32Window left="0", top="0", width="1920", height="1080", title="">
# <Win32Window left="0", top="0", width="1920", height="1080", title="Program Manager">

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)
if w.isActive == False: # 현재 활성화가 되지 않았다면
    w.activate() # 활성화 (맨 앞으로 가져오기)

if w.isMaximized == False: # 현재 최대화가 되지 않았다면
    w.maximize() # 최대화
