# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        bfs = []

        if not root:
            return bfs

        queue = deque([root])

        while queue:
            lvlSize = len(queue)
            lvl = []

            # LOOP THROUGH QUEUE
            for _ in range(lvlSize):
                node = queue.popleft()
                lvl.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            bfs.append(lvl)

        return bfs


