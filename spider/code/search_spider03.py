
import urllib.request
from urllib import parse

# 编码
enstr = parse.urlencode({'kd': '千峰'})
# 打印的结果为 kd=%E5%8D%83%E5%B3%B0
print(enstr)
# 解码
destr = parse.unquote(enstr)
# 解码的结果为 kd=千峰
print(destr)


def baidu_api(search):
    url = 'https://www.baidu.com/s?' + search
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    res = urllib.request.Request(url=url, headers=header)
    r = urllib.request.urlopen(res)
    print(r.read().decode('utf-8'))


if __name__ == '__main__':

    search = input('请输入搜索的数据:')
    wd = parse.urlencode({'wd': search})
    baidu_api(wd)

