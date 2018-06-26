import time, random
from datetime import datetime


# data = [2, 4, 33, 44, 55, 66, 77, 88, 99, 100]
# data1 = list(range(100000))
def random_list(n):
    result = []
    ids = list(range(1001, 1001+n))
    a1 = ['李', '郑', '刘', '林', '王', ]
    a2 = ['爱', '光', '习', '龙', ]
    a3 = ['娟', '丽', '刚', '龙', ]
    for i in range(n):
        age = random.randint(18,60)
        id = ids[i]
        name = random.choice(a1)+random.choice(a2)+\
               random.choice(a3)
        dict_ran = {'id':id, 'name':name, 'age':age}
        result.append(dict_ran)
    return result


data = random_list(50)


def call_time(func):
    def wrapper(*args, **kwargs):
        t1 = datetime.now()
        x = func(*args, **kwargs)
        t2 = datetime.now()
        print("Time cost:", func.__name__, t2-t1)
        return x
    return wrapper


@call_time
def linear_search(data_set, value):
    for i in range(len(data_set)):
        if data_set[i] == value:
            return print(i)


linear_search(data, 234232)


@call_time
def bin_search(data_set, value):
    '''

    :param data_set: 所查找的数组
    :param value: 所查找的值
    :return: 所查找值的下标
    '''
    low = 0
    high = len(data_set) - 1 # 下标只到len-1
    while low <= high: # 常规判断
        mid = (low+high)//2
        if data_set[mid] == value:
            return print(mid)
        elif data_set[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return print(False)

bin_search(data, 1035)


def bin_search(data_set, value):
    '''

    :param data_set: 所查找的数组
    :param value: 所查找的值
    :return: 所查找值的下标
    '''
    low = 0
    high = len(data_set) - 1 # 下标只到len-1
    while low <= high: # 常规判断
        mid = (low+high)//2
        if data_set[mid].get('id') == value:
            return print(data_set[mid])
        elif data_set[mid].get('id') > value:
            high = mid - 1
        else:
            low = mid + 1
    return print(False)

bin_search(data, 1035)








