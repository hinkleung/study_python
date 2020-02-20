def fib(n):
    if n < 1:
        return 0
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib2(n):
    a, b = 1, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b



if __name__ == '__main__':
    # print(fib(20))
    fib2(20)
