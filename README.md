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

### PEP 8风格指南
  
  - [风格指南](PEP 8风格指南.md)

### Django知识库
  - [第一天:环境与创建项目]
      - [django概念介绍](django/1.1django_pattern.md)
      - [virtualenv环境](django/1.2python_virtualenv.md)
      - [创建django项目](django/1.3django_halloWorld.md)
      - [admin管理](django/1.4django_admin.md)
  - [第二天:模型]
      - [模型设计](django/2.1django_models.md)
      - [练习](django/2.2django_mysql_lianxi.md)
  - [第三天:模型加餐/模板]
      - [模型关联设计](django/3.1django_model_more.md)
      - [模板](django/3.2django_temp.md)
  - [第四天:视图1]
      - [路由/反向解析](django/4.1django_urls.md)
  - [第五天:视图2]
      - [cookies/session](django/5.1django_coo_sess.md)
      - [登录/注册--自己实现](django/5.2django_regist_login.md)
      - [登录/注册--django实现](django/5.3django_regist_login.md)
  - [第六天:插件]
      - [验证码/中间件/分页](django/6.1django_plug.md)
      - [文件上传](django/6.2django_media.md)
  
  - [第七天:日志/restful]
      - [日志](django/7.1django_log.md)
      - [restful1](django/7.2django_restful.md)
  - [第八天:权限、角色]
	  - [权限、角色](django/8.1django_role_premission.md)
  - [第九天:restframework2]
	  - [响应结构/ajax-CRUD](django/9.1django_restful3.md)
  - [第十天:restframework3]
	  - [分页/过滤/筛选](django/10.1django_restful4.md)
  - [第十一天到十五天：项目]
	  - [爱鲜蜂案例](https://github.com/coco369/axf)
	  - [centos7部署项目](centos部署.md)

### Flask知识库
  - [第一天:HelloFlask]
  
	  	- flask配置：微的定义，最小flask的web引用，虚拟环境搭建，安装flask
		- mvc概念
		- 项目运行管理：flask_script库使用，debug配置等
	  - [flask简介](flask/1.0flask_helloflask.md)
	  - [flask蓝图](flask/1.1flask_blueflask.md)
  - [第二天:views]
	  
		- 请求与响应：POST/GET请求传参，类字典的区别
		-  session/cookie概念：用法，redis的配置
		
	  - [flask请求与响应/错误处理](flask/2.1flask_request_response_error.md)
	  - [session/cookie](flask/2.2flask_session_cookie.md)
  - [第三天:templates与models]
	  - [flask-template](flask/3.1flask_templates.md)
	  - [flask-models1](flask/3.2flask_models.md)
  - [第四天:models与一对多关系]
	  - [flask-models2](flask/4.1flask_models.md)
  - [第五天:多对多关系/debugtoolbal]
	  - [flask-models3](flask/5.1flask_models.md)
	  - [flask-extensions](flask/5.2flask_extensions.md)
  - [第六天到第10天：项目]
	  - [爱家案例](https://github.com/coco369/aj)

### 爬虫


  - [第一天:爬虫]
		
		- 概念：爬虫的由来/用来做什么
		- 数据采集与分析：urllib/requests/bs4/mongodb/mysql/redis等
		- 请求头-反爬虫：User-Agent，Accept，Accept-Language等
		- 百度搜索：中文的编码解码
		- ssl: ssl认证
		- 应用案例1：urllib获取百度首页源代码，其中User-Agent的使用
		- 应用案例2：爬去智联上某工作某地点的岗位个数
		- 作业：爬取qq音乐的歌曲，并保存
	  - [爬虫引入/User-Agent讲解](spider/1.0spider_concept_urllib.md)
	  - [应用案例:爬取智联工作/百度源码](spider/1.1spider_baidu_zhilian_search.md)


  - [第二天:数据采集]
		
		- 爬取工具：requests使用、bs4使用、urllib使用
		- xpath语法、re正则表达式语法
		- 应用案例1：获取豆瓣电影中动态加载电影资源信息
		- 应用案例2:爬取知乎发现里面的提问的链接数，和链接地址
	  - [采集(bs4/requests)](spider/2.0spider_collect.md)
	  - [提取xpath/re](spider/2.2spider_re_xpath.md)
	  - [应用案例:爬知乎的提问](spider/2.1spider_movies_questions.md)

	
  - [第三天:多线程爬虫]
  
  		- 概念：线程、进程、同步、异步、并发、阻塞、非阻塞、并发、并行
	  	- 进程、线程概念：多线程定义，守护线程，线程启动
	  	- 线程锁
	  	- 应用案例1：I/O密集型，计算密集型的单线程多线程对比
	  	
	  - [并发、并行、同步、异步线程、进程](spider/3.0spider_process_threading.md)
	  - [线程锁](spider/3.1spider_threading_lock.md)
	  - [应用案例1:计算密集型和IO密集型的性能对比](spider/3.2spider_threading_IO_calc_GIL.md)
	  - [应用案例2:多线程爬虫](3.3spider_threading_douban.md)
	  

  - [第四天:协程/数据持久化]
	    
 		- 迭代器、生成器的原理概念、斐波那契的实现
	  	- 协程的概念，原理，生产者-消费者的实现
	  	- 数据持久化，redis安装配置、缓存，mongodb安装配置、语法、缓存

	  - [协程](spider/4.0spider_yield.md)
	  - [练习题](spider/4.1spider_yield_practice.md)
	  - [数据库持久化](spider/4.2spider_sql_engine.md)



 - [第五天:动态解析]

		- 动态内容分析: 什么是动态内容，分析豆瓣的动态内容加载
		- javascript逆向，selenium自动化测试框架
		
	  - [动态内容解析](spider/5.0spider_javascript_analyst.md)

  - [第六天:验证]

		- form模拟登陆、验证码


  - [第七天--第九天]
 
	    - scrapy框架
  
  - [第十天:综合案例] 






