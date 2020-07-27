# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 17:39:15 2020

@author: 53013
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/is-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ## 滑动窗口
        if s == '':
            return True
        for i in range(len(t)):
            if s[0] == t[i]:
                print(s,t)
                return Solution.isSubsequence(None, s[1:],t[i+1:])
        return False
    

s = "abc"
t = "ahbgdc"

print(Solution.isSubsequence(None, s, t))