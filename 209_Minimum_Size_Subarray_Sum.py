#Question: Given an array of positive integers nums and a positive integer target, 
#          return the minimal length of a subarray whose sum is greater than or equal to target. 
#          If there is no such subarray, return 0 instead.

'''
key notes: all numbers are positive, hence the sum increases when new numbers are added
'''

#Original version
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < target:
            return 0
        add = 0
        num = 0
        num_min = len(nums)
        left = 0
        for i in range(len(nums)):
            add += nums[i]
            num += 1
            while add >= target:
                num_min = min(num, num_min)
                left += 1
                num -= 1
                add -= nums[left-1]
        return num_min


#Modified version
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < target:
            return 0
        add = 0
        num = 0
        num_min = len(nums)
        left = 0
        for right in range(len(nums)):
            add += nums[right]
            while add >= target:
                num_min = min(right - left + 1, num_min)
                add -= nums[left]
                left += 1
        return num_min
