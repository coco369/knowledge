
import requests
from bs4 import BeautifulSoup


def start_crawl(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    res = requests.get(url, headers=headers)

    # 使用lxml的etree去解析
    # html = etree.HTML(res.text)
    # a = html.xpath('//*[@id="zh-recommend-list"]/div[1]/h2/a/text()')
    # a_href = html.xpath('//*[@id="zh-recommend-list"]/div[1]/h2/a/@href')
    # print(a, a_href)

    # bs4解析
    soup = BeautifulSoup(res.text, 'lxml')
    result = soup.find_all('a', 'question_link')
    questions_list = []
    for i in result:
        href_result = 'https://www.zhihu.com' + i.attrs.get('href')
        a_text = i.get_text().replace('\n', '')
        questions_list.append([href_result, a_text])
    print('知乎发现页面有%s提问' % len(result))
    print('提问的地址和标题:%s' % questions_list)


if __name__ == '__main__':

    url = 'https://www.zhihu.com/explore'
    start_crawl(url)

