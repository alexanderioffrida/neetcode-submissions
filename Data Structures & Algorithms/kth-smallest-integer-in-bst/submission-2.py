# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        solution = root.val

        def valueCheck(node):
            nonlocal count, solution
            if not node: return

            valueCheck(node.left)
            if count == 0:
                return
            count -= 1
            if count == 0:
                solution = node.val
                return
            valueCheck(node.right)

        valueCheck(root)
        return solution