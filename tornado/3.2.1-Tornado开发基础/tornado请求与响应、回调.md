
# tornado使用操作指南--请求与响应

>Auth: 王海飞
>
>Data：2019-02-17
>
>Email：779598160@qq.com
>
>github：https://github.com/coco369/knowledge 

### 1. 传递请求参数

在Web应用开发中最为重要的是请求与响应，如何获取请求URL中传递的参数，以及如何响应都是十分重要的。

参数的传递，可以在动态路由的配置时，通过定义带参URL形式传递参数。除此之外，如果不在URL配置时传递参数，还可以通过<b style="color:red;">get_argument()</b>方法获取参数值。

请求URL地址为: http://location:8888/hello?name=xiaoming&age=18，则获取请求中的参数，采用以下语法格式:

<b> 1）get_argument(name, default, strip=True) </b>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;返回具有给定名称name的参数的值。参数说明: 如果参数name出现在URL中，则获取最后一个name参数对应的值。如果在URL中没有定义参数name，则返回default值。strip参数表示删除字符串两边的空格。

<b> 2）get_arguments(names, strip=True) </b>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;返回具有给定名称name的参数列表。strip参数表示删除字符串两边的空格。


### 2. 请求获取参数案例

获取GET请求传递的参数。

	import tornado.ioloop
	import tornado.web
	from tornado.options import define, options, parse_command_line
	
	# 定义默认的端口
	define('port', default=8000, type=int)
	
	
	class MainHandler(tornado.web.RequestHandler):
	    def get(self, *args, **kwargs):
	        # 获取请求URL中传递的name参数
	        name = self.get_argument('name', '小明')
	        self.write("Hello, %s" % name)
	
	
	def make_app():
	    return tornado.web.Application(handlers=[
	        (r"/hello", MainHandler),
	    ])
	
	
	if __name__ == "__main__":
	    parse_command_line()
	    app = make_app()
	    app.listen(options.port)
	    tornado.ioloop.IOLoop.current().start()

定义get_argument()方法用以捕获请求URL中传递的参数，<b>分析如下</b>:

1) self.get_argument(‘name’, default)方法用于获取请求URL中传递的参数，如果获取不到URL中传递的name参数，则返回默认值。

2) 如果访问地址为http://127.0.0.1:8000/hello，使用self.get_argument(‘name’, default)方法获取不到请求URL中的name参数，则返回default默认值。

3) 如果访问地址为http://127.0.0.1:8000/hello?name=小王，则使用self.get_argument(‘name’, default)方法获取请求URL中的name参数，则返回值为‘小王’

<b style="color:red;">注意: </b>使用get_argument()和get_arguments()方法获取的是提交GET请求时URL中传递的参数和POST请求提交参数的集合。

### 3. 其他请求获取参数方法

获取请求URL中传递的参数还有以下的语法:

1) get_query_argument(name): 和get_argument语法相似，但该方法仅只能从URL中获取传递的参数值。

2) get_query_arguments(name): 和get_arguments语法相似，也是只能仅从URL中获取传递的参数，返回的结果是列表。

3) get_body_argument(name): 和get_argument语法相似，但仅只能从POST请求中获取提交的参数。


4) get_body_arguments(name): 和get_arguments语法相似，也是只能从POST请求中获取提交的参数，返回的结果是列表。

<b style="color:red;">总结:</b> 开发中常用get_argument和get_arguments方法，因为它们是get_query_argument、get_query_arguments和get_body_argument、get_body_arguments的合集。

### 4. 输出

在Web开发中如何正确的响应输出给浏览器中。常用的响应输出的语法如下。

语法格式:

<b> 1) set_status(status_code，reason=None) </b>

	设置响应的状态码，如果有描述信息，则赋值给reason参数。

<b> 2) set_header(name, value) </b>

	设置给定的HTTP响应中Header名称和值，如果Header中已存在设置的名称，则覆盖Hearder的值。

<b> 3) write() </b>

	将给定的块写入到输出缓冲区中，并发送给客户端（浏览器）。如果写入的内容为字典，则数据将以JSON的格式发送给客户端，并同时将响应的Content-Type设置为application/json。

<b> 4) render(template_name, **kwargs) </b>

	用于渲染模板，template_name参数表示需要渲染的模板文件的名称。

<b> 5) redirect(url，permanent=False，status=None) </b>

	用于重定向，url参数表示重定向的URL地址。

<b> 6) add_header(name,value) </b>

	添加HTTP响应中的Header头参数
<b> 7) clear_header(name) </b>

	清空HTTP响应中Header中所有的信息
<b> 8) finish(chunk=None) </b>

	告知Tornado，Response响应已经完成，chunk参数表示传递给客户端的HTTP body。finish()方法适用于异步请求处理。
<b> 9) send_error(status_code=500) </b>

	将给定的HTTP错误代码发送给浏览器
<b> 10) wirte_error() </b>

	自定义错误页面
<b> 11）clear() </b>

	清楚写入Header和body的内容
<b> 12）flush() </b>

	将当前缓冲区数据刷新到网络
<b> 13）set_cookie(name，value) </b>

	以键值对的形式设置cookie值
<b> 14）clear_all_cookies(path=”/”，domain=None) </b>

	清空本次请求中所有cookie
<b> 15）cookies </b>

	获取所有的cookie内容
<b> 16）get_cookie(name，default) </b>

	返回具有给定名称的请求cookie的值，如果获取不到，则返回default参数


### 5. 跳转案例

实现跳转。

	import tornado.ioloop
	import tornado.web
	from tornado.options import define, options, parse_command_line
	
	# 定义默认的端口
	define('port', default=8000, type=int)
	
	
	class HelloHandler(tornado.web.RequestHandler):
	    def get(self, *args, **kwargs):
	        self.write("hello tornado")
	        self.write('<br/>')
	        self.write("实现从路由'/redirect/'跳转到本方法中")
	
	
	class RedirectHandler(tornado.web.RequestHandler):
	    def get(self, *args, **kwargs):
	        # 使用redirect方法，跳转到根路径"/"地址
	        self.redirect('/')
	
	
	def make_app():
	    return tornado.web.Application(handlers=[
	        (r"/redirect/", RedirectHandler),
	        (r"/", HelloHandler),
	    ])
	
	
	if __name__ == "__main__":
	    parse_command_line()
	    app = make_app()
	    app.listen(options.port)
	    tornado.ioloop.IOLoop.current().start()

当在浏览器中访问http://127.0.0.1:8000/redirect/地址时，实现分析如下:

路由匹配规则会自动匹配URL路由表，并调用处理器RedirectHandler中的HTTP行为方法get()，在该方法中进行跳转处理，使用redirect(url)方法进行跳转到url地址。在HelloHandler的get()方法中使用self.write()向缓存中写入数据，当函数结束后才将缓存中的数据渲染到页面中。

### 6. 回调add_callback

IOLoop.current().add_callback(回调任务)



