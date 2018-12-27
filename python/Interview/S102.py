class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def levelRecord(level, result):
            nextLevel = []
            for node in level:
                result.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            return nextLevel

        if not root:
            return []

        q = [root]
        r = []
        while q:
            temp = []
            q = levelRecord(q, temp)
            r.append(temp)
        return r