# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        record = []
        result = []
        self.pathRecord(root, 0, sum, record, result)
        print(result)
        return result

    def pathRecord(self, root, sum, target, record, result):
        if not root or target < sum + root.val:
            return
        print(record)
        print(sum)
        print(root.val)
        record.append(root.val)
        if not root.left and not root.right and sum + root.val == target:
            result.append(list(record))
        self.pathRecord(root.left, sum + root.val, target, record, result)
        self.pathRecord(root.right, sum + root.val, target, record, result)
        record.pop()

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
    head = s.makeList([5,4,8,11,None,13,4,7,2,None,None,None,None,5,1])
    s.pathSum(head, 22)

