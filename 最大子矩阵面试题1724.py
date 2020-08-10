# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 16:43:43 2020

@author: 53013
"""


class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        def maxcontinuousnums(self, nums):
            n = len(nums)
            dp = [0]*n
            dp[0] = nums[0]
            index = [0]
            temp = 0
            for i in range(1,n):
                if dp[i-1] + nums[i] > nums[i]:
                    dp[i] = dp[i-1] + nums[i]
                    index.append(temp)
                else:
                    dp[i] = nums[i]
                    temp = i
                    index.append(temp)
            return max(dp), index[dp.index(max(dp))], dp.index(max(dp))

        maxval = -float("INF")
        x1,y1,x2,y2 = 0,0,0,0
        for j in range(m):
            b = [0]*n
            for k in range(j,m):
                for i in range(n):
                    b[i] += matrix[i][k]
                val, index_y1, index_y2 = maxcontinuousnums(self, b)
                if val > maxval:
                    x1 = index_y1
                    x2 = index_y2
                    y1 = j
                    y2 = k
                    maxval = val
        return [x1,y1,x2,y2]
'''
class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        b    = [0] * cols
        res  = -100000000
        ans  = [0] * 4
        beginr1, beginc1 = 0,0
        for i in range(rows):
            b = [0] * cols
            for j in range(i, rows):
                for k in range(cols):
                    b[k] += matrix[j][k]
                beginr1 = i
                beginc1 = 0
                sum_ = 0
                for k in range(cols):
                    if sum_ <0:
                        sum_ = b[k]
                        beginc1 = k
                    else:
                        sum_ += b[k]
                    if res < sum_:
                        
                        res = sum_
                        ans = [beginr1, beginc1, j,k]
        return ans
'''