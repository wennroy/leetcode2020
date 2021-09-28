# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 17:20:51 2020

@author: wennroy
"""


class Solution:
    def originalDigits(self, s: str) -> str:
        ## 构建我们所需要的数字
        letter = {  'w':0,
                    'u':0,
                    'x':0,
                    'g':0,
                    's':0,
                    'v':0,
                    'i':0,
                    'r':0,
                    'n':0,
                    'z':0}
        ## O(n)时间复杂度
        for i in range(len(s)):
            if s[i] in letter:
                letter[s[i]] += 1
        zero = letter['z']
        six = letter['x']
        two = letter['w']
        four = letter['u']
        eight = letter['g']
        seven = letter['s'] - six
        five = letter['v'] - seven
        three = letter['r'] - four - zero
        nine = letter['i'] - eight-five - six
        one = letter['n'] - seven - nine*2
        return zero*'0'+one*'1'+two*'2'+three*'3'+four*'4'+five*'5'+six*'6'+seven*'7'+eight*'8'+nine*'9'