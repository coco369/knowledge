
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 数据库连接
db_url = 'mysql+pymysql://root:123456@127.0.0.1:3306/tornado_db'

# 创建引擎
engine = create_engine(db_url)

# declarative_base类维持了一个从类到表的关系，通常一个应用使用一个base实例，所有实体类都应该继承此类对象
Base = declarative_base()

#创建和数据库连接会话
DbSession = sessionmaker(bind=engine)
#创建会话对象
session = DbSession()



