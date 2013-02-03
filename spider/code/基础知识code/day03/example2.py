
import threading
import requests
import json
from urllib import parse


def get_html(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    res = requests.get(url, headers=header)
    return res.text


def get_movie_tag(url):
    """
    获取电影的分类tag
    """
    tag_res = get_html(url)
    # 返回的tag_res的结果为'{"tags":["热门","最新","经典","可播放","豆瓣高分","冷门佳片","华语","欧美","韩国","日本","动作","喜剧","爱情","科幻","悬疑","恐怖","成长"]}'
    # 其结果为一个字符串类型的数据，需要将之转化为字典类型的
    result = json.loads(tag_res)
    content = result['tags']
    return content


class SpiderOperation(threading.Thread):

    def __init__(self):
        super(SpiderOperation, self).__init__()
        self.task_lock = threading.Lock()  # 线程锁

    def update_task_list(self):
        """
         多线程操作共享的类对象资源，互斥访问,
         将每个线程处理的结果存入self.task_result_list
        """
        if self.task_lock.acquire():
            print(len(task_result_list))
            link = task_result_list.pop() if task_result_list else ''
            self.task_lock.release()
            return link

    def run(self):
        task_link = self.update_task_list()
        print(task_link)
        if task_link:
            movies_res = get_html(task_link)
            res = json.loads(movies_res)
            result = res['subjects']
            for res in result:
                print('标题:%s，评分：%s' % (res['title'], res['rate']))


if __name__ == '__main__':

    tag_url = 'https://movie.douban.com/j/search_tags?type=movie&source='
    movie_url = 'https://movie.douban.com/j/search_subjects?type=movie&%s&sort=recommend&page_limit=20&page_start=0'
    tags = get_movie_tag(tag_url)
    global task_result_list
    task_result_list = []
    for tag in tags:
        search_url = movie_url
        data = {'tag': tag}
        search_tag = parse.urlencode(data)
        # 搜索出需要爬取的豆瓣分类的url地址
        task_result_list.append(search_url % (search_tag,))

    while True:
        if task_result_list:
            spider1 = SpiderOperation()
            spider2 = SpiderOperation()
            spider1.start()
            spider2.start()
        else:
            break



