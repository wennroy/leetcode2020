class Solution:
    def twoSum(self, nums, target):
        for x in range(len(nums)):
            for y in range(len(nums)):
                if x==y:
                    continue
                if nums[x]+nums[y]==target:
                    return [x,y]
        return None

    print(twoSum([],[3,3],6))