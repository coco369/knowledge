
# mongodb使用指南

>Auth: 王海飞
>
>Data：2018-06-16
>
>Email：779598160@qq.com
>
>github：https://github.com/coco369/knowledge 


### 语法

#### 1. 数据库的创建，删除，切换

	> // 显示所有数据库
	> show dbs
	admin   0.000GB
	config  0.000GB
	local   0.000GB
	> // 创建并切换到spider数据库
	> use spider
	switched to db spider
	> // 删除当前数据库
	> db.dropDatabase()
	{ "ok" : 1 }


注意：如果第一次use spider会创建spider数据库的，但是立马show dbs的时候，并不会展示出当前刚创建的spider的数据库，需要在该数据库下创建了文档才能show dbs看到spider数据库的。这点需要注意一下。

#### 2. 集合的创建、删除、查看

	> // 创建并切换到school数据库
	> use school
	switched to db school

	> // 创建colleges集合
	> db.createCollection('colleges')
	{ "ok" : 1 }

	> // 创建students集合
	> db.createCollection('students')
	{ "ok" : 1 }

	> // 查看所有集合
	> show collections
	colleges
	students

	> // 删除colleges集合
	> db.colleges.drop()
	true
	> 

#### 3. 对文档的CRUD操作

	> // 向students集合插入文档
	> db.students.insert({s_id: 1, name: '王大帅', age: 18})
	WriteResult({ "nInserted" : 1 })

	> // 向students集合插入文档
	> db.students.save({s_id: 2, name: '王帅帅', tel: '12334566789', gender: '男'})
	WriteResult({ "nInserted" : 1 })

	> // 查看所有文档
	> db.students.find()
	{ "_id" : ObjectId("5b24b01f165a0f78dbf82a12"), "s_id" : 2, "name" : "王帅帅", "tel" : "12334566789", "gender" : "男" }
	{ "_id" : ObjectId("5b24b0dc165a0f78dbf82a15"), "s_id" : 1, "name" : "王大帅", "age" : 18 }

	> // 更新s_id为1的文档
	> db.students.update({'s_id':1}, {'$set':{'age':16}})
	WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })


	> // 插入或更新s_id为3的文档
	> db.students.update({s_id: 3}, {'$set': {name: '小妲己', tel: '13022221333', gender: '女'}},  upsert=true)
	WriteResult({
	        "nMatched" : 0,
	        "nUpserted" : 1,
	        "nModified" : 0,
	        "_id" : ObjectId("5b24b30d4717832ad090f2f5")
	})

	> // 查询所有文档
	> db.students.find().pretty()
	{
		"_id" : ObjectId("5b24b01f165a0f78dbf82a12"),
		"s_id" : 2,
		"name" : "王帅帅",
		"tel" : "12334566789",
		"gender" : "男"
	}
	{
		"_id" : ObjectId("5b24b0ba165a0f78dbf82a14"),
		"s_id" : 2,
		"name" : "王帅帅",
		"tel" : "12334566789",
		"gender" : "男"
	}
	{
		"_id" : ObjectId("5b24b0dc165a0f78dbf82a15"),
		"s_id" : 1,
		"name" : "王大帅",
		"tel" : "12334566786",
		"age" : 16
	}
	{
		"_id" : ObjectId("5b24b30d4717832ad090f2f5"),
		"s_id" : 3,
		"gender" : "女",
		"name" : "小妲己",
		"tel" : "13022221333"
	}
	

讲解:我们可以使用 find() 方法来查询指定字段的数据，将要返回的字段对应值设置为 1。但是除了 _id 你不能在一个对象中同时指定 0 和 1。否则同时制定0和1的话，会报错误的。
	
	>> // 查询s_id大于2的文档只显示name和tel字段
	> db.students.find({s_id: {'$gt': 2}}, {_id: 0, name: 1, tel: 1}).pretty()

	>> // 查询s_id大于2的文档除了不显示name和tel字段的其他字段
	> db.students.find({s_id:{'$gt':2}}, {s_id:0, name:0, _id:0})
	{ "gender" : "女", "tel" : "13022221333" }

	>> // 查询s_id大于2的文档只显示_id和name和tel字段
	> db.students.find({s_id:{'$gt':2}}, {s_id:1, name:1, _id:1})
	{ "_id" : ObjectId("5b24b30d4717832ad090f2f5"), "s_id" : 3, "name" : "小妲己" }

筛选查询：

	>>// 查询学生文档跳过第1条文档只查1条文档
	> db.students.find().skip(1).limit(1).pretty()
	{
		"_id" : ObjectId("5b24b0ba165a0f78dbf82a14"),
		"s_id" : 2,
		"name" : "王帅帅",
		"tel" : "12334566789",
		"gender" : "男"
	}


	> // 对查询结果进行排序(1表示升序，-1表示降序)
	> db.students.find().sort({s_id: -1})
	{ "_id" : ObjectId("5b24b30d4717832ad090f2f5"), "s_id" : 3, "gender" : "女", "name" : "小妲己", "tel" : "13022221333" }
	{ "_id" : ObjectId("5b24b01f165a0f78dbf82a12"), "s_id" : 2, "name" : "王帅帅", "tel" : "12334566789", "gender" : "男" }
	{ "_id" : ObjectId("5b24b0ba165a0f78dbf82a14"), "s_id" : 2, "name" : "王帅帅", "tel" : "12334566789", "gender" : "男" }
	{ "_id" : ObjectId("5b24b0dc165a0f78dbf82a15"), "s_id" : 1, "name" : "王大帅", "tel" : "12334566786", "age" : 16 }
