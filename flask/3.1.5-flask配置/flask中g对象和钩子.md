

# flask使用操作指南之应用上下文和钩子函数的使用

>Auth: 王海飞
>
>Data：2018-09-15
>
>Email：779598160@qq.com
>
>github：https://github.com/coco369/knowledge 

### 前言

&nbsp;&nbsp;&nbsp;&nbsp;在Web开发中经常会对所有的请求做一些相同的操作，如果将相同的代码写入每一个视图函数中，那么程序就会变得非常臃肿。为了避免在每个视图函数中定义相同的代码，可以使用钩子函数。如下有三个常见的钩子:

1. before_request: 被装饰的函数会在每个请求被处理之前调用。

2. after_request: 被装饰的函数会在每个请求退出时才被调用。在程序没有抛出异常的情况下，才会被执行。

3. teardown_request: 被装饰的函数会在每个请求退出时才被调用。不论程序是否抛出异常，都会执行。

<b style="color:red;">注意:
 
	1. 这个异常是指代码本身错误（代码中出现10/0）不执行，如果abort抛出异常了，after_request还是会执行。
	2. 必须配置app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False。该配置表示无论如何都将执行teardown_request装饰的方法。
</b>

#### 1. 钩子函数执行顺序

	@blue.before_request
	def before_request():
	    print('before_request')
	
	
	@blue.after_request
	def after_request(response):
	    print('after_request')
	    return response
	
	
	@blue.teardown_request
	def teardown_request(exception):
	    print('teardown_request')
	
	@blue.route('index/')
	def index_requst():
	    return 'index_requst'

分析:访问http://127.0.0.1:8080/app/index/后，在控制台可以看到如下输出:

before_request

after_request

teardown_request

从控制台的输出中可以看出各函数的执行顺序，被before_request装饰的函数会在请求处理之前被调用。而after_request和teardown_request会在请求处理完后才被调用。区别就在于after_request只会在请求正常退出的情况下才会被调用，并且atfer_request函数必须接受一个响应对象，并返回一个响应对象。而teardown_request函数在任何情况下都会被调用，并且必须传入一个参数来接收异常对象。


#### 2. 应用上下文G对象

&nbsp;&nbsp;&nbsp;&nbsp;应用全局对象（g）是Flask为每一个请求自动建立的一个对象。g的作用范围只是在一个请求（也就是一个线程）里，它不能在多个请求中共享数据，故此应用全局变量（g）确保了线程安全。


##### 案例: 连接pymysql，并实现表的创建和数据的插入

	@blue.before_request
	def get_mysql_connect():
	    # 建立mysql数据库的连接
	    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='f_db')
	    cursor = conn.cursor()
	    # 设置当前请求上下文中的应用全局对象
	    g.conn = conn
	    g.cursor = cursor
	
	
	@blue.before_request
	def create_student_table():
	    # 创建student表
	    sql = 'drop table if exists student;'
	    sql1 = 'create table student(id int auto_increment, s_name varchar(10) not null, s_age int not null, primary key(id)) engine=InnoDB default charset=utf8;'
	    # 执行删除表，如果student表存在则删除
	    g.cursor.execute(sql)
	    # 执行创建student表
	    g.cursor.execute(sql1)
	
	
	@blue.route('excute_sql/')
	def excute_sql():
	    # 定义插入sql语句
	    sql = 'insert into student (name, age) values ("%s", "%s")' % ('xiaoming', '18')
	    # 执行插入语句
	    g.cursor.execute(sql)
	    # 提交事务
	    g.conn.commit()
	    return '创建数据'
	
	
	@blue.teardown_request
	def close_mysql_connect(exception):
	    # 关闭mysql数据库的连接
	    g.conn.close()
	
