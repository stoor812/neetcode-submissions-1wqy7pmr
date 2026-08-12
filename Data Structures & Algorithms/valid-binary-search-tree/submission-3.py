# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isValid = self.valid(root,float("-inf"), float("inf"))

        return isValid  
    
    def valid(self, node, lower, upper):
        if not node:
            return True

        if not (lower < node.val < upper):
            return False

        return self.valid(node.left, lower, node.val) and self.valid(node.right, node.val, upper)