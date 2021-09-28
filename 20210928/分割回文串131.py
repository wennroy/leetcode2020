# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:19:39 2020

@author: 53013
"""

'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isparlindrome(self, s):
            n = len(s)
            if n % 2 ==0:
                for i in range(n/2):
                    if not s[i] == s[n-i-1]:
                        return False
            else:
                for i in range((n+1)/2):
                    if not s[i] == s[n-i-1]:
                        return False
            return True

        if len(s) == 1:
            return [[s]]
        elif len(s) == 2:
            if s[0] == s[1]:
                return [
                    [s[0],s[1]],
                    [s]
                ]
            else: return [[s]]
        else:
            if isparlindrome(None, s):
                n = len(s)
                temp = []
                for i in range(round(n/2)):
                    temp_list = []
                    for k in range(i):
                        temp_list.append(s[k])
                    if i == 0:
                        k = -1
                    temp_list.append(s[k+1:n-k-1])
                    if not k == -1:
                        [temp_list.append(_) for _ in temp_list[k::-1]]
                    temp.append(temp_list)
'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        if len(s) == 1:
            return [[s]]
        ret = []
        for i in range(1, len(s)+1):
            if s[:i][::-1] == s[:i]:
                ret += [[s[:i]]+j for j in self.partition(s[i:])]
        return ret
