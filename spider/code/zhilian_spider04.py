
import urllib.request
from urllib import parse
from lxml import etree


def zhaopin_msg(url):
    """
     获取智联上招聘信息
     1. 获取职位的个数
        <span class="search_yx_tj">
            共<em>1473</em>个职位满足条件
        </span>
    """
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    req = urllib.request.Request(url=url, headers=header)
    res = urllib.request.urlopen(req)

    # 正则匹配，查询的结果为职位的个数
    # count_job = re.findall('<em>(\d+)</em>', res.read().decode('utf-8'))

    # return count_job

    # 查询岗位名称和公司名称
    tree = etree.HTML(res.read())
    content1 = tree.xpath('//tr/td/div/a[1]/text()')
    content2 = tree.xpath('//tr/td/a[1]/text()')
    return content1, content2


if __name__ == '__main__':

    # 获取从客户端接收到的参数
    job_name = input('请输入岗位名称:')
    city_name = input('请输入城市名称:')

    # 将输入参数进行编码，输入参数，python和成都，输出结果为:jl=%E6%88%90%E9%83%BD&kw=python
    search_params = parse.urlencode({'jl': city_name, 'kw': job_name})
    # urllib进行解析的网站的url
    url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?%s' % search_params
    # 进行解析地址
    result = zhaopin_msg(url)
    print(result)
