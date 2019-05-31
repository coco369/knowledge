# Django学习知识库
> Auth: 王海飞
>
> Data：2018-04-20
>
> Email：779598160@qq.com
>
> github：https://github.com/coco369/knowledge
>

------

​        python学习之路，就是不断累积，不断学习的过程。该知识库讲解了Python Web框架内容，如Django、DjangoRestFramework、tornado、flask，redis，MySQL，MongoDB，docker，Vue等内容。如下展示知识结构目录图

[TOC]

### git知识库

  - [git安装以及设置](git/git1.md)
  - [git的基本命令](git/git2.md)
### docker知识库

  - [基础操作命令](docker/docker.md)
  - [镜像和容器的基础使用](docker/docker的使用.md)
  - [私有服务搭建与使用](docker/docker私有服务器搭建.md)
  - [docker部署](docker部署.md)

### mysql数据库知识库

- [Mysql数据库基础语法](sql/mysql.md)

- [语法练习1](sql/mysql2_1.md)
- [语法练习2](sql/mysql2_2.md)

- [mysql与python交互](sql/mysql3.md)

### redis知识库

- [redis安装以及基础语法](sql/redis.md)

- [订阅](sql/redis1.md)

### mongodb知识库

  - [安装及配置](sql/mongodb.md)
  - [基础语法](sql/mongodb语法.md)

### celery知识库

  - [安装配置与简单案例](celery/1.celery入门基础/1.安装配置与简单案例.md)

### PEP 8风格指南

  - [风格指南](PEP8风格指南.md)

### Django知识库

<a href="django/images/Django大纲.png">思维导图</a>

  - [虚拟环境与项目初认知](django/1.Django基础入门)

      - 虚拟环境搭建 - mkvirtualenv的使用 / virtualenv的使用 / python3中venv模块的使用 / Pycharm中虚拟环境的配置

      - 项目初认知 - MVC模式 or MVT模式 / 创建Django工程目录 / 创建应用app

      - admin管理后台 - 超级用户的创建，模型注册，模型中数据展示(list_display)、搜索(search_field)、过滤(list_filter)等

  - [模型](django/2.Django模型)

      - 模型概念 - ORM概念 / 模型的定义 / 字段的定义 / 字段参数的定义 / Meta元数据定义 / 表名定义 / 一对一关联 / 一对多关联 / 多对多关联

      - 数据库配置 - pymysql驱动配置 / 数据迁移命令 

      - 比较运算符 - F对象 / Q对象

      - 限制结果集 - contains / startswith / endswith / in / gt / gte / lt / lte / pk等

      - 数据的查询 - all / filter / get / first / last / values等

      - 数据的创建 - create() /  save() 

      - 数据的更新 - update() / save()

      - 数据的删除 - delete()

  - [模板](django/3.Django模板与路由)

      - 模板与静态配置 - 静态staticfiles_dirs的定义 / 静态资源的加载 / 资源反向解析url_for(有参和无参情况)

      - 模板语法 - 模板中逻辑运算符(if、ifequal、forloop、for 、empty等) / 模板继承 / 模板注解 / 过滤器(管道符'|')

  - [视图](django/3.Django模板与路由)

      - 路由规则 - URL正则匹配 / 带参URL定义 / 不带参URL定义

      - 响应 - redirect重定向(传参重定向 / 不传参重定向) / 模板渲染 / JSON数据响应 / 错误状态码(403、404、500)视图定义

      - 请求 - 请求属于与方法(method、path、user、FILEWS、GET、POST等) / 匿名用户AnonymousUser 

      - form表单验证 - 字段的定义 / 错误响应抛出 / 校验失败错误信息解析 / 校验clean方法 / 校验字段clean_fields方法 

- [Cookie与Session](django/4.Django会话)

     - 会话技术 - HTTP无状态协议 / 解决HTTP无状态协议 / Cookie产生场景 / Session产生场景

     - Cookie - 设置cookie / 删除cookie / 设置失效时长

     - Session - django_session表的定义 / 操作Session(增删改查) / 数据存储的时效

     - 登陆注册功能 - 使用django中高耦合用户模块实现功能 / 使用Cookie + Token形式实现功能 / 登陆状态校验装饰器

