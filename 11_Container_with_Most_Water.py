#Question: You are given an integer array height of length n. 
#          There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#          Find two lines that together with the x-axis form a container, such that the container contains the most water.
#          Return the maximum amount of water a container can store.
#          Notice that you may not slant the container.
'''
key points:
similar to question 167
'''

# Original version:
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        ans = 0
        while left < right:
            c = min(height[left], height[right]) * (right - left)
            ans = max(c, ans)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans
