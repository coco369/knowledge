

# flask使用操作指南之模型3

>Auth: 王海飞
>
>Data：2018-05-17
>
>Email：779598160@qq.com
>
>github：https://github.com/coco369/knowledge 

### 1. 关联关系---多对多

定义模型：
	

引入SLALchemy
	
	from flask_sqlalchemy import SQLAlchemy
	
	db = SQLAlchemy()


创建中间表

	
	sc = db.Table('sc',
	    db.Column('s_id', db.Integer, db.ForeignKey('student.s_id'), primary_key=True),
	    db.Column('c_id', db.Integer, db.ForeignKey('courses.c_id'), primary_key=True)
	)

创建学生类Student

	class Student(db.Model):
	
	    s_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	    s_name = db.Column(db.String(20), unique=True)
	    s_age = db.Column(db.Integer, default=18)
	    s_g = db.Column(db.Integer, db.ForeignKey('grade.g_id'), nullable=True)
	
	    __tablename__ = 'student'
	
	    def __init__(self, name, age):
	
	        self.s_name = name
	        self.s_age = age
	        self.s_g = None
	

创建课程表的模型，Course类
	
	class Course(db.Model):
	
	    c_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	    c_name = db.Column(db.String(20), unique=True)
	    students = db.relationship('Student',
	                               secondary=sc,
	                               backref='cou')
	
	    __tablename__ = 'courses'
	
	    def __init__(self, name):
	
	        self.c_name = name


sc表由<font style="color:red;">**db.Table声明**</font>，我们不需要关心这张表，因为这张表将会由SQLAlchemy接管，它唯一的作用是作为students表和courses表关联表，所以必须在db.relationship()中指出<font style="color:red;">**sencondary关联表参数**</font>。lazy是指查询时的惰性求值的方式，这里有详细的参数说明，而db.backref是声明反向身份代理，其中的lazy参数是指明反向查询的惰性求值方式.

### 2. 添加学生和课程之间的关系

通过页面中传递学生的id和课程的id，分别获取学生的对象和课程的对象，在使用关联关系append去添加学生对象，并且add以后再commit后，就可以在中间表sc中查看到新增的关联关系了。

		userid = request.form.get('userid')
        courseid = request.form.get('courseid')

        stu = Student.query.get(userid)
        cou = Course.query.get(courseid)

        cou.students.append(stu)
        db.session.add(cou)
        db.session.commit()

### 3. 删除学生和课程之间的关系

通过页面获取传递的学生的id和课程的id，分别获取学生对象和课程对象，在使用关联关系remove去删除学生对象，并commit将事务提交到数据库中	
	
	stu = Student.query.get(s_id)
    cou = Course.query.get(c_id)

    cou.students.remove(stu)
    db.session.commit()

### 4. 通过课程查询学生的信息

以下定义在课程course的模型中，所以通过课程查询学生的信息，<font style="color:red;">语法为课程的对象.studengs</font>。如果知道学生的信息反过来找课程的信息，则使用backref的反向关联去查询，<font style="color:red;">语语法为学生的对象.cou(反向)</font>

students = db.relationship('Student',secondary=sc,backref='cou')

    cou = Course.query.get(2)
    stus = cou.students

### 5. 通过学生去查询课程的信息


    stu = Student.query.get(id)
    cous = stu.cou
