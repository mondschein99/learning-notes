#Question: Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#          Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
'''
Hint: Tree is a variable here, not a list or an array.
'''


#Reference:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


'''
Study notes:
Tree: A tree is a hierarchical data structure — kind of like a family tree or an organizational chart.
      It consists of nodes, and each node can have children.

A node is usually defined like this:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val        # current value
        self.left = left      # left child (TreeNode)
        self.right = right    # right child (TreeNode)

A tree can be built as:
n4 = TreeNode(4)
n5 = TreeNode(5)
n2 = TreeNode(2, left=n4, right=n5)
n3 = TreeNode(3)
root = TreeNode(1, left=n2, right=n3)       
'''
