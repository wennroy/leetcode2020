# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 15:37:53 2021

@author: WZYWXYWLY
"""


class Solution:
    def flipAndInvertImage(self, A):
        if not A or not A[0]:
            return [[]]
        n = len(A[0])
        for j in range(len(A)):
            for i in range(int(n/2)):
                if not A[j][i] == A[j][-i-1]:
                    temp = A[j][i]
                    A[j][i] = A[j][-i-1]
                    A[j][-i-1] = temp
                print(A[j])
                A[j][i] = Solution.invertImage(self,A[j][i])
                A[j][-i-1] = Solution.invertImage(self,A[j][-i-1])
                print(A[j])
            if not n % 2 ==0:
                A[j][i+1] = Solution.invertImage(self,A[j][i+1])
            
        return A
    def invertImage(self, num):
        if num == 1:
            return 0
        else:
            return 1
        
        
        


A = [[1,1,0],[1,0,1],[0,0,0]]
print(Solution.flipAndInvertImage(None,A))

'''
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        n = len(A)
        for i in range(n):
            left, right = 0, n - 1
            while left < right:
                if A[i][left] == A[i][right]:
                    A[i][left] ^= 1
                    A[i][right] ^= 1
                left += 1
                right -= 1
            if left == right:
                A[i][left] ^= 1
        return A

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/flipping-an-image/solution/fan-zhuan-tu-xiang-by-leetcode-solution-yljd/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''