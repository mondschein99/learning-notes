#Question:  Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
#           If target is not found in the array, return [-1, -1].
#           You must write an algorithm with O(log n) runtime complexity.

#Original Version
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        index = 0
        for num in nums:
            if num not in dic:
                dic[num] = [index, index]
            else:
                dic[num][1] = index
            index += 1
        if target not in dic:
            return [-1, -1]
        return dic[target] 


#Modified Version:
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findleft():
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left + right) // 2
                if   nums[mid] < target:
                    left = mid +  1
                else:
                    right = mid - 1
            return left 
        def findright():
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left, right = findleft(), findright()
        if left <= right:
            return [left, right]
        else:
            return [-1, -1]

'''
note:
For the modified version, the running time is O(logn).
Considering numbers approach from both sides, the number of times numbers can be devided is
log2(n).
'''
