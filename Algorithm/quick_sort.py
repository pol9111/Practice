import random


def quick_sort_run(lst, left, right):
    if left < right: # 让快速排序一直运行的条件， 左下标和右下标相遇即停止
        mid = patition(lst, left, right) # 给下面递归提供的中间值， 一直做分割patition
        quick_sort_run(lst, left, mid - 1) # 中间值左边一直做递归直到，left = right
        quick_sort_run(lst, mid + 1, right) # 中间值右边一直做递归直到，left = right


def patition(lst, left, right):
    '''
    实现快速传递的原理
    :param lst: 传入的数据
    :param left: 数据的左边下标
    :param right: 数据的有下标
    :return: 返回值作为中间值
    '''
    tmp = lst[left] # 先把一个值拿出来，等待
    while left < right: # 让快速排序一直运行的条件， 左下标和右下标相遇即停止
        while left < right and lst[right] >= tmp: # 之所以要在再加left < right， 可能在一个while里面把R/L减到-1
            right -= 1 # 如果满足条件再往前， 跟前一个值比较
        lst[left] = lst[right] # 如果不满足条件， 把右边的值放去左边， 就是给左边的位置赋值
        while left < right and lst[left] <= tmp:
            left += 1
        lst[right] = lst[left]
    lst[left] = tmp # 把早先拿走的值放到停顿的那个位置
    return left # 返回值作为中间值


# def quick_sort(lst): # 传入数据
#     return quick_sort_run(lst, 0, len(lst) - 1) # 返回调用递归函数


data = list(range(1000))
random.shuffle(data)

# quick_sort(data)
quick_sort_run(data, 0, len(data) - 1)
print(data)
