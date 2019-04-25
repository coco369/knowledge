
# 使用centos部署flask项目

>Auth: 王海飞
>
>Data：2018-09-07
>
>Email：779598160@qq.com
>
>github：https://github.com/coco369/knowledge

### 前言

在CentOS中Flask的项目部署和Django项目部署有异曲同工之效, 包括数据库的配置，远程设置访问,python3的安装都是相同的。在部署Flask项目的时候，可以借鉴Django部署的部分配置。[传送门](centos部署.md))

### 项目上线的流程与分支管理
 
在企业中一个项目从开发到部署上线需要经过严格的流程控制，如开发阶段是开发人员进行功能开发的阶段、测试阶段1是测试人员介入进行从简单到复杂的业务测试的阶段、测试阶段2是测试人员进行程序性能测试的阶段、上线阶段是运维人员介入实现程序上线部署的阶段。因此在不同的阶段都需要做程序的部署，而程序的部署方式是根据性能需求和业务需求进行选择。

如下图展示从开发到开发环境部署、测试环境部署、线上环境部署的整个流程，以及git的使用和项目的版本分支管理:

![环境与分支](../flask/images/环境与分支.png)

### 配置

在服务器中首先需要完成以下五步基础环境搭建，才能开始部署操作：

步骤1：创建安装环境文件夹、配置信息文件夹、日志信息文件夹、项目代码文件夹。
	
	命令：mkdir conf logs env src
步骤2：上传项目代码到src文件夹中

步骤3：创建虚拟环境，并安装项目所需要的包
	
	安装：yum install python-virtualenv
	创建：virtualenv --no-site-packages -p /usr/local/python3/python xxenv

	安装包： 指定虚拟环境中的pip3 install -r 指定项目中的requerement.txt文件	

步骤4：安装redis

	安装：yum install redis
	启动：redis-server
	访问：redis-cli

步骤5：配置conf中的xxnginx.conf文件和xxuwsgi.ini文件
	
ajnginx.conf内容如下：

	server {
	    listen    80;
	    server_name 47.106.180.185 localhost;

	    access_log /home/logs/ajaccess.log;
	    error_log /home/logs/error.log;

	    location / {
			include uwsgi_params;
	        uwsgi_pass 127.0.0.1:8891;

			uwsgi_param UWSGI_CHDIR /home/src/aj;
			uwsgi_param UWSGI_SCRIPT manage:app;
	    }    
	}

ajuwsgi.ini内容如下：

	[uwsgi]
	master = true
	socket = 127.0.0.1:8891
	chdir = /home/src/aj
	pythonpath = /home/env/ajenv/bin/python3
	callable = app
	logto = /home/logs/ajuwsgi.log

步骤6：修改总的nginx.conf文件，并重启

在/etc/nginx/nginx.conf文件中加入自定的xxnginx.conf文件。

	引入方式为： inlucde 指定自定义xxnginx.conf的路径；
重启nginx命令，以及相关的命令：

	启动： systemctl start nginx
	暂停： systemctl stop nginx
	重启： systemctl restart nginx
	查看状态： systemctl status nginx

#### 1. 测试环境中部署方式

在测试环境中使用启动命令直接运行项目：

启动命令：

	指定虚拟环境下的python3 指定manage.py路径 runserver -h 0.0.0.0 -p 80 -d

如：

	/home/env/ajenv/bin/python3 /home/src/aj/manage.py runserver -h 0.0.0.0 -p 80 -d

#### 2. 正式环境中部署方式

在正式环境中使用nginx+uwsgi进行部署，安装nginx的方式在部署Django中已经讲解清楚了，如有不清楚，请点击[传送门](centos部署.md)

在正式环境中启动分以下三步骤：

步骤1：在manage.py启动文件中，添加访问首页的路由地址，如下所示：

	# 启动首页地址
	@app.route('/')
	def home_index():
		return redirect(url_for('house.index'))

步骤2：启动nginx

	systemctl restart nginx

步骤3：启动uwsgi

	指定虚拟环境中uwsgi的路径 --ini 指定xxuwsgi.ini路径

如：
	
	/home/env/ajenv/bin/uwsgi --ini /home/conf/xxuwsgi.ini

通过如上的测试，即可部署项目成功。如果访问网站出现‘502 bad gateway’表示网关超时，需要重新启动nginx或者uwsgi。如果出现500 服务器内部错误，则需要查看在xxuwsgi.ini中设置的uwsgi的日志文件。从这两个地方去排查错误，基本可以解决绝大部分的部署问题。