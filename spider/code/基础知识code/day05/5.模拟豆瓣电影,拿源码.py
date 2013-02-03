
import time

from selenium import webdriver


def click_more(browser):
    # 滚动条置底
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(5)

    # 模拟点击更多
    try:
        browser.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div[4]/a').click()
        time.sleep(5)
    except:
        print('到底了')


def start_crawl_douban_movies(url):

    chromeDriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
    browser = webdriver.Chrome(chromeDriver)

    # 打开浏览器，访问url
    browser.get(url)
    time.sleep(3)

    for i in range(20):
        click_more(browser)


    # 获取源码
    html_source = browser.page_source

    print(html_source)

    browser.close()


if __name__ == '__main__':
    url = 'https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0'
    start_crawl_douban_movies(url)
