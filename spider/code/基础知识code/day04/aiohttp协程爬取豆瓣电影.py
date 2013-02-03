
import aiohttp
import asyncio
import json
from pymongo import MongoClient


class DouBanMovie():

    def __init__(self):
        # tag分类的url
        self.tag_url = 'https://movie.douban.com/j/search_tags?type=movie&source='
        # 获取电影的url
        self.movie_url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%s&sort=recommend&page_limit=20&page_start=%s'
        # 分类的信息
        self.tags = []
        # 查询分页的深度
        self.page = 10
        conn = MongoClient('mongodb://127.0.0.1:27017')
        db = conn['douban1']
        # 操作表
        self.collection = db['spider']

    async def get_html_info(self):
        # 获取aiohttp的session实例，通过session去获取url的请求信息
        async with aiohttp.ClientSession() as session:
            async with session.get(self.tag_url) as response:
                # 使用await关键字，在获取网页的源码的时候，如果由于IO关系，
                # 数据一直没有响应，程序可以切换到其他地方去执行，等到有响应的时候，
                # 再切换回来执行
                tags = await self.parse(await response.text())
                self.tags =tags['tags']

            for tag in self.tags:
                for start_page in range(self.page):
                    async with session.get(self.movie_url % (tag, start_page*20)) as response:
                        data = await self.parse(await response.text())
                        for movie_info in data['subjects']:
                            await self.insert_into_db(movie_info)

    async def parse(self, response):
        # 将页面解析的api接口解析为python的字典对象
        tag_json = json.loads(response)
        return tag_json

    async def insert_into_db(self, data):
        # 插入到mongodb中
        self.collection.insert_one(data)

    def run(self):
        # 获取event_loop, 使用event_loop的run_until_complete去启动我们的任务
        loop = asyncio.get_event_loop()
        task = asyncio.wait([self.get_html_info()])
        loop.run_until_complete(task)


if __name__ == '__main__':
    dbm = DouBanMovie()
    dbm.run()

