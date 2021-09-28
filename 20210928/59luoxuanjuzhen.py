# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 21:41:43 2021

@author: 53013
"""


class Solution:
    def generateMatrix(self, n):
        import copy
        ans, cur_ans = [], []
        for _ in range(n):
            cur_ans.append(0)
        for _ in range(n):
            ans.append(copy.copy(cur_ans))

        i, j = 0, 0
        r,l,u,d = 1,0,0,0
        cur_num = n**2
        count = 0
        while cur_num > 0 and count <=20:
            count+=1
            print(i,j)
            while i>=0 and j>=0 and i<=n-1 and j<=n-1 and ans[i][j] == 0:
                ans[i][j] = cur_num
                cur_num -= 1
                i += u+d
                j += l+r
            if r == 1:
                r,l,u,d = 0,0,0,1
                j -= 1
                i += 1
            elif l == -1:
                r,l,u,d = 0,0,-1,0
                j += 1
                i -= 1
            elif d == 1:
                r,l,u,d = 0,-1,0,0
                j -= 1
                i -= 1
            else:
                r,l,u,d = 1,0,0,0
                j += 1
                i += 1
        return ans
    
kk = Solution()
n = 3
print(kk.generateMatrix(n))