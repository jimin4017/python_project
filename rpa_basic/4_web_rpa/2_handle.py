import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://www.w3schools.com/tags/att_input_type_radio.asp')
curr_handle = browser.current_window_handle
print(curr_handle)

browser.find_element_by_xpath('//*[@id="main"]/div[2]/a').click()

handles = browser.window_handles # 모든 핸들 정보
for handle in handles:
    print(handle) # 각 핸들 정보
    browser.switch_to.window(handle) # 
    print(browser.title) 
    print()



print("현재 핸들 닫기")
browser.close() 

browser.switch_to.window(curr_handle)

print(browser.title) 

# 브라우저 컨트롤이 가능한지 확인
time.sleep(5)
browser.get('http://daum.net')

time.sleep(5)
browser.quit()