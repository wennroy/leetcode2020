# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 12:30:25 2020

@author: wennroy
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
"""
class Solution:
    def integerBreak(self, n: int) -> int:
        self.record = {}
        def twointeger(self,a,b):
            ## 保证a>=b
            if a<b:
                temp = b
                b = a
                a = temp
            if (a,b) in self.record.keys():
                return self.record[(a,b)]
            if a == 1 and b == 1:
                return 1
            maxmul = 0
            for k in range(1,a):
                next_val = (a - k)*twointeger(self,k,b)
                if next_val > maxmul:
                    maxmul = next_val
            single = a*b
            if maxmul < single:
                maxmul = single
            self.record[(a,b)] = maxmul
            return maxmul
        max_val = 0
        for l in range(1,n):
            now_val = twointeger(self,l,n-l)
            if now_val > max_val:
                max_val = now_val
        return max_val
    
'''

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]

'''