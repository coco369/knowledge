

# 爬虫学习使用指南--scrapy框架之中间件

> Auth: 王海飞
>
> Data：2019-06-20
>
> Email：779598160@qq.com
>
> github：https://github.com/coco369/knowledge 



### 前言

scrapy提供了两种中间件，下载中间件（Downloader Middleware）和Spider中间件（Spider Middleware） 



#### 1. 下载中间件(DOWNLOADER_MIDDLEWARES)

下载中间件是scrapy提供用于用于在爬虫过程中可修改Request和Response，用于扩展scrapy的功能；比如：

1. 可以在请求被Download之前，请求头部加上某些信息（如IP代理proxy，用户代理User_Agent）；
2. 完成请求之后，回包需要解压等处理；

在scrapy中有默认的许多中间件，如下所示:
```
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',   # 用户代理UserAgent中间件
 'scrapy.downloadermiddlewares.retry.RetryMiddleware'            # 重试URL请求中间件
 'testspider.middlewares.TestspiderDownloaderMiddleware',                
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',    # 
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',      # Cookie中间件
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats'
```

##### 1.1 定义中间件

###### 1）process_request(request, spider)

当每个Request对象经过下载中间件时会被调用，**优先级越高的中间件，越先调用；**该方法应该返回以下对象：`None`/`Response`对象/`Request`对象/抛出`IgnoreRequest`异常；

1. 返回`None`：scrapy会继续执行其他中间件相应的方法；
2. 返回`Response`对象：scrapy不会再调用其他中间件的`process_request`方法，也不会去发起下载，而是直接返回该`Response`对象；
3. 返回`Request`对象：scrapy不会再调用其他中间件的`process_request()`方法，而是将其放置调度器待调度下载；
4. 抛出`IgnoreRequest`异常：已安装中间件的`process_exception()`会被调用，如果它们没有捕获该异常，则`Request.errback`会被调用；如果再没被处理，它会被忽略，且不会写进日志。

 ##### 2）process_response(request, response, spider)

当每个Response经过下载中间件会被调用，**优先级越高的中间件，越晚被调用，与process_request()相反；**该方法返回以下对象：`Response`对象/`Request`对象/抛出`IgnoreRequest`异常。

1. 返回`Response`对象：scrapy会继续调用其他中间件的`process_response`方法；
2. 返回`Request`对象：停止中间器调用，将其放置到调度器待调度下载；
3. 抛出`IgnoreRequest`异常：`Request.errback`会被调用来处理函数，如果没有处理，它将会被忽略且不会写进日志。

##### 3）process_exception(request, exception, spider)

当`process_exception()`和`process_request()`抛出异常时会被调用，应该返回以下对象：None/`Response`对象/`Request`对象；

1. 如果返回`None`：scrapy会继续调用其他中间件的`process_exception()`；
2. 如果返回`Response`对象：中间件链的`process_response()`开始启动，不会继续调用其他中间件的`process_exception()`；
3. 如果返回`Request`对象：停止中间器的`process_exception()`方法调用，将其放置到调度器待调度下载。

 

#### 2. Spider中间件（Spider Middleware）

​	Spider中间件是介入到Scrapy中的spider处理机制的钩子框架，可以插入自定义功能来处理发送给 Spiders 的response，以及spider产生的item和request。 

默认情况下，Spider中间件

- `process_spider_input(response, spider)` 当response通过spider中间件时，这个方法被调用，返回None
- `process_spider_output(response, result, spider)` 当spider处理response后返回result时，这个方法被调用，必须返回Request或Item对象的可迭代对象，一般返回result
- `process_spider_exception(response, exception, spider)` 当spider中间件抛出异常时，这个方法被调用，返回None或可迭代对象的Request、dict、Item

##### 2.1) 使用Spider中间件

```
class MyTestMiddleware():

    def process_spider_input(self, response, spider):
        print('执行响应之前处理')
        # print(response.text)
        return None

    def process_spider_output(self, response, result, spider):
        print('处理完响应之后处理')
        print(list(result))
        return result
```

注意: 当下载中间件将页面源码response获取到后交给spiders进行处理，此时调用process_spider_input方法。当spiders爬虫的parse()方法解析后，返回item后将调用process_spider_output()方法，该方法用于处理result结果值，通常返回result即可。

#### 3. 中间件的使用(IP代理修改)

##### 3.1 process_request和process_response方法的重构

在settings.py文件中的加入自定义的ProxyMiddleware中间件，并设置中间件的优先级

```
DOWNLOADER_MIDDLEWARES = {
   'testspider.middlewares.ProxyMiddleware': 544,
}
```

以下在middlewares.py文件中定义ProxyMiddleware中间件，并设置process_request和process_response

```
class ProxyMiddleware():

    def process_request(self, request, spider):
        request.meta['proxy'] = 'http://60.205.229.126:80'
        return None

    def process_response(self, request, response, spider):
        response.status = 201
        return response
```

注意: process_request方法中修改请求的代理、process_response方法中修改响应的状态码

 

##### 3.2 异常捕获process_exception的重构

​	当使用代理时还是无法访问网站，则将抛出异常，并会调用异常处理process_exception方法。而我们只需重构该方法，并重新设置代理IP即可，再次访问请求地址。

​	如下定义爬虫ProxySpider，其中定义访问地址的make_requests_form_url()方法，该方法为请求地址，并将地址加入调度器中进行下载。

注意:

​	 Request()中的meta={‘download_timeout’: 5}表示请求地址的超时时间，如果超过5秒还没获取到响应，则调用异常处理process_exception方法。

​	dont_filter表示scrapy会自动屏蔽已爬取过当前URL地址，而此处需要不断请求失败的地址，因此dont_filter设置为True，表示可以多次请求当前地址。

```
class ProxySpider(Spider):

    name = 'proxy'

    start_urls = ['https://www.google.com']

    def make_requests_from_url(self, url):
        print('访问')
        return Request(url, meta={'download_timeout': 5}, callback=self.parse, dont_filter=True)

    def parse(self, response):

        print(response.text)
        print(response.status)
```

重构process_exception(request, exception, spider)方法，并设置IP代理（代理IP应该从代理池中获取），并返回请求request待调度器重新下载。

```
def process_exception(self, request, exception, spider):
    # 异常则重新调度
    print('再次尝试请求')
    return request
```



#### 4. 中间件的使用(User-Agent修改)

 ##### 4.1）自定义UserAgent中间件，并禁用Scrapy提供的中间件

 在settings.py文件中的加入自定义的MyUserAgentMiddleware中间件，并设置中间件的优先级

```
DOWNLOADER_MIDDLEWARES = {
   'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,   # 禁用Scrapy自带的UserAgent中间件
   'testspider.middlewares.MyUserAgentMiddleware': 545,  # 使用自定义的MyUserAgent中间件
}
```

##### 4.2）定义自定义UserAgent中间件

```
class MyUserAgentMiddleware():

    def process_request(self, request, spider):
        ua = UserAgent()
        request.headers.setdefault('User-Agent', ua.random)
```

 

 总结:  下载中间件聚焦于下载前后，Spider中间件聚焦于Spider前后，两者略有重合的地方。 

 

 

 

 

