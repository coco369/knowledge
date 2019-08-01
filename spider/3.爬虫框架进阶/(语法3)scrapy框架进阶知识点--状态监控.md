# 爬虫学习使用指南--scrapy框架进阶

> Auth: 王海飞
>
> Data：2019-07-31
>
> Email：779598160@qq.com
>
> github：https://github.com/coco369/knowledge 

### 前言

​		Scrapy使用信号来通知事情发生。可以在Scrapy项目中捕捉一些信号。通过扩展信号来完成一些特定的功能。如监控scrapy爬虫的运行状态。



```
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
def __init__(self):
	#spider启动信号和spider_opened函数绑定
    dispatcher.connect(self.spider_opened, signals.spider_opened)
    dispatcher.connect(self.spider_stopped, signals.engine_stopped)##建立信号和槽，在爬虫结束时调用
    dispatcher.connect(self.spider_closed, signals.spider_closed)##建立信号和槽，在爬虫关闭时调用
    
    #爬虫关闭时 调用本方法
    def spider_closed(self):
        print("i close")

    #爬虫结束时 调用本方法
    def spider_stopped(self):
        print("i done")
```



spider类初始化时就绑定了两个方法,`spider_closed`和`spider_stopped`

注意， signals.spider_closed比signals.engine_stopped先执行

