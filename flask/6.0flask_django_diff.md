
### Django和Flask区别：

#### 1. jiaji2和DjangoTemplates模板引擎相比，jiaja2语法更简单

	比如： loop.index 和 forloop.counter
		   loop.revindex 和 forloop.revcounter
	jiaja2中没有ifequal

#### 2. 耦合
	Django: 大而全，但是耦合性高。Auth，Permission，admin基本没用
			开发快，符合MVC模式

	Flask： 微框架，很小巧。需要哪些功能，自己装。
			需要熟悉MVC模式

### 3. 模型

#### 3.1 模型定义

	1. 模型中不定义数据库的表名：
		在django中默认表名为：'应用app名_模型名小写'
		在flask中默认的表名为：'模型名小写'

	2. 自增id字段：
		在django中默认会创建自增的主键id
		在flask中需要自己写自增的主键id：
			id = db.Column(db.Integer, primary_key=True, autoincrement=True)

	3. 查询所有数据的结果，all()方法
		在django中查询的结果为QuerySet
		在Flask中查询结果为List

	4. 查询满足条件的数据的结果，filter(), filter_by()方法
		在django中查询的结果为QuerySet
		在Flask中查询结果为BaseQuery objects

#### 3.2 模型数据查询

Django：

	一对多：

	  模型1： u 字段为 FOREIGN_KEY，关联到模型2
	  	模型1.u = u对象
	  	模型1.u_id = u对象.id


	  模型1查找模型2的数据
	  	模型2对象=模型1对象.u
	  	模型1对象=模型2对象.模型1_set.all()

	一对一：

	  模型1查找模型2的数据
	  	模型2对象=模型1对象.u
	  	模型1对象=模型2对象.模型1.all()


 Flask：

	一对多：

	 	模型1： u字段为FOREIGN KEY，关联到模型2
	 	模型2: yy字段，定义relationship字段， backref=‘uu’

	 	模型1查找模型2：
	 		模型2对象 = 模型1对象.uu
	 		模型1对象 = 模型2对象.yy