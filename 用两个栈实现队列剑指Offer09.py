class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if self.stack2 == []:
            if self.stack1 == []:
                return -1
            else:
                while not self.stack1 == []:
                    self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 10:28:16 2020

@author: 53013
"""


