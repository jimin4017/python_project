# import pyautogui
# w = pyautogui.getWindowsWithTitle("제목 없음")[0] # 메모장 1개 띄운 상태에서 가져옴
# w.activate()

# pyautogui.write("12345")
# pyautogui.write("NadoCoding", interval=0.25)
# pyautogui.write("나도코딩")

# import pyperclip
# pyperclip.copy("나도코딩") # "나도코딩" 글자를 클립보드에 저장
# pyautogui.hotkey("ctrl", "v") # 클립보드에 있는 내용을 붙여넣기

# def my_write(text):
#     pyperclip.copy(text)
#     pyautogui.hotkey("ctrl", "v")


# my_write("문어")



import pyautogui
print("곧 시작합니다...")
pyautogui.countdown(3)
print("자동화 시작")


pyautogui.alert("자동화 수행에 실패하였습니다.", "경고") # 확인 버튼만 있는 팝업
result = pyautogui.confirm("계속 진행하시겠습니까?", "확인") # 확인, 취소 버튼
print(result)
result = pyautogui.prompt("파일명을 무엇으로 하시겠습니까?", "입력") # 사용자 입력
print(result)
result = pyautogui.password("암호를 입력하세요") # 암호 입력
print(result)