
import time
from datetime import datetime


def main():
    counter = 0
    for i in range(500000000):
        counter += 1
    print(counter)


if __name__ == '__main__':
    print(datetime.now())
    main()
    print(datetime.now())