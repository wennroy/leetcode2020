# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:35:48 2020
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。
@author: 53013
"""


s = "ADOBECODEBANC"
t = "ABC"
s = 'ab'
t = 'A'
s = "cabwefgewcwaefgcf"
t = "cae"
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        if not s or not t:
            return ''
        ns = len(s)
        nt = len(t)
        l = 0
        r = nt - 1
        dict_t = defaultdict(int)
        for letter in t:
            dict_t[letter] += 1
        temp_dict = dict_t.copy()
        for letter in s[l:r+1]:
            if letter in dict_t.keys():
                temp_dict[letter] -= 1
        if set(temp_dict.values()) == {0}:
            return s[l:r+1]
        minlen = float("INF")
        mins = ''
        # 开始滑动
        def tins():
            for count in set(temp_dict.values()):
                if count > 0:
                    return False
            return True
        while True:
            print(l,r)
            if r < ns-1:
                r += 1
            elif not tins():
                break
            if s[r] in dict_t.keys():
                temp_dict[s[r]] -= 1
            while tins():
                curlen = r - l + 1
                if curlen < minlen:
                    mins = s[l:r+1]
                    minlen = curlen

                if s[l] in dict_t.keys():
                    temp_dict[s[l]] += 1
                l += 1
            
        return mins
    
print(Solution.minWindow(None, s,t))
                

'''
    def minWindow(self, s: str, t: str) -> str:
        need=collections.defaultdict(int)
        for c in t:
            need[c]+=1
        needCnt=len(t)
        i=0
        res=(0,float('inf'))
        for j,c in enumerate(s):
            if need[c]>0:
                needCnt-=1
            need[c]-=1
            if needCnt==0:       #步骤一：滑动窗口包含了所有T元素
                while True:      #步骤二：增加i，排除多余元素
                    c=s[i] 
                    if need[c]==0:
                        break
                    need[c]+=1
                    i+=1
                if j-i<res[1]-res[0]:   #记录结果
                    res=(i,j)
                need[s[i]]+=1  #步骤三：i增加一个位置，寻找新的满足条件滑动窗口
                needCnt+=1
                i+=1
        return '' if res[1]>len(s) else s[res[0]:res[1]+1]    #如果res始终没被更新过，代表无满足条件的结果

作者：Mcdull0921
链接：https://leetcode-cn.com/problems/minimum-window-substring/solution/tong-su-qie-xiang-xi-de-miao-shu-hua-dong-chuang-k/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''