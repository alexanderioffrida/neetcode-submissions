# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0 # running max diameter (in edges)

        def maxHeight(root: Optional[TreeNode]) -> int:
            if not root: return 0

            leftHeight = maxHeight(root.left)
            rightHeight = maxHeight(root.right)

            self.diameter = max(self.diameter, leftHeight + rightHeight)

            return 1 + max(leftHeight, rightHeight)     
    
        maxHeight(root)
        return self.diameter