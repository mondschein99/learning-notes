#Question: A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

'''
key notes: 
this problem can be regarded in two ways:
1. the maximum depth is exact the number of levels, hence using BFS to count is available
2. using DFS to see exactly how deep the tree is then accumulate each time.
'''

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

#DFS method: postorder 
class Solution(object):
    def maxDepth(self, root):
        count = 0
        if not root:
            return count
        def postorder_traversal(node):
            if not node:
                return 0
            c1 = postorder_traversal(node.left)
            c2 = postorder_traversal(node.right)
            return max(c1, c2) + 1
        count = postorder_traversal(root)
        return count


    






        
