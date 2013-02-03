
import requests
from urllib import parse
import threading
import time


def get_html(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    res = requests.get(url, headers=header)
    return res.json()


class spiderDB(threading.Thread):
    def __init__(self):
        super(spiderDB, self).__init__()
        self.task_lock = threading.Lock()

    def update_task_list(self):
        if self.task_lock.acquire():
            link = movies_list.pop() if movies_list else ''
            self.task_lock.release()
        return link

    def run(self):
        link = self.update_task_list()
        if link:
            result = get_html(link)
            for res in result['subjects']:
                title = res['title']
                rate = res['rate']
                print(' 电影名称：%s, 评分：%s' % (title, rate))


if __name__ == '__main__':

    tag_url = 'https://movie.douban.com/j/search_tags?type=movie&source='
    movie_url = 'https://movie.douban.com/j/search_subjects?type=movie&%s&sort=recommend&page_limit=20&page_start=0'

    tag_api = get_html(tag_url)
    global movies_list
    movies_list = []
    for tag in tag_api['tags']:
        data = {'tag': tag}
        m_url = movie_url % parse.urlencode(data)
        movies_list.append(m_url)

    while True:
        if movies_list:
            s1 = spiderDB()
            s2 = spiderDB()

            time.sleep(1)
            s1.start()
            s2.start()

        else:
            break


