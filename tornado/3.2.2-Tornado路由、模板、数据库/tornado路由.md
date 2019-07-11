
# tornado使用操作指南--模型

>Auth: 王海飞
>
>Data：2019-06-05
>
>Email：779598160@qq.com
>
>github：https://github.com/coco369/knowledge 

### 前言

在Web开发中，路由的配置定义可以类似Django中urls.py文件这样定义，也可以类似Flask中通过装饰器的形式来定义。当然不同的配置方式都有各自的优势。在Tornado中默认的路由方式的定义如同Django中urls.py文件中的定义格式。如下将修改Tornado的路由定义格式，将采用装饰器的格式来定义路由。


### 1. 思路

Tornado默认路由文件配置:
	
	app = tornado.web.Application(handlers=[
		(r'/index/', IndexHandler),	
	])

Tornado修改默认的路由配置文件:

	@route(r'/index/')
	def IndexHandler(tornado.web.RequestHandler):

		def get(self):
			
			pass

### 2. 修改路由定义

创建 Route 对象，然后再在 Handler 上加上装饰器 @route(r'/')  ，并把 URL 传递进来，其中对应到 __call__ 方法中的 url 参数，然后把路由对应关系以元祖的方式添加到列表中，待所有的路由都添加完成之后，创建Tornado的路有对象，然后把路由表放进去，最后完成注册。


实现代码如下:

	import tornado.ioloop
	import tornado.web
	
	
	class Route(object):
	    """ 把每个URL与Handler的关系保存到一个元组中，然后追加到列表内，列表内包含了所有的Handler """
	
	    def __init__(self):
	        # 路由列表
	        self.urls = list()
	
	    def __call__(self, url, *args, **kwargs):
	        def register(cls):
	            # 把路由的对应关系表添加到路由列表中
	            self.urls.append((url, cls))
	            return cls
	
	        return register
	
	
	route = Route()  # 创建路由表对象
	
	
	@route(r'/')
	class Main1Handler(tornado.web.RequestHandler):
	    def get(self, *args, **kwargs):
	        self.write('Hello main1')
	
	
	@route(r'/hi')
	class Main2Handler(tornado.web.RequestHandler):
	    def get(self, *args, **kwargs):
	        self.write('hello main2')
	
	
	def make_app():
	    # 创建app，并且把路有关系放入到Application对象中
	    return tornado.web.Application(route.urls)
	
	if __name__ == '__main__':
	    app = make_app()
	    app.listen(8000)
	    tornado.ioloop.IOLoop.instance().start()


