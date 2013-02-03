
import time

from selenium import webdriver

chromeDriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(chromeDriver)

# 打开浏览器，访问url
browser.get('https://www.taobao.com/')
# 获取首页的窗口处理手柄
taobao_handle = browser.current_window_handle
# 休眠5秒
time.sleep(5)
# browser.implicitly_wait(15)
# 进行xpath获取元素，并且执行点击事件
# browser.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/div[1]/div/ul/li[1]/a[1]').click()
# 休眠3秒
# time.sleep(3)
# 获取女装窗口处理手柄
# nvzhuang_handle = browser.current_window_handle

# 切换到首页的窗口
# browser.switch_to_window(taobao_handle)

# 搜索max pro并且点击搜索按钮
browser.find_element_by_id('q').send_keys('mac pro')
# 休眠3秒
time.sleep(3)
browser.find_element_by_class_name('btn-search').click()

# 关闭窗口
# browser.close()

# 关闭浏览器
time.sleep(3)
# browser.quit()

# 回退
browser.back()

time.sleep(3)

# 前进
browser.forward()

time.sleep(3)

# browser.execute_script('document.documentElement.scrollTop=2000')

# 滚动条到底
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')

# 滚动条到顶
browser.execute_script('window.scrollTo(0,0)')
