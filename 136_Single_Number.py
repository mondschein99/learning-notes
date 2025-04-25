#Question: Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#          You must implement a solution with a linear runtime complexity and use only constant extra space.

# Final Version
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        single = 0
        for num in nums:
            single ^= num
        return single
        

#Original Version
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        single = next(k for k, v in counts.items() if v == 1  )
        return single
'''
This code is linear computation complexity however it's not a constant extra space, 
'''

