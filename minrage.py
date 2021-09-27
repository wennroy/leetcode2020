# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 16:39:59 2021

@author: 53013
"""


connections = [[1,0],[1,2],[2,3],[4,2]]
n = 5
class Solution:
    def minrange(self, connections, n):
        adjvex = [[] for _ in range(n)]
        for i, [x,y] in enumerate(connections):
            adjvex[x].append(i)
            adjvex[y].append(i)
        ans = 0
        print(adjvex)
        cur_index = adjvex[0][0]
        def countwrongpath(adjvex, l, last_index):
            ans = 0
            nx = l
            while len(adjvex[nx]) == 2:
                if last_index == adjvex[nx][0]:
                    nxt_index = adjvex[nx][1]
                else:
                    nxt_index = adjvex[nx][0]
                last_index = nxt_index
                if connections[nxt_index][0] == nx:
                    ans += 1
                    nx = connections[nxt_index][1]
                else:
                    nx = connections[nxt_index][0]
            print(ans, nx)
            # index = adjvex[nx][0]
            # if connections[index][0] == nx:
            #     ans += 1
            return ans
        
        if connections[cur_index][0] == 0:
            ans += 1
            l = connections[cur_index][1]
        else:
            l = connections[cur_index][0]
        last_index = cur_index
        ans += countwrongpath(adjvex, l, last_index)
        print(ans, l, last_index)
        if len(adjvex[0]) == 2:
            cur_index = adjvex[0][1]
            if connections[cur_index][0] == 0:
                ans += 1
                l = connections[cur_index][1]
            else:
                l = connections[cur_index][0]
            last_index = cur_index
            ans += countwrongpath(adjvex, l, last_index)
        print(ans, l, last_index)
        return ans



'''
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        ######## 邻接表，建无向图
        adjvex = [[] for _ in range(n)]
        for i, [x,y] in enumerate(connections):
            adjvex[x].append(i)
            adjvex[y].append(i)
        ######## 从0出发，其实是有向图，方向是倒着的
        res = 0
        visited = [False for _ in range(n - 1)] #mark的是connections中的index
        Q = [0]
        while Q:
            cur_len = len(Q)
            for _ in range(cur_len):
                cur = Q.pop(0)
                for i in adjvex[cur]: 
                    if visited[i] == False:
                        visited[i] = True

                        [x, y] = connections[i]
                        if cur == x:
                            res += 1
                            Q.append(y)
                        else:
                            Q.append(x)

        return res

作者：Hanxin_Hanxin
链接：https://leetcode-cn.com/problems/reorder-routes-to-make-all-paths-lead-to-thex`-city-zero/solution/cpython3-tan-xin-0wei-qi-dian-bfs-by-han-zu59/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

kk = Solution()
print(kk.minrange(connections,n))