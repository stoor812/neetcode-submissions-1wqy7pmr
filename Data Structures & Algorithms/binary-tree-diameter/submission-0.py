# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dmeter = self.helper(root)

        return dmeter[1]

        

    def helper(self, node) -> List[int]:
        if not node:
            return [0,0]
        
        left = self.helper(node.left)
        right = self.helper(node.right)

        dMax = max(left[0] + right[0], left[1], right[1])



        return [1 + max(left[0], right[0]), dMax] 