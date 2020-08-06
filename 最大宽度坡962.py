# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 10:56:48 2020

@author: 53013
"""


class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        '''
        maxlen = 0
        for i in range(len(A)-1):
            if i >= len(A) - 1-maxlen:
                continue
            for j in range(i,len(A)):
                if j-i<=maxlen:
                    continue
                if A[i]<=A[j] and maxlen<j-i:
                    maxlen = j-i
        return maxlen
        '''
        ans = 0
        m = float('inf')
        for i in sorted(range(len(A)), key = A.__getitem__):
            ans = max(ans, i - m)
            m = min(m, i)
        return ans
    
'''
class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        stack = []
        n = len(A)
        for i in range(n):
            if not stack or A[stack[-1]] > A[i]:
                stack.append(i)

        res = 0
        i = n - 1
        while i > res:  # 当res大于等于i时没必要继续遍历了 
            while stack and A[stack[-1]] <= A[i]:
                res = max(res, i - stack[-1])
                stack.pop()
            i -= 1

        return res

作者：Elmer
链接：https://leetcode-cn.com/problems/maximum-width-ramp/solution/dan-diao-zhan-python-yi-kan-jiu-dong-by-elmer/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
O(n) O(n)
'''