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

​        python学习之路，就是不断累积，不断学习的过程。该知识库讲解了Python Web框架内容，如Django、DjangoRestFramework、tornado、flask，redis，MySQL，MongoDB，docker，Vue等内容。如下展示已整理的知识：

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
  - [部署](部署)
      - [centos7部署项目](部署/aj_centos部署.md)
      - [ubuntu部署博客项目](部署/blog部署.md)
  - [Flask和Django区别]
      - [区别](flask/flask和django的区别.md)


### 爬虫


  - [爬虫入门与实战](spider/1.爬虫入门与实战)

       - 爬虫概念 - 爬虫原理 / 请求(请求头、cookie、headers等) / 响应(响应状态码、响应内容、响应headers等)
       - 数据采集库 - urllib / requests /  Selenium/ / Scrapy
       - 数据分析 - 正则表达式 / lxml / BeautifulSoup4  / xpath
       - 案例1 - 使用urllib库爬取智联上某工作某地点的工作名称，公司等信息
       - 案例2 - 使用requests库爬取猫眼电影的信息

       - 案例3 - 获取豆瓣电影中动态加载电影资源信息

       - 案例4- 爬取知乎发现里面的提问的链接数，和链接地址

  - [爬虫动态剖析与实战](spider/2.爬虫动态剖析入门与实战)

     - 自动化工具Selenium - 动态网站分析 / Selenium中标准选择器、CSS选择器、标签选择器语法
     - 案例1 - 知乎和豆瓣电影的动态信息的爬取 
     - 案例2 - 验证码破解（B站极验验证码的破解、图片验证码的破解）
     - 案例3 - 爱奇艺VIP视频爬取

  - [Scrapy框架](spider/3.爬虫框架进阶)

      - Scrapy框架 - Scrapy框架图解 / 下载中间件 / Spider中间件 / Spiders爬虫 / Item实体 / Pipelines项目管道 
      - 代理 - IP代理切换proxy / User_Agent用户代理切换 / Cookie代理池切换
      - 分布式Scrapy-redis - 分布式概念 / 爬取队列维护 / 主机master / 从机slave

  - [爬虫性能](spider/4.爬虫性能)

      - 同步、异步、协程、多线程、单线程、多进程
      - 异步aiohttp


### Tornado知识库

  - [入门基础](tornado/3.2.1-Tornado开发基础) 
      - Tornado配置 - 虚拟环境搭建 / tornado的安装 / 最小tornado的web应用 / 启动命令端口配置
      - 请求与响应 - HTTP行为方法 / 切入点函数 / 请求参数(get_argument) / 响应参数
      - 路由 - 路由匹配规则
  - [进阶](tornado/3.2.2-Tornado路由、模板、数据库)
     - tornado静态资源与模板 - 模型的继承与模板语法 / 静态资源的加载static_url
     - 数据库 -  sqlalchemy的安装 / 模型定义 / 模型迁移
     - Tornado WebSocket网络协议: - 保持浏览器与服务器之间的通信，并实现持久化连接，数据的双向传递等

  - [同步与异步](tornado/3.2.3-Tornado异步、协程)
     - tornado跨站请求伪造XSRF - 概念 / 防范
     - 同步与异步 - 同步 / 异步 / 阻塞 / 非阻塞 / 协程 / 异步生成器 / ab压力测试
     - 队列 
     - 应用案例1: 开发websocket聊天系统
  - [实战项目](tornado/3.2.4-Tornado项目)
         - 案例1: WebSocket聊天室



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

  - [入门](vue/vue入门基础)
      - Vue配置 - node.js安装 / cnpm的安装 / vue的安装 / vue项目的创建 / 项目启动run / 项目build
      - Vue组件 - 自定义组件 / 加载组件 / 配置链接地址
      - Vue内部指令 - v-text / v-html / v-if / v-else / v-show / v-model / v-bind / v-on等
      - Vue计算属性 - computed / 监听watch
  - [提升](vue/vue提升)
      - Vue的全局操作 - 生命周期 / axios请求 / 跨域配置 
      - Vue部署 - 项目build相关配置 / Nginx配置 / 反向代理配置

### K8s

- k8s的概念、安装 / minikube的使用