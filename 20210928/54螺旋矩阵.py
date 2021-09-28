# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 11:38:06 2021

@author: 53013
"""


class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        ans = []
        i,j = 0,-1
        while j < n-1:
            j += 1
            ans.append(matrix[i][j])
        while i < m-1:
            i += 1
            ans.append(matrix[i][j])
        if not m == 1:
            while j > 0:
                j -= 1
                ans.append(matrix[i][j])
        if not n==1:
            while i > 1:
                i -= 1
                print(i,j)
                ans.append(matrix[i][j])
        
        new_matrix =  []
        for row_in in range(1,m-1):
            new_matrix.append(matrix[row_in][1:n-1])
        
        if not new_matrix or not new_matrix[0]:
            return ans
        new_ans = self.spiralOrder(new_matrix)
        for kk in new_ans:
            ans.append(kk)
        return ans
    
    
    
kk = Solution()
matrix = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
print(kk.spiralOrder(matrix))