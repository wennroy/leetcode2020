# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 09:22:20 2020

@author: 53013
"""

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        i = 0
        count1 = 1
        count2 = 0
        ans = 0
        while i < len(s)-1:
            if s[i] == s[i+1]:
                count1 += 1
            else:
                if count2>count1:
                    ans += count1
                count2 = count1
                count1 = 1
            if count1 == count2:
                ans += count1
            i += 1
        if count2>count1:
            ans += count1
        return ans

'''
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        pre, cur, res, prec = 0, 1, 0, s[0]
        for c in s[1:]:
            if c != prec: pre, cur = cur, 1
            else: cur += 1
            if cur <= pre: res += 1
            prec = c
        return res

作者：kknike
链接：https://leetcode-cn.com/problems/count-binary-substrings/solution/ti-sheng-su-du-xiao-tie-shi-by-kknike/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
s = "10101"
print(Solution.countBinarySubstrings(None, s))