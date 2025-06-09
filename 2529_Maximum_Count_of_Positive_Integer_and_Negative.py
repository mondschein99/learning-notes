#Question: Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.
#          In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, 
#          then return the maximum of pos and neg.

'''
key notes: using lower-bound
'''

#Original Version:
class Solution(object):
    def lower_bound(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg = self.lower_bound(nums, 0) - 1 + 1
        pos = len(nums) - self.lower_bound(nums, 1)
        print(neg)
        print(pos)
        return max(neg, pos)

        
