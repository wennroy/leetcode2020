class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        dict1 = {}
        for index,x in enumerate(nums):
            dict1[x]=index


        # 解法一
        # from itertools import combinations as com
        # dic, l = collections.defaultdict(list), [*com(range(len(nums)), 2)]
        # for a, b in l: dic[target - nums[a] - nums[b]].append((a, b))
        # r = [(*ab, c, d) for c, d in l for ab in dic[nums[c] + nums[d]]]
        # return [*set(tuple(sorted(nums[i] for i in t)) for t in r if len(set(t)) == 4)]
a
        # 解法二
        # nums.sort()
        # ans = set()
        #
        # for i in range(len(nums) - 3):
        #     for j in range(i + 1, len(nums) - 2):  # 固定两个数
        #         left = j + 1  # 左指针
        #         right = len(nums) - 1  # 右指针
        #         while (right > left):
        #             temp = nums[i] + nums[j] + nums[left] + nums[right]
        #             if temp == target:
        #                 ans.add((nums[i], nums[j], nums[left], nums[right]))
        #                 left += 1
        #                 right -= 1
        #             if temp > target: right -= 1  # 太大了，右指针左移
        #             if temp < target: left += 1  # 反之
        # # 去重
        # rec = []
        # for i in ans:
        #     rec.append(list(i))
        # return rec

    nums=[1,0,-1,0,-2,-2]
    target=0
    print(fourSum([],nums,target))