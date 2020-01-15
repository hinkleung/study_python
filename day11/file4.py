import time


def main():
    with open('致橡树.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    with open('致橡树.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    #返回list
    with open('致橡树.txt', encoding='utf-8') as f:
        lines = f.readlines()
    print(lines)


if __name__ == '__main__':
    main()
