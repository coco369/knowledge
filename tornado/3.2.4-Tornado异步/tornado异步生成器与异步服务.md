
# tornado使用操作指南--异步

>Auth: 王海飞
>
>Data：2019-03-12
>
>Email：779598160@qq.com
>
>github：https://github.com/coco369/knowledge


### 1. 前言
Tornado在处理严峻的网络流量时表现的非常强悍，是Python编写的强大、易扩展的Web服务，其利用非阻塞的方式和对epoll的运用，可以处理数以千计的连接，是理想的实时通信Web框架。 以下编写基于异步的Web服务。

### 2. 同步

大多数Web应用都是阻塞方式的，当一个耗时的请求被处理时，整个进程将会被阻塞，直到该请求响应。如何解决阻塞，可以通过启动多进程处理，也可以使用异步编程来处理。以下示例模拟同步调用bing的搜索接口，并响应时间。

同步Tornado Web服务
	
	import tornado.httpserver
	import tornado.ioloop
	import tornado.options
	import tornado.web
	import tornado.httpclient
	from tornado.options import parse_command_line
	import datetime
	
	
	from tornado.options import define, options
	define("port", default=8080, help="run on the given port", type=int)
	
	
	class IndexHandler(tornado.web.RequestHandler):
	    def get(self):
			#获取URL中的q参数
	        query = self.get_argument('q')
			#获取HTTPClient类对象，并调用fetch()方法获取源码
	        client = tornado.httpclient.HTTPClient()
	        response = client.fetch("https://cn.bing.com/search?q={}".format(query))
	        body = response.body
	        now = datetime.datetime.utcnow()
	        self.write("""
	            <div style="text-align: center">
	                <div style="font-size: 72px">%s</div>
	                <div style="font-size: 144px">%s</div>
	            </div>""" % (query, now))
	
	
	def make_app():
	    return tornado.web.Application(handlers=[
	        (r"/", IndexHandler),
	    ])
	
	
	if __name__ == "__main__":
	    parse_command_line()
	    app = make_app()
	    http_server = tornado.httpserver.HTTPServer(app)
	    http_server.listen(options.port)
	    tornado.ioloop.IOLoop.instance().start()

示例中定义了一个IndexHandler类用于处理访问根路径时的请求，在IndexHandler类的get()方法中通过self.get_argument('q')方法获取访问URL中的参数q。接下来通过实例化HTTPClicent类的对象，并调用对象的fetch()方法来获取响应HTTPResponse对象，其body属性包含整个页面的源码信息，最后返回给浏览器一个简单的HTML页面。

实例中虽然定义了一个简单的搜索功能，而且当访问根路径时，程序本身响应也是足够的快。但如果遇到网络延迟，程序3秒才响应一个请求，即程序每隔2秒才响应一个请求，这样的设计肯定不能解决C10K问题，也不是高性能、高扩展性应用。为了凸显性能问题，将使用apache的ab命令模拟多线程并发请求，测试服务器压力。

### 3. ab压力测试

启动Tornado项目，执行压力测试命令为: ab -c 10 -n 1000 http://127.0.0.1:8080/?q=python，其中-c参数表示:模型10个并发，相当于10个人同时访问统一地址，-n参数表示:发出1000个请求，测试结果如图11-5所示:
 
同步ab压力测试从图中可以分析几个ab命令中几个比较重要的性能指标:

	吞吐量(Requests per second): 服务器并发处理能力的量化描述，即某个用法用户数下单位时间内能处理的最大请求数。

	用户平均请求等待时间(Time per request): 计算公式为处理完所有请求所花费的时间/(总请求数/并发用户数)。

	请求消耗时间Time per request (mean, across all concurrent requests): 并发的每个请求平均消耗时间。

	并发用户数(Concurrentcy Level)
	
	完成请求数(Complete requests)

	失败请求数(Failed requests)

	流量(Transfer rate): 平均每秒网络上的流量，用于排查是否有网络流量过大导致网络延迟的问题。

### 4. 异步

在Tornado的异步库中最常用的就是自带的AsyncHTTPClicen，可以执行异步非阻塞的HTTP请求。AsyncHTTPClicen类对象的fetch()方法不用立马返回调用的结果，而是可以指定一个回调callback参数。

