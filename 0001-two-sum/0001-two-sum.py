class Solution:
    def twoSum(self, nums, target):
        hashmap = {}

        for idx, val in enumerate(nums):
            difference = target - val
            if difference in hashmap:
                return [hashmap[difference], idx]
            else:
                hashmap[val] = idx