

# flask使用操作指南之登录注册

>Auth: 王海飞
>
>Data：2018-10-08
>
>Email：779598160@qq.com
>
>github：https://github.com/coco369/knowledge 

### 前言

在flask中如何快速的实现登录注册注销功能，以及登录状态验证等功能? flask的扩展库中有Flask-Login库就可快速的实现以上的功能，实现起来是非常的便利。

### 1. 安装Flask-Login

	pip install flask-login

### 2. 实现登录功能

#### 2.1 定义login.html模板


	{% extends 'base.html' %}
	
	{% block title %}
	    登录页面
	{% endblock %}
	
	{% block content %}
	    <form action="" method="post">
	        姓名:<input type="text" name="username">
	        密码:<input type="text" name="password">
	        <input type="submit" value="提交">
	    </form>
	{% endblock %}

#### 2.2 实现登录功能

登录方法中定义被login_manager.user_loader装饰的回调函数，回调函数在如下两个地方被调用:

1）该函数表明当前用户登录成功时调用login_user()方法时，会被回调的函数。回调函数实现的功能是向会话上下文session中存储最为中间的键值对，key为user_id， value为当前登录用户的ID值。

2）回调函数在访问任何一个路由地址时也会被调用。

注意: 因为请求上下文在每次建立连接时，都需要获取当前登录用户并将当前登录用户设置为全局上下文current_user，因此回调函数返回的是当前登录系统的用户对象。

	from flask_login import LoginManager, login_required, login_user, logout_user，current_user
	
	# 获取登录管理对象
	login_manager = LoginManager()	

	@login_manager.user_loader
	def load_user(user_id):
	    # 必须编写一个函数用于从数据库加载用户。
	    # 这个函数在login_user(user)存储当前登录用户到session中时，会被调用
	    # 在每次访问地址的时候都被被调用，用于向请求上下文中绑定当前登录的用户信息
	    return User.query.get(user_id)


	@blue.route('/login/', methods=['GET', 'POST'])
	def login():
	    if request.method == 'GET':
	        return render_template('login.html')
	
	    if request.method == 'POST':
	        username = request.form.get('username')
	        password = request.form.get('password')
	        # 校验用户名和密码是否填写完成
	        if not all([username, password]):
	            return render_template('login.html')
	        # 通过用户名获取用户对象
	        user = User.query.filter_by(username=username).first()
	        # 校验密码是否正确
	        if check_password_hash(user.password, password):
	            # 实现登录
	            # login_user()能够将已登录并通过load_user()的用户对应的User对象保存在session中
	            # 在session中会创建一个键值对，key为user_id，value为当前登录用户的id值
	            # 如果希望应用记住用户的登录状态, 只需要为 login_user()的形参 remember 传入 True 实参就可以了.
	            login_user(user)
	            return redirect(url_for('user.index'))
	        else:
	            flash('用户名或者密码错误')
	
	        return redirect(url_for('user.index'))

#### 2.3 启动文件进行配置

session_protection: 设置存储用户登录状态的安全级别

login_view: 设置登录验证失败的跳转地址

	from user.views import login_manager

	app.config['SECRET_KEY'] = os.urandom(24)

	# 登录管理，初始化app
	# 可以设置None,'basic','strong'以提供不同的安全等级,一般设置strong,如果发现异常会登出用户
	# session_protection 能够更好的防止恶意用户篡改 cookies, 当发现 cookies 被篡改时, 该用户的 session 对象会被立即删除, 导致强制重新登录。
	login_manager.session_protection='strong'

	# 当登录认证不通过，则跳转到该地址
	login_manager.login_view='user.login'
	login_manager.init_app(app)

 
#### 2.4 访问首页，登录校验

使用装饰器login_required()进行登录校验。

核心思想: 校验session中是否存在key为user_id的键值对。如果校验成功，则继续访问被装饰的函数。如果校验失败，则跳转到启动文件中定义的login_manager.login_view定义的视图函数。

	@blue.route('/index/')
	@login_required
	def index():
	    return render_template('index.html')


如果登录校验成功，则渲染index.html首页，在页面中可以解析全局变量current_user参数。

	{% extends 'base.html' %}
	
	{% block title %}
	    首页页面
	{% endblock %}
	
	{% block content %}
	    <p>我是首页</p>
	    <p>当前登录系统用户为: {{ current_user.username }}</p>
	{% endblock %}

#### 2.5 注销

使用logout_user()方法实现注销，核心功能就是删除当前会话上下文session中的user_id键值对。

	# 退出
	@blue.route('/logout/', methods=['GET'])
	@login_required
	def logout():
	    logout_user()
	    return redirect(url_for('user.login'))