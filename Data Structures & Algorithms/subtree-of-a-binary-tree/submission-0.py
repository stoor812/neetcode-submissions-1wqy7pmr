# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root:
            return False
        if root.val == subRoot.val:
            check = self.helper(root, subRoot)
            if check == True: 
                return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def helper(self, root, subRoot) -> bool:

        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False
        elif root.val != subRoot.val:
            return False

        left = self.helper(root.left, subRoot.left)
        right = self.helper(root.right, subRoot.right)

        return left and right
