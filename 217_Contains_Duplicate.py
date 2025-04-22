#Question: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#Original version: The speed of this code is not quite fast maybe due to the new variable is built
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_clean = set(nums) # All duplicates will be removed as a set format, hence the length will change
        return len(nums) != len(nums_clean) 

#Modified version:

class Solution(object):
    def containsDuplicate(self, nums):

        return len(nums) != len(set(nums_clean)) 
