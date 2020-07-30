# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:12:25 2020

@author: wennroy
我们得到了一副藏宝图，藏宝图显示，在一个迷宫中存在着未被世人发现的宝藏。

迷宫是一个二维矩阵，用一个字符串数组表示。它标识了唯一的入口（用 'S' 表示），和唯一的宝藏地点（用 'T' 表示）。但是，宝藏被一些隐蔽的机关保护了起来。在地图上有若干个机关点（用 'M' 表示），只有所有机关均被触发，才可以拿到宝藏。
要保持机关的触发，需要把一个重石放在上面。迷宫中有若干个石堆（用 'O' 表示），每个石堆都有无限个足够触发机关的重石。但是由于石头太重，我们一次只能搬一个石头到指定地点。
迷宫中同样有一些墙壁（用 '#' 表示），我们不能走入墙壁。剩余的都是可随意通行的点（用 '.' 表示）。石堆、机关、起点和终点（无论是否能拿到宝藏）也是可以通行的。
我们每步可以选择向上/向下/向左/向右移动一格，并且不能移出迷宫。搬起石头和放下石头不算步数。那么，从起点开始，我们最少需要多少步才能最后拿到宝藏呢？如果无法拿到宝藏，返回 -1 。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xun-bao
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def minimalSteps(self, maze):
        n = len(maze)
        m = len(maze[0])
        maze_list = []
        for l in range(n):
            item = maze[l]
            temp = []
            for k in range(m):
                if item[k] == '.':
                    temp.append(0)
                elif item[k] == 'M':
                    temp.append(1)
                elif item[k] == 'T':
                    temp.append(2)
                elif item[k] == 'S':
                    start_point = (l,k)
                    temp.append(3)
                elif item[k] == 'O':
                    temp.append(4)
                else:
                    temp.append(-1)
            maze_list.append(temp)
        end_point  = (2,2)
        dist = {}
        def mindistance(self, maze_list,start_point,end_point,dist):
            
            if start_point[0]<0 or start_point[0]>len(maze_list)-1 or start_point[1]<0 or start_point[1]>len(maze_list[0])-1\
                or maze_list[start_point[0]][start_point[1]] == -1:
                    dist[start_point,end_point] = 99999999
                    return 99999999
            if start_point == end_point:
                return 0
            if (start_point,end_point) in dist.keys():
                return dist[start_point,end_point]
            elif (end_point, start_point) in dist.keys():
                return dist[end_point,start_point]
            else:
                up = start_point[0], start_point[1] + 1
                down = start_point[0], start_point[1] - 1
                left = start_point[0]-1, start_point[1]
                right = start_point[0]+1, start_point[1]
                dist[start_point,end_point] = 1 + min(mindistance(None,maze_list,up,end_point,dist),\
                                                      mindistance(None,maze_list,down,end_point,dist),\
                                                      mindistance(None,maze_list,left,end_point,dist),\
                                                      mindistance(None,maze_list,right,end_point,dist))
                return dist[start_point, end_point]
                    
        distance = mindistance(None, maze_list, start_point, end_point, dist)
        print(distance)
maze = ["S#O", "M..", "M.T"]
Solution.minimalSteps(None, maze)


