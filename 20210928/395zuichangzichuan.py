# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 20:08:20 2021

@author: WZYWXYWLY
"""

class Solution:
    def longestSubstring(self, s, k):
        if not s or k>len(s):
            return 0
        ans = 0
        from collections import defaultdict
        left, right = 0, len(s)-1
        frequency = defaultdict(int)
        for letter in s:
            frequency[letter] += 1

        while left + k-1 <= right:
            if frequency[s[left]] < k:
                frequency[s[left]] -= 1
                left += 1
            else:
                break
        while left + k-1 <= right:
            if frequency[s[right]] < k:
                frequency[s[right]] -= 1
                right -= 1
            else:
                break
        
        if self.checkstatus(frequency,k):
            ans = right-left +1
        else:
            for i in range(left, right+1):
                if frequency[s[i]] < k:
                    return max(self.longestSubstring(s[left: i],k), self.longestSubstring(s[i: (right+1)], k))
        if ans <k:
            return 0
        return ans
    
    def checkstatus(self, d, k):
        for key in d.keys():
            if d[key] > 0 and d[key] < k:
                return False
        return True

class Solution:
    def longestSubstring(self, s, k):
        if not s:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)
    

s = "aaabb"
k = 3

Solu = Solution()
print(Solution.longestSubstring(Solu, s, k))

