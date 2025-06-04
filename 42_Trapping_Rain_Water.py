#Question: Given n non-negative integers representing an elevation map where the width of each bar is 1, 
#          compute how much water it can trap after raining.

'''
key notes: 
For each bar, the rain trapped depends on maximum heights on both sides of this bar and its own height.
On particular bar, the rain it traps is min(max_left, max_right)  
'''

#Original version
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        max_left = 0
        max_right = 0
        left = []
        right = []
        maximum = 0
        for i in range(n):
            maximum = max(maximum, height[i])
            left.append(maximum)
        maximum = 0
        for i in range(n-1, -1, -1):
            maximum = max(maximum, height[i])
            right.append(maximum)
        right.reverse()
        min_height = [min(a, b) for a, b in zip(left, right)]
        result = [a - b for a, b in zip(min_height, height)] 
        return sum(result)


'''
key notes: 
From two sides, we can know the min height of it is min(max_left/max_right, its own height).
Then we can get the space directly and do not need to build an array to store.
'''
#Saving-Space version
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = 0
        right = n - 1
        max_left = 0
        max_right = 0
        ans = 0
        while left <= right:
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])
            if max_left < max_right:
                ans += max_left - height[left]
                left += 1
            else:
                ans += max_right - height[right]
                right -= 1
        return ans


