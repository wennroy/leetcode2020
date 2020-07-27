class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None


    nums = [1,2,3,4,5,6,2,5,3,5,7,8,9,5,6,6,2,13,4,5,3,684,6,5,8,79,6,2,35,46,5]
    target=16

    print(twoSum([],nums,target))