- [中间件、表单、文件上传](django/5.Django中间件与表单与文件上传)

     - 中间件middleware - 工作原理与处理流程 / 拦截各阶段的请求 / 重构拦截各阶段请求 / 登陆状态校验中间件

     - form表单验证 - 字段的定义 / 错误响应抛出 / 校验失败错误信息解析 / 校验clean方法 / 校验字段clean_fields方法 

     - 文件上传 - Pillow安装 / 存储路径media地址定义 / 模板解析文件

- [分页与权限](django/6.Django分页与权限)

     - 分页 - Paginator工作原理 / 分页角码 / 上一页 / 下一页 / 总数据库 / 当前页等

     - 权限模型定义 - User模型 / Group模型 / Permission模型 / 模型的ManyToManyFiled关联关系 / 权限中间表数据的增、删、清空

     - 权限装饰器 - permission_reqired('应用app.权限名')

     - 菜单控制 - 通过全局perms变量进行权限和菜单的控制

- [日志/celery](django/7.Django日志与celery)

     - 日志的配置与构成 - logging的四大组件(loggers 、handlers、filters、formatters) / 日志处理流程 / 日志中间件

     - celery

- [DRF](django/8.Django的DRF)
  - 架构设计指导原则 - 接口定义规则 / REST风格 / 资源 / HTTP请求方式 / HTTP状态码
  - DRF的应用 - djangorestframework安装 / django-filter安装 / 接口的定义 / 资源的CRUD
  - 重构api响应结构 - 响应结构重构与定义
  - 序列化serializer - 字段校验 / 错误信息自定义 / 验证方法validate / Serializer和ModelSerializer
  - 分页配置
  - 过滤类filter_class - 过滤字段 / 过滤方法method

