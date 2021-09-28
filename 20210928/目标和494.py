# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 17:47:22 2020

@author: 53013
"""


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.record = {}
        nums_tu = tuple(nums)
        def findsum(self, nums_tu, S):
            if (nums_tu,S) in self.record.keys():
                return self.record[nums_tu,S]
            else:
                if len(nums_tu) == 1:
                    if S == 0 and nums_tu[0] == 0:
                        return 2
                    elif abs(S) == abs(nums_tu[0]):
                        return 1
                    else:
                        return 0
                self.record[nums_tu,S] = findsum(self, nums_tu[1:], S-nums_tu[0]) + findsum(self, nums_tu[1:], S+nums_tu[0])
                return self.record[nums_tu,S]
        return findsum(self, nums_tu, S)