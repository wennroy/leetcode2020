# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 10:31:28 2020

@author: 53013
"""


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = 0
        while numBottles>=numExchange:
            k = numBottles//numExchange
            count += k * numExchange
            numBottles = k + numBottles%numExchange
        return count + numBottles