- [项目(后端渲染页面)]
  - [爱鲜蜂案例2班](https://github.com/coco369/axf)
  - [爱鲜蜂案例3班](https://github.com/coco369/django-teaching-15days/tree/master/qf_1803/1.django/day09/%E4%BB%A3%E7%A0%81/axf)
  - [爱鲜蜂案例4班](https://github.com/coco369/django-teaching-15days/tree/master/qf_1804/1.django/day14/%E4%BB%A3%E7%A0%81/axf4)
  - [天天生鲜案例5班]
     - [前台代码](https://github.com/coco369/django-teaching-15days/tree/master/qf_1805/1.django/day15/%E4%BB%A3%E7%A0%81/fresh_shop)
      - [后台代码](https://github.com/coco369/django-teaching-15days/tree/master/qf_1805/1.django/day15/%E4%BB%A3%E7%A0%81/fresh_shop_back)

- [项目(前后分离渲染)]
    - 前端vue框架
  - 后端drf框架
     - [vue框架源代码地址](https://github.com/coco369/m_axf)
     - [开发前技术准备](django/项目技术准备/准备.md)
     - [drf框架后端源代码](https://github.com/coco369/m_axf_drf)

- [部署]
  - [centos7部署项目](部署/centos部署.md)
  - [ubuntu部署项目](部署/ubuntu部署.md)

- [拓展]
  - [调试工具](django/9.Django扩展/1.debug的安装与使用.md)
  - [kindeditor富文本编辑器](django/9.Django扩展/2.kindeditor富文本编辑器.md)

### Flask知识库

<a href="flask/images/Flask大纲.png">思维导图</a>

  - [Flask初认知](flask/3.1.1-flask开发基础)
       - Flask框架 - 微型框架的定义 / Django、Flask、Sanic、Tornado等框架的对比
       - Flask最小应用项目 - 最简Web项目定义 / 启动命令参数 / Flask_Script的使用
       - 路由规则 -  转化器的定义(int、string、uuid、float、path等) 
       - 请求与响应：POST/GET请求传参，类字典的区别
       - 蓝图Flask_Blueprint - 路由模块化管理 / 路由前缀url_prefix / 重定向url_for方向解析

  - [视图](flask/3.1.2-flask视图)
     -  cookie概念与用法 - cookie的设置与删除 / cookie + token实现状态保持
     -  session概念与用法 - flask默认使用cookie存储session的数据 /  引入flask_session扩展库，实现使用数据库存储session中数据
     -  装饰器 - 登陆状态校验装饰器
     -  案例1 - 分别使用两种存储session数据方式实现模拟登陆功能，以及装饰器的定义使用
     -  案例2 - 使用flask-login扩展库实现用户登录注销功能

  - [模板](flask/3.1.3-flask模板)
        - 模板概念 - 基础模板的定义 / 模板的继承 / 挖坑以及填坑 / 静态文件static的配置
        - 模板中逻辑控制 - for / if / loop / 过滤器 / 宏定义macro
        - 表单 - Flask-WTF的form表单定义 / 字段校验DareRequired / 长度校验Length / 字段相等EqualTo / 方法validate_fields定义 / 异常抛出ValidateError / 错误信息解析errors 

  - [数据库](flask/3.1.4-flask数据库)
     - 模型 - 模型字段定义 / 模型字段约束 / 模型表明tablename定义 / 模型一对一关联 / 模型一对多关联
     - ORM操作(增 / 改) - 事务add() / add_all() / commit()
     - ORM操作(删) - 事务delete()
     - ORM操作(查) - filter / filter_by / contains、startswith 、like 、endswith、gt、ge、lt、le、offset、limit、get、first、paginate、and__、or_、not_、in_、notin_
  - [拓展](flask/3.1.5-flask拓展)
        - 钩子函数 - before_request, after_request, teardown_request
        - 应用上下文g对象
        - 应用案例1: 钩子函数+g对象的使用，实现pymysql连接MySQL，并执行查询操作
        - 应用案例1: 登录、注册、登录验证
        - 应用案例2: 邮件发送
        - 应用案例3: 文件上传

  - [第六天到第10天：项目]
      - [爱家案例](https://github.com/coco369/aj)
        - [爱家案例2班](https://github.com/coco369/django-teaching-15days/tree/master/qf_1802/2.flask/day9/%E4%BB%A3%E7%A0%81/day06)
        - [爱家案例3班](https://github.com/coco369/django-teaching-15days/tree/master/qf_1803/2.flask/day09/%E4%BB%A3%E7%A0%81/aj)
        
        - [centos7部署项目](部署/aj_centos部署.md)
        - [ubuntu部署博客项目](部署/blog部署.md)

  - [Flask和Django区别]
      - [区别](flask/flask和django的区别.md)


### 爬虫


  - [第一天:爬虫]
  
      	- 概念：爬虫的由来/用来做什么
      	- 数据采集与分析：urllib/requests/bs4/mongodb/mysql/redis等
      	- 请求头-反爬虫：User-Agent，Accept，Accept-Language等
      	- 百度搜索：中文的编码解码
      	- ssl: ssl认证
      	- 应用案例1：urllib获取百度首页源代码/爬取智联某工作某地点的岗位信息
      	- 应用案例2：猫眼网站信息
      	- 作业1：爬取智联上某工作某地点的工作名称，公司等信息
      	- 作业2：爬取格言网(https://www.geyanw.com/)上的某一个模块的名言警句

      - [爬虫基础概念](spider/1爬虫基本概念.md)
      - [爬虫引入/User-Agent讲解](spider/1.0spider_concept_urllib.md)
      - [应用案例1:爬取智联工作/百度源码](spider/1.1spider_baidu_zhilian_search.md)
      - [应用案例2:猫眼](spider/1猫眼网站实战.md)

  - [第二天:数据采集]
    
     	- 爬取工具：requests使用、bs4使用、urllib使用
     	- xpath语法、re正则表达式语法
     	- 应用案例1：获取豆瓣电影中动态加载电影资源信息
     	- 应用案例2:爬取知乎发现里面的提问的链接数，和链接地址
       ​       
	  - [采集(bs4)](spider/2数据采集bs.md)
	  - [采集(requests)](spider/2数据采集requests.md)
      - [提取xpath/re](spider/2.2spider_re_xpath.md)
      - [应用案例1:爬知乎的提问/豆瓣电影信息](spider/2.1spider_movies_questions.md)
      - [应用案例2:爬取搜狐体育的新闻信息](spider/2.3spider_souhu_sports.md)

  - [第三天:多线程爬虫]
  
    	- 概念：线程、进程、同步、异步、并发、阻塞、非阻塞、并发、并行
        - 进程、线程概念：多线程定义，守护线程，线程启动
        - 线程锁
        - 应用案例1：I/O密集型，计算密集型的单线程多线程对比
        
      - [并发、并行、同步、异步线程、进程](spider/3.0spider_process_threading.md)
      - [线程锁](spider/3.1spider_threading_lock.md)
      - [应用案例1:计算密集型和IO密集型的性能对比](spider/3.2spider_threading_IO_calc_GIL.md)
      - [应用案例2:多线程爬虫](spider/3.3spider_threading_douban.md)

  - [第四天:协程/数据持久化]

   		- 迭代器、生成器的原理概念、斐波那契的实现
        - 协程的概念，原理，生产者-消费者的实现
        - 数据持久化，redis安装配置、缓存，mongodb安装配置、语法、缓存
        - aiohttp:异步非阻塞的

      - [协程](spider/4.0spider_yield.md)
      - [练习题](spider/4.1spider_yield_practice.md)
      - [数据库持久化](spider/4.2spider_sql_engine.md)
      - [应用案例1:使用协程爬取豆瓣电影并持久化](spider/4.3spider_async_await.md)



 - [第五天:动态解析]

		- 动态内容分析: 什么是动态内容，分析豆瓣的动态内容加载
		- javascript逆向，selenium自动化测试框架
		- 应用案例1: 使用selenium模拟登陆知乎
		- 应用案例2: 使用selenium解析豆瓣电影信息
		
	  - [动态内容解析/selenium用法](spider/5.0spider_javascript_analyst.md)
	  - [模拟登陆知乎并截图/解析豆瓣电影信息](spider/5.1spider_selenium_login_zhihu_and_douban_movies.md)

  - [第六天:验证]
	
		- 模拟登陆:请求url分析,请求参数分析，模拟登陆状态保持
		- form模拟登陆、验证码

	- [应用案例1：模拟登陆github](spider/6.0spider_github_login.md)
	- [应用案例2: 验证码识别](6.1spider_verifi_aliyun.md)

  - [第七天--第十天]
  
	    - scrapy框架组件，处理流程，数据持久化
	    - scrapy项目环境搭建，创建项目命令，执行启动操作，各相关文件的处理逻辑
	    - scrapy_redis分布式爬虫原理
	    
	    - 案例1：爬取起点小说网的小说分类，以及分类的url
	    - 案例2：爬取豆瓣电影的信息，并使用mongodb持久化
		- 案例3：爬取链家房源信息，并存储在csv文件
		- 案例4：爬取微博大V的粉丝数，关注，博客等信息

      	- [scrapy框架的介绍以及案例1](spider/7.0spider_scrapy1.md)
      	- [scrapy爬虫豆瓣信息](spider/7.1spider_scrapy2.md) 
      	- [scrapy爬取链家信息](spider/code/scrapy框架/lianjiaspider)
      	- [scrapy爬取微博用户信息](spider/7.2spider_weibo_scrapy3.md)
	  
	- [分析接口](spider/7.2spider_weibo_scrapy3.md)
	- [分析用户信息](spider/7.3spider_weibo_scrapy_user_info.md)
	- [分析关注信息](spider/7.4spider_weibo_scrapy_follows_info.md)
	- [分析粉丝信息](spider/7.5spider_weibo_scrapy_fans_info.md)
	- [IP代理池/User-Agent设置](spider/7.6spider_weibo_scrapy_ips_user_agent.md)
	- [scrapy爬取豆瓣即将上线电影/正在热播电影信息](spider/code/scrapy框架/doubanMoviespider)
	- [分布式爬虫](spider/7.7spider_scrapy_redis.md)


### Tornado知识库

  - [第一天: 入门基础]

	    - Tornado配置：虚拟环境搭建和tornado的安装、最小tornado的web应用、启动命令端口配置等
		- 请求与响应: 请求参数、响应参数等
		- 路由: 路由匹配规则

	 - [Tornado简介/入门](tornado/3.2.1-Tornado开发基础/tornado介绍与入门.md)
	 - [Tornado请求与响应](tornado/3.2.1-Tornado开发基础/tornado请求与响应.md)
	 - [Tornado路由规则/HTTP行为方法/切入点函数](tornado/3.2.1-Tornado开发基础/tornado路由与切入点函数.md)

  - [第二天: 进阶]
     ​      
     - tornado静态资源与模板: 模型的继承与模板语法、静态资源的加载static_url等
       - 数据库: sqlalchemy的安装、模型定义、模型迁移等
       - Tornado WebSocket网络协议: 保持浏览器与服务器之间的通信，并实现持久化连接，数据的双向传递等。 

      - [Tornado模板与静态资源加载](tornado/3.2.2-Tornado进阶/tornado模板资源.md)
      - [Tornado模型](tornado/3.2.2-Tornado进阶/tornado数据库.md)

  - [第三天: 进阶2]
	 		
		- tornado跨站请求伪造XSRF
		- 同步、异步、阻塞、非阻塞概念，以及同步Web服务
		- ab压力测试
		- tornado异步服务与异步生成器
  		- 应用案例1: 开发websocket聊天系统
	​	
	 - [Tornado跨站请求伪造](tornado/3.2.3-Tornado进阶2/tornado跨站请求.md)
	 - [Tornado异步服务](tornado/3.2.3-Tornado进阶2/tornado异步生成器与异步服务.md)
	 - [应用案例1: websocket聊天室](tornado/3.2.3-Tornado进阶2/tornado-websocket.md)
	
  - [第四天: 人脸识别项目]

	     - tornado人脸识别，实现注册登录功能
	

	 - [Tornado人脸识别项目](tornado/3.2.4-Tornado项目/tornado人脸识别.md)


  - [第五天: 数据监控后台项目]

	    - 数据监控项目: 前端页面采用echarts展示图像报表、后端采用tornado进行数据实时更新

	 - [Tornado数据监控后台项目](tornado/3.2.5-Tornado项目/tornado数据监控后台项目.md)


### 机器学习

  - [第一天: jupyter入门]
  - [第二天: pandas入门]
  - [第三天: pandas进阶1]
  - [第四天: pandas进阶2]
  - [第五天: scipy]
  - [第六天: matpoltlib]
  - [第七天: KNN]
  - [第八天: KNN]
  - [第九天: 线性回归与逻辑斯蒂回归]
  - [第十天: 决策树与贝叶斯]
  - [第十一天: SVM与K均值聚类]
  - [第十二天: 机器学习框架 TensorFlow1]
  - [第十三天: 机器学习框架 TensorFlow2]
  - [第十四天: 自然语言处理与社交网络处理]
  - [第十五天:  综合案例信用卡反欺诈]

### VUE框架

  - [第一天: 入门]

	    - Vue配置: node.js安装、cnpm的安装、vue的安装、vue项目的创建以及项目的启动
	    - Vue组件: 新增组件，修改启动页面的展示效果
	    - Vue内部指令: v-text、v-html、v-if、v-else、v-show、v-model、v-bind、v-on等
        - Vue计算computed、监听watch
	    - 应用案例1: 路由配置与点击链接渲染页面
	    - 应用案例2: 外部数据的引入，点击按钮修改页面数据

	 - [Vue配置与启动](vue/vue入门基础/vue入门基础.md)
	 - [自定义组件](vue/vue入门基础/vue第一个组件.md)
	 - [路由router-link](vue/vue入门基础/vue路由.md)
	 - [Vue指令](vue/vue入门基础/vue指令.md)
     - [Vue重要选项](vue/vue入门基础/vue重要选项.md)
	 - [应用案例1: 路由点击事件](vue/vue入门基础/vue路由配置应用.md)
	 - [应用案例2: 数据引入与属性修改](vue/vue入门基础/vue数据引入与属性修改.md)

  - [第二天: 提升]
	​    
        - Vue的全局操作、生命周期
        - Vue中axios的使用
        - Vue的Django进行前后交互中的跨域解决问题
        - Vue部署
      
     - [Vue生命周期](vue/vue提升/vue生命周期.md)
     - [Vue的axios使用](vue/vue提升/vue的axios使用.md)
	 - [Django后端的跨域配置](vue/vue提升/vue跨域.md)
	 - [Vue部署](vue/vue部署/部署.md)
	