class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def levelRecord(level, result, order):
            nextLevel = []

            if order:
                for node in reversed(level):
                    result.append(node.val)
                    if node.left:
                        nextLevel.append(node.left)
                    if node.right:
                        nextLevel.append(node.right)
            else:
                for node in reversed(level):
                    result.append(node.val)
                    if node.right:
                        nextLevel.append(node.right)
                    if node.left:
                        nextLevel.append(node.left)

            return nextLevel

        if not root:
            return []

        q = [root]
        r = []
        order = True
        while q:
            temp = []
            q = levelRecord(q, temp, order)
            r.append(temp)
            order = not order
        return r


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    # root.left.left = TreeNode(3)
    # root.left.right = TreeNode(4)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    s = Solution()
    print(s.zigzagLevelOrder(root))
