# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 09:38:27 2020

@author: 53013
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        ans = 0
        def caltwo(self, a, num):
            ans = 0
            n = len(num)
            a = int(a)
            for i in range(n-1,-1,-1):
                ans += 10 ** (n-1-i)*(int(num[i]))*a
            return ans
        
        for i in range(n1-1,-1,-1):
            ans += caltwo(self, num1[i],num2) * 10**(n1-1-i)
        return str(ans)

    
num1 = '123'
num2 = '456'
print(Solution.multiply(None, num1, num2))