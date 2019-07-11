import os

import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line

from app.views import IndexHandler, TempHandler, CreateDBHandler, StuHandler

# 定义默认的端口
define('port', default=8000, type=int)


def make_app():
    return tornado.web.Application(
        handlers=[
            (r"/", IndexHandler),
            (r"/create_db/", CreateDBHandler),
            (r"/temp/", TempHandler),
            (r"/add_stu/", StuHandler),
        ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), 'static')
    )


if __name__ == "__main__":
    # 解析命令行
    parse_command_line()
    # 获取Application对象
    app = make_app()
    # 监听端口
    app.listen(options.port)
    # 启动IOLoop实例
    tornado.ioloop.IOLoop.current().start()