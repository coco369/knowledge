
# python连接Mysql数据库

>Auth: 王海飞
>Data：2018-04-17
>Email：779598160@qq.com
>github：https://github.com/coco369/knowledge

#### 设计背景
    使用python连接数据库，使用py脚本形式去更新表的数据，实现CRUD操作
#### 事务
事务机制具备四点：原子性，一致性，隔离性，持久性，简称ACID特性

```
原子性（atomicity）：一个事务是不可分割的一个整体，执行操作的话，要做就要一起做，不做的话就都不做
一致性（consistency）：数据库的状态从一个状态变到另外一个状态
隔离性（isolation）：一个事务在执行的时候不能被其他的事务干扰。即各各事务之间的操作是互不干扰的
持久性（durability）：一个事务一旦提交以后，对数据库的变化就是永久性的
```
注解 理解原子性和一致性， 举个例子：
转账：张三给李四转账100元。那数据库假设需要 张三扣100，李四加100，记录一条流水。
如果流水没记录成功，那整体回滚，张三也没转账成功，李四也没多钱。这就是原子性的体现。

而张三必须扣100，李四必须加100，这个就是一致性了，如果因为某些逻辑原因，导致张三扣了100，流水记录100转账，而李四只加了60。然后这3条操作都成功了，那原子性就符合了，但是一致性就不符合了


#### 连接数据库

##### py2.x版本中连接数据库

    确保已经安装PyMySQL库

##### py3.x版本中连接数据库

###### 安装PyMySQL
```
pip install PyMySQL
```

###### 前提条件
1. 确保已经创建了数据库TEST
2. 确保已经在数据库TEST中已经创建了表STUDENT
3. 确保连接数据库的密码和数据库名称，以及端口和数据库的IP地址
4. 确认以及安装了PyMySQL模块了

###### 测试例子

1. 简单的访问，查询一条数据
```
    # -*- encoding:utf-8 -*-
    import pymysql

    # 打开数据库连接（connect, Connect, Connection）
    #db = pymysql.connect("localhost IP地址","root账号","password密码","TEST数据库", 3306 端口)
    db = pymysql.Connect(host='localhost', port=3306, user='root', passwd='123456', db='srs', charset='utf8')
    
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询 
    cursor.execute("SELECT VERSION()")

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()

    print ("Database version : %s " % data)

    # 关闭数据库连接
    db.close()

```
注意其中获取数据的方法有如下几种：
fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
fetchall(): 接收全部的返回结果行.

2. 获取访问数据库，并且插入数据

```
import pymysql
 
# 打开数据库连接
db = pymysql.connect("localhost","testuser","test123","TESTDB" )
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
 
# SQL 插入语句
sql = """INSERT INTO STUDENT(s_name, s_tel)
         VALUES (%s, %s)""" % ('张三', '15664322132')
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚
   db.rollback()
 
# 关闭数据库连接
db.close()
```
注意,其中在执行插入，以及修改，删除语句的时候需要使用commit提交到数据库

3. 事务
提交：
    commit()方法游标的所有更新操作，
回滚：
    rollback（）方法回滚当前游标的所有操作
