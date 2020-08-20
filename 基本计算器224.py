# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 16:52:54 2020

@author: 53013
"""


class Solution:
    def calculate(self, s: str) -> int:
        def calorder(stack):
            while len(stack) != 1:
                print(stack)
                cur = stack.pop(0)
                cur2 = stack.pop(0)
                if cur2 == '+':
                    stack.insert(0,str(int(cur) + int(stack.pop(0))))
                elif cur2 == '-':
                    stack.insert(0,str(int(cur) - int(stack.pop(0))))
            return stack
        index = [-1]
        stack = []
        n = len(s)
        ans = 0
        i = -1
        while i < len(s)-1:
            i += 1
            a = s[i]
            print(stack)
            if a == ' ':
                continue
            
            if a == '(':
                stack.append('(')
                index.append(len(stack)-1)
            elif a == '+':
                stack.append('+')
            elif a == '-':
                stack.append('-')
            elif a == ')':
                index.pop()
                cur = stack.pop()
                cur2 = stack.pop()
                while  cur2 != '(':
                    if cur2 == '+':
                        stack.append(str(int(stack.pop()) + int(cur)))
                    elif cur2 == '-':
                        stack.append(str(int(stack.pop()) - int(cur)))
                    cur = stack.pop()
                    cur2 = stack.pop()
                stack.append(cur)
                print(index)
                stack = stack[:index[-1]+1] + calorder(stack[index[-1]+1:])
            else:
                while i < n-1 and s[i+1] in ['0','1','2','3','4','5','6','7','8','9']:
                    a += s[i+1]
                    i += 1
                if stack==[]:
                    stack.append(a)
                    continue
                cur = stack.pop()
                if cur =='(':
                    stack.append('(')
                    stack.append(a)
                    continue

                if cur == '+':
                    cur = stack.pop()
                    stack.append(str(int(cur) + int(a)))
                    continue
                if cur == '-':
                    cur = stack.pop()
                    stack.append(str(int(cur) - int(a)))
                    continue
        # print(stack)
        # stack = calorder(stack)
        
        return int(stack.pop())

s = "(1+(4+5+2)-3)+(6+80)"
s = "(7)-(0)+(4)"
s = "2-4-(8+2-6+(8+4-(1)+8-10))"
import time
start_time = time.time()
print(Solution.calculate(None, s))
print('经过了%ss'%(time.time() - start_time))