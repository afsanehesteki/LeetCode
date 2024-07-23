# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        Diam = 0
        def maxDepth(node):
            nonlocal Diam
            if not node:
                return 0
            LD = maxDepth(node.left)
            RD = maxDepth(node.right)
            Diam = max (LD + RD , Diam)
            return 1 + max (LD , RD)
        
        maxDepth(root)
        return Diam
