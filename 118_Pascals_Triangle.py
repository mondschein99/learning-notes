#Question: Given an integer numRows, return the first numRows of Pascal's triangle.
#          In Pascal's triangle, each number is the sum of the two numbers directly above it.

#Original Version
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = [[1]]
    
        for i in range(1, numRows):
            row_pre = triangle[i - 1]
            row_curr = [1]
            for j in range(1, i):
                row_curr.append(row_pre[j] + row_pre[j - 1])
            row_curr.append(1)
            triangle.append(row_curr)
        return triangle

#Modified Version
class Solution(object):
    def generate(self, numRows):
      triangle = [[1] for i in range(numsRows)]
      if numRows = 1:
        return triangle
      for i in range(numRows):
        for j in range(i):
          triange[i] += triange[i-1][j] +  triange[i-1][j-1] 
        triangle[i] += 1
      return triangle

#Sample code fron Leetcode
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows ==1:
            return [[1]]  #Handle the edge case
        dfs=[[1] for i in range(0,numRows)] #Initialize, since the first element of each row is always 1
        for i in range(1,numRows):  #Iterate the row
            for j in range(1,i):
                dfs[i]+= [dfs[i-1][j-1]+dfs[i-1][j]] #Add the element on ith row column by column
            dfs[i]+=[1] #Completement the last element on each line
        return dfs


 
