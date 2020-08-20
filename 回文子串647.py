# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:03:53 2020

@author: 53013
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        count = 1

        def findoddpalindrome(s, mid):
            left = mid
            right = mid
            while left >= 0 and right <= n-1:
                if not s[left] == s[right]:
                    break
                left -= 1 
                right += 1
            return mid - left

        def findevenpalindrome(s ,mid):
            left = mid - 1
            right = mid
            if not s[left] == s[right]:
                return 0
            while left >= 0 and right <= n-1:
                if not s[left] == s[right]:
                    break
                left -= 1 
                right += 1
            return mid - left - 1

        for i in range(1,n):
            print(count)
            count += findoddpalindrome(s, i)
            count += findevenpalindrome(s ,i)
        return count

# class Solution:
#     def countSubstrings(self, S):
#         N = len(S)
#         ans = 0
#         for center in range(2*N - 1):
#             left = center // 2
#             right = left + center % 2
#             while left >= 0 and right < N and S[left] == S[right]:
#                 ans += 1
#                 left -= 1
#                 right += 1
#         return ans

# class Solution:
#     def countSubstrings(self, S):
#         def manachers(S):
#             A = '@#' + '#'.join(S) + '#$'
#             Z = [0] * len(A)
#             center = right = 0
#             for i in range(1, len(A) - 1):
#                 if i < right:
#                     Z[i] = min(right - i, Z[2 * center - i])
#                 while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
#                     Z[i] += 1
#                 if i + Z[i] > right:
#                     center, right = i, i + Z[i]
#             return Z

#         return sum((v+1) // 2 for v in manachers(S))


import time
s = 'abc'
start = time.time()
print(Solution.countSubstrings(None, s))
print('过去了%s秒'%(time.time()-start))
