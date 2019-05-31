

# flask使用操作指南之插件

>Auth: 王海飞
>
>Data：2018-05-17
>
>Email：779598160@qq.com
>
>github：https://github.com/coco369/knowledge 


### 1. 开发，页面调试工具debugtoolbar

#### 1.1 安装

	pip install flask-debugtoolbar

#### 1.2 配置

	from flask import Flask

	from flask_debugtoolbar import DebugToolbarExtension
	
	app = Flask(__name__)
	
	app.debug = True
	
	app.config['SECRET_KEY'] = '<replace with a secret key>'
	
	toolbar = DebugToolbarExtension(app)

### 2. restful

Flask-RESTful 提供的最主要的基础就是资源(resources)。资源(Resources)是构建在 Flask 可拔插视图 之上，只要在你的资源(resource)上定义方法就能够容易地访问多个 HTTP 方法

[官网](http://www.pythondoc.com/Flask-RESTful/quickstart.html)上描述了一个最简单的restful风格的api，如下：

	from flask import Flask
	from flask.ext import restful
	
	app = Flask(__name__)
	api = restful.Api(app)
	
	class HelloWorld(restful.Resource):
	    def get(self):
	        return {'hello': 'world'}
	
	api.add_resource(HelloWorld, '/')
	
	if __name__ == '__main__':
	    app.run(debug=True)	


#### 2.1 安装

	pip install flask_restful

#### 2.2 配置

在create_app()获取Flask(__name__)对象中，设置如下配置

	from flask_restful import Api
	
	api = Api()
	
	api.init_app(app=app)

在views中需要引入配置的api还有Resource
	
	# 导入包和restful中的Api对象
	from flask_restful import Resource
	from utils.functions import api

	# 定义类，启动包含了对数据处理的GET,POST,PATCH,PUT,DELETE请求
	class CreateCourse(Resource):

    def get(self, id):
        course = Course.query.get(id)
        return course.to_dict()

    def post(self):

        courses = ['大学英语', '大学物理', '线性代数', '高数',
                   'VHDL', 'ARM', '马克思主义', '农场劳动']
        course_list = []
        for course in courses:
            c = Course()
            c.c_name = course
            course_list.append(c)
        db.session.add_all(course_list)
        db.session.commit()

        courses = Course.query.all()
        return [course.to_dict() for course in courses]

    def patch(self, id):
        c_name = request.form.get('c_name')
        course = Course.query.get(id)
        course.c_name = c_name
        db.session.commit()
        return {'code': 200, 'data': course.to_dict(), 'msg': '请求成功'}

    def delete(self, id):
        course = Course.query.get(id)
        db.session.delete(course)
        db.session.commit()
        return {'code': 200, 'msg': '删除成功'}


	# 绑定处理url
	api.add_resource(CreateCourse, '/api/course/<int:id>/', '/api/course/')

#### 2.3 端点(Endpoints)

在一个 API 中，你的资源可以通过多个 URLs 访问。你可以把多个 URLs 传给 Api 对象的 Api.add_resource() 方法。每一个 URL 都能访问到你的 Resource

如：

	api.add_resource(CreateCourse, '/api/course/<int:id>/', '/api/course/')

#### 2.4 返回响应

Flask-RESTful 支持视图方法多种类型的返回值。同 Flask 一样，你可以返回任一迭代器，它将会被转换成一个包含原始 Flask 响应对象的响应。Flask-RESTful 也支持使用多个返回值来设置响应代码和响应头

如：

    def get(self, id):
        course = Course.query.get(id)
        return course.to_dict(), 200