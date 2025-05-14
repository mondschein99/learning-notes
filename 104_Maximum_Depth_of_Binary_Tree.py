#Question: A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

#BFS method
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        count = 0
        if not root:
            return count
        queue = deque([root])
        while queue:
            count += 1
            size = len(queue)
            for s in range(size):
                node = queue.popleft()
                if not node: continue
                else:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        return count

#DFS method



        
