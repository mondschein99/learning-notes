#Question: Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
#          Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
#          Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
#          The tests are generated such that there is exactly one solution. You may not use the same element twice.

'''
Key Decision:
Numbers are sorted, hence two pins from two ends can be utilized.
'''

#Original Version
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        while left <= right:
            if numbers[left] + numbers[right] == target:
                break
            if numbers[left] + numbers[right] > target:
                right = right - 1
            else:
                left = left + 1
        return [left + 1, right + 1]


'''
notes:
Numbers are sorted, so, when the sum of two ends is less than target, the sum of head and any other numbers is less than target.
Similarly, when the sum of two ends is larger than target, the sum of the end and any other numbers is larger than target.
So we can deleted the haed number or the end number according to their sum until the condition is met.
'''
