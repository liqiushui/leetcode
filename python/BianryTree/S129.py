class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        r = []
        sum = [0]
        self.calTreeNumbers(root, r, sum)
        return sum[0]


    def calTreeNumbers(self, root, record, sum):
        if not root:
            return
        record.append(str(root.val))
        if not root.left and not root.right:
            temp = list(record)
            sum[0] += int("".join(temp))
        if root.left:
            self.calTreeNumbers(root.left, record, sum)
        if root.right:
            self.calTreeNumbers(root.right, record, sum)
        record.pop()


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(s.sumNumbers(root))
