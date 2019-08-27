# tornado使用操作指南--aiomysql

> Auth: 王海飞
>
> Data：2019-08-27
>
> Email：779598160@qq.com
>
> github：https://github.com/coco369/knowledge

### 1. 前言

aiomysql这是一个基于asyncio和pymysql的库

使用场景: 根据项目中使用mysql查询的频率来选择是使用单独的connection还是使用连接池，查询较少的可以选择使用connection，使用一次以后就断开，再次使用再次连接，但是对于mysql，每次连接的开销都很高，所以建议还是使用连接池。

### 2. 安装

安装aiomysql:

```
pip install aiomysql
```

### 3. 创建单个连接


```
import json

import aiomysql
import tornado.web
import tornado.ioloop


async def connect_mysql():
    return await aiomysql.connect(
        host='127.0.0.1',
        password='',
        db='tornado_test',
        port=3306,
        user='root'
    )


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('hello index')


class DeptHandler(tornado.web.RequestHandler):
    async def get(self, no):
        async with self.settings['mysql'].cursor() as cursor:
            await cursor.execute("select * from tb_dept where dno=%s" % no)
            if cursor.rowcount == 0:
                result = json.dumps({
                    'code': 1001,
                    'msg': f'没有编号为{no}的部门'
                })
                self.write(result)
                return
            row = await cursor.fetchone()
            self.write(json.dumps(row))

class MakeApp(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/index/', IndexHandler),
            (r'/api/depts/(.*)', DeptHandler)
        ]
        mysql = tornado.ioloop.IOLoop.current().run_sync(connect_mysql)
        return super().__init__(handlers=handlers,
                                mysql=mysql)

if __name__ == '__main__':
    app = MakeApp()
    app.listen(8001)
    tornado.ioloop.IOLoop.current().start()
```
