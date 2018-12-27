class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        dl = self.isTreeDepth(root.left)
        dr = self.isTreeDepth(root.right)
        if abs(dl - dr) > 1:
            return False

        bl = self.isBalanced(root.left)
        br = self.isBalanced(root.right)

        return  bl and br


    def isTreeDepth(self, root):
        if not root:
            return 0
        return max(1 + self.isTreeDepth(root.left), 1 + self.isTreeDepth(root.right))
