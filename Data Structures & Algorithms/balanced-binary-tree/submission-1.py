# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.helper(root) != -1

    # HELPER FUNCTION
    def helper(self, node) -> int:
        if not node:
            return 0

        left = self.helper(node.left)
        right = self.helper(node.right)

        if left == -1 or right == -1:
            return -1    
        elif abs(left - right) > 1:
            return - 1
        else:
            return 1 + max(left, right)