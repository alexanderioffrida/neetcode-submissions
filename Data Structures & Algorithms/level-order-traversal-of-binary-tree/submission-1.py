# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lot = []

        q = collections.deque()
        q.append(root)

        while q:
            level = []
            for _ in range(len(q)): # snapshotting the queue length at the start of each iteration is the mechanism that lets me group nodes by level.
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                lot.append(level)
        return lot