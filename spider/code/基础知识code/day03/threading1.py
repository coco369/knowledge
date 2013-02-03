
import time
import threading


class Study(threading.Thread):

    def __init__(self, name):
        super(Study, self).__init__()
        self.s_name = name

    def run(self):
        print('当前线程开始 %s' % threading.current_thread().name)
        print('开始学习 %s'% self.s_name)
        time.sleep(2)
        print('学习%s结束' % self.s_name)
        print('当前线程结束 %s' % threading.current_thread().name)


if __name__ == '__main__':

    s1 = Study('语文')
    s2 = Study('数学')

    # 守护线程
    # s1.daemon = True
    # s2.daemon = True
    # 启动
    s1.start()
    # s1.join()
    #
    s2.start()
    # s2.join()

    # s1.run()
    # s2.run()


    print('学习结束，可以玩了')
# s1.run()