异步Web服务:

	import tornado.httpserver
	import tornado.ioloop
	import tornado.options
	import tornado.web
	import tornado.httpclient
	import datetime
	from tornado.options import define, options
	
	define("port", default=8090, help="run on the given port", type=int)
	
	
	class IndexHandler(tornado.web.RequestHandler):
	    @tornado.web.asynchronous # 在get方法的定义之前
	    def get(self):
	        query = self.get_argument('q')
	        client = tornado.httpclient.AsyncHTTPClient()
	        client.fetch("https://cn.bing.com/search?q={}".format(query), callback=self.on_response)
	
	    def on_response(self, response):
	        body = response.body
	        now = datetime.datetime.utcnow()
	        self.write("""
	            <div style="text-align: center">
	                <div style="font-size: 72px">%s</div>
	                <div style="font-size: 144px">%s</div>
	            </div>""" % (self.get_argument('q'), now))
	        # 回调方法结尾处调用
	        self.finish()
	
	
	def make_app():
	    return tornado.web.Application(handlers=[
	        (r"/", IndexHandler),
	    ])
	
	
	if __name__ == "__main__":
	    tornado.options.parse_command_line()
	    app = make_app()
	    http_server = tornado.httpserver.HTTPServer(app)
	    http_server.listen(options.port)
	    tornado.ioloop.IOLoop.instance().start()

示例中使用AsyncHTTPClient类，并调用对象的fetch()方法，AsyncHTTPClicent对象的fetch()方法并不直接返回结果，而且指定一个callback参数，在callback指定的方法中将获取HTTPResponse响应，最后返回给浏览器一个简单的HTML页面。示例中代码需要注意以下几点:

1）<b>装饰器@tornado.web.asynchronous:</b> 在Tornado中会默认的在函数处理结束时关闭客户端的连接，但在异步操作时需要等待回调callback指定的方法执行结束才关闭客户端的连接，因此需要保持开启连接状态直到回调函数执行完毕。所以使用装饰器@tornado.web.asynchronous告诉Tornado保持连接开启。

2）<b>self.finish():</b>使用装饰器@tornado.web.asynchronous来告诉Tornado不要自己关闭连接，因此在回调callback方法执行完毕后，要显式的调用self.finish()方法告诉Tornado关闭连接。


### 5. 异步生成器

为了将同步的Web服务优化为异步Web服务，于是将代码切割为两个方法，并通过ab压力测试，发现Tornado的Web服务在性能上获得了极大程度上的扩展。但如果需要处理更多的异步请求，那程序的维护和编码将变得非常困难。比如在编写爬虫程序时以深度优先算法进行爬取数据，则将会出现一个回调函数调用回调函数的回调函数。如下示例所示:

#### 5.1 异步链式回调
	
	def get(self):
	    client = AsyncHTTPClient()
	    client.fetch("http://example1.com", callback=on_response)
	
	def on_response(self, response):
	    client = AsyncHTTPClient()
	    client.fetch("http://example2.com/", callback=on_response2)
	
	def on_response2(self, response):
	    client = AsyncHTTPClient()
	    client.fetch("http://example3.com/", callback=on_response3)
	
	def on_response3(self, response):
		client = AsyncHTTPClient()
	client.fetch("http:// example4.com/", callback=on_response4)
	
	def on_response3(self, response):
		……

在异步编程中应尽量避免嵌套的使用回调函数，否则将会给程序的维护和扩展带来非常大的麻烦。Tornado中可以使用装饰器tornado.web.gen.coroutine简化异步编程，避免写嵌套的回调函数，提高代码的灵活性、可读性、可扩展性。如下示例使用装饰器tornado.web.gen.coroutine进行优化代码。

#### 5.2 非阻塞coroutine的使用
	
	import tornado.httpserver
	import tornado.ioloop
	import tornado.options
	import tornado.web
	import tornado.httpclient
	import datetime
	from tornado.options import define, options
	
	define("port", default=8090, help="run on the given port", type=int)
	
	
	class IndexHandler(tornado.web.RequestHandler):
	    @tornado.web.asynchronous # 在get方法的定义之前
	    @tornado.web.gen.coroutine
	    def get(self):
	        query = self.get_argument('q')
	        client = tornado.httpclient.AsyncHTTPClient()
	        response = yield client.fetch("https://cn.bing.com/search?q={}".format(query))
	
	        body = response.body
	        now = datetime.datetime.utcnow()
	        self.write("""
	            <div style="text-align: center">
	                <div style="font-size: 72px">%s</div>
	                <div style="font-size: 144px">%s</div>
	            </div>""" % (self.get_argument('q'), now))
	        self.finish() # 回调方法结尾处调用
	
	
	def make_app():
	    return tornado.web.Application(handlers=[
	        (r"/", IndexHandler),
	    ])
	
	
	if __name__ == "__main__":
	    tornado.options.parse_command_line()
	    app = make_app()
	    http_server = tornado.httpserver.HTTPServer(app)
	    http_server.listen(options.port)
	    tornado.ioloop.IOLoop.instance().start()

示例中使用装饰器tornado.web.gen.coroutine 和Python的yield关键字，yield的使用允许运行在HTTP请求进行中执行其他任务，而不需要等待响应挂起进程，只需当HTTP响应完成后，RequestHandler方法在其停止的地方恢复并执行其余代码。

