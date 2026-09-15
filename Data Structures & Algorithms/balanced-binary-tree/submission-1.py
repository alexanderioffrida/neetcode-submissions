class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.difference = 0

        def maxHeight(root: Optional[TreeNode]) -> int:
            if not root: return 0

            leftHeight = maxHeight(root.left)
            rightHeight = maxHeight(root.right)

            self.difference = max(self.difference, abs(leftHeight - rightHeight))

            return 1 + max(leftHeight, rightHeight)
        
        maxHeight(root)
        if self.difference > 1:
            return False
        else:
            return True