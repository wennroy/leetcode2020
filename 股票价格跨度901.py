# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 09:45:46 2020

@author: wennroy
编写一个 StockSpanner 类，它收集某些股票的每日报价，并返回该股票当日价格的跨度。

今天股票价格的跨度被定义为股票价格小于或等于今天价格的最大连续日数（从今天开始往回数，包括今天）。

例如，如果未来7天股票的价格是 [100, 80, 60, 70, 60, 75, 85]，那么股票跨度将是 [1, 1, 1, 2, 1, 4, 6]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/online-stock-span
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class StockSpanner:
    '''
    暴力解答，超时
    def __init__(self):
        self.stack = []
    def next(self, price: int) -> int:
        self.stack.append(price)
        n = len(self.stack)
        for i in range(n-2,-1,-1):
            if self.stack[i]>price:
                return n-1-i
        return n
    '''
    def __init__(self):
        self.stack = []
        self.record = []
    def next(self, price: int) -> int:
        self.stack.append(price)
        n = len(self.stack)
        i = n-2
        count = 1
        while i >= 0 :
            if self.stack[i]<=price:
                count += self.record[i]
                i -= self.record[i]
            else: break
        self.record.append(count)
        return count
'''
class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        weight = 1
        while self.stack and self.stack[-1][0] <= price:
            weight += self.stack.pop()[1]
        self.stack.append((price,weight))
        return weight
'''
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)