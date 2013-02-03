# coding=utf-8

import re
import urllib.request

import pymysql


def decode_html(html, charsets=('utf-8', 'gbk')):
    # 编码
    page_html = ''
    for charset in charsets:
        try:
            page_html = html.decode(charset)
            break
        except Exception as e:
            print('编码出错')
    return page_html


def pattern_regex(html, pattern, flags=re.S):
    html_regex = re.compile(pattern, flags)
    return html_regex.findall(html) if html else []


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=headers)
    res = urllib.request.urlopen(req)
    page_html = decode_html(res.read())
    return page_html


def get_mysql(sql, params_list):
    conn = pymysql.connect(host='localhost', port=3306, user='root',
                           password='123456', database='spider', charset='utf8')
    cursor = conn.cursor()
    cursor.executemany(sql, params_list)
    conn.commit()
    cursor.close()


def start_crawl(url):
    page_html = get_html(url)
    link_list = pattern_regex(page_html, "<a test=a href='(.*?)'")
    params_list = []
    for link_url in link_list:
        html = get_html(link_url)
        # 标题
        title = pattern_regex(html, '<h1>(.*?)<span class="article-tag">')
        # 内容
        content = pattern_regex(html, '<article class="article" id="mp-editor">(.*?)</article>')
        # 格式 [['1','2', ['3','4']]]
        params_list.append([title[0], content[0]])

    sql = 'insert into result_souhu values (%s, %s)'
    get_mysql(sql, params_list)


if __name__ == '__main__':

    url = 'http://sports.sohu.com/nba_a.shtml'
    start_crawl(url)



