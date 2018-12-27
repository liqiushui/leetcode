# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        cur = []
        cur.append(root)
        nexts = []
        temp = []
        while cur or nexts:
            if cur:
                root = cur.pop(0)
                temp.append(root.val)
                if root.left:
                    nexts.append(root.left)
                if root.right:
                    nexts.append(root.right)
            else:
                result.append(temp)
                temp = []
                cur = nexts
                nexts = []
        if temp:
            result.append(temp)
        return result[::-1]


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(Solution().levelOrderBottom(root))