"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:

    def twoSum(self, nums, target):
        if nums is None or len(nums) < 2 or target is None:
            return
        num_dict = {}
        index = 0
        while index < len(nums):
            num = nums[index]
            if num in num_dict:
                return [num_dict[num], index]
            else:
                num_dict[target - num] = index
                index += 1

if __name__ == '__main__':
    s = Solution()
    arr = [2, 7, 11, 15]
    print(s.twoSum(arr, 9))
    print(s.twoSum(arr, 26))
