class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        nums_dict = {x:0 for x in nums}

        for num in nums_dict:
            if num - 1 not in nums_dict:
                nums_dict[num] += 1
                next = num + 1
                while next in nums_dict:
                    next += 1
                    nums_dict[num] += 1
                length = max(nums_dict[num], length)
        return length
                