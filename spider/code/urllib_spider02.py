
import urllib.request

# r = urllib.request.urlopen('https://www.baidu.com')
# print(r.read().decode('utf-8'))



header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

res = urllib.request.Request('https://www.baidu.com', headers=header)
r = urllib.request.urlopen(res)
print(r.read().decode('utf-8'))