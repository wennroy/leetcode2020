# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 14:50:05 2021

@author: 53013
"""


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        ## O(n^2) 能过。9800ms 5%
        # if len(nums)<3: return False
        # n = len(nums)
        # for i in range(n-2):
        #     max_value = nums[i+1]
        #     for j in range(i+2,n):
        #         if nums[j]<=nums[i]:
        #             continue
        #         if nums[j] >= max_value:
        #             max_value = nums[j]
        #         else:
        #             # print(nums[i],max_value,nums[j])
        #             return True
        # return False

        # O(n)

        N = len(nums)
        leftMin = [float("inf")] * N
        for i in range(1, N):
            leftMin[i] = min(leftMin[i - 1], nums[i - 1])
        stack = []
        for j in range(N - 1, -1, -1):
            numsk = float("-inf")
            while stack and stack[-1] < nums[j]:
                numsk = stack.pop()
            if leftMin[j] < numsk:
                return True
            stack.append(nums[j])
        return False