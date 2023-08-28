class Solution:
    def twoSum(self, nums, target):
        origin = {}
        
        for idx, val in enumerate(nums):
            if val in origin:
                origin[val].append(idx)
            else:
                origin[val] = [idx]
        print(origin)
            
        nums.sort()
        
        left, right = 0, len(nums)-1
        
        while left < right:
            if (nums[left] + nums[right]) < target:
                left += 1
            elif (nums[left] + nums[right]) > target:
                right -= 1
            else:
                return [origin[nums[left]][0], origin[nums[right]][-1]]