#Question: Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
#          A subarray is a contiguous non-empty sequence of elements within an array.

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_pre = {0: 1}
        sum_current = 0
        count = 0

        for num in nums:
            sum_current += num
            if sum_current - k in sum_pre:
                count += sum_pre[sum_current - k]
            if sum_current in sum_pre:
                sum_pre[sum_current] += 1
            else:
                sum_pre[sum_current] = 1
        
        return count
            

'''
Key decision:
Use prefix sum + hash map to track running totals and efficiently detect subarrays that sum to k
If the sum of a subarray nums[i...j] is k,
then: prefix_sum[j] - prefix_sum[i - 1] = k
'''
