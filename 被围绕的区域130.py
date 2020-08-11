# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 10:15:36 2020

@author: 53013
"""
'''
该方法另外添加了一个list来存储已经改变过的变量，这样消耗了大量的时间
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board == [] or board == [[]]:
            return
        n = len(board)
        m = len(board[0])
        self.record = []
        def extend_board(x,y):
            if x < 0 or x > n-1 or y<0 or y>m-1:
                return
            if board[x][y] == 'O':
                if [x,y] in self.record:
                    return
                self.record.append([x,y])
                extend_board(x+1,y)
                extend_board(x,y+1)
                extend_board(x-1,y)
                extend_board(x,y-1)
            else:
                return
        for i in range(n):
            extend_board(i,0)
            extend_board(i,m-1)
        for j in range(m):
            extend_board(0,j)
            extend_board(n-1,j)
        for i in range(1,n-1):
            for j in range(1,m-1):
                if board[i][j] == 'O' and not [i,j] in self.record:
                    board[i][j] = 'X'