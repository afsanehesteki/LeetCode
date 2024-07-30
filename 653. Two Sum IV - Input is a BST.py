# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        myset = set()
        def traverse(node):
            if not node:
                return False
            if (k - node.val) in myset:
                return True
            myset.add(node.val)
            tl = traverse(node.left) 
            tr = traverse(node.right)
            if tl ==True or tr==True:
                return True

        return  traverse(root) ==True
