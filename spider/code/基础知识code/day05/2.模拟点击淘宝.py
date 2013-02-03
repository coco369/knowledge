
import time

from selenium import webdriver

chromdriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(chromdriver)

browser.get('https://www.taobao.com/')

# 输入搜索ipad
browser.find_element_by_id('q').send_keys('ipad')

time.sleep(3)

# 模拟点击搜索按钮
browser.find_element_by_class_name('btn-search').click()

# 关闭浏览器
# browser.close()


