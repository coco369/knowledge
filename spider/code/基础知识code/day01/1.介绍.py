
import urllib.request
import ssl

# url = 'https://www.baidu.com'
url = 'https://www.12306.cn/mormhweb/'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

req = urllib.request.Request(url, headers=header)

content = ssl._create_unverified_context()
res = urllib.request.urlopen(req, context=content)

print(res.read().decode('utf-8'))
