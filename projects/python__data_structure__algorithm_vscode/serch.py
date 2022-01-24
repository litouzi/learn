'''
判断算法复杂度
  确定问题规模n
  循环减半过程→logn
  k层关于n的循环→n的k次幂 
'''

'''
查找：在一些数据元素中，通过一定的方法找出与给定关键字相同的数据元素的过程
列表查找(线性表查找)：从列表中查找指定元素
 输入：列表、待查找元素
 输出：元素下标(未找到元素时一般返回None或-1)(下标由0开始)
内置列表查找函数:index()

顺序查找：也叫线性查找，从列表第一个元素开始，顺序进行搜索，直到找到元素或搜索到列表最后一个元素为止
二分查找：又叫折半查找，从有序列表的初始候选区li[0:n]开始，通过对待查找的值与候选区中间值的比较，可以使候选区减少一半
        当left>right 候选区无值 结束算法

'''
from cal_time import *


@cal_time
def linear_serch(li, val):  # 线性查找 list为列表 val为待查找元素 时间复杂度O(n)
    for ind, v in enumerate(li):  # index下标 value值
        if v == val:
            return ind  #  找到与待查找元素相同的的值 返回其下标
    else:
         return None  # 没找到

@cal_time
def binary_serch(li, val):  # 二分法查找 列表元素已由小到大排好序 时间复杂度O(logn) 循环减半
    left = 0                # left为第一个元素下标0
    right = len(li) - 1     # right为最后一个元素的下标n-1
    while left<=right:          # 候选区有值时执行循环
        mid = (left + right)//2 # 整除
        if li[mid] == val:  # 当中间下标对应的值为待查找元素的值 返回此下标
            return mid
        elif li[mid] > val: # 待查找值在mid左边
            right = mid-1   # 取左半候选区为下一个候选区 将right移到mid左边
        else:               # li[mid] > val 待查找的值在mid右侧
            left = mid+1    # 取右半候选区 将left移到mid右边
    else:                       # else对应while while执行完了还没有返回值 候选区无值时返回None
        return None             # 这里的else指的是while正常执行完之后 中间也没有遇到break 就会接着执行else里面的语句
                                #
        # 若起初不满足while的条件 就不会执行else里面的语句直接往下执行

#li = [1,2,3,4,5,6,7,8,9]
#print(binary_serch(li,3))
#li = [1,2,3,4,5,6,7,8,9]
li = list(range(1000000000))
print(linear_serch(li, 38900000))
print(binary_serch(li, 38900000))






