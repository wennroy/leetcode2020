class Solution:
    def longestSubstring(self, s, k):
        # dict1 = {}
        # for index,x in enumerate(s):
        #     if dict1.__contains__(x):
        #         dict1[x].append(index)
        #         dict1[x].sort()
        #     else:
        #         dict1[x] = [index]
        # shortest = float('inf')
        # wordposstart = 0
        # wordposend = 0
        # print(dict1)
        # for x in dict1.keys():
        #     if len(dict1[x])>=k:
        #         for l in range(len(dict1[x])-k+1):
        #             interval = dict1[x][l+k-1]-dict1[x][l]
        #             if interval < shortest:
        #                 shortest = interval
        #                 wordposstart = dict1[x][l]
        #                 wordposend = dict1[x][l+k-1]
        #                 print(wordposstart)
        #                 print(wordposend)
        #
        # if shortest == float('inf'):
        #     return None
        # else:
        #     sho = s[wordposstart:wordposend]
        #     return sho

    #     if k == 1:
    #         gstartp = 0
    #         gendp = len(s)-1
    #     else:
    #         ginterval = 0
    #         for i in range(len(s)):
    #             dict1 = {}
    #             interval = 0
    #             for j in range(len(s[i+1:])+1):
    #                 ins = 0
    #                 index = j+i
    #                 if dict1.__contains__(s[index]):
    #                     dict1[s[index]].append(index)
    #                 else:
    #                     dict1[s[index]] = [index]
    #                 for l in dict1.keys():
    #                     if len(dict1[l]) < k:
    #                         ins = 1
    #                 print(dict1)
    #                 if ins == 0:
    #                     startp = i
    #                     endp = index
    #                     interval = j
    #             if interval > ginterval:
    #                 gstartp = startp
    #                 gendp = endp
    #                 ginterval = interval
    #         if ginterval == 0:
    #             return None
    #     anss = s[gstartp:gendp+1]
    #     ans = '最长子串为' + anss + '，其中 '
    #     ansdict = {}
    #     for index1,x in enumerate(anss):
    #         if ansdict.__contains__(x):
    #             ansdict[x].append(index1)
    #         else:
    #             ansdict[x] = [index1]
    #     for x in ansdict.keys():
    #         num = len(ansdict[x])
    #         ans = ans + x + '重复了' + str(num) + '次，'
    #     ans = ''.join(list(ans[:-1])) + '。'
    #     return ans
    #

        # def longestSubstring(self, s, k):
        #     if len(s) < k:
        #         return 0
        #     # 获取出现次数最少的字符
        #     c = min(set(s), key=s.count)
        #     if s.count(c) >= k:
        #         return len(s)
        #     return max(self.longestSubstring(t, k) for t in s.split(c))

        if not s:
            return 0
        for c in set(s):
            if s.count(c) < k:
                print(s.split(c))
                return max(self.longestSubstring([],t, k) for t in s.split(c))
        return len(s)
    s = "abaabcddfe"
    k = 2
    a = longestSubstring([],s,k)
    print(a)
