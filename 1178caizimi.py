# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 11:32:50 2021

@author: WZYWXYWLY
"""
import collections
class Solution:

    def findNumOfValidWords(self, words, puzzles):
        answer = []
        [answer.append(0) for _ in range(len(puzzles))]
        for i in range(len(puzzles)):
            puzzle = puzzles[i]
            first_letter = puzzle[0]
            for word in words:
                if not first_letter in word:
                    continue
                indicator = 0
                for j in range(len(word)):
                    letter = word[j]
                    if not letter in puzzle:
                        indicator = 1
                        break

                if indicator == 0:
                    answer[i] += 1
        return answer


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        frequency = collections.Counter()

        for word in words:
            mask = 0
            for ch in word:
                mask |= (1 << (ord(ch) - ord("a")))
            if str(bin(mask)).count("1") <= 7:
                frequency[mask] += 1

        ans = list()
        for puzzle in puzzles:
            total = 0

            # 枚举子集方法一
            # for choose in range(1 << 6):
            #     mask = 0
            #     for i in range(6):
            #         if choose & (1 << i):
            #             mask |= (1 << (ord(puzzle[i + 1]) - ord("a")))
            #     mask |= (1 << (ord(puzzle[0]) - ord("a")))
            #     if mask in frequency:
            #         total += frequency[mask]

            # 枚举子集方法二
            mask = 0
            for i in range(1, 7):
                mask |= (1 << (ord(puzzle[i]) - ord("a")))

            subset = mask
            while subset:
                s = subset | (1 << (ord(puzzle[0]) - ord("a")))
                if s in frequency:
                    total += frequency[s]
                subset = (subset - 1) & mask

            # 在枚举子集的过程中，要么会漏掉全集 mask，要么会漏掉空集
            # 这里会漏掉空集，因此需要额外判断空集
            if (1 << (ord(puzzle[0]) - ord("a"))) in frequency:
                total += frequency[1 << (ord(puzzle[0]) - ord("a"))]

            ans.append(total)

        return ans

'''
作者：LeetCode - Solution
链接：https: // leetcode - cn.com / problems / number - of - valid - words -
for -each - puzzle / solution / cai - zi - mi - by - leetcode - solution - 345u /
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

words = ["aaaa","asas","able","ability","actt","actor","access"]
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]

kk = Solution()
print(Solution.findNumOfValidWords(kk, words, puzzles))
