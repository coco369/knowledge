
import urllib3

# 你需要一个PoolManager实例来生成请求,由该实例对象处理与线程池的连接以及
# 线程安全的所有细节，不需要任何人为操作
http = urllib3.PoolManager()

# request()方法创建一个GET请求去获取百度的网页信息，返回的r是一个HttpResponse对象
r = http.request('GET', 'https://www.baidu.com')
# 打印请求的状态
print(r.status)
# 打印请求网页的内容
print(r.data)



'''
Accept: text/html, */*;q=0.8 # 浏览器告诉服务器可以接收的文本类型, */*表示任何类型都可以接收
Accept-Encoding: gzip, deflate # 浏览器告诉服务器，数据可以压缩，页面可以解压数据然后进行渲染。做爬虫的时候，最好不要写该参数
Accept-Language: zh-CN,zh;q=0.9 # 语言类型
Cache-Control: max-age=0 # 
Connection: keep-alive # 保持连接
Cookie: Hm_lvt_3bfcc098e0da26d58c321ba579b04b2f=1527581188,1528137133
Host: www.cdtopspeed.com # 域名
Upgrade-Insecure-Requests: 1

# 用户代理, 使得服务器能够识别请求是通过浏览器请求过来的，其中包含浏览器的名称/版本等信息
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
'''