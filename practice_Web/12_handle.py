from selenium import webdriver
import time
browser = webdriver.Chrome()

browser.maximize_window()

browser.get("https://www.w3schools.com/tags/att_input_type_radio.asp")\
curr_handle = browser.current_window_handle

print(curr_handle)

browser.find_element_by_xpath('////*[@id="main"]/div[2]/a').click()

handles = browser.window_handles ## 모든 핸들 정보를  가져온다

for handle in handles :
    print(handle)
    browser.switch_to.window(handle)
    print(browser.title)
    print()

print("현재 핸들 닫기")
browser.close()

print("처음 핸들로 돌아오기")
print(browser.title)
# 이전 핸들로 돌아오기
time.sleep(10)

browser.quit()