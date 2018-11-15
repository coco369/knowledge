

# flask使用操作指南之模型1

>Auth: 王海飞
>
>Data：2018-05-15
>
>Email：779598160@qq.com
>
>github：https://github.com/coco369/knowledge 


### 1. Flask模型

Flask默认并没有提供任何数据库操作的API

我们可以选择任何适合自己项目的数据库来使用

Flask中可以自己的选择数据，用原生语句实现功能，也可以选择ORM（SQLAlchemy，MongoEngine）

SQLAlchemy是一个很强大的关系型数据库框架，支持多种数据库后台。SQLAlchemy提供了高层ORM，也提供了使用数据库原生SQL的低层功能。

ORM：

	将对对象的操作转换为原生SQL
	优点
		易用性，可以有效减少重复SQL
		性能损耗少
		设计灵活，可以轻松实现复杂查询
		移植性好

针对于Flask的支持，[官网地址](http://flask-sqlalchemy.pocoo.org/2.3/)

	pip install flask-sqlalchemy
	
安装驱动

	pip install pymysql

### 2. 定义模型

使用SQLALchemy的对象去创建字段

其中__tablename__指定创建的数据库的名称

	创建models.py文件，其中定义模型

	from flask_sqlalchemy import SQLAlchemy
	
	db = SQLAlchemy()
	
	
	class Student(db.Model):
	
	    s_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	    s_name = db.Column(db.String(16), unique=True)
	    s_age = db.Column(db.Integer, default=1)
	
	    __tablename__ = "student"

其中：

Integer表示创建的s_id字段的类型为整形，

primary_key表示是否为主键

String表示该字段为字符串

unique表示该字段唯一

default表示默认值

autoincrement表示是否自增


### 3. 创建数据表

在视图函数中我们引入models.py中定义的db

	from App.models import db
	
	@blue.route("/createdb/")
	def create_db():
	    db.create_all()
	    return "创建成功"
	
	@blue.route('/dropdb/')
	def drop_db():
	    db.drop_all()
	    return '删除成功'


其中： db.create_all()表示创建定义模型中对应到数据库中的表

db.drop_all()表示删除数据库中的所有的表



### 4. 初始化SQLALchemy

在定义的__init__.py文件中使用SQLALchemy去整合一个或多个Flask的应用

有两种方式：

	第一种：

	from flask_sqlalchemy import SQLALchemy
	
	app = Flask(__name__)
	db = SQLAlchemy(app)

	第二种：

	from App.models import db
	
    def create_app():
        app = Flask(__name__)
        db.init_app(app)
        return app


### 5. 配置数据库的访问地址

[官网配置参数](http://www.pythondoc.com/flask-sqlalchemy/config.html)

数据库连接的格式：

	dialect+driver://username:password@host:port/database

	dialect数据库实现
	
	driver数据库的驱动

例子：
访问mysql数据库，驱动为pymysql，用户为root，密码为123456，数据库的地址为本地，端口为3306，数据库名称HelloFlask

设置如下： "mysql+pymysql://root:123456@localhost:3306/HelloFlask"

在初始化__init__.py文件中如下配置：

	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/HelloFlask"

### 6. 对学生数据进行CRUD操作

语法：

	类名.query.xxx

获取查询集：

	all()
	
	filter(类名.属性名==xxx)

	filter_by(属性名=xxx)

数据操作：

	在事务中处理，数据插入

	db.session.add(object)

	db.session.add_all(list[object])
	
	db.session.delete(object)

	db.session.commit()
	
	修改和删除基于查询



#### 6.1 想学生表中添加数据

	@blue.route('/createstu/')
	def create_stu():
	
	    s = Student()
	    s.s_name = '小花%d' % random.randrange(100)
	    s.s_age = '%d' % random.randrange(30)
	
	    db.session.add(s)
	    db.session.commit()
	
	    return '添加成功'

提交事务，使用commit提交我们的添加数据的操作

#### 6.2 获取所有学生信息

将学生的全部信息获取到，并且返回给页面，在页面中使用for循环去解析即可

	@blue.route("/getstudents/")
	def get_students():
	    students = Student.query.all()
	    return render_template("StudentList.html", students=students)

#### 6.3 获取s_id=1的学生的信息

写法1：

	students = Student.query.filter(Student.s_id==1)

写法2：

	students = Student.query.filter_by(s_id=2)

注意：filter中可以接多个过滤条件

写法3：
	
	sql = 'select * from student where s_id=1'
    students = db.session.execute(sql)

#### 6.4 修改学生的信息

写法1：

    students = Student.query.filter_by(s_id=3).first()
    students.s_name = '哈哈'
    db.session.commit()

写法2：

	Student.query.filter_by(s_id=3).update({'s_name':'娃哈哈'})
 
    db.session.commit()

#### 6.5 删除一个学生的信息

写法1：

    students = Student.query.filter_by(s_id=2).first()
    db.session.delete(students)
    db.session.commit()

写法2：

    students = Student.query.filter_by(s_id=1).all()
    db.session.delete(students[0])
    db.session.commit()

注意：filter_by后的结果是一个list的结果集

<b>重点注意：在增删改中如果不commit的话，数据库中的数据并不会更新，只会修改本地缓存中的数据，所以一定需要db.session.commit()</b>
