
# tornado使用操作指南--模型

>Auth: 王海飞
>
>Data：2019-03-11
>
>Email：779598160@qq.com
>
>github：https://github.com/coco369/knowledge 

### 前言

在Web开发中，数据的存储与读取都离不开数据库的支持，本章中将使用MySQL作为数据库，并使用pymysql驱动来连接Mysql。当然还有很多数据库可以用于Web开发的数据存储，比如Redis，MongoDB。且开发中常用ORM（Object Relational Mapping）对象关系映射将数据库中表和面向对象语言中的模型类建议一种对应关系，至此实现操作模型以达到操作数据库中表信息的目的。

[代码地址](数据库)

### 1. 数据库配置

SQLALchemy为最成熟最常用的ORM工具之一，因此使用SQLALchemy框架。

#### 1.1	安装

安装SQLALchemy和pymysql。

	pip install sqlalchemy
	pip install pymysql

#### 1.2	连接格式

    使用SQLALchemy连接不同的数据库需要配置不同的格式，连接不同数据库的格式可以从官网上查询

连接语法格式为: 

	dialect+driver://username:password@host:port/database
	其中:
	dialect为数据库类型
	driver为数据库驱动名称
	username为账号
	password为密码
	host为主机IP地址
	port为端口
	database为MySQL中数据库名称

### 2. 使用
#### 2.1 数据库连接配置

	from sqlalchemy import create_engine

	# 数据库连接
	db_url = 'mysql+pymysql://root:123456@127.0.0.1:3306/tornado_db'

	# 创建引擎
	engine = create_engine(db_url)

    示例中定义连接本地3306端口的MySQL中的tornado_db数据库，并通过create_engine()方法创建引擎，用以初始化数据库连接。

#### 2.2 数据库模型定义与映射

    模型的创建是对现实世界中实物的抽象化，如以下示例将创建学生对象的抽象化模型，并定义学生模型中具备的三个字段: 自增主键id字段、唯一姓名s_name字段、默认为19的年龄字段。

学生模型定义:

	from sqlalchemy.ext.declarative import declarative_base
	from sqlalchemy import Column, Integer, String

	# 创建对象的基类，用以维持模型类和数据库表中的对应关系
	Base = declarative_base()
	
	class Students(Base):
	    id = Column(Integer, primary_key=True, autoincrement=True)
	    s_name = Column(String(10), unique=False, nullable=False)
	    s_age = Column(Integer, default=19)
	
	    __tablename__ = 'students'

注意: 模型类的定义必须继承基类Base。模型中__tablename__参数如果不定义则表示将模型映射到数据库中时，表名称为模型名Students的小写，即表名为students。

Student模型定义后将模型映射到数据库tornado_db中可以定义如下示例的方法:

#### 2.3 创建、删除数据表

	# 创建数据表
	Base.metadata.create_all()
	
	# 删除数据表
	Base.metadata.drop_all()

注意: Base.metadata.create_all()方法将找到所有Base的子类，并在数据库中创建这些子类对应的表。而drop_all()表示删除这些表。

### 3. ORM编程

使用SQLALchemy的ORM进行数据表中数据的增删改查操作，需创建数据库会话对象。

#### 3.1 创建会话对象

	from sqlalchemy.orm import sessionmaker
	
	#创建和数据库连接会话
	DbSession = sessionmaker(bind=engine)
	#创建会话对象
	session = DbSession()

注意: 获取到会话对象session后，可以通过会话对象实现对数据库中数据的增删改查操作。

#### 3.2 增数据

语法格式:

	会话对象session.add(对象): 添加新增的对象
	会话对象session.add_all(对象列表): 批量添加新增的对象

<b>创建学生信息:</b>
	
	# 第一种方式创建
	stu = Students()
	stu.s_name = u'小四'
	session.add(stu)
	session.commit()

	# 第二种方式: 批量添加
	stu_list = []
	for i in range(5):
	    stu = Students()
	    stu.s_name = '小明_%s' % i
	    stu_list.append(stu)
	session.add_all(stu_list)
	session.commit()

#### 3.3 查数据
    
语法格式: 

	all(): 查询所有数据
	filter(): 过滤出符合条件的数据，可以多个filter()方法一起调用
	filter_by(): 过滤出符合条件的数据，可以多个filter_by()方法一起调用
	get(): 获取指定主键的行数据

<b>查询所有学生信息:</b>

	# 获取所有的学生对象
	stu = session.query(Students).all()
	
	# 获取名字为小明的学生对象
	stu = session.query(Students).filter(Students.s_name == '小明').first()
	stu = session.query(Students).filter_by(s_name='小明').first()


示例中通过all()方法、filter()、first()方法进行结果的筛选获取,分析如下:
1）获取满足条件的数据，可以使用filter()和filter_by()，其接收的参数略微有所不同。filter()中接收的参数为: ’模型名.查询的字段’，而filter_by()中接收的参数为: 查询的字段。
2）获取所有的学生信息，可以使用all()方法，返回结果为列表。

#### 3.4 删数据

语法格式:

	delete(): 删除对象

<b>删除学生对象：</b>

	# 第一种方式
	stu = session.query(Students).filter(Students.s_name == '小明').first()
	session.delete(stu)
	session.commit()
	
	# 第二种方式
	session.query(Students).filter_by(s_name='小明').delete()
	session.commit()

#### 3.5 修改数据

语法格式:

	update(): 更新数据，更新字段参数以键值对的形式。如update({key1:value1, key2:value2})

<b>修改学生信息：</b>

	# 第一种方式
	stu = session.query(Students).filter(s_name='小明').first()
	stu.s_name = '小李'
	session.add(stu)
	session.commit()
	
	# 第二种方式
	session.query(Students).filter(s_name='小明').update({'s_name': '小李'})
	session.commit()

注意: 以上案例代码中通过数据库会话对象session实现数据的增删改查。在增删改操作中通过修改学生对象，并调用commit()方法实现数据的持久化操作，将会话中的数据提交给数据库进行持久化保存。

