class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def levelTree(root, last_level):
            if not root:
                return last_level
            l = last_level + 1
            r = last_level + 1
            if root.left:
                l = levelTree(root.left, last_level + 1)
            if root.right:
                r = levelTree(root.right, last_level + 1)
            return max(l, r)

        return levelTree(root, 0)
