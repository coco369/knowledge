
import tornado.web

from app.models import init_db, Students

from utils.connect import session


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('index')


class CreateDBHandler(tornado.web.RequestHandler):

    def get(self):
        # 找到Base的所有子类，并在数据库中创建这些表
        init_db()
        self.write('创建数据库成功')


class TempHandler(tornado.web.RequestHandler):

    def get(self):
        items = ['Python', 'Html', 'Django', 'Flask', 'Tornado']
        self.render('temp.html', items=items)


class StuHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        stu = session.query(Students).all()

        self.write('查询学生信息成功')

    def post(self, *args, **kwargs):
        # 第一种方式
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
        self.write('创建学生信息成功')

    def delete(self, *args, **kwargs):
        # 第一种方式
        stu = session.query(Students).filter(Students.s_name == '小明').first()
        session.delete(stu)
        session.commit()
        # 第二种方式
        session.query(Students).filter_by(s_name='小明').delete()
        session.commit()
        self.write('删除数据成功')

    def patch(self, *args, **kwargs):
        # 第一种方式
        stu = session.query(Students).filter(s_name='小明').first()
        stu.s_name = '小李'
        session.add(stu)
        session.commit()
        # 第二种方式
        session.query(Students).filter(s_name='小明').update({'s_name': '小李'})
        session.commit()

        self.write('修改学生数据成功')



