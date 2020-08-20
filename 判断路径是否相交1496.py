# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 15:44:06 2020

@author: 53013
"""


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        record = [(0,0)]
        i = j = 0
        for s in path:
            if s == 'N':
                j += 1
            elif s == 'S':
                j-=1
            elif s == 'E':
                i +=1
            else:
                i -=1
            cur = (i,j)
            if cur in record:
                return True
            else:
                record.append(cur)
        return False

path = 'N'*2500+ 'E'*2500 + 'S'*2000 + 'W'*2500
import time
start_time = time.time()
print(Solution.isPathCrossing(None, path))
print('经过了%ss'%(time.time() - start_time))