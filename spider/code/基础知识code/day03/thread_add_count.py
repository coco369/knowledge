
import threading
from datetime import datetime


def add_count(a, b):
    n = 0
    for i in range(a, b):
        n += 1
    return n


class AddThread(threading.Thread):

    def __init__(self, func):
        super(AddThread, self).__init__()
        self.func = func

    def run(self):
        self.result = self.func

    def get_result(self):
        return self.result


print(datetime.now())

a1 = AddThread(add_count(0, 100000000))
a2 = AddThread(add_count(100000000, 200000000))
a3 = AddThread(add_count(200000000, 300000000))
a4 = AddThread(add_count(300000000, 400000000))
a5 = AddThread(add_count(400000000, 500000000))

a1.start()
a2.start()
a3.start()
a4.start()
a5.start()

a1.join()
a2.join()
a3.join()
a4.join()
a5.join()

print(a1.get_result() + a2.get_result() + a3.get_result()+a4.get_result()+a5.get_result() )

print(datetime.now())





