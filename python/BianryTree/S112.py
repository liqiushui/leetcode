class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None





class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        return self.checkPathSum(root, sum)

    def checkPathSum(self, root, sum):
        if not root:
            return sum == 0
        return self.checkPathSum(root.left, sum - root.val) or self.checkPathSum(root.right, sum - root.val)


    def makeList(self, nums):
        if not nums:
            return None

        headval = nums.pop(0)
        head = None
        if headval:
            head = TreeNode(headval)
        if not head:
            return None
        q = [head]
        while q and nums:
            cur = q.pop(0)
            v = nums.pop(0) if nums else None
            if v:
                cur.left = TreeNode(v)
            q.append(cur.left if cur else None)

            v = nums.pop(0) if nums else None
            if v:
                cur.right = TreeNode(v)
            q.append(cur.right if cur else None)

        return head


if __name__ == '__main__':
    s = Solution()
    # [5,4,8,11,None,13,4,7,2,None,None,None,1]
    head = s.makeList([5,4,8,11,None,13,4,7,2,None,None,None,1])
    print(s.hasPathSum(head, 22))
