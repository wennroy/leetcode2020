# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 09:46:05 2020

@author: lengwaifang
"""

import time
grid =[[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]

class Solution:
    def minPathSum(self, grid):
        ## 动态规划，逆推法
        m,n = len(grid), len(grid[0])
        
        # def transpose(self, grid):
        #     newgrid = []
        #     for i in range(len(grid[0])):
        #         tempi = []
        #         for j in range(len(grid)):
        #             tempi.append(grid[j][i])
        #         newgrid.append(tempi)
        #     return newgrid
        
        # ## 转换成一定是行比列多的形式
        # if m < n:
        #     grid = transpose(None,grid)
        #     temp = n
        #     n = m
        #     m = temp
            
        newgrid = [[-1]*n for _ in range(m)]

        
        def minfunction(self,grid,newgrid,i,j):
            if not newgrid[i][j] == -1:
                return newgrid[i][j]
            if i == 0 and j==0:
                return grid[0][0]
            ## 在顶点
            if j == 0:
                left = 9999999999 # 给一个超大的数
            else:
                left = minfunction(None,grid,newgrid,i,j-1)
                
            if i == 0:
                up = 9999999999
            else:
                up = minfunction(None,grid,newgrid,i-1,j)
            
            if left > up:
                newgrid[i][j] = up + grid[i][j]
            else:
                newgrid[i][j] = left + grid[i][j]
            return newgrid[i][j]
            
        # return minfunction(None, grid, newgrid, m-1, n-1)
            

        print(minfunction(None, grid, newgrid, m-1, n-1))

start = time.clock()
Solution.minPathSum(None,grid)
elapsed = (time.clock() - start)
print("Time used:",elapsed)