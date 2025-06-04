#Question: Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
#          such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#          Notice that the solution set must not contain duplicate triplets.
'''
key notes:
refer to question 167
'''

#Original version:
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        list = []
        for i in range(len(nums)-2):
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break
            if i > 0 and nums[i-1] == nums[i]:
                continue
            j = i + 1
            k = len(nums) - 1
            if nums[i] + nums[-2] + nums[-1] < 0:
                continue
            while j < k:
                if nums[k] < 0:
                    break
                if nums[i] + nums[j] + nums[k] == 0:
                    if [nums[i], nums[j], nums[k]] not in list:
                        list += [[nums[i], nums[j], nums[k]]]
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return list 

        