'''
from queue import Queue

class Solution:
    def minimalSteps(self, maze: List[str]) -> int:
        # 四个方向
        dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # 计算（x, y）到maze中其他点的距离，结果保存在ret中
        def bfs(x, y, maze, m, n):
            ret = [[-1]*n for _ in range(m)]
            ret[x][y] = 0
            q = Queue()
            q.put((x,y))
            while q.qsize():
                curx, cury = q.get()
                for dx, dy in dd:
                    nx = curx + dx
                    ny = cury + dy
                    if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] != '#' and ret[nx][ny] == -1:
                        ret[nx][ny] = ret[curx][cury] + 1
                        q.put((nx, ny))
            return ret

        m = len(maze)
        n = len(maze[0])

        startX = -1
        startY = -1
        endX = -1
        endY = -1

        # 机关 & 石头
        buttons = []
        stones = []

        # 记录所有特殊信息的位置
        for i in range(m):
            for j in range(n):
                if maze[i][j] == 'S':
                    startX = i
                    startY = j
                elif maze[i][j] == 'T':
                    endX = i
                    endY = j
                elif maze[i][j] == 'O':
                    stones.append((i,j))
                elif maze[i][j] == 'M':
                    buttons.append((i,j))
                else:
                    pass
        
        nb = len(buttons)
        ns = len(stones)

        startToAnyPos = bfs(startX, startY, maze, m, n)

        # 若没有机关，最短距离就是(startX, startY)到(endX, endY)的距离
        if nb == 0:
            return startToAnyPos[endX][endY]

        # 记录第i个机关到第j个机关的最短距离
        # dist[i][nb]表示到起点的距离， dist[i][nb+1]表示到终点的距离
        dist = [[-1]*(nb+2) for _ in range(nb)]

        # 遍历所有机关，计算其和其他点的距离
        buttonsToAnyPos = []
        for i in range(nb):
            bx, by = buttons[i]
            # 记录第i个机关到其他点的距离
            iToAnyPos = bfs(bx, by, maze, m, n)
            buttonsToAnyPos.append(iToAnyPos)
            # 第i个机关到终点的距离就是(bx, by)到(endX, endY)的距离
            dist[i][nb + 1] = iToAnyPos[endX][endY]
        
        for i in range(nb):
            # 计算第i个机关到(startX, startY)的距离
            # 即从第i个机关出发，通过每个石头(sx, sy)，到(startX, startY)的最短距离
            tmp = -1
            for j in range(ns):
                sx, sy = stones[j]
                if buttonsToAnyPos[i][sx][sy] != -1 and startToAnyPos[sx][sy] != -1:
                    if tmp == -1 or tmp > buttonsToAnyPos[i][sx][sy] + startToAnyPos[sx][sy]:
                        tmp = buttonsToAnyPos[i][sx][sy] + startToAnyPos[sx][sy]

            dist[i][nb] = tmp

            # 计算第i个机关到第j个机关的距离
            # 即从第i个机关出发，通过每个石头(sx, sy)，到第j个机关的最短距离
            for j in range(i+1, nb):
                mn = -1
                for k in range(ns):
                    sx, sy = stones[k]
                    if buttonsToAnyPos[i][sx][sy] != -1 and buttonsToAnyPos[j][sx][sy] != -1:
                        if mn == -1 or mn > buttonsToAnyPos[i][sx][sy] + buttonsToAnyPos[j][sx][sy]:
                            mn = buttonsToAnyPos[i][sx][sy] + buttonsToAnyPos[j][sx][sy]
                # 距离是无向图，对称的
                dist[i][j] = mn
                dist[j][i] = mn
        
        # 若有任意一个机关 到起点或终点没有路径(即为-1),则说明无法达成，返回-1
        for i in range(nb):
            if dist[i][nb] == -1 or dist[i][nb+1] == -1:
                return -1
        
        # dp数组， -1代表没有遍历到, 1<<nb表示题解中提到的mask, dp[mask][j]表示当前处于第j个机关，总的触发状态为mask所需要的最短路径, 由于有2**nb个状态，因此1<<nb的开销必不可少
        dp = [[-1]*nb for _ in range(1 << nb)]
        # 初识状态，即从start到第i个机关，此时mask的第i位为1，其余位为0
        for i in range(nb):
            dp[1 << i][i] = dist[i][nb]
        
        # 二进制中数字大的mask的状态肯定比数字小的mask的状态多，所以直接从小到大遍历更新即可
        for mask in range(1, (1 << nb)):
            for i in range(nb):
                # 若当前位置是正确的，即mask的第i位是1
                if mask & (1 << i) != 0:
                    for j in range(nb):
                        # 选择下一个机关j,要使得机关j目前没有到达，即mask的第j位是0
                        if mask & (1 << j) == 0:
                            nextMask = mask | (1 << j)
                            if dp[nextMask][j] == -1 or dp[nextMask][j] > dp[mask][i] + dist[i][j]:
                                dp[nextMask][j] = dp[mask][i] + dist[i][j]

        # 最后一个机关到终点
        ans = -1
        finalMask = (1 << nb) - 1
        for i in range(nb):
            if ans == -1 or ans > dp[finalMask][i] + dist[i][nb + 1]:
                ans = dp[finalMask][i] + dist[i][nb + 1]
        return ans

作者：li-bo-8
链接：https://leetcode-cn.com/problems/xun-bao/solution/python3-bfsdpzhuang-tai-ya-suo-by-li-bo-8/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''