# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 14:10:46 2020

@author: 53013
"""


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if matrix == []:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = []
        [dp.append([-float("INF")]*n) for _ in range(m)]
        px = [1,0,-1,0]
        py = [0,1,0,-1]
        '''
        第ij格为起点开始的最长路径
        '''
        def longestincrease(self, i, j):
            if not dp[i][j] == -float("INF"):
                return dp[i][j]
            else:
                cur_val = matrix[i][j]
                max_count = 1
                for k in range(4):
                    cur_count = 1
                    x = px[k] + i
                    y = py[k] + j
                    if x >= m or x <0 or y >=n or y<0 or cur_val >= matrix[x][y]:
                        continue
                    else:
                        cur_count = longestincrease(self,x,y)+ 1
                        if cur_count >= max_count:
                            max_count = cur_count
                dp[i][j] = max_count
            return dp[i][j]
        max_val = 1
        for i in range(m):
            for j in range(n):
                longestincrease(self, i, j)
                if dp[i][j] > max_val:
                    max_val = dp[i][j]
        return max_val