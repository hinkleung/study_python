import json


def main():
    mydict = {
        'name': '阿东',
        'age': 38,
        'qq': 156168848,
        'friends': ['金丝豆', '挥洒'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }

    try:
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(mydict, f)
    except IOError as e:
        print(e)
    print('保存数据完成')


if __name__ == '__main__':
    main()
