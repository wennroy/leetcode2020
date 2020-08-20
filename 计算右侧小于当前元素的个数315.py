# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 14:33:22 2020

@author: 53013
"""


class Solution:
    def countSmaller(self, nums):
        # from collections import defaultdict
        # self.record = defaultdict(int)
        # counts = []
        # for i in nums[::-1]:
        #     count = 0
        #     for k in self.record.keys():
        #         if k < i:
        #             count += self.record[k]
        #     counts.append(count)
        #     self.record[i]+=1
        # return counts[::-1]
        
        n = len(nums)
        self.index = list(range(n))
        self.inv_count = [0]*n
        self.tmp = [0]*n
        self.nums = nums
        l, r = 0, n-1

        def mergeSort(self,l,r):
            if l>= r:
                return 
            mid = (l+ r) // 2

            mergeSort(self,l,mid)
            mergeSort(self,mid + 1, r)
            i, j, pos = l, mid + 1, l
            index = [0]*n
            while i <= mid and j<= r:
                if nums[i]<= self.nums[j]:
                    self.tmp[pos] = self.nums[i]
                    index[pos] = self.index[i]
                    i += 1
                    self.inv_count[index[pos]] += (j - (mid + 1))
                else:
                    self.tmp[pos] = self.nums[j]
                    index[pos] = self.index[j]
                    j += 1
                pos += 1
            for k in range(i,mid + 1):
                self.tmp[pos] = nums[k]
                index[pos] = self.index[k]
                self.inv_count[index[pos]] += j - (mid + 1)
                pos += 1
            for k in range(j, r + 1):
                self.tmp[pos] = nums[k]
                index[pos] = self.index[k]
                pos += 1
            self.nums[l:r+1] = self.tmp[l:r+1]
            self.index[l:r+1] = index[l:r+1]
            return

        mergeSort(self,0,n-1)
        return self.inv_count
        
        '''
        if not nums: return []
        
        sorted_nums = []
        ans = []
        for n in nums[::-1]:
            index = bisect.bisect_left(sorted_nums,n)
            bisect.insort(sorted_nums,n)
            ans.append(index)
        return ans[::-1]
        '''
    
nums = list(range(10000,-1,-1))
r = Solution()
import time
start_time = time.time()
print(Solution.countSmaller(r, nums))
print('经过了%ss'%(time.time() - start_time))