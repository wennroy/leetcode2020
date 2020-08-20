# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 14:03:04 2020

@author: 53013
"""

'''
class Solution:
    def __init__(self):
        self.record = {}

    def removeStones(self, stones):
        if not isinstance(stones,tuple):
            tmp = []
            for stone in stones:
                tmp.append(tuple(stone))
            stones = tuple(tmp)
        if stones in self.record.keys():
            return self.record[stones]
        x_cor = []
        y_cor = []
        for l in stones:
            x_cor.append(l[0])
            y_cor.append(l[1])
        if len(set(x_cor)) == len(x_cor) and len(set(y_cor)) == len(y_cor):
            return 0
        max_count = 0
        for stone in stones:
            x = stone[0]
            y = stone[1]
            x_stones = []
            for stone1 in stones:
                if stone1[0] == x:
                    continue
                x_stones.append(stone1)
            x_stones.append(stone)
            x_stones = tuple(x_stones)
            if set(x_stones) == set(stones):
                continue
            # print(x_stones, stones,stone)
            max_count = max(max_count, 1 + Solution.removeStones(self, x_stones))
            y_stones = []
            for stone1 in stones:
                if stone1[1] == y:
                    continue
                y_stones.append(stone1)
            y_stones.append(stone)
            y_stones = tuple(y_stones)
            if set(y_stones) == set(stones):
                continue
            max_count = max(max_count, 1 + Solution.removeStones(self, y_stones))
        self.record[stones] = max_count
        # print(stones, max_count)
        return max_count
    题目理解错了
'''
class DSU:
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

class Solution(object):
    def removeStones(self, stones):
        N = len(stones)
        dsu = DSU(20000)
        for x, y in stones:
            dsu.union(x, y + 10000)

        return N - len({dsu.find(x) for x, y in stones})

import collections
class Solution(object):
    def removeStones(self, stones):
        graph = collections.defaultdict(list)
        for i, x in enumerate(stones):
            for j in range(i):
                y = stones[j]
                if x[0]==y[0] or x[1]==y[1]:
                    graph[i].append(j)
                    graph[j].append(i)

        N = len(stones)
        ans = 0

        seen = [False] * N
        for i in range(N):
            if not seen[i]:
                stack = [i]
                seen[i] = True
                while stack:
                    ans += 1
                    node = stack.pop()
                    for nei in graph[node]:
                        if not seen[nei]:
                            stack.append(nei)
                            seen[nei] = True
                ans -= 1
        return ans

import time
stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
stones = [[0,0]]
stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2],[3,3],[4,4],[4,5],[5,6],[7,9],[1,10],[3,5]]
stones = [[0,0],[0,1],[0,2]]
start = time.time()
kkk = Solution()
print(Solution.removeStones(kkk, stones))
print('过去了%s秒'%(time.time()-start))