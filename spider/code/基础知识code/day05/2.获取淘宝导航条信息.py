
from selenium import webdriver

chromdriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(chromdriver)

# 打开淘宝
browser.get('https://www.taobao.com/')

# 处理爬取数据的业务
lis = browser.find_elements_by_css_selector('.service-bd li a')
for li in lis:
    print(li.text)
    print(li.get_attribute('href'))


# 关闭浏览器
browser.close()
