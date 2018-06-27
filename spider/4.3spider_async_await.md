
# 爬虫学习使用指南--协程

>Auth: 王海飞
>
>Data：2018-06-15
>
>Email：779598160@qq.com
>
>github：https://github.com/coco369/knowledge 

### aiohttp

aiohttp是什么，官网上有这样一句话介绍：Async HTTP client/server for asyncio and Python，是异步的HTTP框架

#### 1. 安装

	pip install aiohttp

#### 2. 爬取豆瓣电影资源

	import aiohttp
	import json
	import asyncio
	from pymongo import MongoClient
	
	
	class DouBan(object):
	    def __init__(self):
	        self.tag_url = 'https://movie.douban.com/j/search_tags?type=movie&source='
	        self.bash_url = 'https://movie.douban.com/j/search_subjects?type=movie&tag={tag}&sort=recommend&page_limit=20&page_start={page_start}'
	        self.tag_key = []
	        self.max_page = 10
	        client = MongoClient(host='127.0.0.1', port=27017)
	        db = client['unsplash']
	        self.collection = db['images']
	
	    async def get_img_info(self):
	        async with aiohttp.ClientSession() as session:
	            # 获取电影分类的信息
	            async with session.get(self.tag_url) as tag_rsponse:
	                self.tag_key = self.parse_tag(await tag_rsponse.text())
	            print(self.tag_key)
	            # 循环去获取网页api内容信息
	            for key in self.tag_key:
	                for page in range(0, self.max_page):
	                    async with session.get(self.bash_url.format(tag=key, page_start=page*20)) as response:
	                        await self.parse(await response.text())
	
	    def parse_tag(self, response):
	        json_data = json.loads(response)['tags']
	        return json_data
	
	    async def parse(self,response):
	        json_data = json.loads(response)['subjects']
	        for data in json_data:
	            await self.do_insert(data)
	
	    async def do_insert(self, document):
	        try:
	            result = self.collection.insert_one(document)
	        except BaseException as e:
	            print('error%s' % e)
	        else:
	            print('result %s' % repr(result.inserted_id))
	
	    def run(self):
	        loop = asyncio.get_event_loop()
	        tasks = [self.get_img_info()]
	        loop.run_until_complete(asyncio.wait(tasks))
	
	
	if __name__ == '__main__':
	    us = DouBan()
	    us.run()
