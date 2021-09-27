# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 16:12:04 2021

@author: WZYWXYWLY
"""
import copy

class Solution:
    def subsets(self, nums):
        res = []
        if not nums:
            return [[]]
        last = Solution.subsets(self, nums[1:])
        res += last
        print(res)
        res_copy = copy.deepcopy(last)
        for word in res_copy:
            word.append(nums[0])
            res += [word]
            print(res)
        return res
    
nums = [1,2,3]
kk = Solution()
print(Solution.subsets(kk, nums))


'''
class Solution:
    def subsets(self, nums):
        res = [[]]
        for i in nums:
            print(res)
            res = res + [[i] + num for num in res]
        return res

作者：powcai
链接：https://leetcode-cn.com/problems/subsets/solution/hui-su-suan-fa-by-powcai-5/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''