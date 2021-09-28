# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 08:52:31 2020

@author: 53013
"""

'''
class Solution:
    def smallestRange(self, nums):
        n = len(nums)
        maxlen = 0
        for k in range(n):
            templen = len(nums[k])
            if templen >maxlen:
                maxlen = templen
        
        pt = []
        [pt.append(0) for _ in range(n)]
        minrange = float("INF")
        maxpt = 0
        minpt = 0
        oldminpt = 3600
        minrangeindex = [0,0]
        def indexofMin():
            minindex = 0
            currentindex = 1
            while currentindex < n:
                if nums[currentindex][pt[currentindex]] < nums[minindex][pt[minindex]]:
                    minindex = currentindex
                currentindex += 1
            return minindex
        def indexofMax():
            maxindex = 0
            currentindex = 1
            while currentindex < n:
                if nums[currentindex][pt[currentindex]] > nums[maxindex][pt[maxindex]]:
                    maxindex = currentindex
                currentindex += 1
            return maxindex
        maxpt = indexofMax()
        
        while minrange != 0 and pt[minpt] < maxlen:
            print(minrangeindex)
            minpt = indexofMin()
            if minpt == oldminpt and oldpt == pt[minpt]:
                break
            temprange = nums[maxpt][pt[maxpt]] - nums[minpt][pt[minpt]]
            print(temprange)
            if temprange < minrange:
                minrange = temprange
                minrangeindex[0], minrangeindex[1] = nums[minpt][pt[minpt]], nums[maxpt][pt[maxpt]]
            oldpt = pt[minpt]
            if not pt[minpt] == len(nums[minpt])-1:
                pt[minpt] += 1
            oldminpt = minpt
            if nums[minpt][pt[minpt]] > nums[maxpt][pt[maxpt]]:
                maxpt = minpt
                
        return minrangeindex
'''     
    
    

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        import collections
        indices = collections.defaultdict(list)
        xMin, xMax = 10**9, -10**9
        for i, vec in enumerate(nums):
            for x in vec:
                indices[x].append(i)
            xMin = min(xMin, *vec)
            xMax = max(xMax, *vec)
        
        freq = [0] * n
        inside = 0
        left, right = xMin, xMin - 1
        bestLeft, bestRight = xMin, xMax

        while right < xMax:
            right += 1
            if right in indices:
                for x in indices[right]:
                    freq[x] += 1
                    if freq[x] == 1:
                        inside += 1
                while inside == n:
                    if right - left < bestRight - bestLeft:
                        bestLeft, bestRight = left, right
                    if left in indices:
                        for x in indices[left]:
                            freq[x] -= 1
                            if freq[x] == 0:
                                inside -= 1
                    left += 1

        return [bestLeft, bestRight]

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/smallest-range-covering-elements-from-k-lists/solution/zui-xiao-qu-jian-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        
'''
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        rangeLeft, rangeRight = -10**9, 10**9
        maxValue = max(vec[0] for vec in nums)
        priorityQueue = [(vec[0], i, 0) for i, vec in enumerate(nums)]
        heapq.heapify(priorityQueue)

        while True:
            minValue, row, idx = heapq.heappop(priorityQueue)
            if maxValue - minValue < rangeRight - rangeLeft:
                rangeLeft, rangeRight = minValue, maxValue
            if idx == len(nums[row]) - 1:
                break
            maxValue = max(maxValue, nums[row][idx + 1])
            heapq.heappush(priorityQueue, (nums[row][idx + 1], row, idx + 1))
        
        return [rangeLeft, rangeRight]

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/smallest-range-covering-elements-from-k-lists/solution/zui-xiao-qu-jian-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
'''
from collections import defaultdict
class Solution:
	def smallestRange(self,nums):
		size=len(nums)
		cnt=[0]*size #nums[i]所指示的列表中有多少个元素在当前双指针所划定的区域内
		rec=defaultdict(list) #各个数字分别存在于哪些子列表中
		for i,j in enumerate(nums):
			for k in j:
				rec[k].append(i)
		Nums=sorted(rec)
		le=n=0 #左指针 当前的双指针所划定的区域内有多少个子列表是有元素存在着的
		ansL=ansB=int(1e9) #最终结果两数之差 最终结果中较大的数字
		for riVal in Nums:
			for i in rec[riVal]:
				cnt[i]+=1
				if cnt[i]==1:
					n+=1
			while n==size:
				v=Nums[le]
				if riVal-v<ansL:
					ansL,ansB=riVal-v,riVal
				for i in rec[v]:
					cnt[i]-=1
					if cnt[i]==0:
						n-=1
						break
				le+=1
		return [ansB-ansL,ansB]
'''
nums = [[-5,-4,-3,-2,-1],[1,2,3,4,5]] 
nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]

print(Solution.smallestRange(None, nums))