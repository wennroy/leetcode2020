# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 16:14:24 2020

@author: 53013
"""


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:

        # 执行用时：568 ms, 在所有 Python3 提交中击败了8.78%的用户
        # 内存消耗：14.1 MB, 在所有 Python3 提交中击败了100.00%的用户
        # 执行时间血亏
        k = [a,b,c]
        k.sort()
        self.record = {}
        def nummoves(self,x,y,z):
            if (x,y,z) in self.record.keys():
                return self.record[(x,y,z)]
            final_min = float('INF')
            final_max = 0
            if x  == y -1 and y == z-1:
                return [0,0]
            if x  == y +1 and y == z+1:
                return [0,0]
            for k in range(x + 1,z):
                if k==y:
                    continue
                elif k < y:
                    xminnum,xmaxnum = nummoves(self,k,y,z)
                    zminnum,zmaxnum = nummoves(self,x,k,y)
                else:
                    xminnum,xmaxnum = nummoves(self,y,k,z)
                    zminnum,zmaxnum = nummoves(self,x,y,k)
                # print(xmaxnum,zminnum,x,y,z,k)
                minnum = min(xminnum,zminnum)
                maxnum = max(xmaxnum,zmaxnum)
                if final_min > minnum:
                    final_min = minnum
                if final_max <maxnum:
                    final_max = maxnum
            final_max += 1
            final_min += 1
            # print(final_max,final_min,self.record)
            self.record[(x,y,z)] = [final_min, final_max]
            return [final_min, final_max]
        return nummoves(self,k[0],k[1],k[2])


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        tmp = [a,b,c] # 先对xyz赋值
        tmp.sort()
        x,y,z = tmp[0],tmp[1],tmp[2]
        if x + 1 == y and y + 1 == z: # a,b,c连续
            return [0,0]
        else:
            if y-x == 2 or z-y == 2 or (x+1 == y or y + 1 == z):  # 中间隔一个或者有两个挨着
                minimum_moves = 1
            else:
                minimum_moves = 2
            maximum_moves = (y-x)+(z-y)-2
        return [minimum_moves,maximum_moves]
'''
作者：z1m
链接：https://leetcode-cn.com/problems/moving-stones-until-consecutive/solution/python3-yi-dong-shi-zi-by-ml-zimingmeng/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''