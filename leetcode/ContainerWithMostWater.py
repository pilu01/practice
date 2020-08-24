# -*- coding: utf-8 -*-
# @Time    : 2020/8/14 10:43
# @Author  : xhb
# @FileName: ContainerWithMostWater.py
# @Software: PyCharm

"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，
使得它们与 x 轴共同构成的容器可以容纳最多的水

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


"""
[1,8,6,2,5,4,8,3,7]
   ↑             ↑
通过两个指针前后迭代
s = len 指针怎么* min(ai, aj)
指针怎么移动，选用演绎法

用两个指针从两端走，记录下当前的最大值，然后让其中较小的一边移动一位。
为什么移动较小的一个呢：

假设移动最大的那一个
小为x，大为y
s = (y-x)*x

接下来数字为 z
if z >= y:
    return s
else:
    if z > x:
        # 距离小了
        retun s
    elif z <= x:
        # 距离、宽度都小了
        return s
    
综上，应该移动最小那位
"""


def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    l, r = 0, len(height)-1

    currentMax = 0

    while l != r:
        currentMax = max(min(height[r], height[l]) * (r-l), currentMax)
        if height[r] > height[l]:
            l += 1
        else:
            r -= 1
    return currentMax