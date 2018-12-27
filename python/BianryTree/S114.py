class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        q = []
        self.preorder(root, q)
        last = None
        while q:
            cur = q.pop(0)
            cur.left = None
            if last:
                last.right = cur
            last = cur

        return root

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

    def preorder(self, root, record):
        if not root:
            return
        record.append(root)
        self.preorder(root.left, record)
        self.preorder(root.right, record)


if __name__ == '__main__':
    s = Solution()
    head = s.makeList([1,2,5,3,4,None,6])
    temp = []
    s.preorder(head, temp)
    print(temp)
    head = s.flatten(head)
    print(head)
