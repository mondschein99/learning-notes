#Question: Given the root of a binary tree, return the level order traversal of its nodes' values. 
#          (i.e., from left to right, level by level).
'''
Key points: A BFS question. 
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        else:
            queue = deque([root])
            while queue:
                size = len(queue)
                tempt = []
                for s in range(size):
                    node = queue.popleft()
                    if not node: continue    
                    else:
                        tempt += [node.val]
                        if node.left:
                            queue.append(node.left)
                        if node.right:
                            queue.append(node.right)
                result.append(tempt)
            return result
        