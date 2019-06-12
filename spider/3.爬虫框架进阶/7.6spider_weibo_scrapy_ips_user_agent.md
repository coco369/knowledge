
# 爬虫学习使用指南

>Auth: 王海飞
>
>Data：2018-07-05
>
>Email：779598160@qq.com
>
>github：https://github.com/coco369/knowledge
>

### 1. 设置User_Agent

User-Agent是我们在提交请求的时候，服务器来判断请求的来源是否是爬虫还是浏览器的标志，为了防止被限制爬取，我们可以定义很多的User_Agent的参数，在爬取页面的时候，随机去获取一个User_Agent的参数即可，具体操作如下：

#### 1.1 定义一个User_Agent_list的列表

在settings.py中设置如下的参数

	USER_AGENT_LIST = [

	    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
	    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
	    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
	    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
	    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
	    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
	    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
	    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
	    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
	    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
	    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
	    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
	    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
	    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
	    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
	    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
	    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
	    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
	    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36",
	    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0"

	] 

#### 1.2 定义下载中间件的类，随机从USER_AGENT_LIST中获取一个参数

	import random
	
	from scrapy.conf import settings
	
	from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
	
	
	class RandomUserAgent(UserAgentMiddleware):
	
	    def process_request(self, request, spider):
			# 获取随机的一个user_agent的参数
	        user_agent = random.choice(settings['USER_AGENT_LIST'])
			# 设置请求头中的User-Agent的参数
	        request.headers.setdefault('User-Agent', user_agent)

#### 1.3 settings.py中设置启动我们定义的中间件
	
	# 下载中间件
	DOWNLOADER_MIDDLEWARES = {
	    'dbspider.middlewares.RandomUserAgent': 554,
	}


### 2. 设置代理IP池

#### 2.1 在settings.py中模拟我们有很多的代理ip信息

	# 代理proxy参数
	PROXY = [
	    '106.56.102.131:8070',
	    '221.228.17.172:8181',
	    '124.89.2.250:63000',
	    '101.236.19.165:8866',
	    '125.121.116.43:808',
	    '223.145.229.165:666',
	    '182.88.14.206:8123',
	    '183.128.240.76:666',
	    '117.86.9.145:18118'
	]

#### 2.2 在中间件中定义我们的代理设置

		
	import random
	
	from scrapy.conf import settings


	class ProxyMiddleware(object):
	
	    def process_request(self, request, spider):
			
			# 随机去获取一个代理的ip
	        proxy = random.choice(settings['PROXY'])
			# 设置代理的地址
	        request.meta['proxy'] = 'http://%s' % proxy

#### 2.3 在settings.py中设置中间件

	DOWNLOADER_MIDDLEWARES = {
	    'dbspider.middlewares.RandomUserAgent': 554,
	    'dbspider.middlewares.ProxyMiddleware': 553,
	}


### 3. 获取IP代理池

在上面settigns.py中定义的ip代理参数，其实这些ip值很快就会失效。但是我们的爬虫是整天整天的运行的，那ip代理池中的ip失效了，那我们的爬虫就会被限制爬取了。

我们怎么去解决这个ip代理池的问题呢？我们可以直接找到一个免费的代理页面，从该页面中可以爬取到代理的ip和端口，只需要简单的验证一下ip是否有效即可。在爬取代码的时候，每次爬取页面就可以不断的切换ip代理池中的ip信息，放在爬虫被ban掉。

#### 3.1 获取(http://www.xicidaili.com/nn/)代理IP网页中的IP和PORT信息

	import scrapy
	from xiciSpider_master.items import xiciItem
	
	class xiciSpider(scrapy.Spider):
	    name='xiciSpider'
	    start_list = []
	    for i in range(1,10):
	        url = r'http://www.xicidaili.com/nn/%s' %str(i)
	        start_list.append(url)
	    start_urls=start_list
	
	    def start_requests(self):
	        user_agent ="Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
	        headers= {'User-Agent':user_agent}
	        for url in self.start_list:
	            yield scrapy.Request(url=url,headers=headers,method='GET',callback=self.parse)
	
	    def parse(self, response):
	        #//*[@id="ip_list"]
	        #tdinfo.xpath('td[2]/text()')[0].extract()
	        #<a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' /></a>
	        #re
	        #response.xpath('//a[contains(@href, "image")]/text()').re(r'Name:\s*(.*)')
	
	        lists=response.xpath('//*[@id="ip_list"]/tr')
	        # print(lists)
	        with open('data.txt',"a") as wd:
	            for index, tdinfo in enumerate(lists):
	                if index != 0:
	                    # xiciI = xiciItem()
	                    # xiciI['ipaddress'] = tdinfo.xpath('td[2]/text()').extract_first()
	                    # xiciI['dk'] = tdinfo.xpath('td[3]/text()').extract_first()
	                    # yield xiciI
	                    ipline = tdinfo.xpath('td[2]/text()').extract_first() +":"+tdinfo.xpath('td[3]/text()').extract_first()
	                    print(ipline)
	                    wd.write(ipline+u"\n")



#### 3.2 验证爬取到的IP结果是否失效，将没有失效的IP保存起来以供爬虫代码使用

	import urllib
	import urllib.request
	import time
	
	def validateIp(ip,port):
	    #头文件
	    user_agent= 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'
	    headers={'User-Agent':user_agent}
	    proxy = {'http':'http://%s:%s'%(ip,port)}
	
	    #代理设置
	    proxy_handler = urllib.request.ProxyHandler(proxy)
	    opener = urllib.request.build_opener(proxy_handler)
	    urllib.request.install_opener(opener)
	
	    #请求网址
	    validateUrl = 'https://www.baidu.com'
	    req = urllib.request.Request(url=validateUrl,headers=headers)
	    # 延时,等待反馈结果
	    time.sleep(4)
	
	    #判断结果
	    try:
	        res = urllib.request.urlopen(req)
	        # 延时,等待反馈结果
	        time.sleep(2)
	        content = res.read()
	        # 写入文件
	        if content:
	            print('is ok')
	            with open('data2.txt', 'a') as wd:
	                wd.write(ip + u':' + port + u'\n')
	        else:
	            # 未通过
	            print('is not ok')
	    except urllib.request.URLError as e:
	        print(e.reason)
	
	
	if __name__ == '__main__':
	    with open('data.txt','r') as rd:
	        iplist = rd.readlines()
	        for ip in iplist:
	            # print(ip.split(u':')[0])
	            validateIp(ip.split(u':')[0],ip.split(u':')[1])