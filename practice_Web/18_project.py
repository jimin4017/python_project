
import time
 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option('prefs',{'download.default_directory':r'C:\Users\정지민\Desktop\python_project\python_project'})


browser = webdriver.Chrome(options=chrome_options)

browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download")

browser.switch_to.frame('iframeResult')



elem = browser.find_element_by_xpath('/html/body/p[2]/a')
elem.click()

print(browser.title)

time.sleep(5)

browser.quit( )