
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max = float("-inf")

        self.maxPathNode(root)

        return max(0, self.max)

    def maxPathNode(self, node):
        if not node:
            return 0
        leftMax = max(0, self.maxPathNode(node.left))
        rightMax = max(0, self.maxPathNode(node.right))
        self.max = max(self.max, leftMax + rightMax + node.val)
        return max(0, max(leftMax, rightMax) + node.val)

if __name__ == '__main__':
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    # root.left.left = TreeNode(1)
    # root.left.right = TreeNode(3)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    # root.left.left.left = TreeNode(-1)

    s = Solution()

    print(s.maxPathSum(root))