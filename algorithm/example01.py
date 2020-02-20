if __name__ == '__main__':
    items1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10))))
    print(items1)