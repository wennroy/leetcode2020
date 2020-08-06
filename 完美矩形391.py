# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 16:38:16 2020

@author: 53013
"""


class Solution:
    def isRectangleCover(self, rectangles):
        import numpy as np
        n = np.max(rectangles)+1
        used = []
        [used.append([0]*n) for _ in range(n)]
        minx, miny = n-1,n-1
        maxx, maxy = 0,0
        for rec in rectangles:
            x1,y1,x2,y2 = rec[0],rec[1],rec[2],rec[3]
            if x1 > x2:
                temp = x2
                x2 = x1
                x1 = temp
            if y1>y2:
                temp = y1
                y2 = y1
                y1 = temp
            if x1 < minx:
                minx = x1
            if x2 > maxx:
                maxx = x2
            if y1 < miny:
                miny = y1
            if y2 > maxy:
                maxy = y2
            print(x1,y1,x2,y2)
            for x in range(x1,x2+1):
                for y in range(y1,y2+1):
                    if x==x1 or y==y2 or x==x2 or y==y1:
                        used[x][y] += .5
                        continue
                    used[x][y] += 1
                    
        for k in used:
            print(k)
        print('\n')
        val = used[minx][miny] * 2
        for x in range(minx,maxx+1):
            for y in range(miny,maxy+1):
                if x == minx or x== maxx or y==miny or y == maxy:
                    if used[x][y] != val/2:
                        return False
                elif used[x][y] != val:
                    return False

        return True
rec = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]
'''
rec = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]
rec =  [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]
'''
print(Solution.isRectangleCover(None, rec))