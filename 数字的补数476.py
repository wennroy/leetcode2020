# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:04:53 2020

@author: wennroy
"""

'''
给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。

输入: 5
输出: 2
解释: 5 的二进制表示为 101（没有前导零位），其补数为 010。所以你需要输出 2 。
'''
class Solution:
    def findComplement(self, num: int) -> int:
        ## 先寻找 n
        if num ==0:
            return 1
        N = 1
        x = 0
        while N <= num:
            N *= 2
        print(N)
        while N>1:
            N /= 2
            x += N * (-(num//N) + 1)
            print(num,N,x,num//N)
            num -= N * (num//N)
        return x

x = 128
print(Solution.findComplement(None, x))