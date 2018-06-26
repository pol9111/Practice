import random

test = list(range(100))
random.shuffle(test)


def bubble_sort(lst):
    '''
    列表排序
    :param lst: 需要排序的列表
    :return: 返回已经排好序的列表
    '''
    for i in range(len(lst) - 1): # 需要排序的列表长度（一趟）, 跟j + 1 比较所以len-1, 最底下那个数已经在本来位置
        exchange = False # set a default
        for j in range(len(lst) - i - 1): # 每趟的长度（步长）
            if lst[j] > lst[j + 1]: # 比较前后二个值的大小
                lst[j], lst[j + 1] = lst[j + 1], lst[j] # 交换前后两个值的位置
                exchange = True # 改变默认判断值
        if not exchange: # 如果默认值不变（没有交换发生）
            break # 跳出该循环
    return lst # 返回有序列表


# bubble_sort(test)
# print(test)


def select_sort(lst):
    for i in range(len(lst) - 1): # 需要排序的列表长度（一趟）， 最后一个没东西比较，就在他本来位置
        min_loc = i # set 一个默认最小值
        for j in range(i + 1, len(lst)): # 从i后面一个值开始比较到最后一个值
            if lst[j] < lst[min_loc]:
                min_loc = j # 最小值的下标变为j
        lst[i], lst[min_loc] = lst[min_loc], lst[i] # 旧的放回去继续比较， 新的拿出来归位
# 1.要判断的i值 2.i or j值 3.旧j位置or原本最小值位置  4.最小值的位置
        # 列表 值 互换位置
    return lst

# select_sort(test)
# print(test)


def insert_sort(lst):
    for i in range(1, len(lst)): # 从第二个开始
        tmp = lst[i] # 为什么要设置tmp， 因为在while循环的一行lst[i]的值换了
        j = i -1 # 地下都是j 和 tmp
        while j >= 0 and lst[j] > tmp:
            lst[j + 1] = lst[j] # 其实都是一个值， 这个值不停地往前直到停止
            j = j - 1 # 让下标j 一直往前
        lst[j + 1] = tmp # 原本的i位置被j 停止时的值替换
    return lst

insert_sort(test)
print(test)



