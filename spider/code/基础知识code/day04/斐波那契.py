
# 实现斐波那契算法 0 1 1 2 3 5 8 13 21 34 55


# def f(n):
#     a, b = 0, 1
#     print(a, end=' ')
#     for i in range(n):
#         a, b = b, a + b
#         print(a, end=' ')

def f(n):
    a, b, c = 0, 1, 0
    while c < n:
        yield a
        a, b = b, a+b
        c += 1


if __name__ == '__main__':
    result = f(10)
    for i in range(10):
        b = result.__next__()
        print(b)

