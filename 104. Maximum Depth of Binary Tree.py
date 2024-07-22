# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxDep(node):
            if not node:
                return 0
            leftDepth = maxDep(node.left)
            rightDepth = maxDep(node.right)
            return 1 + max(leftDepth , rightDepth)

        return maxDep(root)
