#Question: Given an integer array nums, find the subarray with the largest sum, and return its sum
#Basic thought: Kadane’s Algorithm
'''
Key decision:
If adding the current number to current_sum makes it better (than current number), continue.
If it makes it worse, drop the old subarray and start fresh from the current number.
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_list = [0]
        while(nums):
            num = nums.pop(-1)
            max_list.append(max(num, num + max_list[-1]))
        return max(max_list[1:])
      

