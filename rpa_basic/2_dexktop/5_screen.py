import pyautogui

img = pyautogui.screenshot()

# img.save("screenshot.png")


# pyautogui.mouseInfo()

# 1260,267 30,30,30 #1E1E1E
# 1260,267 30,30,30 #1E1E1E
pixel = pyautogui.pixel(1260,267)

print(pixel)

print(pyautogui.pixelMatchesColor(1260,267,(30,30,30)))
print(pyautogui.pixelMatchesColor(1260,267,pixel))
print(pyautogui.pixelMatchesColor(1260,267,pixel))