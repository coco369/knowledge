
# tornado使用操作指南--路由规则与行为方法与切入点函数

>Auth: 王海飞
>
>Data：2019-02-17
>
>Email：779598160@qq.com
>
>github：https://github.com/coco369/knowledge 

### 1. tornado路由规则定义

Tornado的官网中对路由的定义有一句描述: “A collection of request handlers that make up a web application.”即<b style="color:red;">一个Web应用是由请求处理器集合和路由表组成。</b>

在tornado.web.Application类中接收一个handlers参数，该参数由元祖组成，<b style="color:red;">每个元组中包含匹配模式pattern和处理器handler。</b>

当HTTPServer接收到一个HTTP请求时，服务端会从请求中解析出URL路由，然后去匹配路由表，如果能匹配到某个pattern，则将此HTTP请求交给pattern对应的处理器handler处理。

### 2. 动态路由映射

Tornado框架是基于正则的动态路由映射，动态路由的定义方式和Django类似。动态路由可以定义为<b>带参数形式</b>或<b>不带参数形式</b>，其中还可以使用<b style="color:red;">‘(?P<参数名>)’</b>这种形式来设置请求处理器接收参数的指定名称。

<b> 1) 指定带参数的动态路由 </b>

    新增带参数的动态路由，并使用正则匹配规则‘(?P<参数名>)’来设置接收参数的名称。

	class IndexHandler(tornado.web.RequestHandler):
	    def get(self, month, year):
	        self.write('日期:%s年%s月' % (year, month))
	
	
	def make_app():
	    return tornado.web.Application(handlers=[
	        (r"/index/(?P<year>\d{4})/(?P<month>\d{2})/", IndexHandler),
	    ])

示例中定义了接收参数的动态路由” /index/(?P<year>\d{4})/(?P<month>\d{2})/”，例如路由匹配规则会匹配“/index/2018/11”地址，其中URL中的参数2018和11会以参数的相似传递给IndexHandler类的get()方法，get()方法中可以通过设定的参数名来获取对应的参数值。如year的值为2018，month的值为11。   

<b> 2）不指定参数名的动态路由 </b>

	定义接收参数的动态路由。
	class NewIndexHandler(tornado.web.RequestHandler):
	    def get(self, a, b, c):
	        self.write('%s %s %s' % (a, b, c))


	def make_app():
	    return tornado.web.Application(handlers=[
	        (r"/index2/(\d+)/(\d+)/(\d+)/", NewIndexHandler),
	    ])


示例中定义了接收三个参数的动态路由，如在浏览器中访问“/index2/2018/11/7/“地址，URL中的参数2018、11和7以参数的形式传递给NewIndexHandler类的get()方法，get(self, a, b, c)方法中接收三个参数,其中a的值为2018、b的值为11、c的值为7。

注意: 

传递带参数的URL需要注意以下<b style="color:red;">两点</b>:

1. 使用(?P<参数名>)来设置传递的参数名称，在继承RequestHandler类中的get()方法中接收参数的参数名顺序可以任意排序。

2. 不指定动态路由中传递的参数名称，则在继承RequestHandler类中get()方法中设置接受参数的参数名，get()方法中第一个参数将取动态路由URL中第一个参数的值，get()方法中第二个参数将取动态路由URL中第二个参数的值....依次类推。

<b> 3）不带参数的路由  </b>

如下定义匹配根路径“/”的路由，并调用请求处理MainHandler类中与HTTP请求方式对应的get()方法来响应这个请求。

	定义不带参数的动态路由。
	class MainHandler(tornado.web.RequestHandler):
	    def get(self):
	        self.write("Hello, world")
	
	
	def make_app():
	    return tornado.web.Application(handlers=[
	        (r"/", MainHandler),
	    ])

### 2. HTTP行为方法

在示例中的RequestHandler类都自定义了一个HTTP方法的行为，但是处理同一个URL的时候，有可能除了GET请求方式，也有可能会提交POST请求方式以及PATCH等请求方式。因此在自定义的RequestHandler类中还可以自定义HTTP请求的行为方法，如下展示常用的行为方法:

1）RequestHandler.get(*args, **kwargs)

2）RequestHandler.post(*args, **kwargs)

3）RequestHandler.delete(*args, **kwargs)

4）RequestHandler.patch(*args, **kwargs)

5）RequestHandler.put(*args, **kwargs)

6）RequestHandler.head(*args, **kwargs)

7）RequestHandler.options(*args, **kwargs)

【示例11-8】定义继承RequestHandler的子类的HTTP请求的行为方法。
class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("处理get请求")

    def post(self, *args, **kwargs):
        self.write("处理post请求")

    def patch(self, *args, **kwargs):
        self.write("处理patch请求")

    def put(self, *args, **kwargs):
        self.write("处理put请求")

    def head(self, *args, **kwargs):
        self.write("处理head请求")

    def options(self, *args, **kwargs):
        self.write("处理options请求")

    def delete(self, *args, **kwargs):
        self.write("处理delete请求")

### 3. 切入点函数

继承tornado.web.RequestHandler的子类中至少定义一个HTTP请求的行为方法，如get()函数、post()函数等。这些与HTTP请求所对应的行为方法也被叫做“Entry points”即<b>切入点函数</b>。

切入点函数除了get()函数、post()函数，还有如下方法:

<b> 1）RequestHandler.initialize()</b>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;用于子类的初始化。

<b> 2）RequestHandler.prepare()</b>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在调用get()或post()方法之前被调用。

<b> 3）RequestHandler.on_finish()</b>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在请求结束后调用，用于执行清理，日志记录等功能。

### 4. 切入点函数的调用

创建tornado_entry_points.py文件

	import tornado.ioloop
	import tornado.web
	import tornado.httpserver
	from tornado.options import define, options, parse_command_line
	
	# 定义默认的端口
	define('port', default=8000, type=int)
	
	
	class MainHandler(tornado.web.RequestHandler):
	    def initialize(self):
	        self.name = ‘Python’
	        print('实例对象的初始化，并给name参数赋值')
	
	    def prepare(self):
	        print('在执行HTTP行为方法之前被调用')
	
	    def get(self):
	        print('执行GET方法')
	        self.write("name: %s" % self.name)
	
	    def on_finish(self):
	        print('响应后调用此方法，用于清理内存或日志记录等功能')
	
	
	def make_app():
	    return tornado.web.Application(handlers=[
	        (r"/", MainHandler),
	    ])
	
	
	if __name__ == "__main__":
	    parse_command_line()
	    app = make_app()
	    app.listen(options.port)
	    tornado.ioloop.IOLoop.current().start()

<b style="color:red;">执行流程分析:</b>

<b>步骤1:</b> tornado.web.Application 会根据 URL 寻找一个匹配的 RequestHandler 类，并初始化它。它的 __init__() 方法会调用子类中定义的initialize() 方法。

<b>步骤2:</b> 接着根据不同的 HTTP 请求方式寻找该 handler 的 get/post() 等方法，并在执行前运行 prepare()。

<b>步骤3:</b> 最后会调用 handler 的 finish() 方法，这个方法最好别覆盖。它会调用 on_finish() 方法，它可以被覆盖，用于处理一些善后的事情（例如关闭数据库连接）

<b style="color:red;">启动项目:</b>
	
	python tornado_entry_points.py --port=8888