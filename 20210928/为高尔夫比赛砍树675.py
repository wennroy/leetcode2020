# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 16:15:45 2020

@author: 53013
"""
'''
又理解错题意啦！！！
'''


class Solution:
    def cutOffTree(self, forest):
        if forest == []:
            return 0
        m = len(forest)
        n = len(forest[0])
        max_height = 0
        for i in range(m):
            for j in range(n):
                max_height = max(max_height, forest[i][j])
        used = []
        [used.append([0] * n) for _ in range(m)]
        px = [1,0,-1,0]
        py = [0,1,0,-1]
        def dfs(forest, i, j, cur_height, used):
            import copy
            forest = copy.deepcopy(forest)
            used = copy.deepcopy(used)
            if forest[i][j] == 0 or used[i][j]==1:
                return -1
            used[i][j] = 1
            ## 碰到非道路
            if forest[i][j] == max_height:
                return 1
            flag = 0
            if forest[i][j] >= 2:
                if cur_height < forest[i][j]:
                    cur_height = forest[i][j]
                    forest[i][j] = 1
                    used = []
                    flag = 1
                    [used.append([0] * n) for _ in range(m)]
                else:
                    return -1
            count = float("INF")
            for k in range(4):
                # print(count)
                x = px[k] + i
                y = py[k] + j
                if x<0 or y<0 or x>m-1 or y>n-1:
                    continue
                next_step = dfs(forest, x,y,cur_height,used)
                if next_step > 0 and next_step < count:
                    count = next_step + 1
                else:
                    continue
            if count == float("INF"):
                return -1
            else:
                print(forest)
                print(i,j,count, cur_height)
                return count
        ans = dfs(forest, 0,0,1,used) - 1
        if ans >0:
            return ans
        else:
            return -1


import time
forest = [[2,3,4],[0,0,5],[8,7,6]]
forest = [
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
forest = [
 [1,2,3],
 [0,0,0],
 [7,6,5]
]
forest = [[54581641,64080174,24346381,69107959],
          [86374198,61363882,68783324,79706116],
          [668150,92178815,89819108,94701471],
          [83920491,22724204,46281641,47531096],
          [89078499,18904913,25462145,60813308]]
forest = [[9,12,5,14],
          [17,11,13,15],
          [2,20,19,21],
          [16,4,7,8],
          [18,3,6,10]]
start = time.time()
print(Solution.cutOffTree(None, forest))
print('过去了%s秒'%(time.time()-start))