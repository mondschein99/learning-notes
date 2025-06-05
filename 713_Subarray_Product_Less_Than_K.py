#Question: Given an array of integers nums and an integer k, 
#          return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

'''
key notes:
similar to Problem 209
'''

#Original version
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        multi = 1
        num = 0
        left = 0
        if k <= 1:
            return num
        for right, x in enumerate(nums):
            multi *= x
            while multi >= k:
                multi /= nums[left]
                left += 1
            num += right - left + 1
        return num
