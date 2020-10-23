# -*- coding: utf-8 -*-
# @Time    : 2020/10/14 16:53
# @Author  : xhb
# @FileName: 查找排序.py
# @Software: PyCharm


"""
       时间复杂度      空间复杂度
冒泡、  O(n^2)          O(1)
快速、  O(NlnN)         O(log2N) - O(N)
归并、
堆排序  O(Nln2N)         O(1)

二分查找、线性查找
"""


# 冒泡
def bubbleSort(arr):
    l = len(arr)
    for i in range(1, l):
        for j in range(0, l-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def partition(arr, low, high):
    pivot = arr[high]
    i = low -1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr,low,high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)
    return arr




list02 = ['name', 'age', '21', 20]
str02 = ''.join(list02)
print(str02)



