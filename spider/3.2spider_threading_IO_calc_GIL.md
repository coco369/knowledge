
# 爬虫学习使用指南

>Auth: 王海飞
>
>Data：2018-06-13
>
>Email：779598160@qq.com
>
>github：https://github.com/coco369/knowledge
>

#### 前言

由于我们从Python官方网站下载并安装好Python后，我们就直接获得了一个官方版本的解释器：CPython。这个解释器是用C语言开发的，所以叫CPython。在命令行下运行python就是启动CPython解释器。

但是随之就引来了一个限制多线程效率的问题:GIL(全局解释性锁 GLOBAL INTERPRETER LOCK)

其实:
Python语言和GIL没有半毛钱关系。仅仅是由于历史原因在Cpython虚拟机(解释器)，难以移除GIL。

>GIL：全局解释器锁。每个线程在执行的过程都需要先获取GIL，保证同一时刻只有一个线程可以执行代码。

>线程释放GIL锁的情况： 在IO操作等可能会引起阻塞的system call之前,可以暂时释放GIL,但在执行完毕后,必须重新获取GIL Python 3.x使用计时器（执行时间达到阈值后，当前线程释放GIL）或Python 2.x，tickets计数达到100


那如何提升多核CPU的资源呢，解决办法就是Python使用多进程。

如果需要使用多线程的情况下，就要看该处理任务是用于做什么计算了, 总结如下：


	在 处理像科学计算 这类需要持续使用cpu的任务的时候 单线程会比多线程快
	    
	在 处理像IO操作等可能引起阻塞的这类任务的时候 多线程会比单线程。如：多线程爬取比单线程性能有提升，因为遇到IO阻塞会自动释放GIL锁


### 案例

#### 1. 模拟科学计算，1加到14000的总和

先使用单线程的方式去计算和，并打印计算的时间

	
	from datetime import datetime
	
	
	def main(a, b):
	    result = 0
	    for i in range(a, b):
	        result += i
	    return result
	
	
	if __name__ == '__main__':
	    print(datetime.now())
	    result = main(2, 14000)
	    print(result)
	    print(datetime.now())


结果：
	
	按照单线程去运算，计算结果如下

	>2018-06-04 22:45:55.151221
	>97992999
	>2018-06-04 22:45:55.152221

从结算结果中可以看出，计算2到14000的总和，基本花销时间在CPU的处理上,处理时间只花了0.001秒


#### 2. 模拟科学计算，使用多线程算1到14000的总和

	
	import threading
	import time
	from datetime import datetime
	
	
	class CalcCount(threading.Thread):
	
	    def __init__(self, func):
			
			# 它会查找所有的超类，以及超类的超类，直到找到所需的特性为止。
	        super(CalcCount, self).__init__()
	        self.func = func
	
	    def run(self):
	        self.result = self.func
	
	    def get_result(self):
	        return self.result
	
	
	def calc(a, b):
	    result = 0
	    for i in range(a, b):
	        result += i
	    return result

	
	# 打印主线程开始时间
	print(datetime.now())
	
	# 实例子线程
	a1 = CalcCount(calc(2, 4000))
	a2 = CalcCount(calc(4001, 6000))
	a3 = CalcCount(calc(6001, 8000))
	a4 = CalcCount(calc(8001, 10000))
	a5 = CalcCount(calc(10001, 12000))
	a6 = CalcCount(calc(12001, 14000))
	
	# 启动子线程
	a1.start()
	a2.start()
	a3.start()
	a4.start()
	a5.start()
	a6.start()
	
	# 阻塞子线程
	a1.join()
	a2.join()
	a3.join()
	a4.join()
	a5.join()
	a6.join()
	
	
	a7 = a1.get_result()+a2.get_result()+a3.get_result()+a4.get_result()+a5.get_result()+a6.get_result()
	print(a7)
	print(datetime.now())
	
结果：
	
	>2018-06-04 22:51:21.066863
	>97952999
	>2018-06-04 22:51:21.069863

从结果中可以看出，计算1到14000的总和，使用多线程的话，时间花销用了0.003秒。主要的时间花销主要用于了线程的切换上了


#### 总结

以上案例体现出了：

>在 处理像科学计算 这类需要持续使用cpu的任务的时候 单线程会比多线程快

如果在网络爬虫的案例中可以体验出如下结论：

>在 处理像IO操作等可能引起阻塞的这类任务的时候 多线程会比单线程。因为在网络请求结束后，不管你的程序是否对IO进行操作，线程都会切换到就绪的线程中去执行。如果是单线程的话，就需要你将所有的IO操作等待运行结束后，才能进行下一个网络爬虫的请求，这样换来的就是，时间的延长。导致单线程比多线程效率更低的关键因素