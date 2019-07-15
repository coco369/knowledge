# tornado使用操作指南--队列Queue

> Auth: 王海飞
>
> Data：2019-07-11
>
> Email：779598160@qq.com
>
> github：https://github.com/coco369/knowledge 

### 1. 前言

​	队列可以并发的执行多个线程，线程概念: 处理线程与请求线程

​        处理线程只需要讲请求的数据放入到队列容器的内存中，而请求处理线程只需要来队列容器内存中获取数据并处理即可。两种不同线程之间互相不影响，处理数据的线程down掉不会影响到请求数据的线程 。

​	队列实现了解耦（消费者与生产者模式），提高了效率与性能。

​	在Python中有四种内置的同步队列:

​		Queue：FIFO 即first in first out 先进先出

​		LifoQueue：LIFO 即last in first out 后进先出

​		PriorityQueue：优先队列，级别越低，越优先

​		deque: 双边队列

​	Tornado的`tornado.queue`采用协程实现了异步的生产者/消费者模式，跟Python内置的通过线程实现的queue模块功能类似。 



#### 2. Queue语法 

Tornado中队列Queue支持异步操作

##### 1) 获取队列中数据

Queue.get() 获取队列中元素，如果队列中没有元素，则一直等到queue中有元素。

每次get()执行后，需执行task_done()，表示这个任务执行完毕 

##### 2）向队列中加入数据

Queue.put()向队列中插入数据，如果队列已达最大长度限制，会暂停，直到队列有空闲空间 

##### 3）队列Join

等待，直到所有任务都执行完毕，即所有元素都调用了task_done() 



























