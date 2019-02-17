
# flask使用操作指南2

>Auth: 王海飞
>
>Data：2018-05-14
>
>Email：779598160@qq.com
>
>github：https://github.com/coco369/knowledge 


### 1. 什么是蓝图

在Flask项目中可以用Blueprint(蓝图)实现模块化的应用，使用蓝图可以让应用层次更清晰，开发者更容易去维护和开发项目。蓝图将作用于相同的URL前缀的请求地址，将具有相同前缀的请求都放在一个模块中，这样查找问题，一看路由就很快的可以找到对应的视图，并解决问题了。

### 2. 使用蓝图

#### 2.1 安装

	pip install flask_blueprint

#### 2.2 实例化蓝图应用

	blue = Blueprint(‘first’，\_\_name\_\_)

注意：Blueprint中传入了两个参数，第一个是蓝图的名称，第二个是蓝图所在的包或模块，\_\_name\_\_代表当前模块名或者包名

#### 2.3 注册

	app = Flask(\_\_name\_\_)

	app.register_blueprint(blue, url_prefix='/user')

注意：第一个参数即我们定义初始化定义的蓝图对象，第二个参数url_prefix表示该蓝图下，所有的url请求必须以/user开始。这样对一个模块的url可以很好的进行统一管理

#### 3 使用蓝图

修改视图上的装饰器，修改为@blue.router(‘/’)

	@blue.route('/', methods=['GET', 'POST'])
	def hello():
	    # 视图函数
	    return 'Hello World'

注意：该方法对应的url为127.0.0.1:5000/user/



#### 4 url_for反向解析

##### 后端中使用反向解析:

语法:
	
	无参情况: url_for('蓝图中定义的第一个参数.函数名')
	有参情况: url_for('蓝图中定义的第一个参数.函数名', 参数名=value)
	
定义跳转：

	from flask import url_for, redirect
	# 第一步: 生成蓝图对象
	blueprint = Blueprint('first', __name__)
	
	
	@blueprint.route('/')
	def hello():
	    return 'hello'
	
	
	@blueprint.route('/stu/<id>/')
	def stu(id):
	    return 'hello stu: %s' % id
	
	
	# 1. 定义路由跳转到hello方法
	@blueprint.route('/redirect/')
	def my_redirect():
		# 第一种方法
	    # redirect: 跳转
	    # url_for: 反向解析
	    # 'first.hello': 蓝图第一个参数.跳转到的函数名
	    return redirect(url_for('first.hello'))
		# 第二种方法
	    return redirect('/hello/index/')
		
	# 2. 定义路由跳转到stu方法
	@blueprint.route('/redirect_id/')
	def stu_redirect():
	    return redirect(url_for('first.stu', id=3))

注意: 反向解析可以使用url_for方法，也可以直接定义跳转的路由地址。
	
		

##### 前端中使用反向解析

语法:

	无参形式: {{ url_for('蓝图中定义的第一个参数.函数名') }}

	有参形式: {{ url_for('蓝图中定义的第一个参数.函数名'，参数名=value) }}
