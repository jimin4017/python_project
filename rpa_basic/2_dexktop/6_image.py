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

 
2. 범위 선정  속도 개빨라짐 개굿굿

trash_icon = pyautogui.locateOnScreen("trash.png",region=(1802,820,1861-1802,880-820)) 
pyautogui.moveTo(trash_icon)jimi

pyautogui.mouseInfo()
위치 확인용

3. 정확



pyautogui.moveTo(trash_icon) 
  1828,847 204,204,204 #CCCCCC


좌표 얻어 두기
1802,820 30,30,30 #1E1E1E
1861,880 30,30,30 #1E1E1E