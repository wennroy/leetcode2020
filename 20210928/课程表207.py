# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:34:24 2020

@author: wennroy
"""

'''
错误做法，应用邻接表
'''
class Node:
    def __init__(self, val, point = list()):
        self.val = val
        self.point = point

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list) -> bool:
        val = [-1] * numCourses
        index = Node(val) ## val是第i门课程的指针所在的位置
        ## 构建有向图
        rootnum = []
        for req in prerequisites:
            n = len(req)
            for i in range(n):
                if index.val[req[i]] == -1:
                    index.val[req[i]] = len(index.point)
                    root = Node(req[i])
                    index.point = index.point + [root]
                else:
                    root = index.point[index.val[req[i]]]
                if i == 0:
                    oldroot = root
                    rootnum.append(oldroot.val)
                    continue
                else:
                    # print(root.val,oldroot.val)
                    oldroot.point = oldroot.point + [root]
                    oldroot = root
        print(rootnum)
        ## 寻找是否构成环路，若构成环路则不成立。
        from queue import Queue
        for num in rootnum:
            root = index.point[index.val[num]]
            # print(root.point[0].val)
            used = [0]*numCourses
            q = Queue()
            q.put(root)
            while q.qsize():
                pt = q.get()
                for i in range(len(pt.point)):
                    if used[pt.point[i].val] == 1:
                        return False
                    else:
                        used[pt.point[i].val] = 1
                        q.put(pt.point[i])
        return True
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        visited = [0] * numCourses
        result = list()
        valid = True

        for info in prerequisites:
            edges[info[1]].append(info[0])
        
        def dfs(u: int):
            nonlocal valid
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v] == 1:
                    valid = False
                    return
            visited[u] = 2
            result.append(u)
        
        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)
        
        return valid
'''
print(Solution.canFinish(None, 2, [[1,0]]))