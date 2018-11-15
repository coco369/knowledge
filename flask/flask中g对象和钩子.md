

# flask使用操作指南之应用上下文和钩子函数的使用

>Auth: 王海飞
>
>Data：2018-09-15
>
>Email：779598160@qq.com
>
>github：https://github.com/coco369/knowledge 

### 前言


	@blue.before_request
	def before_request1():
	    print('before_request')
	    # 如果有返回，则不再执行其余的before_request钩子函数
	    return 'hello'
	
	@blue.before_request
	def before_request2():
	    print('before_request_2')
	
	
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
	
	数据库的连接，使用请求钩子
	from flask import g
	import pymysql
	
	
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
	
