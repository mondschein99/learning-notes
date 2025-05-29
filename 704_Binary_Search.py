#Question:  Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
#           If target exists, then return its index. Otherwise, return -1.
#           You must write an algorithm with O(log n) runtime complexity.


#Original version
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dic = {}
        index = 0
        for num in nums:
            dic[num] = index
            index += 1
        if target not in dic:
            return -1
        return dic[target]
