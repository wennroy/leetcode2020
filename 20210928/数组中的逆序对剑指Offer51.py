# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 13:49:35 2020

@author: 53013
"""
# from math import *
# class Solution:
#     def reversePairs(self, nums):
#         def mergesort(self, nums):
#             n = len(nums)
#             if n==1:
#                 return nums
#             mid = floor(n/2)
#             L = mergesort(self, nums[:mid])
#             R = mergesort(self, nums[mid:])
#             lpt = 0
#             rpt = 0
#             M = []
#             while lpt <= mid-1 and rpt <= (n-mid-1) :
#                 if L[lpt] < R[rpt]:
#                     self.ans += rpt+ 1
#                     M.append(L[lpt])
#                     lpt += 1
#                 else:
#                     M.append(R[rpt])
#                     rpt += 1
#             print(L,R,self.ans)
#             if lpt > mid-1:
#                 while rpt <= n-mid-1:
#                     M.append(R[rpt])
#                     self.ans += rpt + 1
#                     rpt +=1
#             else:
#                 while lpt <= mid -1:
#                     M.append(L[lpt])
#                     lpt += 1
#             return M
#         self.ans = 0
#         print(mergesort(self,nums))
#         return self.ans

class Solution:
    def mergeSort(self, nums, tmp, l, r):
        if l >= r:
            return 0

        mid = (l + r) // 2
        inv_count = self.mergeSort(nums, tmp, l, mid) + self.mergeSort(nums, tmp, mid + 1, r)
        i, j, pos = l, mid + 1, l
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                tmp[pos] = nums[i]
                i += 1
                inv_count += (j - (mid + 1))
            else:
                tmp[pos] = nums[j]
                j += 1
            pos += 1
        for k in range(i, mid + 1):
            tmp[pos] = nums[k]
            inv_count += (j - (mid + 1))
            pos += 1
        for k in range(j, r + 1):
            tmp[pos] = nums[k]
            pos += 1
        nums[l:r+1] = tmp[l:r+1]
        return inv_count

    def reversePairs(self, nums):
        n = len(nums)
        tmp = [0] * n
        return self.mergeSort(nums, tmp, 0, n - 1)

        
num = [7, 5, 6, 4]
ans = Solution()
print(Solution.reversePairs(ans, num))
