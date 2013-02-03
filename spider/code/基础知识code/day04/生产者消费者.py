
def customer():
    r = ''
    while True:
        n = yield r
        print('[CUSTOMER]第%s次吃鸡翅，超级开心' % n)


def product(customer):
    # 生产者
    customer.__next__()
    n = 1
    while n < 5:
        print('[PRODUCT]第%s次做鸡翅' % n)
        # 引入消费者来消费
        customer.send(n)
        print('[PRODUCT]第%s次卖完了，重新去生产' % n)
        n += 1
    customer.close()


if __name__ == '__main__':
    customer = customer()
    product(customer)

