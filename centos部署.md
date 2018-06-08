
# 使用centos部署django项目

>Auth: 王海飞
>
>Data：2018-06-07
>
>Email：779598160@qq.com
>
>github：https://github.com/coco369/knowledge


### 安装MariaDB

安装命令

	yum -y install mariadb mariadb-server

安装完成MariaDB，首先启动MariaDB

	systemctl start mariadb

设置开机启动

	systemctl enable mariadb

### 设置密码

命令: mysql\_secure\_installation

	Enter current password for root:<–初次运行直接回车
	
	设置密码
	
	Set root password? [Y/n] <– 是否设置root用户密码，输入y并回车或直接回车
	
	New password: <– 设置root用户的密码
	Re-enter new password: <– 再输入一次你设置的密码
	
	其他配置
	
	Remove anonymous users? [Y/n] <– 是否删除匿名用户，回车
	
	Disallow root login remotely? [Y/n] <–是否禁止root远程登录,回车,
	
	Remove test database and access to it? [Y/n] <– 是否删除test数据库，回车
	
	Reload privilege tables now? [Y/n] <– 是否重新加载权限表，回车
	
	初始化MariaDB完成，接下来测试登录
	
	mysql -u root -p password

### 开启远程连接

在mysql数据库中的user表中可以看到默认是只能本地连接的，所有可以添加一个新的用户，该用户可以远程访问

#### 1. 创建用户

	# 先使用数据库
	use mysql;

	# 针对ip
	create user 'root'@'192.168.10.10' identified by 'password';
	
	#全部
	 create user 'root'@'%' identified by 'password';

#### 2. 授权

	# 给用户最大权限
	grant all privileges on *.* to 'root'@'%' identified by 'password';
	
	# 给部分权限(test 数据库)
	
	grant all privileges on test.* to 'root'@'%' identified by 'password' with grant option;

	# 刷新权限表
 	flush privileges;

	# 查看
	show grants for 'root'@'localhost';

接下来就可以在远程的数据库可视化工具中直接访问该服务器中的mysql了。

	# 访问数据库
	mysql -u root -p

### 安装python3.6

在centos中，系统默认只提供python2.7的版本，但是项目我们使用的python3.6的版本。所有我们自己安装python3


#### 安装Python3的方法

首先安装依赖包

	yum -y groupinstall "Development tools"
	
	yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel

然后根据自己需求下载不同版本的Python3，我下载的是Python3.6.2

	wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tar.xz

	然后解压压缩包，进入该目录，安装Python3

	tar -xvJf  Python-3.6.2.tar.xz
	cd Python-3.6.2
	./configure --prefix=/usr/local/python3
	make && make install

最后创建软链接

	ln -s /usr/local/python3/bin/python3 /usr/bin/python3
	
	ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3


### 安装环境

#### 1. 安装virtualenv

	yum install python-virtualenv

#### 2. 创建虚拟环境

	virtualenv --no-site-packages env

	cd env
	
	# 激活虚拟环境
	source bin/activate

#### 3. 安装环境需要的包

	pip install -r re_install.txt

	其中re_install.txt文件中记录的是需要安装包的名称以及对应的版本

### 部署

该部署采用的是cenots7系统来部署

Django的项目中，在工程目录下settings.py文件中有一个DEBUG=True参数，如果DEBUG=False则会出现js,css，img无法加载的情况出现。

原因如下：

Django框架仅在开发模式下提供静态文件服务。当我开启DEBUG模式时，Django内置的服务器是提供静态文件的服务的，所以css等文件访问都没有问题，但是关闭DEBUG模式后，Django便不提供静态文件服务了。想一想这是符合Django的哲学的：这部分事情标准服务器都很擅长，就让服务器去做吧！

#### 1. 测试环境中部署方式

在测试环境中一般都直接使用python manage.py runserver的方式去运行项目。其中就涉及到DEBUG=False的修改，静态目录的修改等，具体修改如下：

	修改settings.py配置文件中的DEBUG=False模式，修改ALLOEWD_HOST=['*']

	修改工程目录下的urls.py

	from django.views.static import serve

	urlpatterns = [
	    url(r'^admin/', admin.site.urls),
	    url(r'^axf/', include('axf.urls', namespace='axf')),

		# 增加以下的url路由
	    url(r'^static/(?P<path>.*)$', serve, {"document_root": settings.STATIC_ROOT}),

	    url(r'^$', views.home)
	]
	





