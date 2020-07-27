# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 09:21:15 2020

@author: lengwaifang
"""


class Solution:
    def divisorGame(self, N: int) -> bool:
        # if N % 2 == 0:
        #     return True
        # else:return False
        return N%2==0


#2.
        # if N == 2:
        #     return True
        # elif N==3 or N == 1:
        #     return False
        
        # for i in range(1,round(N/2)+1):
        #     if not N % i == 0:
        #         continue
        #     if not Solution.divisorGame(None, N-i):
        #         return True
        # return False
        
#3. 
#         dct = {}

#         def dfs(N: int) -> bool:
#             if N == 1:
#                 return False
#             if N in dct:
#                 return dct[N]
#             dct[N] = any(not dfs(N-i) for i in range(1, N//2+1) if N%i == 0)
#             return dct[N]

#         return dfs(N)

                