class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.maxDifference = 0

        def maxHeight(node: Optional[TreeNode]) -> int:
            if not node: return 0

            leftHeight = maxHeight(node.left)

            if leftHeight == -1: return -1

            rightHeight = maxHeight(node.right)

            if rightHeight == -1: return -1

            if abs(leftHeight - rightHeight) > 1: return -1

            return 1 + max(leftHeight, rightHeight)
        
        return maxHeight(root) != -1