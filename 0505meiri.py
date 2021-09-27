# -*- coding: utf-8 -*-
"""
Created on Fri May  7 15:54:26 2021

@author: 53013
"""


class Solution:
    def __init__(self):
        from collections import defaultdict
        record = defaultdict(int)

    def deleteAndEarn(self, nums):
        if len(nums) <=2:
            return max(nums)
        n = len(nums)
        for index, num in enumerate(nums):
            print(index)
            print(num)
        
n = len(nums)
pos = defaultdict(list)
for index, num in enumerate(nums):
    pos[num].append(index)