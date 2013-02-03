
from selenium import webdriver

chromdriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'

browser = webdriver.Chrome(chromdriver)

browser.get('https://www.baidu.com/')

browser.close()
