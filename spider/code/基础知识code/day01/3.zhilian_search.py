
import re
import urllib.request
from urllib import parse


def get_zhilian_html(url):

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/65.0.3325.181 Safari/537.36'
    }

    req = urllib.request.Request(url, headers=header)
    res = urllib.request.urlopen(req)
    return res.read().decode('utf-8')


def get_job_num(html):
    # 获取岗位的个数
    result = re.findall('<em>(\d+)</em>', html)
    if result:
        return result[0]
    else:
        return 0


def get_table(html):
    table = '<div class="newlist_list_content" id="newlist_list_content_table">(.*?)</div>'
    print(re.findall(table, html))


def get_company_name(html):
    result = re.findall('<td class="gsmc"><a href=.*?>(.*?)</a>', html, re.S)
    print(result)


if __name__ == '__main__':

    city = input('请输入搜索城市:')
    job = input('请输入搜索岗位:')
    search = parse.urlencode({'jl': city, 'kw': job})
    url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?%s' % search
    html = get_zhilian_html(url)
    result = get_job_num(html)
    print('城市:%s 岗位:%s 需求量:%s' % (city, job, result))
    get_company_name(html)
