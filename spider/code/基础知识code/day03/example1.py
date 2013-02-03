
import threading
import time

my_lock = threading.Lock()


class MyThread(threading.Thread):

    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name

    def run(self):
        time.sleep(1)
        if my_lock.acquire():
            global n
            print('number:%s, threading name: %s' % (n, self.name))
            n += 1
            # my_lock.release()


if __name__ == '__main__':
    n = 0
    threads_list = []
    for i in range(200):
        t1 = MyThread(i)
        threads_list.append(t1)
    for i in threads_list:
        i.start()

