
import urllib.request
from urllib import parse


def main(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/65.0.3325.181 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=header)
    res = urllib.request.urlopen(req)
    return res.read().decode('utf-8')


if __name__ == '__main__':
    msg = input('请输入搜索信息:')
    search = parse.urlencode({'wd': msg})
    url = 'https://www.baidu.com/s?%s' % search
    result = main(url)
    print(result)

