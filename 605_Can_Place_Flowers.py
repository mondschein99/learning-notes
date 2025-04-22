#Question:You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
#         Given an integer array flowerbed containing 0's and 1's
#         where 0 means empty and 1 means not empty, and an integer n
#         return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
'''
Key decision:
You can only place a flower if both neighbors are empty (or don't exist)
'''


# Brutal-Force Try
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        num_avail = 0
        size = len(flowerbed)

        for i in range(size):
            pit = flowerbed[i]
            pit_pre = 0 if i - 1 < 0 else flowerbed[i-1]
            pit_nxt = 0 if i + 1 >= size else flowerbed[i+1]
            if pit == pit_pre == pit_nxt == 0:
                num_avail += 1
                flowerbed[i] = 1
            if num_avail >= n:
                return True
            
        return False

# Fuctional Try

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        num_avail = 0
        bed = [0] + flowerbed + [0]
        size = len(bed)
        i = 1
        while i < size - 1:
          if bed[i] != 0:
            i += 2
            continue
          else:
            if bed[i-1] == bed[i+1]  == 0:
              num_avail += 1
              bed[i] = 1
              i += 2
            else:
              i += 1  
          if num_avail >= n:
            return True
      
        return num_avail >= n

#Challenge: What if flowers can be placed at most every 2 plots instead of 1?

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        num_avail = 0
        bed = [0, 0] + flowerbed + [0, 0]
        size = len(bed)
        i = 2
        while i < size - 2:
          if bed[i] != 0:
            i += 3
            continue
          else:
            if bed[i-2] == bed[i-1] == bed[i+1] == bed[i+2] == 0:
              num_avail += 1
              bed[i] = 1
              i += 3
            else:
              i += 1  
          if num_avail >= n:
            return True
      
        return False
