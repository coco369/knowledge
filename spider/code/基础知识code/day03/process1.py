
import os
import time
import random
from multiprocessing import Process


def studying():
    while True:
        print('起床看书ing，PID: %s' % os.getpid())
        time.sleep(random.randint(1,5))
        print('玩会手机，PID:%s' % os.getpid())


def chiji():
    while True:
        print('开始吃鸡，PID: %s' % os.getpid())
        time.sleep(random.randint(1,3))
        print('开始王者荣耀，PID：%s' % os.getpid())


if __name__ == '__main__':

    p1 = Process(target=studying)
    p2 = Process(target=chiji)

    p1.start()
    # 阻塞
    p1.join()

    p2.start()





