
from sqlalchemy import Column, Integer, String

from utils.connect import Base


def init_db():
    # 创建数据表
    Base.metadata.create_all()


def drop_db():
    # 删除数据表
    Base.metadata.drop_all()


class Students(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    s_name = Column(String(10), unique=False, nullable=False)
    s_age = Column(Integer, default=19)

    __tablename__ = 'students'


