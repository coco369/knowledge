# 知识库
知识库，总结在项目中实际使用的git命令，docker部署，mongodb，mysql等知识点

### git知识库

  - [git安装以及设置](git/git1.md)
  - [git的基本命令](git/git2.md)
### docker知识库

  - [基础](docker/docker.md)

### mysql数据库知识库

  - [第一天:基础]
      - [Mysql数据库基础语法](sql/mysql.md)
  - [第二天:提升练习]
      - [语法练习1](sql/mysql2_1.md)
      - [语法练习2](sql/mysql2_2.md)
  - [第三天:mysql与python交互]
      - [交互](sql/mysql3.md)
### redis知识库

  - [第一天:安装/基础]
      - [redis安装以及基础语法](sql/redis.md)
  - [第二天:订阅]
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

  - [第一天:环境与创建项目]

        - 环境搭建: virtualenv的安装与使用,pycharm中环境的配置
        - Django概念: MVC模式/MVT模式
        - 项目创建: 创建Django工程目录，创建应用app，使用admin管理后台
        - admin管理后台：超级用户的创建，模型注册，模型中数据展示(list_display)、搜索(search_field)、过滤(list_filter)等

      - [django概念介绍](django/1.Django基础入门/1.django概念.md)
      - [virtualenv环境](django/1.Django基础入门/2.virtualenv虚拟环境.md)
      - [创建django项目](django/1.Django基础入门/3.django简单项目.md)
      - [admin管理](django/1.Django基础入门/4.django管理后台.md)

  - [第二天:模型]

        - M模型：模型的定义，字段的定义，字段参数的定义。Meta元数据定义，定义表名称
        - 数据库配置，pymysql驱动配置，数据迁移执行命令
        - ORM对象关系映射概念：什么是ORM，ORM用于做什么？
        - 比较运算符，F/Q对象，限制结果集：contains，startswith，endswith，in，gt，gte，lt，lte，pk等
        - 数据的查询，all，filter，get，first，last，values等
        - 数据的创建：create()，对象save()，初始化模型再save()
        - 数据的更新：update()，对象save()
        - 数据的删除：delete()
      - [模型设计](django/2.Django模型/1.django模型定义.md)
      - [数据的CRUD练习](django/2.Django模型/2.django数据的CRUD练习.md)

  - [第三天:模型加餐/模板]

        - 模型设计概念：一对一，一对多，多对多的模型定义
        - 模型设计案例：学生和学生拓展表一对一模型设计，学生和课程表多对多模型设计，学生和班级一对多模型设计
        - 模板1：在settings.py文件中静态static的配置定义，在页面中静态文件的加载
        - 模板2：模板中逻辑运算符，if、ifequal、forloop、for empty等
        - 模板3：父模板中定义block块和子模板中继承与调用父模板中block块
        - 模板4：模板中注解，注解代码的可见与不可见，三种注解的区别
        - 模板5：模板中定义修饰变量的过滤器，使用管道符‘|’，以及Django中过滤器的自定义
          
      - [模型关联设计](django/2.Django模型/3.django模型关联关系.md)
      - [模板](django/3.Django模板与路由/1.django模板.md)

  - [第四天:视图1]

        - URL的正则匹配与带参URL和不带参URL定义
        - 带参URL的redirect跳转与参数传递，以及页面内中URL反向解析的定义
        - Django中DEBUG为False和True的区别,以及当DEBUG为False时，静态文件解析与错误(403、404、500)视图的定义
        - 请求与响应：请求中属性和方法，响应中属性和方法

      - [路由/反向解析](django/3.Django模板与路由/2.django路由.md)

  - [第五天:视图2]

        - form表单：字段的定义、form中错误信息的重定义、页面中错误信息的展示
        - 登录注册注销：django中如何快速的实现登录注册注销功能
        - 什么是会话技术，什么是HTTP无状态协议，解决HTTP无状态协议的方案----> cookie + session
        - cookie的使用：如何设置cookie，删除cookie，如何设置失效
        - session的使用：如何使用session，删除session，session中数据存储的时效。在Django中如何配置session，数据库中django_session表的使用
        - 案例1：cookie和session实现的原理
       
      - [cookies/session](django/4.Django会话/1.cookie与session.md)
      - [登录/注册--自己实现](django/4.Django会话/2.django注册登录(1).md)
      - [登录/注册--django实现](django/4.Django会话/3.django注册登录(2).md)

  - [第六天:插件]

        - 中间件middleware的工作原理，如何拦截各阶段的请求，重构拦截各阶段的方法
        - 数据分页：掌握Paginator分页的工作原理，实现分页的方式
        - 定义模型中上传文件字段，安装Pillow，定义上传文件的media路径，定义页面中如何解析media中上传图片
        - 中间件案例1： 实现登录注册功能
        - 上传文件与解析案例2: 实现文件上传功能
     
      - [验证码/分页](django/6.Django分页与权限/1.django分页.md)
      - [中间件](django/5.Django中间件与表单与文件上传/1.django中间件.md)
      - [文件上传](django/5.Django中间件与表单与文件上传/2.django文件上传.md)
      - [表单form](django/5.Django中间件与表单与文件上传/3.djangoform表单.md)
      - [文件上传练习](django/5.Django中间件与表单与文件上传/4.django文件上传练习.md)

  - [第七天:权限、角色]

          - 如何拓展Django的User模型，并自定义相关的权限
          - 权限系统中User模型、Group模型、Permission模型的ManyToManyFiled关联关系，以及数据的增、删、清空。
          - 权限装饰器: permission_reqired('应用app.权限名')
          - 菜单控制：通过全局perms变量进行权限和菜单的控制

       - [权限系统](django/6.Django分页与权限/2.django权限控制.md)

  - [第八天:日志/restful]

          - setting.py中日志logging文件的配置，logging的四大组成，loggers，handlers，filters，formatters的处理流程，以及日志打印
          
      - [日志](django/7.Django日志与celery/1.django日志.md)
      - [celery](django/7.Django日志与celery/2.django_celery.md)
      

  - [第九天:restframework2]
 
		 - 架构设计指导原则，rest的核心定义，如何定义符合规范的api接口。资源、请求、状态码的理解。
         - Django中restframework安装，settings.py中的定义，以及如何定义对资源的CRUD操作
         - 重构api响应结构，api中异常响应结构重构与定义
         - 定义序列化serializer，验证每一个字段的错误信息，配置参数等
         
       - [restful概念](django/8.Django的DRF/1.restful概念.md)
       - [响应结构/ajax-CRUD](django/8.Django的DRF/2.rest响应重构与mixins父类.md)

  - [第十天:restframework3]

         - api返回数据的分页配置，过滤类的定义与配置
		 - 调用postman实现通过api对数据进行CRUD操作
         - 总结drf中的视图、序列化器、过滤器等

      - [分页/过滤/筛选](django/8.Django的DRF/3.rest过滤分页筛选.md)
      - [总结](django/8.Django的DRF/4.djangorestframework总结.md)

  - [第十一天到十五天：项目(后端渲染页面)]
      - [爱鲜蜂案例2班](https://github.com/coco369/axf)
      - [爱鲜蜂案例3班](https://github.com/coco369/django-teaching-15days/tree/master/qf_1803/1.django/day09/%E4%BB%A3%E7%A0%81/axf)
      - [爱鲜蜂案例4班](https://github.com/coco369/django-teaching-15days/tree/master/qf_1804/1.django/day14/%E4%BB%A3%E7%A0%81/axf4)
      - [天天生鲜案例5班]
      	 - [前台代码](https://github.com/coco369/django-teaching-15days/tree/master/qf_1805/1.django/day15/%E4%BB%A3%E7%A0%81/fresh_shop)
      	 - [后台代码](https://github.com/coco369/django-teaching-15days/tree/master/qf_1805/1.django/day15/%E4%BB%A3%E7%A0%81/fresh_shop_back)
	
  - [第十一天到十五天: 项目(前后分离渲染)]
	
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

  - [第一天:入门基础]
  
	  	- flask配置：微的定义，最小flask的web应用，虚拟环境搭建，安装flask
		- mvc概念,项目的符合MVC模式的拆分
		- 项目运行管理：flask_script库使用，debug配置等
		- 路由: 路由匹配规则
		- 请求与响应：POST/GET请求传参，类字典的区别

	  - [flask简介/路由规则](flask/3.1.1-flask开发基础/flask入门与路由.md)
	  - [flask请求与响应与错误处理](flask/3.1.1-flask开发基础/flask请求与响应与异常.md)
	  - [flask蓝图](flask/3.1.1-flask开发基础/flask蓝图.md)
	
  - [第二天:视图]
  
		-  session/cookie概念与用法：
			-  1) flask默认使用cookie存储session的数据。 
			-  2)引入flask_session扩展库，实现使用数据库存储session中数据。
		-  应用案例1：分别使用两种存储session数据方式实现模拟登陆功能，以及装饰器的定义使用
		-  应用案例2：使用flask-login扩展库实现用户登录注销功能

	  - [session/cookie](flask/3.1.2-flask视图/cookie与会话(1).md)
	  - [应用案例1：自定义登录校验](flask/3.1.2-flask视图/会话(2).md)
	  - [应用案例2：flask-login登录校验](flask/3.1.2-flask视图/flask-login登录注册.md)
	  - [flask模板](flask/3.1.2-flask视图/flask模板.md)

  - [第三天: 模板]

	    - 基础模板的定义，模板的继承，挖坑以及填坑。宏定义
	    - 模板中逻辑控制，过滤器，以及静态static的配置
	    - 应用案例1: flask-wtf的form表单的使用

	  - [flask模板](flask/3.1.3-flask模板/flask模板.md)
	  - [flask表单](flask/3.1.3-flask模板/flask表单验证.md)

  - [第四天: 数据库]
  
		- 模型的定义，数据库的创建，模型之间的关联关系的定义以及CRUD操作
		- 深入数据库的增删改查，查询数据filter和filter_by
        - 运算符--contains、startswith、__gt__等
        - 筛选--offset、limit、get、first、paginate等
        - 逻辑运算符--and_、or_、not_
        - 模型之间的一对多的关联关系的定义
       
	  - [flask模型初窥](flask/3.1.4-flask数据库/flask模型1.md)
	  - [flask模型深入1](flask/3.1.4-flask数据库/flask模型2.md)
	  - [flask模型深入2](flask/3.1.4-flask数据库/flask模型3.md)
	
  - [第五天: 配置]

        - 钩子函数: before_request, after_request, teardown_request
        - 应用上下文g对象
        - 应用案例1: 钩子函数+g对象的使用，实现pymysql连接MySQL，并执行查询操作
        - 应用案例1: 登录、注册、登录验证
        - 应用案例2: 邮件发送
        - 应用案例3: 文件上传
       
	  - [钩子函数](flask/3.1.5-flask配置/flask中g对象和钩子.md)
	  - [文件上传](flask/3.1.5-flask配置/flask文件上传.md)
	  - [拓展](flask/3.1.5-flask配置/flask拓展.md)
	  - [邮件发送](flask/3.1.5-flask配置/flask邮件发送.md)
	    
	
  - [第六天到第10天：项目]
	  - [爱家案例](https://github.com/coco369/aj)
	  - [爱家案例2班](https://github.com/coco369/django-teaching-15days/tree/master/qf_1802/2.flask/day9/%E4%BB%A3%E7%A0%81/day06)
	  - [爱家案例3班](https://github.com/coco369/django-teaching-15days/tree/master/qf_1803/2.flask/day09/%E4%BB%A3%E7%A0%81/aj)
	  - [centos7部署项目](部署/aj_centos部署.md)
	
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
	    
        - Vue的全局操作、生命周期
        - Vue中axios的使用
        - Vue的Django进行前后交互中的跨域解决问题
        - Vue部署
        
     - [Vue生命周期](vue/vue提升/vue生命周期.md)
     - [Vue的axios使用](vue/vue提升/vue的axios使用.md)
	 - [Django后端的跨域配置](vue/vue提升/vue跨域.md)
	 - [Vue部署](vue/vue部署/部署.md)
	