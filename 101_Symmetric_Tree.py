#Question: Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

#Reference:
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def isMirror(n1, n2):
            if not n1 and not n2: return True
            if not n1 or not n2: return False
            return(
                   n1.val == n2.val and 
                   isMirror(n1.left, n2.right) and
                   isMirror(n1.right, n2.left)
                   )

        return isMirror(root.left, root.right)

#BFS method
from collections import deque
class Solution(object):
    def isSymmetric(self, root):
        queue = deque([(root.left, root.right)])
        while queue:
            n1, n2 = queue.popleft()
            if not n1 and not n2: continue
            if not n1 or not n2 or n1.val != n2.val: return False
            queue.append((n1.left, n2.right))
            queue.append((n1.right, n2.left))
        return True 

'''
Study notes:
Depth-First Search (DFS): Go as deep as possible before backtracking.
Breadth-First Search (BFS): Visit the tree level by level, left to right.
e.g: DFS algorithm
ef inorder_traversal(node):
    if not node:
        return
    inorder_traversal(node.left)
    print(node.val)
    inorder_traversal(node.right)
running in the tree:
       10
      /  \
     5    15
    / \     \
   3   7     20
expected result:
3 → 5 → 7 → 10 → 15 → 20
'''
